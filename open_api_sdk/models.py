"""
TooBit API Data Models
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class OrderSide(str, Enum):
    """Order side"""
    # Spot trading directions
    BUY = "BUY"
    SELL = "SELL"
    
    # Futures trading directions
    BUY_OPEN = "BUY_OPEN"      # Buy to open (long position)
    SELL_OPEN = "SELL_OPEN"    # Sell to open (short position)
    BUY_CLOSE = "BUY_CLOSE"    # Buy to close (close short)
    SELL_CLOSE = "SELL_CLOSE"  # Sell to close (close long)


class OrderType(str, Enum):
    """Order type"""
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    STOP_LOSS = "STOP_LOSS"
    STOP_LOSS_LIMIT = "STOP_LOSS_LIMIT"
    TAKE_PROFIT = "TAKE_PROFIT"
    TAKE_PROFIT_LIMIT = "TAKE_PROFIT_LIMIT"
    LIMIT_MAKER = "LIMIT_MAKER"


class TimeInForce(str, Enum):
    """Order time in force"""
    GTC = "GTC"  # Good Till Canceled
    IOC = "IOC"  # Immediate or Cancel
    FOK = "FOK"  # Fill or Kill


class OrderStatus(str, Enum):
    """Order status"""
    NEW = "NEW"
    PENDING_NEW = "PENDING_NEW"  # New: Pending new order status
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELED = "CANCELED"
    PENDING_CANCEL = "PENDING_CANCEL"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"


class APIResponse(BaseModel):
    """API Response base model"""
    success: bool = Field(..., description="Whether request is successful")
    data: Optional[Any] = Field(None, description="Response data")
    message: Optional[str] = Field(None, description="Response message")
    code: Optional[int] = Field(None, description="Response code")


class RequestConfig(BaseModel):
    """Request configuration"""
    timeout: Optional[int] = Field(None, description="Request timeout time")
    headers: Optional[Dict[str, str]] = Field(default_factory=dict, description="Request header")
    params: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Request parameters")


class OrderRequest(BaseModel):
    """Create Order Request model"""
    symbol: str = Field(..., description="Symbol")
    side: OrderSide = Field(..., description="Order Side")
    type: OrderType = Field(..., description="Order type")
    quantity: Optional[float] = Field(None, description="Quantity")
    price: Optional[float] = Field(None, description="Price")
    time_in_force: Optional[TimeInForce] = Field(TimeInForce.GTC, description="Order time in force", alias="timeInForce")
    stop_price: Optional[float] = Field(None, description="Stop Loss Price", alias="stopPrice")
    iceberg_qty: Optional[float] = Field(None, description="Iceberg quantity", alias="icebergQty")
    new_client_order_id: Optional[str] = Field(None, description="Client order ID", alias="newClientOrderId")
    recv_window: Optional[int] = Field(None, description="Receive window", alias="recvWindow")

    
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class CreateOrderResponse(BaseModel):
    """Create Order Response model - based on actual API response"""
    account_id: str = Field(..., description="Account ID", alias="accountId")
    symbol: str = Field(..., description="Symbol")
    symbol_name: str = Field(..., description="Symbol Name", alias="symbolName")
    client_order_id: str = Field(..., description="Client order ID", alias="clientOrderId")
    order_id: str = Field(..., description="Order ID", alias="orderId")
    transact_time: str = Field(..., description="Trade Time", alias="transactTime")
    price: str = Field(..., description="Price")
    orig_qty: str = Field(..., description="Original quantity", alias="origQty")
    executed_qty: str = Field(..., description="Executed quantity", alias="executedQty")
    status: OrderStatus = Field(..., description="Order status")
    time_in_force: TimeInForce = Field(..., description="Order time in force", alias="timeInForce")
    type: OrderType = Field(..., description="Order type")
    side: OrderSide = Field(..., description="Order Side")
    
    model_config = ConfigDict(use_enum_values=True)


class CreateFuturesOrderResponse(BaseModel):
    """Futures Create Order Response model - Based on actual API response"""
    time: str = Field(..., description="Order creation time timestamp")
    updateTime: str = Field(..., description="Order last update time timestamp")
    orderId: str = Field(..., description="Order ID")
    clientOrderId: str = Field(..., description="User-defined order ID")
    symbol: str = Field(..., description="Symbol")
    price: str = Field(..., description="Order price")
    leverage: str = Field(..., description="Order leverage")
    origQty: str = Field(..., description="Order quantity")
    executedQty: str = Field(..., description="Order Executed quantity")
    avgPrice: str = Field(..., description="Average trade price")
    marginLocked: str = Field(..., description="Margin locked by this order")
    type: OrderType = Field(..., description="Order type (LIMIT and STOP)")
    side: OrderSide = Field(..., description="Order Side")
    timeInForce: TimeInForce = Field(..., description="Time in force order type")
    status: OrderStatus = Field(..., description="Order status")
    priceType: str = Field(..., description="Price type (INPUT, OPPONENT, QUEUE, OVER, MARKET)")
    
    model_config = ConfigDict(use_enum_values=True)


class CancelFuturesOrderResponse(BaseModel):
    """Futures Cancel Order Response model - Based on actual API response"""
    time: str = Field(..., description="Order creation time timestamp")
    updateTime: str = Field(..., description="Order last update time timestamp")
    orderId: str = Field(..., description="Order ID")
    clientOrderId: str = Field(..., description="User-defined order ID")
    symbol: str = Field(..., description="Symbol")
    price: str = Field(..., description="Order price")
    leverage: str = Field(..., description="Order leverage")
    origQty: str = Field(..., description="Order quantity")
    executedQty: str = Field(..., description="Order Executed quantity")
    avgPrice: str = Field(..., description="Average trade price")
    marginLocked: str = Field(..., description="Margin locked by this order")
    type: OrderType = Field(..., description="Order type (LIMIT and STOP)")
    side: OrderSide = Field(..., description="Order Side")
    timeInForce: TimeInForce = Field(..., description="Time in force order type")
    status: OrderStatus = Field(..., description="Order status")
    priceType: str = Field(..., description="Price type (INPUT, OPPONENT, QUEUE, OVER, MARKET)")
    
    model_config = ConfigDict(use_enum_values=True)


class QueryFuturesOrderResponse(BaseModel):
    """Futures Query Order Response model - Based on actual API response"""
    time: str = Field(..., description="Order creation time timestamp")
    updateTime: str = Field(..., description="Order last update time timestamp")
    orderId: str = Field(..., description="Order ID")
    clientOrderId: str = Field(..., description="User-defined order ID")
    symbol: str = Field(..., description="Symbol")
    price: str = Field(..., description="Order price")
    leverage: str = Field(..., description="Order leverage")
    origQty: str = Field(..., description="Order quantity")
    executedQty: str = Field(..., description="Order Executed quantity")
    avgPrice: str = Field(..., description="Average trade price")
    marginLocked: str = Field(..., description="Margin locked by this order")
    type: OrderType = Field(..., description="Order type (LIMIT and STOP)")
    side: OrderSide = Field(..., description="Order Side")
    timeInForce: TimeInForce = Field(..., description="Time in force order type")
    status: OrderStatus = Field(..., description="Order status")
    priceType: str = Field(..., description="Price type (INPUT, OPPONENT, QUEUE, OVER, MARKET)")
    
    model_config = ConfigDict(use_enum_values=True)


class FuturesOpenOrderResponse(BaseModel):
    """Futures Open Orders Response model - Based on actual API response"""
    time: str = Field(..., description="Order creation time timestamp")
    updateTime: str = Field(..., description="Order last update time timestamp")
    orderId: str = Field(..., description="Order ID")
    clientOrderId: str = Field(..., description="User-defined order ID")
    symbol: str = Field(..., description="Symbol")
    price: str = Field(..., description="Order price")
    leverage: str = Field(..., description="Order leverage")
    origQty: str = Field(..., description="Order quantity")
    executedQty: str = Field(..., description="Order Executed quantity")
    avgPrice: str = Field(..., description="Average trade price")
    marginLocked: str = Field(..., description="Margin locked by this order")
    type: OrderType = Field(..., description="Order type (LIMIT and STOP)")
    side: OrderSide = Field(..., description="Order Side")
    timeInForce: TimeInForce = Field(..., description="Time in force order type")
    status: OrderStatus = Field(..., description="Order status")
    priceType: str = Field(..., description="Price type (INPUT, OPPONENT, QUEUE, OVER, MARKET)")
    
    model_config = ConfigDict(use_enum_values=True)


class CancelAllOrdersResponse(BaseModel):
    """Cancel All Order Response model - Based on actual API response"""
    code: int = Field(..., description="Response code")
    message: str = Field(..., description="Response message")
    timestamp: int = Field(..., description="Time Timestamp")
    
    model_config = ConfigDict()


class BatchCancelOrderResult(BaseModel):
    """Batch Cancel Orders Result item model"""
    orderId: str = Field(..., description="Order ID")
    code: int = Field(..., description="Cancel order Result Code")
    
    model_config = ConfigDict()


class BatchCancelOrdersResponse(BaseModel):
    """Batch Cancel Order Response model - Based on actual API response"""
    code: int = Field(..., description="Response code")
    result: list[BatchCancelOrderResult] = Field(default=[], description="Cancel order Result List, Empty Array Represents All Success")
    
    model_config = ConfigDict()


class BatchOrderResult(BaseModel):
    """Batch Order Result model"""
    code: int = Field(..., description="Order result code")
    msg: str = Field(None, description="Error message")
    order: CreateOrderResponse = Field(None, description="Success Create of Order information")
    
    model_config = ConfigDict()


class BatchCreateOrderResponse(BaseModel):
    """Batch Create Order Response model - Based on actual API response"""
    code: int = Field(..., description="Response code")
    result: list[BatchOrderResult] = Field(..., description="Batch order result list")
    
    model_config = ConfigDict()


class CancelOpenOrdersResponse(BaseModel):
    """Cancel Open Orders Response model - Based on actual API response"""
    success: bool = Field(..., description="Whether request is successful")
    
    model_config = ConfigDict()


class FuturesOrderRequest(BaseModel):
    """Futures Order Request model"""
    newClientOrderId: str = Field(..., description="User-defined order ID")
    symbol: str = Field(..., description="Symbol")
    side: OrderSide = Field(..., description="Order Side")
    type: OrderType = Field(..., description="Order type")
    price: float = Field(..., description="Order price")
    quantity: float = Field(..., description="Order quantity")
    priceType: str = Field(..., description="Price type")
    
    model_config = ConfigDict(use_enum_values=True)


class BatchFuturesOrderResult(BaseModel):
    """Batch Futures Create Order Result item model"""
    code: int = Field(..., description="Order result code")
    order: Optional[CreateFuturesOrderResponse] = Field(None, description="Order details, returned when successful")
    msg: Optional[str] = Field(None, description="Failure reason, returned when failed")
    
    model_config = ConfigDict()


class BatchCreateFuturesOrdersResponse(BaseModel):
    """Batch Create Futures Order Response model - Based on actual API response"""
    code: int = Field(..., description="Response code")
    result: list[BatchFuturesOrderResult] = Field(..., description="Batch Create Order Result List")
    
    model_config = ConfigDict()


class FuturesPosition(BaseModel):
    """Futures Position model - Based on actual API response"""
    symbol: str = Field(..., description="Symbol")
    side: str = Field(..., description="Position Side")
    avgPrice: str = Field(..., description="Average open price")
    position: str = Field(..., description="Open Quantity (Contract)")
    available: str = Field(..., description="Available close quantity (contract)")
    leverage: str = Field(..., description="Current position leverage")
    lastPrice: str = Field(..., description="Latest futures market execution price")
    positionValue: str = Field(..., description="Position value")
    flp: str = Field(..., description="Forced close price")
    margin: str = Field(..., description="Position Margin")
    marginRate: str = Field(..., description="Current Position of Margin Rate")
    unrealizedPnL: str = Field(..., description="Current Position of Not Implementation PnL")
    profitRate: str = Field(..., description="Current position profit rate")
    realizedPnL: str = Field(..., description="Current Futures of Already Implementation PnL")
    maxNotionalValue: str = Field(..., description="Maximum position contract number with current leverage multiple")
    markPrice: str = Field(..., description="Mark price")
    marginType: str = Field(..., description="Margin type")
    
    model_config = ConfigDict()


class SetPositionTradingStopRequest(BaseModel):
    """Set Position Take Profit Stop Loss Request model"""
    symbol: str = Field(..., description="Symbol")
    side: str = Field(..., description="Position side, LONG (Long) or SHORT (Short)")
    takeProfit: Optional[str] = Field(None, description="Take Profit Price")
    stopLoss: Optional[str] = Field(None, description="Stop Loss Price")
    tpTriggerBy: Optional[str] = Field(None, description="Take profit conditional order parameters. Trigger type: MARK_PRICE (mark price), CONTRACT_PRICE (latest futures price). Default CONTRACT_PRICE")
    slTriggerBy: Optional[str] = Field(None, description="Stop loss conditional order parameters. Trigger type: MARK_PRICE (mark price), CONTRACT_PRICE (latest futures price). Default CONTRACT_PRICE")
    
    model_config = ConfigDict()


class SetPositionTradingStopResponse(BaseModel):
    """Set Position Take Profit Stop Loss Response model - Based on actual API response"""
    symbol: str = Field(..., description="Symbol")
    side: str = Field(..., description="Position Side")
    takeProfit: Optional[str] = Field(None, description="Take Profit Price")
    stopLoss: Optional[str] = Field(None, description="Stop Loss Price")
    tpTriggerBy: Optional[str] = Field(None, description="Take Profit Trigger Type")
    slTriggerBy: Optional[str] = Field(None, description="Stop Loss Trigger Type")
    
    model_config = ConfigDict()


class QueryFuturesHistoryOrdersRequest(BaseModel):
    """Query historical orders request model"""
    symbol: Optional[str] = Field(None, description="Symbol")
    orderId: Optional[str] = Field(None, description="Order ID")
    type: Optional[OrderType] = Field(None, description="Order type (LIMIT, STOP)")
    startTime: Optional[int] = Field(None, description="Start time timestamp, default value: three days before")
    endTime: Optional[int] = Field(None, description="End time timestamp")
    limit: Optional[int] = Field(20, description="Number of returned records, default 20, minimum 1, maximum 1000")
    
    model_config = ConfigDict()


class FuturesBalance(BaseModel):
    """Futures account balance model"""
    asset: str = Field(..., description="Asset")
    balance: str = Field(..., description="Total Balance")
    availableBalance: str = Field(..., description="Available margin, contains unrealized PnL")
    positionMargin: str = Field(..., description="Position Margin")
    orderMargin: str = Field(..., description="Order margin (locked when creating order)")
    crossUnRealizedPnl: str = Field(..., description="Cross Not Implementation PnL")
    
    model_config = ConfigDict()


class AdjustIsolatedMarginRequest(BaseModel):
    """Adjust isolated margin request model"""
    symbol: str = Field(..., description="Symbol")
    side: str = Field(..., description="Position side, LONG (Long) or SHORT (Short)")
    amount: str = Field(..., description="Increase (positive value) or decrease (negative value) margin quantity")
    
    model_config = ConfigDict()


class AdjustIsolatedMarginResponse(BaseModel):
    """Adjust isolated margin response model"""
    code: int = Field(..., description="Response code 200 = Success")
    msg: str = Field(..., description="Response message")
    symbol: str = Field(..., description="Symbol")
    margin: str = Field(..., description="Update After of Position Margin")
    timestamp: int = Field(..., description="Update Time Timestamp")
    
    model_config = ConfigDict()


class QueryFuturesTradeHistoryRequest(BaseModel):
    """Query futures account trade history request model"""
    symbol: str = Field(..., description="Symbol")
    fromId: Optional[int] = Field(None, description="Start from trade ID (used to query execution order)")
    toId: Optional[int] = Field(None, description="End at trade ID (used to query execution order)")
    startTime: Optional[int] = Field(None, description="Start time timestamp")
    endTime: Optional[int] = Field(None, description="End time timestamp")
    limit: Optional[int] = Field(20, description="Number of returned records, default 20, minimum 1, maximum 1000")
    
    model_config = ConfigDict()


class FuturesTrade(BaseModel):
    """Futures execution record model"""
    time: str = Field(..., description="Execution Time")
    id: str = Field(..., description="Execution ID")
    orderId: str = Field(..., description="Order ID")
    symbol: str = Field(..., description="Symbol")
    price: str = Field(..., description="Execution Price")
    qty: str = Field(..., description="Execution Quantity")
    commissionAsset: str = Field(..., description="Fee Type (Token Name)")
    commission: str = Field(..., description="Actual fee")
    makerRebate: str = Field(..., description="Negative maker rebate")
    type: str = Field(..., description="Order type (LIMIT, MARKET)")
    isMaker: bool = Field(..., description="Whether is maker")
    side: str = Field(..., description="Order Side (BUY_OPEN, SELL_OPEN, BUY_CLOSE, SELL_CLOSE)")
    realizedPnl: str = Field(..., description="Execution PnL")
    ticketId: str = Field(..., description="ticketId")
    
    model_config = ConfigDict()


class QueryFuturesAccountFlowRequest(BaseModel):
    """Query futures account flow request model"""
    symbol: Optional[str] = Field(None, description="Asset")
    flowType: Optional[int] = Field(None, description="Flow type")
    fromId: Optional[int] = Field(None, description="Forward query data")
    endId: Optional[int] = Field(None, description="Reverse query data")
    startTime: Optional[int] = Field(None, description="Start time")
    endTime: Optional[int] = Field(None, description="End time")
    limit: Optional[int] = Field(None, description="Number of records per page")
    
    model_config = ConfigDict()


class FuturesAccountFlow(BaseModel):
    """Futures account flow model"""
    id: int = Field(..., description="Flow ID")
    accountId: int = Field(..., description="Account ID")
    coin: str = Field(..., description="Asset")
    coinId: str = Field(..., description="Asset ID")
    coinName: str = Field(..., description="Asset Name")
    symbol: str = Field(..., description="Symbol Name")
    symbolId: str = Field(..., description="Symbol ID")
    flowTypeValue: int = Field(..., description="Flow type value")
    flowType: str = Field(..., description="Flow type Name")
    flowName: str = Field(..., description="Flow type Description")
    change: str = Field(..., description="Change value")
    total: str = Field(..., description="Change After Current token Id Total Asset")
    created: int = Field(..., description="Create time")
    
    model_config = ConfigDict()


class QueryFuturesUserFeeRateRequest(BaseModel):
    """Query futures user fee rate request model"""
    symbol: str = Field(..., description="Symbol")
    
    model_config = ConfigDict()


class FuturesUserFeeRate(BaseModel):
    """Futures user fee rate model"""
    openMakerFee: str = Field(..., description="Open Open Orders of Fee Fee Rate")
    openTakerFee: str = Field(..., description="Open Taker of Fee Fee Rate")
    closeMakerFee: str = Field(..., description="Close Open Orders of Fee Fee Rate")
    closeTakerFee: str = Field(..., description="Close Taker of Fee Fee Rate")
    
    model_config = ConfigDict()


class FuturesTodayPnL(BaseModel):
    """Futures today PnL model"""
    dayProfit: str = Field(..., description="Today PnL UTC+0 timezone")
    dayProfitRate: str = Field(..., description="Today PnL rate UTC+0 timezone")
    
    model_config = ConfigDict()


class MarginType(str, Enum):
    """Margin type enumeration"""
    CROSS = "CROSS"  # Cross
    ISOLATED = "ISOLATED"  # Isolated


class ChangeMarginTypeRequest(BaseModel):
    """Change to cross mode request model"""
    symbol: str = Field(..., description="Symbol")
    marginType: MarginType = Field(..., description="Margin Type: CROSS=Cross, ISOLATED=Isolated")
    
    model_config = ConfigDict()
    
    def model_dump(self, **kwargs):
        """Override model_dump method to ensure enum fields use name values"""
        data = super().model_dump(**kwargs)
        if 'marginType' in data and isinstance(data['marginType'], MarginType):
            data['marginType'] = data['marginType'].name
        return data


class ChangeMarginTypeResponse(BaseModel):
    """Change to cross mode response model"""
    code: int = Field(..., description="Response code 200=Success")
    symbol: str = Field(..., description="Symbol")
    marginType: str = Field(..., description="Margin Type: CROSS=Cross, ISOLATED=Isolated")
    
    model_config = ConfigDict()


class AdjustLeverageRequest(BaseModel):
    """Adjust open leverage request model"""
    symbol: str = Field(..., description="Symbol")
    leverage: int = Field(..., description="Leverage Multiple")
    
    model_config = ConfigDict()


class AdjustLeverageResponse(BaseModel):
    """Adjust open leverage response model"""
    code: int = Field(..., description="Response code 200=Success")
    symbolId: str = Field(..., description="Symbol")
    leverage: str = Field(..., description="Leverage Multiple")
    
    model_config = ConfigDict()


class QueryLeverageRequest(BaseModel):
    """Query leverage multiple and position mode request model"""
    symbol: str = Field(..., description="Symbol")
    
    model_config = ConfigDict()


class AccountLeverage(BaseModel):
    """Account leverage information model"""
    symbolId: str = Field(..., description="Symbol")
    leverage: str = Field(..., description="Leverage Multiple")
    marginType: str = Field(..., description="Margin Type: CROSS=Cross, ISOLATED=Isolated")
    
    model_config = ConfigDict()


class SpotBalance(BaseModel):
    """Spot account balance model"""
    asset: str = Field(..., description="Asset")
    assetId: str = Field(..., description="Asset ID")
    assetName: str = Field(..., description="Asset Name")
    total: str = Field(..., description="Total Quantity")
    free: str = Field(..., description="Available amount")
    locked: str = Field(..., description="Locked amount")
    
    model_config = ConfigDict()


class SpotAccountInfo(BaseModel):
    """Spot account information model"""
    balances: list[SpotBalance] = Field(..., description="Balance List")
    
    model_config = ConfigDict()


class SpotSubAccount(BaseModel):
    """Spot sub account model"""
    accountId: str = Field(..., description="Account ID")
    accountName: str = Field(..., description="Sub Account Name")
    accountType: int = Field(..., description="Sub account type: 1=spot account, 3=futures account")
    accountIndex: int = Field(..., description="Account index: 0=default account, >0=created sub account")
    
    model_config = ConfigDict()


class ApiKeyType(BaseModel):
    """API key type model"""
    accountType: str = Field(..., description="Account Type: master=Main Account, sub=Sub Account")
    
    model_config = ConfigDict()


class OrderResponse(BaseModel):
    """Query order response model - Returned when querying open orders and order status"""
    symbol: str = Field(..., description="Symbol")
    order_id: str = Field(..., description="Order ID", alias="orderId")
    client_order_id: str = Field(..., description="Client order ID", alias="clientOrderId")
    price: str = Field(..., description="Price")
    orig_qty: str = Field(..., description="Original quantity", alias="origQty")
    executed_qty: str = Field(..., description="Executed quantity", alias="executedQty")
    cummulative_quote_qty: str = Field(..., description="Cumulative execution amount", alias="cummulativeQuoteQty")
    status: OrderStatus = Field(..., description="Order status")
    time_in_force: TimeInForce = Field(..., description="Order time in force", alias="timeInForce")
    type: OrderType = Field(..., description="Order type")
    side: OrderSide = Field(..., description="Order Side")
    stop_price: str = Field(..., description="Stop Loss Price", alias="stopPrice")
    iceberg_qty: str = Field(..., description="Iceberg quantity", alias="icebergQty")
    time: str = Field(..., description="Order Time", alias="time")
    update_time: str = Field(..., description="Update Time", alias="updateTime")
    is_working: bool = Field(..., description="Whether is working", alias="isWorking")
    
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class CancelOrderRequest(BaseModel):
    """Cancel order request model"""
    symbol: str = Field(..., description="Symbol")
    order_id: Optional[str] = Field(None, description="Order ID", alias="orderId")
    orig_client_order_id: Optional[str] = Field(None, description="Original client order ID", alias="origClientOrderId")
    new_client_order_id: Optional[str] = Field(None, description="New client order ID", alias="newClientOrderId")
    recv_window: Optional[int] = Field(None, description="Receive window", alias="recvWindow")
    
    model_config = ConfigDict(populate_by_name=True)


class CancelOrderResponse(BaseModel):
    """Cancel order response model - Based on actual API response"""
    symbol: str = Field(..., description="Symbol")
    order_id: str = Field(..., description="Order ID", alias="orderId")
    client_order_id: str = Field(..., description="Client order ID", alias="clientOrderId")
    price: str = Field(..., description="Price")
    orig_qty: str = Field(..., description="Original quantity", alias="origQty")
    executed_qty: str = Field(..., description="Executed quantity", alias="executedQty")
    status: OrderStatus = Field(..., description="Order status")
    time_in_force: TimeInForce = Field(..., description="Order time in force", alias="timeInForce")
    type: OrderType = Field(..., description="Order type")
    side: OrderSide = Field(..., description="Order Side")
    transact_time: str = Field(..., description="Trade Time", alias="transactTime")
    
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class OrderQueryRequest(BaseModel):
    """Query order request model"""
    symbol: str = Field(..., description="Symbol")
    orderId: Optional[int] = Field(None, description="Order ID")
    origClientOrderId: Optional[str] = Field(None, description="Original client order ID")
    recvWindow: Optional[int] = Field(None, description="Receive window")
    
    model_config = ConfigDict()


class Trade(BaseModel):
    """Execution record model"""
    id: int = Field(..., description="Execution ID")
    price: float = Field(..., description="Execution Price")
    qty: float = Field(..., description="Execution Quantity")
    commission: float = Field(..., description="Fee")
    commissionAsset: str = Field(..., description="Fee Asset")
    time: int = Field(..., description="Execution Time")
    isBuyer: bool = Field(..., description="Whether is buyer")
    isMaker: bool = Field(..., description="Whether is maker")
    isBestMatch: bool = Field(..., description="Whether is best match")
    
    model_config = ConfigDict()


class ExchangeInfo(BaseModel):
    """Trade all information model"""
    timezone: Optional[str] = Field(None, description="Timezone")
    serverTime: Optional[int] = Field(None, description="Server Time")
    rateLimits: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="Rate limit")
    brokerFilters: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="Trading filters")
    symbols: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="Symbol List")
    
    model_config = ConfigDict()


class Ticker24hr(BaseModel):
    """24 hour price change model"""
    t: int = Field(..., description="Time")
    a: str = Field(..., description="Highest ask price")
    b: str = Field(..., description="Highest bid price")
    s: str = Field(..., description="Symbol")
    c: str = Field(..., description="Latest execution price")
    o: str = Field(..., description="Open price")
    h: str = Field(..., description="Highest price")
    l: str = Field(..., description="Lowest price")
    v: str = Field(..., description="Volume")
    qv: str = Field(..., description="Amount")
    pc: str = Field(..., description="24 Hour Price Change")
    pcp: str = Field(..., description="24 Hour Price Change Percentage")
    
    model_config = ConfigDict()


class OrderBook(BaseModel):
    """Order book model"""
    t: Optional[int] = Field(None, description="Most After Update ID")
    b: Optional[List[List[float]]] = Field(default_factory=list, description="Buy order [Price, Quantity]")
    a: Optional[List[List[float]]] = Field(default_factory=list, description="Sell order [Price, Quantity]")
    
    model_config = ConfigDict()


class Kline(BaseModel):
    """K-line model"""
    openTime: int = Field(..., description="Open Time")
    open: float = Field(..., description="Open price")
    high: float = Field(..., description="Highest price")
    low: float = Field(..., description="Lowest price")
    close: float = Field(..., description="Close price")
    volume: float = Field(..., description="Volume")
    closeTime: int = Field(..., description="Close time")
    quoteAssetVolume: float = Field(..., description="Amount")
    numberOfTrades: int = Field(..., description="Number of trades")
    takerBuyBaseAssetVolume: float = Field(..., description="Main active buy volume")
    takerBuyQuoteAssetVolume: float = Field(..., description="Main active buy amount")
    
    model_config = ConfigDict() 