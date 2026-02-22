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
    OrderRequest, CancelOrderRequest,
    OrderQueryRequest, OrderSide,
    FuturesOrderRequest, SetPositionTradingStopRequest,
    QueryFuturesHistoryOrdersRequest, AdjustIsolatedMarginRequest, QueryFuturesTradeHistoryRequest, QueryFuturesAccountFlowRequest,
    QueryFuturesUserFeeRateRequest,
    ChangeMarginTypeRequest,
    AdjustLeverageRequest,
    QueryLeverageRequest
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
    
    # ==================== Market Data API ====================
    
    def ping(self) -> Dict[str, Any]:
        """Test Server Connectivity"""
        return self._make_request('GET', '/quote/v1/ping')
    
    def get_server_time(self) -> Dict[str, Any]:
        """Get Server Time"""
        return self._make_request('GET', '/quote/v1/time')
    
    def get_exchange_info(self) -> Dict[str, Any]:
        """Get Trade All Information"""
        return self._make_request('GET', '/api/v1/exchangeInfo')
    
    def get_order_book(self, symbol: str, limit: int = 100) -> Dict[str, Any]:
        """Get Order Book Depth Information"""
        params = {
            'symbol': symbol,
            'limit': limit
        }
        return self._make_request('GET', '/quote/v1/depth', params)
    
    def get_recent_trades(self, symbol: str, limit: int = 100) -> list:
        """Get Recent Trades Record"""
        params = {
            'symbol': symbol,
            'limit': limit
        }
        return self._make_request('GET', '/quote/v1/trades', params)
    
    def get_klines(self, symbol: str, interval: str, limit: int = 500) -> list:
        """Get KLine Data"""
        params = {
            'symbol': symbol,
            'interval': interval,
            'limit': limit
        }
        return self._make_request('GET', '/quote/v1/klines', params)
    
    def get_24hr_ticker(self, symbol: Optional[str] = None) -> Union[Dict[str, Any], list]:
        """Get 24-hour price change statistics"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        return self._make_request('GET', '/quote/v1/ticker/24hr', params)
    
    def get_latest_price(self, symbol: Optional[str] = None) -> list:
        """Get Latest Price"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        return self._make_request('GET', '/quote/v1/ticker/price', params)
    
    def get_all_prices(self) -> list:
        """Get All Trading Pair of Latest Price"""
        return self.get_latest_price()
    
    def get_best_order_book(self, symbol: Optional[str] = None) -> list:
        """Get Best Open Orders Information (bookTicker)"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        return self._make_request('GET', '/quote/v1/ticker/bookTicker', params)

    # ==================== Spot Signature API ====================
    
    def create_order(self, order_request: OrderRequest) -> Dict[str, Any]:
        """Create Order"""
        params = order_request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('POST', '/api/v1/spot/order', params, signed=True)
    
    def batch_create_orders(self, order_requests: list[OrderRequest]) -> Dict[str, Any]:
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
        
        return self._make_request('POST', '/api/v1/spot/batchOrders', params, data=request_body, signed=True)
    
    def batch_cancel_spot_orders(self, order_ids: list[str]) -> Dict[str, Any]:
        """Spot Batch Cancel Orders"""
        # Build batch cancel orders parameters
        params = {
            'ids': ','.join(order_ids)
        }
        
        return self._make_request('DELETE', '/api/v1/spot/cancelOrderByIds', params, signed=True)

    def cancel_open_orders(self, symbol: Optional[str] = None, side: Optional[OrderSide] = None) -> Dict[str, Any]:
        """Cancel open orders - can specify trading pair and side"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        if side:
            params['side'] = side.value
        
        return self._make_request('DELETE', '/api/v1/spot/openOrders', params, signed=True)

    def cancel_order(self, symbol: str, order_id: Optional[str] = None, client_order_id: Optional[str] = None) -> Dict[str, Any]:
        """Cancel order"""
        # Create cancel order request object
        cancel_request = CancelOrderRequest(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=client_order_id
        )
        params = cancel_request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('DELETE', '/api/v1/spot/order', params, signed=True)
    
    def get_order(self, query_request: OrderQueryRequest) -> Dict[str, Any]:
        """Query Spot Order"""
        params = query_request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('GET', '/api/v1/spot/order', params, signed=True)
    
    def get_open_orders(self, symbol: Optional[str] = None) -> list:
        """Query Current Spot Open Orders"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        
        return self._make_request('GET', '/api/v1/spot/openOrders', params, signed=True)
    
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
        
        return self._make_request('GET', '/api/v1/spot/tradeOrders', params, signed=True)

    
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
        quantity: str,
        from_uid: Optional[int] = None,
        to_uid: Optional[int] = None
    ) -> list:
        """Master Sub Account Universal Transfer (TRADE)"""
        params = {
            'fromAccountType': from_account_type,
            'toAccountType': to_account_type,
            'asset': asset,
            'quantity': quantity
        }
        if from_uid:
            params['fromUid'] = from_uid
        if to_uid:
            params['toUid'] = to_uid
        response = self._make_request('POST', '/api/v1/subAccount/transfer', params, signed=True)
        return response
    
    def create_futures_order(self, order_request: OrderRequest) -> Dict[str, Any]:
        """Futures Create Order (TRADE)"""
        params = order_request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('POST', '/api/v1/futures/order', params, signed=True)

    def batch_create_futures_orders(self, order_requests: list[FuturesOrderRequest]) -> Dict[str, Any]:
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
        
        return self._make_request('POST', '/api/v1/futures/batchOrders', params, data=request_body, signed=True)
    

    
    def get_futures_order(
        self,
        symbol: str,
        order_id: Optional[str] = None,
        client_order_id: Optional[str] = None,
        order_type: Optional[str] = None,
        category: Optional[str] = None
    ) -> Dict[str, Any]:
        """Query Futures Order (USER_DATA)"""
        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_order_id:
            params['origClientOrderId'] = client_order_id
        if order_type:
            params['type'] = order_type
        if category:
            params['category'] = category
        
        return self._make_request('GET', '/api/v1/futures/order', params, signed=True)
    
    def cancel_futures_order(
        self,
        symbol: str,
        order_id: Optional[str] = None,
        client_order_id: Optional[str] = None,
        order_type: Optional[str] = None,
        category: Optional[str] = None
    ) -> Dict[str, Any]:
        """Cancel Futures Order (TRADE)"""
        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_order_id:
            params['origClientOrderId'] = client_order_id
        if order_type:
            params['type'] = order_type
        if category:
            params['category'] = category
        
        return self._make_request('DELETE', '/api/v1/futures/order', params, signed=True)
    
    def get_futures_open_orders(
        self,
        symbol: Optional[str] = None,
        order_id: Optional[int] = None,
        order_type: Optional[str] = None,
        limit: int = 20,
        category: Optional[str] = None,
        recv_window: Optional[int] = None
    ) -> list:
        """View all open orders (USER_DATA)"""
        params = {'limit': limit}
        if symbol:
            params['symbol'] = symbol
        if order_id:
            params['orderId'] = order_id
        if order_type:
            params['type'] = order_type
        if category:
            params['category'] = category
        if recv_window:
            params['recvWindow'] = recv_window
        
        return self._make_request('GET', '/api/v1/futures/openOrders', params, signed=True)

    def get_futures_positions(
        self,
        symbol: Optional[str] = None,
        side: Optional[str] = None,
        category: Optional[str] = None,
        recv_window: Optional[int] = None
    ) -> list:
        """Query Current Position (USER_DATA)"""
        params = {}
        if symbol:
            params['symbol'] = symbol
        if side:
            params['side'] = side
        if category:
            params['category'] = category
        if recv_window:
            params['recvWindow'] = recv_window
        
        return self._make_request('GET', '/api/v1/futures/positions', params, signed=True)

    def set_position_trading_stop(self, request: SetPositionTradingStopRequest) -> Dict[str, Any]:
        """Set Position Take Profit Stop Loss (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('POST', '/api/v1/futures/position/trading-stop', params, signed=True)

    def get_futures_history_orders(self, request: QueryFuturesHistoryOrdersRequest) -> list:
        """Query Historical orders (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('GET', '/api/v1/futures/historyOrders', params, signed=True)

    def get_futures_balance(self) -> list:
        """Query Futures Account Balance (USER_DATA)"""
        return self._make_request('GET', '/api/v1/futures/balance', {}, signed=True)

    def adjust_isolated_margin(self, request: AdjustIsolatedMarginRequest) -> Dict[str, Any]:
        """Adjust Isolated Margin (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('POST', '/api/v1/futures/positionMargin', params, signed=True)

    def get_futures_trade_history(self, request: QueryFuturesTradeHistoryRequest) -> list:
        """Query Futures Account Trade history (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('GET', '/api/v1/futures/userTrades', params, signed=True)

    def get_futures_account_flow(self, request: QueryFuturesAccountFlowRequest) -> list:
        """Query Futures Account Flow (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('GET', '/api/v1/futures/balanceFlow', params, signed=True)

    def get_futures_user_fee_rate(self, request: QueryFuturesUserFeeRateRequest) -> Dict[str, Any]:
        """Query Futures User Fee Rate (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('GET', '/api/v1/futures/commissionRate', params, signed=True)

    def get_futures_today_pnl(self) -> Dict[str, Any]:
        """Query Futures Today PnL (USER_DATA)"""
        return self._make_request('GET', '/api/v1/futures/todayPnL', {}, signed=True)

    def change_margin_type(self, request: ChangeMarginTypeRequest) -> Dict[str, Any]:
        """Change to Cross Mode (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('POST', '/api/v1/futures/marginType', params, signed=True)

    def adjust_leverage(self, request: AdjustLeverageRequest) -> Dict[str, Any]:
        """Adjust Open Leverage (TRADE)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('POST', '/api/v1/futures/leverage', params, signed=True)

    def get_account_leverage(self, request: QueryLeverageRequest) -> list:
        """Query Leverage Multiple And Position Mode (USER_DATA)"""
        params = request.model_dump(exclude_none=True, by_alias=True)
        return self._make_request('GET', '/api/v1/futures/accountLeverage', params, signed=True)

    def get_spot_account_info(self) -> Dict[str, Any]:
        """Query Spot Account information (USER_DATA)"""
        return self._make_request('GET', '/api/v1/account', {}, signed=True)

    def get_spot_sub_accounts(self) -> list:
        """Query Spot Sub Account (USER_DATA)"""
        return self._make_request('GET', '/api/v1/account/subAccount', {}, signed=True)

    def get_api_key_type(self) -> Dict[str, Any]:
        """Get API KEY Type (USER_DATA)"""
        return self._make_request('GET', '/api/v1/account/checkApiKey', {}, signed=True)

    def get_sub_accounts(self, user_id: Optional[int] = None, email: Optional[str] = None) -> list:
        """Query Sub Account (USER_DATA)"""
        params = {}
        if user_id:
            params['userId'] = user_id
        if email:
            params['email'] = email
        return self._make_request('GET', '/api/v1/subAccount/list', params, signed=True)
    

    

    

    
    def get_transfer_history(
        self,
        asset: Optional[str] = None,
        from_account_type: Optional[str] = None,
        to_account_type: Optional[str] = None,
        limit: int = 100,
        flow_type: Optional[int] = None
    ) -> list:
        """Get Transfer History"""
        params = {'limit': limit}
        if asset:
            params['asset'] = asset
        if from_account_type:
            params['fromAccountType'] = from_account_type
        if to_account_type:
            params['toAccountType'] = to_account_type
        if flow_type:
            params['flowType'] = flow_type
        
        response = self._make_request('GET', '/api/v1/account/balanceFlow', params, signed=True)
        return response
    
    def cancel_all_orders(self, symbol: str) -> Dict[str, Any]:
        """Cancel All Order (TRADE)"""
        params = {'symbol': symbol}
        return self._make_request('DELETE', '/api/v1/futures/batchOrders', params, signed=True)
    
    def batch_cancel_orders(self, symbol: str, order_ids: list[str]) -> Dict[str, Any]:
        """Batch Cancel order (TRADE)"""
        params = {
            'symbol': symbol,
            'orderIds': ','.join(order_ids)
        }
        return self._make_request('DELETE', '/api/v1/futures/batchOrders', params, signed=True)
    

    
    def close(self):
        """Close client"""
        if self.session:
            self.session.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
