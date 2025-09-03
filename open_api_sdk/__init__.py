"""
TooBit API SDK - 一个功能完整的加密货币交易所API客户端库
"""

from .client import TooBitClient
from .config import TooBitConfig
from .exceptions import TooBitException, APIError, ConfigurationError, AuthenticationError, OrderError, RateLimitError, ValidationError, NetworkError
from .models import (
    OrderRequest, CreateOrderResponse, OrderResponse, CancelOrderRequest, CancelOrderResponse,
    OrderQueryRequest, Trade, ExchangeInfo, Ticker24hr,
    OrderBook, Kline, OrderSide, OrderType, TimeInForce, OrderStatus, 
    CreateFuturesOrderResponse, CancelFuturesOrderResponse, QueryFuturesOrderResponse,
    FuturesOpenOrderResponse, CancelAllOrdersResponse, BatchCancelOrderResult, BatchCancelOrdersResponse,
    BatchCreateOrderResponse
)

__version__ = "1.0.0"
__all__ = [
    "TooBitClient",
    "TooBitConfig", 
    "TooBitException",
    "APIError",
    "ConfigurationError",
    "AuthenticationError",
    "OrderError",
    "RateLimitError",
    "ValidationError",
    "NetworkError",
    "OrderRequest",
    "OrderResponse",
    "CancelOrderRequest",
    "CancelOrderResponse",
    "OrderQueryRequest",
    "Trade",
    "AccountInfo",
    "ExchangeInfo",
    "Ticker24hr",
    "OrderBook",
    "Kline",
    "OrderSide",
    "OrderType",
    "TimeInForce",
    "OrderStatus",
    "CreateFuturesOrderResponse",
    "CancelFuturesOrderResponse",
    "QueryFuturesOrderResponse",
    "FuturesOpenOrderResponse",
    "CancelAllOrdersResponse",
    "BatchCancelOrderResult",
    "BatchCancelOrdersResponse",
    "BatchCreateOrderResponse"
] 