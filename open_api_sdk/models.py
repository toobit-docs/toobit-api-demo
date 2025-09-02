"""
TooBit API 数据模型
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class OrderSide(str, Enum):
    """订单方向"""
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    """订单类型"""
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    STOP_LOSS = "STOP_LOSS"
    STOP_LOSS_LIMIT = "STOP_LOSS_LIMIT"
    TAKE_PROFIT = "TAKE_PROFIT"
    TAKE_PROFIT_LIMIT = "TAKE_PROFIT_LIMIT"
    LIMIT_MAKER = "LIMIT_MAKER"


class TimeInForce(str, Enum):
    """订单有效期"""
    GTC = "GTC"  # Good Till Canceled
    IOC = "IOC"  # Immediate or Cancel
    FOK = "FOK"  # Fill or Kill


class OrderStatus(str, Enum):
    """订单状态"""
    NEW = "NEW"
    PENDING_NEW = "PENDING_NEW"  # 新增：等待新订单状态
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELED = "CANCELED"
    PENDING_CANCEL = "PENDING_CANCEL"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"


class APIResponse(BaseModel):
    """API响应基础模型"""
    success: bool = Field(..., description="请求是否成功")
    data: Optional[Any] = Field(None, description="响应数据")
    message: Optional[str] = Field(None, description="响应消息")
    code: Optional[int] = Field(None, description="响应代码")


class RequestConfig(BaseModel):
    """请求配置"""
    timeout: Optional[int] = Field(None, description="请求超时时间")
    headers: Optional[Dict[str, str]] = Field(default_factory=dict, description="请求头")
    params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="请求参数")


class OrderRequest(BaseModel):
    """下单请求模型"""
    symbol: str = Field(..., description="交易对")
    side: OrderSide = Field(..., description="订单方向")
    type: OrderType = Field(..., description="订单类型")
    quantity: Optional[float] = Field(None, description="数量")
    price: Optional[float] = Field(None, description="价格")
    time_in_force: Optional[TimeInForce] = Field(TimeInForce.GTC, description="订单有效期", alias="timeInForce")
    stop_price: Optional[float] = Field(None, description="止损价格", alias="stopPrice")
    iceberg_qty: Optional[float] = Field(None, description="冰山数量", alias="icebergQty")
    new_client_order_id: Optional[str] = Field(None, description="客户端订单ID", alias="newClientOrderId")
    recv_window: Optional[int] = Field(None, description="接收窗口", alias="recvWindow")

    
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class CreateOrderResponse(BaseModel):
    """创建订单响应模型 - 根据实际API响应"""
    account_id: str = Field(..., description="账户ID", alias="accountId")
    symbol: str = Field(..., description="交易对")
    symbol_name: str = Field(..., description="交易对名称", alias="symbolName")
    client_order_id: str = Field(..., description="客户端订单ID", alias="clientOrderId")
    order_id: str = Field(..., description="订单ID", alias="orderId")
    transact_time: str = Field(..., description="交易时间", alias="transactTime")
    price: str = Field(..., description="价格")
    orig_qty: str = Field(..., description="原始数量", alias="origQty")
    executed_qty: str = Field(..., description="已执行数量", alias="executedQty")
    status: OrderStatus = Field(..., description="订单状态")
    time_in_force: TimeInForce = Field(..., description="订单有效期", alias="timeInForce")
    type: OrderType = Field(..., description="订单类型")
    side: OrderSide = Field(..., description="订单方向")
    
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class OrderResponse(BaseModel):
    """查询订单响应模型 - 查询挂单、订单状态时返回"""
    symbol: str = Field(..., description="交易对")
    order_id: str = Field(..., description="订单ID", alias="orderId")
    client_order_id: str = Field(..., description="客户端订单ID", alias="clientOrderId")
    price: str = Field(..., description="价格")
    orig_qty: str = Field(..., description="原始数量", alias="origQty")
    executed_qty: str = Field(..., description="已执行数量", alias="executedQty")
    cummulative_quote_qty: str = Field(..., description="累计成交金额", alias="cummulativeQuoteQty")
    status: OrderStatus = Field(..., description="订单状态")
    time_in_force: TimeInForce = Field(..., description="订单有效期", alias="timeInForce")
    type: OrderType = Field(..., description="订单类型")
    side: OrderSide = Field(..., description="订单方向")
    stop_price: str = Field(..., description="止损价格", alias="stopPrice")
    iceberg_qty: str = Field(..., description="冰山数量", alias="icebergQty")
    time: str = Field(..., description="订单时间", alias="time")
    update_time: str = Field(..., description="更新时间", alias="updateTime")
    is_working: bool = Field(..., description="是否在工作", alias="isWorking")
    
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class CancelOrderRequest(BaseModel):
    """取消订单请求模型"""
    symbol: str = Field(..., description="交易对")
    order_id: Optional[str] = Field(None, description="订单ID", alias="orderId")
    orig_client_order_id: Optional[str] = Field(None, description="原始客户端订单ID", alias="origClientOrderId")
    new_client_order_id: Optional[str] = Field(None, description="新客户端订单ID", alias="newClientOrderId")
    recv_window: Optional[int] = Field(None, description="接收窗口", alias="recvWindow")
    
    model_config = ConfigDict(populate_by_name=True)


class CancelOrderResponse(BaseModel):
    """取消订单响应模型 - 根据实际API响应"""
    symbol: str = Field(..., description="交易对")
    order_id: str = Field(..., description="订单ID", alias="orderId")
    client_order_id: str = Field(..., description="客户端订单ID", alias="clientOrderId")
    price: str = Field(..., description="价格")
    orig_qty: str = Field(..., description="原始数量", alias="origQty")
    executed_qty: str = Field(..., description="已执行数量", alias="executedQty")
    status: OrderStatus = Field(..., description="订单状态")
    time_in_force: TimeInForce = Field(..., description="订单有效期", alias="timeInForce")
    type: OrderType = Field(..., description="订单类型")
    side: OrderSide = Field(..., description="订单方向")
    transact_time: str = Field(..., description="交易时间", alias="transactTime")
    
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class OrderQueryRequest(BaseModel):
    """查询订单请求模型"""
    symbol: str = Field(..., description="交易对")
    order_id: Optional[int] = Field(None, description="订单ID", alias="orderId")
    orig_client_order_id: Optional[str] = Field(None, description="原始客户端订单ID", alias="origClientOrderId")
    recv_window: Optional[int] = Field(None, description="接收窗口", alias="recvWindow")
    
    model_config = ConfigDict(populate_by_name=True)


class Trade(BaseModel):
    """成交记录模型"""
    id: int = Field(..., description="成交ID")
    price: float = Field(..., description="成交价格")
    qty: float = Field(..., description="成交数量")
    commission: float = Field(..., description="手续费")
    commission_asset: str = Field(..., description="手续费资产", alias="commissionAsset")
    time: int = Field(..., description="成交时间")
    is_buyer: bool = Field(..., description="是否买方", alias="isBuyer")
    is_maker: bool = Field(..., description="是否挂单方", alias="isMaker")
    is_best_match: bool = Field(..., description="是否最佳匹配", alias="isBestMatch")
    
    model_config = ConfigDict(populate_by_name=True)


class AccountInfo(BaseModel):
    """账户信息模型"""
    maker_commission: int = Field(..., description="挂单手续费", alias="makerCommission")
    taker_commission: int = Field(..., description="吃单手续费", alias="takerCommission")
    buyer_commission: int = Field(..., description="买方手续费", alias="buyerCommission")
    seller_commission: int = Field(..., description="卖方手续费", alias="sellerCommission")
    can_trade: bool = Field(..., description="是否可以交易", alias="canTrade")
    can_withdraw: bool = Field(..., description="是否可以提现", alias="canWithdraw")
    can_deposit: bool = Field(..., description="是否可以充值", alias="canDeposit")
    update_time: int = Field(..., description="更新时间", alias="updateTime")
    account_type: str = Field(..., description="账户类型", alias="accountType")
    balances: List[Dict[str, Any]] = Field(..., description="余额列表")
    
    model_config = ConfigDict(populate_by_name=True)


class ExchangeInfo(BaseModel):
    """交易所信息模型"""
    timezone: Optional[str] = Field(None, description="时区")
    server_time: Optional[int] = Field(None, description="服务器时间", alias="serverTime")
    rate_limits: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="速率限制", alias="rateLimits")
    broker_filters: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="交易所过滤器", alias="brokerFilters")
    symbols: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="交易对列表")
    
    model_config = ConfigDict(populate_by_name=True)


class Ticker24hr(BaseModel):
    """24小时价格变动模型"""
    symbol: str = Field(..., description="交易对")
    price_change: float = Field(..., description="价格变动", alias="priceChange")
    price_change_percent: float = Field(..., description="价格变动百分比", alias="priceChangePercent")
    weighted_avg_price: float = Field(..., description="加权平均价格", alias="weightedAvgPrice")
    prev_close_price: float = Field(..., description="前收盘价", alias="prevClosePrice")
    last_price: float = Field(..., description="最新价格", alias="lastPrice")
    last_qty: float = Field(..., description="最新成交量", alias="lastQty")
    bid_price: float = Field(..., description="买一价", alias="bidPrice")
    ask_price: float = Field(..., description="卖一价", alias="askPrice")
    open_price: float = Field(..., description="开盘价", alias="openPrice")
    high_price: float = Field(..., description="最高价", alias="highPrice")
    low_price: float = Field(..., description="最低价", alias="lowPrice")
    volume: float = Field(..., description="成交量")
    quote_volume: float = Field(..., description="成交额", alias="quoteVolume")
    open_time: int = Field(..., description="开盘时间", alias="openTime")
    close_time: int = Field(..., description="收盘时间", alias="closeTime")
    first_id: Optional[int] = Field(None, description="首笔成交ID", alias="firstId")
    last_id: Optional[int] = Field(None, description="末笔成交ID", alias="lastId")
    count: int = Field(..., description="成交笔数")
    
    model_config = ConfigDict(populate_by_name=True)


class DepthEntry(BaseModel):
    """深度条目模型"""
    price: float = Field(..., description="价格")
    quantity: float = Field(..., description="数量")


class OrderBook(BaseModel):
    """订单簿模型"""
    last_update_id: Optional[int] = Field(None, description="最后更新ID", alias="lastUpdateId")
    bids: Optional[List[List[float]]] = Field(default_factory=list, description="买单 [价格, 数量]")
    asks: Optional[List[List[float]]] = Field(default_factory=list, description="卖单 [价格, 数量]")
    
    model_config = ConfigDict(populate_by_name=True)


class Kline(BaseModel):
    """K线模型"""
    open_time: int = Field(..., description="开盘时间", alias="openTime")
    open: float = Field(..., description="开盘价")
    high: float = Field(..., description="最高价")
    low: float = Field(..., description="最低价")
    close: float = Field(..., description="收盘价")
    volume: float = Field(..., description="成交量")
    close_time: int = Field(..., description="收盘时间", alias="closeTime")
    quote_asset_volume: float = Field(..., description="成交额", alias="quoteAssetVolume")
    number_of_trades: int = Field(..., description="成交笔数", alias="numberOfTrades")
    taker_buy_base_asset_volume: float = Field(..., description="主动买入成交量", alias="takerBuyBaseAssetVolume")
    taker_buy_quote_asset_volume: float = Field(..., description="主动买入成交额", alias="takerBuyQuoteAssetVolume")
    
    model_config = ConfigDict(populate_by_name=True) 