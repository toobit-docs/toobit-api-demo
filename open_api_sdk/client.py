"""
TooBit API 核心客户端
"""

import hashlib
import hmac
import time
import urllib.parse
from typing import Dict, Any, Optional, Union
import requests

from .config import TooBitConfig
from .exceptions import TooBitException, raise_toobit_exception
from .models import (
    OrderRequest, OrderResponse, CreateOrderResponse, CancelOrderRequest, CancelOrderResponse,
    OrderQueryRequest, AccountInfo, ExchangeInfo, Ticker24hr, OrderBook, Kline, OrderSide, OrderType,
    CreateFuturesOrderResponse
)


class TooBitClient:
    """TooBit API 客户端"""
    
    def __init__(self, config: TooBitConfig):
        """初始化客户端"""
        self.config = config
        self.config.validate()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "TooBit-SDK/1.0.0",
            "Content-Type": "application/x-www-form-urlencoded"
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
                # TooBit API的POST请求通常把参数放在URL后面，而不是请求体中
                response = self.session.post(
                    url, 
                    params=params,  # 改为params，参数放在URL后面
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
            if 'code' in data and data['code'] != 200:
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
    
    # ==================== 公开接口 ====================
    
    def ping(self) -> bool:
        """测试服务器连通性"""
        try:
            response = self._make_request('GET', '/api/v1/ping')
            return True
        except:
            return False
    
    def get_server_time(self) -> int:
        """获取服务器时间"""
        response = self._make_request('GET', '/api/v1/time')
        return response['serverTime']
    
    def get_exchange_info(self) -> ExchangeInfo:
        """获取交易规则和交易对信息"""
        response = self._make_request('GET', '/api/v1/exchangeInfo', signed=False)
        return ExchangeInfo(**response)
    
    def get_order_book(self, symbol: str, limit: int = 100) -> OrderBook:
        """获取深度信息"""
        params = {'symbol': symbol, 'limit': limit}
        response = self._make_request('GET', '/api/v1/depth', params)
        return OrderBook(**response)
    
    def get_recent_trades(self, symbol: str, limit: int = 500) -> list:
        """获取最近成交"""
        params = {'symbol': symbol, 'limit': limit}
        response = self._make_request('GET', '/api/v1/trades', params)
        return response
    
    def get_klines(
        self, 
        symbol: str, 
        interval: str, 
        limit: int = 500,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None
    ) -> list:
        """获取K线数据"""
        params = {
            'symbol': symbol,
            'interval': interval,
            'limit': limit
        }
        if start_time:
            params['startTime'] = start_time
        if end_time:
            params['endTime'] = end_time
        
        response = self._make_request('GET', '/api/v1/klines', params)
        return response
    
    def get_24hr_ticker(self, symbol: Optional[str] = None) -> Union[Ticker24hr, list]:
        """获取24小时价格变动情况"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        
        response = self._make_request('GET', '/api/v1/ticker/24hr', params)
        
        if symbol:
            return Ticker24hr(**response)
        else:
            return [Ticker24hr(**item) for item in response]
    
    def get_price(self, symbol: Optional[str] = None) -> Union[Dict[str, str], list]:
        """获取最新价格"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        
        response = self._make_request('GET', '/api/v1/ticker/price', params)
        return response
    
    def get_best_order_book(self, symbol: str) -> Dict[str, Any]:
        """获取当前最优挂单"""
        params = {'symbol': symbol}
        response = self._make_request('GET', '/api/v1/ticker/bookTicker', params)
        return response
    
    # ==================== 现货签名接口 ====================
    
    def create_order(self, order_request: OrderRequest) -> CreateOrderResponse:
        """下单"""
        params = order_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/spot/order', params, signed=True)
        return CreateOrderResponse(**response)
    
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
        
        response = self._make_request('GET', '/api/v1/spot/allOrders', params, signed=True)
        return [OrderResponse(**item) for item in response]
    
    def get_account_info(self) -> AccountInfo:
        """获取现货账户信息"""
        response = self._make_request('GET', '/api/v1/spot/account', signed=True)
        return AccountInfo(**response)
    
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
        
        response = self._make_request('GET', '/api/v1/spot/myTrades', params, signed=True)
        return response
    
    # ==================== 合约接口 ====================
    
    def get_sub_accounts(self) -> list:
        """查询子账户 (USER_DATA)"""
        response = self._make_request('GET', '/api/v1/subAccount/list', signed=True)
        return response
    
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
    
    def change_margin_mode(self, symbol: str, margin_mode: str) -> Dict[str, Any]:
        """变换逐全仓模式 (TRADE)"""
        params = {
            'symbol': symbol,
            'marginMode': margin_mode
        }
        response = self._make_request('POST', '/api/v1/futures/marginMode', params, signed=True)
        return response
    
    def adjust_leverage(self, symbol: str, leverage: int) -> Dict[str, Any]:
        """调整开仓杠杆 (TRADE)"""
        params = {
            'symbol': symbol,
            'leverage': leverage
        }
        response = self._make_request('POST', '/api/v1/futures/leverage', params, signed=True)
        return response
    
    def get_leverage_and_margin_mode(self, symbol: str) -> Dict[str, Any]:
        """查询杠杆倍数和仓位模式 (USER_DATA)"""
        params = {'symbol': symbol}
        response = self._make_request('GET', '/api/v1/futures/leverage', params, signed=True)
        return response
    
    def create_futures_order(self, order_request: OrderRequest) -> OrderResponse:
        """合约下单 (TRADE)"""
        params = order_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/futures/order', params, signed=True)
        return CreateFuturesOrderResponse(**response)
    
    def batch_create_futures_orders(self, orders: list) -> list:
        """合约批量下单 (TRADE)"""
        params = {'orders': orders}
        response = self._make_request('POST', '/api/v1/futures/batchOrders', params, signed=True)
        return response
    
    def get_futures_order(self, symbol: str, order_id: Optional[str] = None, client_order_id: Optional[str] = None) -> OrderResponse:
        """查询合约订单 (USER_DATA)"""
        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_order_id:
            params['origClientOrderId'] = client_order_id
        
        response = self._make_request('GET', '/api/v1/futures/order', params, signed=True)
        return OrderResponse(**response)
    
    def cancel_futures_order(self, symbol: str, order_id: Optional[str] = None, client_order_id: Optional[str] = None) -> CancelOrderResponse:
        """撤销合约订单 (TRADE)"""
        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_order_id:
            params['origClientOrderId'] = client_order_id
        
        response = self._make_request('DELETE', '/api/v1/futures/order', params, signed=True)
        return CancelOrderResponse(**response)
    
    def get_futures_open_orders(self, symbol: Optional[str] = None) -> list:
        """查看当前全部挂单 (USER_DATA)"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        
        response = self._make_request('GET', '/api/v1/futures/openOrders', params, signed=True)
        return response
    
    def get_futures_positions(self, symbol: Optional[str] = None) -> list:
        """查询当前持仓 (USER_DATA)"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        
        response = self._make_request('GET', '/api/v1/futures/position', params, signed=True)
        return response
    
    def get_futures_all_orders(
        self, 
        symbol: str, 
        order_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: int = 500
    ) -> list:
        """查询历史订单 (USER_DATA)"""
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
        
        response = self._make_request('GET', '/api/v1/futures/allOrders', params, signed=True)
        return response
    
    def get_futures_account_balance(self) -> list:
        """账户余额 (USER_DATA)"""
        response = self._make_request('GET', '/api/v1/futures/account', signed=True)
        return response
    
    def adjust_isolated_margin(self, symbol: str, amount: str, type: str) -> Dict[str, Any]:
        """调整逐仓保证金 (TRADE)"""
        params = {
            'symbol': symbol,
            'amount': amount,
            'type': type
        }
        response = self._make_request('POST', '/api/v1/futures/margin', params, signed=True)
        return response
    
    def get_futures_trade_history(
        self, 
        symbol: str, 
        limit: int = 500,
        from_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None
    ) -> list:
        """账户成交历史 (USER_DATA)"""
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
        
        response = self._make_request('GET', '/api/v1/futures/myTrades', params, signed=True)
        return response
    
    def get_futures_account_flow(
        self,
        symbol: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: int = 100
    ) -> list:
        """查询合约账户流水 (USER_DATA)"""
        params = {'limit': limit}
        if symbol:
            params['symbol'] = symbol
        if start_time:
            params['startTime'] = start_time
        if end_time:
            params['endTime'] = end_time
        
        response = self._make_request('GET', '/api/v1/futures/account/flow', params, signed=True)
        return response
    
    def get_user_fee_rate(self, symbol: str) -> Dict[str, Any]:
        """用户手续费率 (USER_DATA)"""
        params = {'symbol': symbol}
        response = self._make_request('GET', '/api/v1/futures/fee', params, signed=True)
        return response
    
    def get_today_pnl(self) -> Dict[str, Any]:
        """获取今日盈亏 (USER_DATA)"""
        response = self._make_request('GET', '/api/v1/futures/todayPnl', signed=True)
        return response
    
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
    
    def cancel_all_orders(self, symbol: str) -> list:
        """撤销全部订单 (TRADE)"""
        params = {'symbol': symbol}
        response = self._make_request('DELETE', '/api/v1/futures/order', params, signed=True)
        return response
    
    # ==================== 便捷方法 ====================
    
    def buy_limit(self, symbol: str, quantity: float, price: float, **kwargs) -> OrderResponse:
        """限价买入"""
        order_request = OrderRequest(
            symbol=symbol,
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            quantity=quantity,
            price=price,
            **kwargs
        )
        return self.create_order(order_request)
    
    def sell_limit(self, symbol: str, quantity: float, price: float, **kwargs) -> OrderResponse:
        """限价卖出"""
        order_request = OrderRequest(
            symbol=symbol,
            side=OrderSide.SELL,
            type=OrderType.LIMIT,
            quantity=quantity,
            price=price,
            **kwargs
        )
        return self.create_order(order_request)
    
    def buy_market(self, symbol: str, quantity: float, **kwargs) -> OrderResponse:
        """市价买入"""
        order_request = OrderRequest(
            symbol=symbol,
            side=OrderSide.BUY,
            type=OrderType.MARKET,
            quantity=quantity,
            **kwargs
        )
        return self.create_order(order_request)
    
    def sell_market(self, symbol: str, quantity: float, **kwargs) -> OrderResponse:
        """市价卖出"""
        order_request = OrderRequest(
            symbol=symbol,
            side=OrderSide.SELL,
            type=OrderType.MARKET,
            quantity=quantity,
            **kwargs
        )
        return self.create_order(order_request)
    
    def cancel_order_by_id(self, symbol: str, order_id: int) -> CancelOrderResponse:
        """通过订单ID取消订单"""
        cancel_request = CancelOrderRequest(symbol=symbol, order_id=order_id)
        return self.cancel_order(cancel_request)
    
    def get_balance(self, asset: str) -> Optional[Dict[str, Any]]:
        """获取指定资产余额"""
        account_info = self.get_account_info()
        for balance in account_info.balances:
            if balance['asset'] == asset:
                return balance
        return None
    
    def close(self):
        """关闭客户端"""
        if self.session:
            self.session.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
