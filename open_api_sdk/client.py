"""
TooBit API 核心客户端
"""

import hashlib
import hmac
import json
import time
import urllib.parse
from typing import Dict, Any, Optional, Union
import requests

from .config import TooBitConfig
from .exceptions import TooBitException, raise_toobit_exception
from .models import (
    OrderRequest, OrderResponse, CreateOrderResponse, CancelOrderRequest, CancelOrderResponse,
    OrderQueryRequest, ExchangeInfo, Ticker24hr, OrderBook, Kline, OrderSide, OrderType,
    CreateFuturesOrderResponse, CancelFuturesOrderResponse, QueryFuturesOrderResponse,
    FuturesOpenOrderResponse, CancelAllOrdersResponse, BatchCancelOrderResult, BatchCancelOrdersResponse,
    BatchCreateOrderResponse, CancelOpenOrdersResponse, FuturesOrderRequest, BatchFuturesOrderResult,
    BatchCreateFuturesOrdersResponse, FuturesPosition, SetPositionTradingStopRequest, SetPositionTradingStopResponse,
    QueryFuturesHistoryOrdersRequest, FuturesBalance,     AdjustIsolatedMarginRequest, AdjustIsolatedMarginResponse,     QueryFuturesTradeHistoryRequest, FuturesTrade, QueryFuturesAccountFlowRequest, FuturesAccountFlow
)


