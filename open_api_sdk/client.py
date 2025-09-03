"""
TooBit API core client
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
    BatchOrderResult, BatchCreateOrderResponse, CancelOpenOrdersResponse, FuturesOrderRequest, BatchFuturesOrderResult,
    BatchCreateFuturesOrdersResponse, FuturesPosition, SetPositionTradingStopRequest, SetPositionTradingStopResponse,
    QueryFuturesHistoryOrdersRequest, FuturesBalance,     AdjustIsolatedMarginRequest, AdjustIsolatedMarginResponse,     QueryFuturesTradeHistoryRequest, FuturesTrade, QueryFuturesAccountFlowRequest, FuturesAccountFlow,
    QueryFuturesUserFeeRateRequest, FuturesUserFeeRate, FuturesTodayPnL,
    ChangeMarginTypeRequest, ChangeMarginTypeResponse,
    AdjustLeverageRequest, AdjustLeverageResponse,
    QueryLeverageRequest, AccountLeverage,
    SpotBalance, SpotAccountInfo, SpotSubAccount, ApiKeyType
)


class TooBitClient:
    """TooBit API Client"""
    
    def __init__(self, config: TooBitConfig):
        """Initialize client"""
        self.config = config
        self.config.validate()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "TooBit-SDK/1.0.0"
        })
    
    def _generate_signature(self, params: Dict[str, Any]) -> str:
        """Generate HMAC SHA256 signature"""
        # Convert parameters to query string
        query_string = urllib.parse.urlencode(params)
        # Use API secret as key to generate signature
        signature = hmac.new(
            self.config.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return signature
    
    def _add_auth_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Add authentication parameters"""
        # Add timestamp
        params['timestamp'] = int(time.time() * 1000)
        # Add receive window
        if 'recvWindow' not in params:
            params['recvWindow'] = self.config.recv_window
        # Generate signature
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
        """Send HTTP request"""
        url = f"{self.config.base_url}{endpoint}"
        
        if params is None:
            params = {}
        
        # If it's a signed request, add authentication parameters
        if signed:
            params = self._add_auth_params(params)
            # Add API key to request header
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
                # TooBit API POST request supports parameters in URL or request body
                if data:
                    # If there's a request body, use JSON format
                    headers = kwargs.get('headers', {})
                    headers['Content-Type'] = 'application/json'
                    kwargs['headers'] = headers
                    
                    # If data is a string, parse as JSON object
                    if isinstance(data, str):
                        json_data = json.loads(data)
                    else:
                        json_data = data
                    
                    response = self.session.post(
                        url, 
                        params=params,
                        json=json_data,  # Use json parameters
                        timeout=self.config.timeout,
                        **kwargs
                    )
                else:
                    # TooBit API POST request usually puts parameters in URL, not in request body
                    response = self.session.post(
                        url,
                        params=params,  # Change to params, parameters in URL
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
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            # Check HTTP status code
            if response.status_code >= 400:
                error_msg = f"HTTPError: StatusCode {response.status_code}"
                try:
                    error_detail = response.json()
                    print(f"Request Failed: {error_msg}")
                    print(f"Error Response Details: {error_detail}")
                    error_msg += f" | ErrorDetails: {error_detail}"
                except:
                    print(f"Request Failed: {error_msg}")
                    print(f"Response content: {response.text}")
                    error_msg += f" | Response content: {response.text}"
                raise TooBitException(error_msg)
            
            response.raise_for_status()
            
            # Parse response
            try:
                data = response.json()
            except ValueError as e:
                error_msg = f"Response parsing failed: Unable to parse JSON response, Status code: {response.status_code}, Response content: {response.text}"
                print(f"Request Failed: {error_msg}")
                raise TooBitException(error_msg)
            
            # Check API error
            if 'code' in data and data['code'] != 200 and data['code'] != 0:
                error_msg = f"APIError: ErrorCode {data['code']}, ErrorInformation: {data.get('msg', '')}"
                print(f"Request Failed: {error_msg}")
                print(f"Complete error response: {data}")
                raise_toobit_exception(data['code'], data.get('msg', ''), data)
            
            return data
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Network request error: {str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.json()
                    print(f"Request Failed Details: {error_detail}")
                    error_msg += f" | ResponseDetails: {error_detail}"
                except:
                    error_msg += f" | HTTP status code: {e.response.status_code} | Response content: {e.response.text}"
            print(f"Request Failed: {error_msg}")
            raise TooBitException(error_msg)
        except ValueError as e:
            error_msg = f"ParametersError: {str(e)}"
            print(f"Request Failed: {error_msg}")
            raise TooBitException(error_msg)
        except Exception as e:
            error_msg = f"Unknown error: {str(e)}"
            print(f"Request Failed: {error_msg}")
            raise TooBitException(error_msg)
    
    # ==================== Spot Signature API ====================
    
    # ==================== Spot Signature API ====================
    
    def create_order(self, order_request: OrderRequest) -> CreateOrderResponse:
        """Create Order"""
        params = order_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/spot/order', params, signed=True)
        return CreateOrderResponse(**response)
    
    def batch_create_orders(self, order_requests: list[OrderRequest]) -> BatchCreateOrderResponse:
        """Batch Create Order"""
        # Convert multiple order requests to parameters list
        orders_data = []
        for order_request in order_requests:
            order_data = order_request.model_dump(exclude_none=True, by_alias=True)
            orders_data.append(order_data)
        
        # Build request body
        import json
        request_body = json.dumps(orders_data)
        
        # Build query string - only contains authentication related parameters
        params = {}
        
        response = self._make_request('POST', '/api/v1/spot/batchOrders', params, data=request_body, signed=True)
        return BatchCreateOrderResponse(**response)
    
    def batch_cancel_spot_orders(self, order_ids: list[str]) -> BatchCancelOrdersResponse:
        """Spot Batch Cancel Orders"""
        # Build batch cancel orders parameters
        params = {
            'ids': ','.join(order_ids)
        }
        
        response = self._make_request('DELETE', '/api/v1/spot/cancelOrderByIds', params, signed=True)
        return BatchCancelOrdersResponse(**response)

    def cancel_open_orders(self, symbol: Optional[str] = None, side: Optional[OrderSide] = None) -> CancelOpenOrdersResponse:
        """Cancel open orders - can specify trading pair and side"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        if side:
            params['side'] = side.value
        
        response = self._make_request('DELETE', '/api/v1/spot/openOrders', params, signed=True)
        return CancelOpenOrdersResponse(**response)

    def cancel_order(self, symbol: str, order_id: Optional[str] = None, client_order_id: Optional[str] = None) -> CancelOrderResponse:
        """Cancel order"""
        # Create cancel order request object
        cancel_request = CancelOrderRequest(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=client_order_id
        )
        params = cancel_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('DELETE', '/api/v1/spot/order', params, signed=True)
        return CancelOrderResponse(**response)
    
    def get_order(self, query_request: OrderQueryRequest) -> OrderResponse:
        """Query Spot Order"""
        params = query_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/spot/order', params, signed=True)
        return OrderResponse(**response)
    
    def get_open_orders(self, symbol: Optional[str] = None) -> list:
        """Query Current Spot Open Orders"""
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
        """Query All Spot Order"""
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
        """Get Spot Account Trade history"""
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
    
    # ==================== FuturesAPI ====================
    
    def transfer_between_accounts(
        self,
        from_account_type: str,
        to_account_type: str,
        asset: str,
        quantity: str
    ) -> list:
        """Master Sub Account Universal Transfer (TRADE)"""
        params = {
            'fromAccountType': from_account_type,
            'toAccountType': to_account_type,
            'asset': asset,
            'quantity': quantity
        }
        response = self._make_request('POST', '/api/v1/subAccount/transfer', params, signed=True)
        return response
    
    def create_futures_order(self, order_request: OrderRequest) -> OrderResponse:
        """Futures Create Order (TRADE)"""
        params = order_request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/futures/order', params, signed=True)
        return CreateFuturesOrderResponse(**response)

    def batch_create_futures_orders(self, order_requests: list[FuturesOrderRequest]) -> BatchCreateFuturesOrdersResponse:
        """Futures Batch Create Order (TRADE)"""
        # Convert multiple order requests to parameters list
        orders_data = []
        for order_request in order_requests:
            order_data = order_request.model_dump(exclude_none=True, by_alias=True)
            orders_data.append(order_data)
        
        # Build request body - directly is order array
        request_body = json.dumps(orders_data)
        
        # Build query string - only contains authentication related parameters
        params = {}
        
        response = self._make_request('POST', '/api/v1/futures/batchOrders', params, data=request_body, signed=True)
        return BatchCreateFuturesOrdersResponse(**response)
    

    
    def get_futures_order(self, symbol: str, order_id: Optional[str] = None, client_order_id: Optional[str] = None) -> QueryFuturesOrderResponse:
        """Query Futures Order (USER_DATA)"""
        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_order_id:
            params['origClientOrderId'] = client_order_id
        
        response = self._make_request('GET', '/api/v1/futures/order', params, signed=True)
        return QueryFuturesOrderResponse(**response)
    
    def cancel_futures_order(self, symbol: str, order_id: Optional[str] = None, client_order_id: Optional[str] = None) -> QueryFuturesOrderResponse:
        """Cancel Futures Order (TRADE)"""
        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_order_id:
            params['origClientOrderId'] = client_order_id
        
        response = self._make_request('DELETE', '/api/v1/futures/order', params, signed=True)
        return QueryFuturesOrderResponse(**response)
    
    def get_futures_open_orders(self, symbol: Optional[str] = None) -> list[FuturesOpenOrderResponse]:
        """View all open orders (USER_DATA)"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        
        response = self._make_request('GET', '/api/v1/futures/openOrders', params, signed=True)
        return [FuturesOpenOrderResponse(**order) for order in response]

    def get_futures_positions(self, symbol: Optional[str] = None, side: Optional[str] = None) -> list[FuturesPosition]:
        """Query Current Position (USER_DATA)"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        if side:
            params['side'] = side
        
        response = self._make_request('GET', '/api/v1/futures/positions', params, signed=True)
        return [FuturesPosition(**position) for position in response]

    def set_position_trading_stop(self, request: SetPositionTradingStopRequest) -> SetPositionTradingStopResponse:
        """Set Position Take Profit Stop Loss (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/futures/position/trading-stop', params, signed=True)
        return SetPositionTradingStopResponse(**response)

    def get_futures_history_orders(self, request: QueryFuturesHistoryOrdersRequest) -> list[QueryFuturesOrderResponse]:
        """Query Historical orders (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/futures/historyOrders', params, signed=True)
        return [QueryFuturesOrderResponse(**order) for order in response]

    def get_futures_balance(self) -> list[FuturesBalance]:
        """Query Futures Account Balance (USER_DATA)"""
        response = self._make_request('GET', '/api/v1/futures/balance', {}, signed=True)
        return [FuturesBalance(**balance) for balance in response]

    def adjust_isolated_margin(self, request: AdjustIsolatedMarginRequest) -> AdjustIsolatedMarginResponse:
        """Adjust Isolated Margin (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/futures/positionMargin', params, signed=True)
        return AdjustIsolatedMarginResponse(**response)

    def get_futures_trade_history(self, request: QueryFuturesTradeHistoryRequest) -> list[FuturesTrade]:
        """Query Futures Account Trade history (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/futures/userTrades', params, signed=True)
        return [FuturesTrade(**trade) for trade in response]

    def get_futures_account_flow(self, request: QueryFuturesAccountFlowRequest) -> list[FuturesAccountFlow]:
        """Query Futures Account Flow (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/futures/balanceFlow', params, signed=True)
        return [FuturesAccountFlow(**flow) for flow in response]

    def get_futures_user_fee_rate(self, request: QueryFuturesUserFeeRateRequest) -> FuturesUserFeeRate:
        """Query Futures User Fee Rate (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/futures/commissionRate', params, signed=True)
        return FuturesUserFeeRate(**response)

    def get_futures_today_pnl(self) -> FuturesTodayPnL:
        """Query Futures Today PnL (USER_DATA)"""
        response = self._make_request('GET', '/api/v1/futures/todayPnL', {}, signed=True)
        return FuturesTodayPnL(**response)

    def change_margin_type(self, request: ChangeMarginTypeRequest) -> ChangeMarginTypeResponse:
        """Change to Cross Mode (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/futures/marginType', params, signed=True)
        return ChangeMarginTypeResponse(**response)

    def adjust_leverage(self, request: AdjustLeverageRequest) -> AdjustLeverageResponse:
        """Adjust Open Leverage (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('POST', '/api/v1/futures/leverage', params, signed=True)
        return AdjustLeverageResponse(**response)

    def get_account_leverage(self, request: QueryLeverageRequest) -> list[AccountLeverage]:
        """Query Leverage Multiple And Position Mode (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        response = self._make_request('GET', '/api/v1/futures/accountLeverage', params, signed=True)
        return [AccountLeverage(**leverage) for leverage in response]

    def get_spot_account_info(self) -> SpotAccountInfo:
        """Query Spot Account information (USER_DATA)"""
        response = self._make_request('GET', '/api/v1/account', {}, signed=True)
        return SpotAccountInfo(**response)

    def get_spot_sub_accounts(self) -> list[SpotSubAccount]:
        """Query Spot Sub Account (USER_DATA)"""
        response = self._make_request('GET', '/api/v1/account/subAccount', {}, signed=True)
        return [SpotSubAccount(**account) for account in response]

    def get_api_key_type(self) -> ApiKeyType:
        """Get API KEY Type (USER_DATA)"""
        response = self._make_request('GET', '/api/v1/account/checkApiKey', {}, signed=True)
        return ApiKeyType(**response)
    

    

    

    
    def get_transfer_history(
        self,
        asset: Optional[str] = None,
        from_account_type: Optional[str] = None,
        to_account_type: Optional[str] = None,
        limit: int = 100
    ) -> list:
        """Get Transfer History"""
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
        """Cancel All Order (TRADE)"""
        params = {'symbol': symbol}
        response = self._make_request('DELETE', '/api/v1/futures/batchOrders', params, signed=True)
        return CancelAllOrdersResponse(**response)
    
    def batch_cancel_orders(self, symbol: str, order_ids: list[str]) -> BatchCancelOrdersResponse:
        """Batch Cancel order (TRADE)"""
        params = {
            'symbol': symbol,
            'orderIds': ','.join(order_ids)
        }
        response = self._make_request('DELETE', '/api/v1/futures/batchOrders', params, signed=True)
        return BatchCancelOrdersResponse(**response)
    

    
    def close(self):
        """Close client"""
        if self.session:
            self.session.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