class TooBitClient:
    """TooBit API 客户端"""
    
    def __init__(self, config: TooBitConfig):
        """初始化客户端"""
        self.config = config
        self.config.validate()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "TooBit-SDK/1.0.0"
        })
    
    def _generate_signature(self, params: Dict[str, Any]) -> str:
        """生成HMAC SHA256签名"""
        # 将参数转换为查询字符串
        query_string = urllib.parse.urlencode(params)
        # 使用API Secret作为密钥生成签名
        signature = hmac.new(
            self.config.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return signature
    
    def _add_auth_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """添加认证参数"""
        # 添加时间戳
        params['timestamp'] = int(time.time() * 1000)
        # 添加接收窗口
        if 'recvWindow' not in params:
            params['recvWindow'] = self.config.recv_window
        # 生成签名
        params['signature'] = self._generate_signature(params)
        return params
    
    def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None,
        data: Optional[str] = None,
        signed: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """发送HTTP请求"""
        url = f"{self.config.base_url}{endpoint}"
        
        if params is None:
            params = {}
        
        # 如果是签名请求，添加认证参数
        if signed:
            params = self._add_auth_params(params)
            # 添加API Key到请求头
            headers = kwargs.get('headers', {})
            headers['X-BB-APIKEY'] = self.config.api_key
            kwargs['headers'] = headers
        
        try:
            if method.upper() == 'GET':
                response = self.session.get(
                    url, 
                    params=params, 
                    timeout=self.config.timeout,
                    **kwargs
                )
            elif method.upper() == 'POST':
                # TooBit API的POST请求支持参数放在URL后面或请求体中
                if data:
                    # 如果有request body，使用JSON格式
                    headers = kwargs.get('headers', {})
                    headers['Content-Type'] = 'application/json'
                    kwargs['headers'] = headers
                    
                    # 如果data是字符串，解析为JSON对象
                    if isinstance(data, str):
                        json_data = json.loads(data)
                    else:
                        json_data = data
                    
                    response = self.session.post(
                        url, 
                        params=params,
                        json=json_data,  # 使用json参数
                        timeout=self.config.timeout,
                        **kwargs
                    )
                else:
                    # 否则参数放在URL后面，使用form格式
                    headers = kwargs.get('headers', {})
                    headers['Content-Type'] = 'application/x-www-form-urlencoded'
                    kwargs['headers'] = headers
                    
                    response = self.session.post(
                        url, 
                        params=params,
                        timeout=self.config.timeout,
                        **kwargs
                    )
            elif method.upper() == 'DELETE':
                response = self.session.delete(
                    url, 
                    params=params, 
                    timeout=self.config.timeout,
                    **kwargs
                )
            else:
                raise ValueError(f"不支持的HTTP方法: {method}")
            
            # 检查HTTP状态码
            if response.status_code >= 400:
                error_msg = f"HTTP错误: 状态码 {response.status_code}"
                try:
                    error_detail = response.json()
                    print(f"请求失败: {error_msg}")
                    print(f"错误响应详情: {error_detail}")
                    error_msg += f" | 错误详情: {error_detail}"
                except:
                    print(f"请求失败: {error_msg}")
                    print(f"响应内容: {response.text}")
                    error_msg += f" | 响应内容: {response.text}"
                raise TooBitException(error_msg)
            
            response.raise_for_status()
            
            # 解析响应
            try:
                data = response.json()
            except ValueError as e:
                error_msg = f"响应解析失败: 无法解析JSON响应, 状态码: {response.status_code}, 响应内容: {response.text}"
                print(f"请求失败: {error_msg}")
                raise TooBitException(error_msg)
            
            # 检查API错误
            if 'code' in data and data['code'] != 200 and data['code'] != 0:
                error_msg = f"API错误: 错误码 {data['code']}, 错误信息: {data.get('msg', '')}"
                print(f"请求失败: {error_msg}")
                print(f"完整错误响应: {data}")
                raise_toobit_exception(data['code'], data.get('msg', ''), data)
            
            return data
            
        except requests.exceptions.RequestException as e:
            error_msg = f"网络请求错误: {str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.json()
                    print(f"请求失败详情: {error_detail}")
                    error_msg += f" | 响应详情: {error_detail}"
                except:
                    error_msg += f" | HTTP状态码: {e.response.status_code} | 响应内容: {e.response.text}"
            print(f"请求失败: {error_msg}")
            raise TooBitException(error_msg)
        except ValueError as e:
            error_msg = f"参数错误: {str(e)}"
            print(f"请求失败: {error_msg}")
            raise TooBitException(error_msg)
        except Exception as e:
            error_msg = f"未知错误: {str(e)}"
            print(f"请求失败: {error_msg}")
            raise TooBitException(error_msg)
    
    # ==================== 现货签名接口 ====================
    
    # ==================== 现货签名接口 ====================
    
    def create_order(self, order_request: OrderRequest) -> CreateOrderResponse:
        """下单"""
        params = order_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/spot/order', params, signed=True)
        return CreateOrderResponse(**response)
    
    def batch_create_orders(self, order_requests: list[OrderRequest]) -> BatchCreateOrderResponse:
        """批量下单"""
        # 将多个订单请求转换为参数列表
        orders_data = []
        for order_request in order_requests:
            order_data = order_request.model_dump(exclude_none=True, by_alias=True)
            orders_data.append(order_data)
        
        # 构建request body
        import json
        request_body = json.dumps(orders_data)
        
        # 构建query string - 只包含认证相关参数
        params = {}
        
        response = self._make_request('POST', '/api/v1/spot/batchOrders', params, data=request_body, signed=True)
        return BatchCreateOrderResponse(**response)
    
    def batch_cancel_spot_orders(self, order_ids: list[str]) -> BatchCancelOrdersResponse:
        """现货批量撤单"""
        # 构建批量撤单参数
        params = {
            'ids': ','.join(order_ids)
        }
        
        response = self._make_request('DELETE', '/api/v1/spot/cancelOrderByIds', params, signed=True)
        return BatchCancelOrdersResponse(**response)

    def cancel_open_orders(self, symbol: Optional[str] = None, side: Optional[OrderSide] = None) -> CancelOpenOrdersResponse:
        """撤销挂单 - 可指定交易对和方向"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        if side:
            params['side'] = side.value
        
        response = self._make_request('DELETE', '/api/v1/spot/openOrders', params, signed=True)
        return CancelOpenOrdersResponse(**response)

    def cancel_order(self, symbol: str, order_id: Optional[str] = None, client_order_id: Optional[str] = None) -> CancelOrderResponse:
        """撤销订单"""
        # 创建取消订单请求对象
        cancel_request = CancelOrderRequest(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=client_order_id
        )
        params = cancel_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('DELETE', '/api/v1/spot/order', params, signed=True)
        return CancelOrderResponse(**response)
    
    def get_order(self, query_request: OrderQueryRequest) -> OrderResponse:
        """查询现货订单"""
        params = query_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/spot/order', params, signed=True)
        return OrderResponse(**response)
    
    def get_open_orders(self, symbol: Optional[str] = None) -> list:
        """查询当前现货挂单"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        
        response = self._make_request('GET', '/api/v1/spot/openOrders', params, signed=True)
        return [OrderResponse(**item) for item in response]
    
    def get_all_orders(
        self, 
        symbol: str, 
        order_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: int = 500
    ) -> list:
        """查询所有现货订单"""
        params = {
            'symbol': symbol,
            'limit': limit
        }
        if order_id:
            params['orderId'] = order_id
        if start_time:
            params['startTime'] = start_time
        if end_time:
            params['endTime'] = end_time
        
        response = self._make_request('GET', '/api/v1/spot/tradeOrders', params, signed=True)
        return [OrderResponse(**item) for item in response]

    
    def get_trade_history(
        self, 
        symbol: str, 
        limit: int = 500,
        from_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None
    ) -> list:
        """获取现货账户成交历史"""
        params = {
            'symbol': symbol,
            'limit': limit
        }
        if from_id:
            params['fromId'] = from_id
        if start_time:
            params['startTime'] = start_time
        if end_time:
            params['endTime'] = end_time
        
        response = self._make_request('GET', '/api/v1/account/trades', params, signed=True)
        return response
    
    # ==================== 合约接口 ====================
    
    def transfer_between_accounts(
        self,
        from_account_type: str,
        to_account_type: str,
        asset: str,
        quantity: str
    ) -> list:
        """母子账户万能划转 (TRADE)"""
        params = {
            'fromAccountType': from_account_type,
            'toAccountType': to_account_type,
            'asset': asset,
            'quantity': quantity
        }
        response = self._make_request('POST', '/api/v1/subAccount/transfer', params, signed=True)
        return response
    
    def create_futures_order(self, order_request: OrderRequest) -> OrderResponse:
        """合约下单 (TRADE)"""
        params = order_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/futures/order', params, signed=True)
        return CreateFuturesOrderResponse(**response)

    def batch_create_futures_orders(self, order_requests: list[FuturesOrderRequest]) -> BatchCreateFuturesOrdersResponse:
        """合约批量下单 (TRADE)"""
        # 将多个订单请求转换为参数列表
        orders_data = []
        for order_request in order_requests:
            order_data = order_request.model_dump(exclude_none=True, by_alias=True)
            orders_data.append(order_data)
        
        # 构建request body - 直接是订单数组
        request_body = json.dumps(orders_data)
        
        # 构建query string - 只包含认证相关参数
        params = {}
        
        response = self._make_request('POST', '/api/v1/futures/batchOrders', params, data=request_body, signed=True)
        return BatchCreateFuturesOrdersResponse(**response)
    

    
    def get_futures_order(self, symbol: str, order_id: Optional[str] = None, client_order_id: Optional[str] = None) -> QueryFuturesOrderResponse:
        """查询合约订单 (USER_DATA)"""
        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_order_id:
            params['origClientOrderId'] = client_order_id
        
        response = self._make_request('GET', '/api/v1/futures/order', params, signed=True)
        return QueryFuturesOrderResponse(**response)
    
    def cancel_futures_order(self, symbol: str, order_id: Optional[str] = None, client_order_id: Optional[str] = None) -> QueryFuturesOrderResponse:
        """撤销合约订单 (TRADE)"""
        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_order_id:
            params['origClientOrderId'] = client_order_id
        
        response = self._make_request('DELETE', '/api/v1/futures/order', params, signed=True)
        return QueryFuturesOrderResponse(**response)
    
    def get_futures_open_orders(self, symbol: Optional[str] = None) -> list[FuturesOpenOrderResponse]:
        """查看当前全部挂单 (USER_DATA)"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        
        response = self._make_request('GET', '/api/v1/futures/openOrders', params, signed=True)
        return [FuturesOpenOrderResponse(**order) for order in response]

    def get_futures_positions(self, symbol: Optional[str] = None, side: Optional[str] = None) -> list[FuturesPosition]:
        """查询当前持仓 (USER_DATA)"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        if side:
            params['side'] = side
        
        response = self._make_request('GET', '/api/v1/futures/positions', params, signed=True)
        return [FuturesPosition(**position) for position in response]

    def set_position_trading_stop(self, request: SetPositionTradingStopRequest) -> SetPositionTradingStopResponse:
        """设置持仓止盈止损 (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/futures/position/trading-stop', params, signed=True)
        return SetPositionTradingStopResponse(**response)

    def get_futures_history_orders(self, request: QueryFuturesHistoryOrdersRequest) -> list[QueryFuturesOrderResponse]:
        """查询历史订单 (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/futures/historyOrders', params, signed=True)
        return [QueryFuturesOrderResponse(**order) for order in response]

    def get_futures_balance(self) -> list[FuturesBalance]:
        """查询合约账户余额 (USER_DATA)"""
        response = self._make_request('GET', '/api/v1/futures/balance', {}, signed=True)
        return [FuturesBalance(**balance) for balance in response]

    def adjust_isolated_margin(self, request: AdjustIsolatedMarginRequest) -> AdjustIsolatedMarginResponse:
        """调整逐仓保证金 (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/futures/positionMargin', params, signed=True)
        return AdjustIsolatedMarginResponse(**response)

    def get_futures_trade_history(self, request: QueryFuturesTradeHistoryRequest) -> list[FuturesTrade]:
        """查询合约账户成交历史 (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/futures/userTrades', params, signed=True)
        return [FuturesTrade(**trade) for trade in response]

    def get_futures_account_flow(self, request: QueryFuturesAccountFlowRequest) -> list[FuturesAccountFlow]:
        """查询合约账户流水 (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/futures/balanceFlow', params, signed=True)
        return [FuturesAccountFlow(**flow) for flow in response]
    

    

    

    
    def get_transfer_history(
        self,
        asset: Optional[str] = None,
        from_account_type: Optional[str] = None,
        to_account_type: Optional[str] = None,
        limit: int = 100
    ) -> list:
        """获取划转历史"""
        params = {'limit': limit}
        if asset:
            params['asset'] = asset
        if from_account_type:
            params['fromAccountType'] = from_account_type
        if to_account_type:
            params['toAccountType'] = to_account_type
        
        response = self._make_request('GET', '/api/v1/account/balanceFlow', params, signed=True)
        return response
    
    def cancel_all_orders(self, symbol: str) -> CancelAllOrdersResponse:
        """撤销全部订单 (TRADE)"""
        params = {'symbol': symbol}
        response = self._make_request('DELETE', '/api/v1/futures/batchOrders', params, signed=True)
        return CancelAllOrdersResponse(**response)
    
    def batch_cancel_orders(self, symbol: str, order_ids: list[str]) -> BatchCancelOrdersResponse:
        """批量撤销订单 (TRADE)"""
        params = {
            'symbol': symbol,
            'orderIds': ','.join(order_ids)
        }
        response = self._make_request('DELETE', '/api/v1/futures/batchOrders', params, signed=True)
        return BatchCancelOrdersResponse(**response)
    

    
    def close(self):
        """关闭客户端"""
        if self.session:
            self.session.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
