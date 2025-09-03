"""
TooBit API 数据模型
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class OrderSide(str, Enum):
    """订单方向"""
    # 现货交易方向
    BUY = "BUY"
    SELL = "SELL"
    
    # 合约交易方向
    BUY_OPEN = "BUY_OPEN"      # 买入开仓 (做多)
    SELL_OPEN = "SELL_OPEN"    # 卖出开仓 (做空)
    BUY_CLOSE = "BUY_CLOSE"    # 买入平仓 (平空)
    SELL_CLOSE = "SELL_CLOSE"  # 卖出平仓 (平多)


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
    
    model_config = ConfigDict(use_enum_values=True)


class CreateFuturesOrderResponse(BaseModel):
    """合约下单响应模型 - 根据实际API响应"""
    time: str = Field(..., description="订单生成时的时间戳")
    updateTime: str = Field(..., description="订单上次更新的时间戳")
    orderId: str = Field(..., description="订单ID")
    clientOrderId: str = Field(..., description="用户定义的订单ID")
    symbol: str = Field(..., description="交易对")
    price: str = Field(..., description="订单价格")
    leverage: str = Field(..., description="订单杠杆")
    origQty: str = Field(..., description="订单数量")
    executedQty: str = Field(..., description="订单已执行数量")
    avgPrice: str = Field(..., description="平均交易价格")
    marginLocked: str = Field(..., description="该订单锁定的保证金")
    type: OrderType = Field(..., description="订单类型（LIMIT和STOP）")
    side: OrderSide = Field(..., description="订单方向")
    timeInForce: TimeInForce = Field(..., description="时效单类型")
    status: OrderStatus = Field(..., description="订单状态")
    priceType: str = Field(..., description="价格类型（INPUT、OPPONENT、QUEUE、OVER、MARKET）")
    
    model_config = ConfigDict(use_enum_values=True)


class CancelFuturesOrderResponse(BaseModel):
    """合约撤销订单响应模型 - 根据实际API响应"""
    time: str = Field(..., description="订单生成时的时间戳")
    updateTime: str = Field(..., description="订单上次更新的时间戳")
    orderId: str = Field(..., description="订单ID")
    clientOrderId: str = Field(..., description="用户定义的订单ID")
    symbol: str = Field(..., description="交易对")
    price: str = Field(..., description="订单价格")
    leverage: str = Field(..., description="订单杠杆")
    origQty: str = Field(..., description="订单数量")
    executedQty: str = Field(..., description="订单已执行数量")
    avgPrice: str = Field(..., description="平均交易价格")
    marginLocked: str = Field(..., description="该订单锁定的保证金")
    type: OrderType = Field(..., description="订单类型（LIMIT和STOP）")
    side: OrderSide = Field(..., description="订单方向")
    timeInForce: TimeInForce = Field(..., description="时效单类型")
    status: OrderStatus = Field(..., description="订单状态")
    priceType: str = Field(..., description="价格类型（INPUT、OPPONENT、QUEUE、OVER、MARKET）")
    
    model_config = ConfigDict(use_enum_values=True)


class QueryFuturesOrderResponse(BaseModel):
    """合约查询订单响应模型 - 根据实际API响应"""
    time: str = Field(..., description="订单生成时的时间戳")
    updateTime: str = Field(..., description="订单上次更新的时间戳")
    orderId: str = Field(..., description="订单ID")
    clientOrderId: str = Field(..., description="用户定义的订单ID")
    symbol: str = Field(..., description="交易对")
    price: str = Field(..., description="订单价格")
    leverage: str = Field(..., description="订单杠杆")
    origQty: str = Field(..., description="订单数量")
    executedQty: str = Field(..., description="订单已执行数量")
    avgPrice: str = Field(..., description="平均交易价格")
    marginLocked: str = Field(..., description="该订单锁定的保证金")
    type: OrderType = Field(..., description="订单类型（LIMIT和STOP）")
    side: OrderSide = Field(..., description="订单方向")
    timeInForce: TimeInForce = Field(..., description="时效单类型")
    status: OrderStatus = Field(..., description="订单状态")
    priceType: str = Field(..., description="价格类型（INPUT、OPPONENT、QUEUE、OVER、MARKET）")
    
    model_config = ConfigDict(use_enum_values=True)


class FuturesOpenOrderResponse(BaseModel):
    """合约挂单响应模型 - 根据实际API响应"""
    time: str = Field(..., description="订单生成时的时间戳")
    updateTime: str = Field(..., description="订单上次更新的时间戳")
    orderId: str = Field(..., description="订单ID")
    clientOrderId: str = Field(..., description="用户定义的订单ID")
    symbol: str = Field(..., description="交易对")
    price: str = Field(..., description="订单价格")
    leverage: str = Field(..., description="订单杠杆")
    origQty: str = Field(..., description="订单数量")
    executedQty: str = Field(..., description="订单已执行数量")
    avgPrice: str = Field(..., description="平均交易价格")
    marginLocked: str = Field(..., description="该订单锁定的保证金")
    type: OrderType = Field(..., description="订单类型（LIMIT和STOP）")
    side: OrderSide = Field(..., description="订单方向")
    timeInForce: TimeInForce = Field(..., description="时效单类型")
    status: OrderStatus = Field(..., description="订单状态")
    priceType: str = Field(..., description="价格类型（INPUT、OPPONENT、QUEUE、OVER、MARKET）")
    
    model_config = ConfigDict(use_enum_values=True)


class CancelAllOrdersResponse(BaseModel):
    """撤销全部订单响应模型 - 根据实际API响应"""
    code: int = Field(..., description="响应代码")
    message: str = Field(..., description="响应消息")
    timestamp: int = Field(..., description="时间戳")
    
    model_config = ConfigDict()


class BatchCancelOrderResult(BaseModel):
    """批量撤单结果项模型"""
    orderId: str = Field(..., description="订单ID")
    code: int = Field(..., description="撤单结果代码")
    
    model_config = ConfigDict()


class BatchCancelOrdersResponse(BaseModel):
    """批量撤销订单响应模型 - 根据实际API响应"""
    code: int = Field(..., description="响应代码")
    result: list[BatchCancelOrderResult] = Field(default=[], description="撤单结果列表，空数组表示全部成功")
    
    model_config = ConfigDict()


class BatchCreateOrderResponse(BaseModel):
    """批量创建订单响应模型 - 根据实际API响应"""
    code: int = Field(..., description="响应代码")
    message: str = Field(..., description="响应消息")
    timestamp: int = Field(..., description="时间戳")
    result: list[CreateOrderResponse] = Field(..., description="创建订单结果列表")
    
    model_config = ConfigDict()


class CancelOpenOrdersResponse(BaseModel):
    """撤销挂单响应模型 - 根据实际API响应"""
    success: bool = Field(..., description="请求是否成功")
    
    model_config = ConfigDict()


class FuturesOrderRequest(BaseModel):
    """合约订单请求模型"""
    newClientOrderId: str = Field(..., description="用户定义的订单ID")
    symbol: str = Field(..., description="交易对")
    side: OrderSide = Field(..., description="订单方向")
    type: OrderType = Field(..., description="订单类型")
    price: float = Field(..., description="订单价格")
    quantity: float = Field(..., description="订单数量")
    priceType: str = Field(..., description="价格类型")
    
    model_config = ConfigDict(use_enum_values=True)


class BatchFuturesOrderResult(BaseModel):
    """批量合约下单结果项模型"""
    code: int = Field(..., description="订单结果代码")
    order: Optional[CreateFuturesOrderResponse] = Field(None, description="订单详情，成功时返回")
    msg: Optional[str] = Field(None, description="失败原因，失败时返回")
    
    model_config = ConfigDict()


class BatchCreateFuturesOrdersResponse(BaseModel):
    """批量创建合约订单响应模型 - 根据实际API响应"""
    code: int = Field(..., description="响应代码")
    result: list[BatchFuturesOrderResult] = Field(..., description="批量下单结果列表")
    
    model_config = ConfigDict()


class FuturesPosition(BaseModel):
    """合约持仓模型 - 根据实际API响应"""
    symbol: str = Field(..., description="交易对")
    side: str = Field(..., description="仓位方向")
    avgPrice: str = Field(..., description="平均开仓价格")
    position: str = Field(..., description="开仓数量（张）")
    available: str = Field(..., description="可平仓数量（张）")
    leverage: str = Field(..., description="仓位现在杠杆")
    lastPrice: str = Field(..., description="合约最新市场成交价")
    positionValue: str = Field(..., description="仓位价值")
    flp: str = Field(..., description="强制平仓价格")
    margin: str = Field(..., description="仓位保证金")
    marginRate: str = Field(..., description="当前仓位的保证金率")
    unrealizedPnL: str = Field(..., description="当前仓位的未实现盈亏")
    profitRate: str = Field(..., description="当前仓位的盈利率")
    realizedPnL: str = Field(..., description="当前合约的已实现盈亏")
    maxNotionalValue: str = Field(..., description="当前杠杆倍数最大可持仓张数")
    markPrice: str = Field(..., description="标记价格")
    
    model_config = ConfigDict()


class SetPositionTradingStopRequest(BaseModel):
    """设置持仓止盈止损请求模型"""
    symbol: str = Field(..., description="交易对")
    side: str = Field(..., description="仓位方向, LONG(多仓)或者 SHORT(空仓)")
    takeProfit: Optional[str] = Field(None, description="止盈价格")
    stopLoss: Optional[str] = Field(None, description="止损价格")
    tpTriggerBy: Optional[str] = Field(None, description="止盈条件单参数.触发类型:MARK_PRICE(标记价格),CONTRACT_PRICE(合约最新价).默认 CONTRACT_PRICE")
    slTriggerBy: Optional[str] = Field(None, description="止损条件单参数.触发类型:MARK_PRICE(标记价格),CONTRACT_PRICE(合约最新价).默认 CONTRACT_PRICE")
    
    model_config = ConfigDict()


class SetPositionTradingStopResponse(BaseModel):
    """设置持仓止盈止损响应模型 - 根据实际API响应"""
    symbol: str = Field(..., description="交易对")
    side: str = Field(..., description="仓位方向")
    takeProfit: Optional[str] = Field(None, description="止盈价格")
    stopLoss: Optional[str] = Field(None, description="止损价格")
    tpTriggerBy: Optional[str] = Field(None, description="止盈触发类型")
    slTriggerBy: Optional[str] = Field(None, description="止损触发类型")
    
    model_config = ConfigDict()


class QueryFuturesHistoryOrdersRequest(BaseModel):
    """查询历史订单请求模型"""
    symbol: Optional[str] = Field(None, description="交易对")
    orderId: Optional[str] = Field(None, description="订单ID")
    type: Optional[OrderType] = Field(None, description="订单类型 (LIMIT, STOP)")
    startTime: Optional[int] = Field(None, description="开始时间戳 默认值:三天前")
    endTime: Optional[int] = Field(None, description="截止时间戳")
    limit: Optional[int] = Field(20, description="返回条数 默认20 最小1 最大1000")
    
    model_config = ConfigDict()


class FuturesBalance(BaseModel):
    """合约账户余额模型"""
    asset: str = Field(..., description="资产")
    balance: str = Field(..., description="总余额")
    availableBalance: str = Field(..., description="可用保证金，包含未实现盈亏")
    positionMargin: str = Field(..., description="仓位保证金")
    orderMargin: str = Field(..., description="委托保证金（下单锁定）")
    crossUnRealizedPnl: str = Field(..., description="全仓未实现盈亏")
    
    model_config = ConfigDict()


class AdjustIsolatedMarginRequest(BaseModel):
    """调整逐仓保证金请求模型"""
    symbol: str = Field(..., description="交易对")
    side: str = Field(..., description="仓位方向，LONG（多仓）或者SHORT（空仓）")
    amount: str = Field(..., description="增加（正值）或者减少（负值）保证金的数量")
    
    model_config = ConfigDict()


class AdjustIsolatedMarginResponse(BaseModel):
    """调整逐仓保证金响应模型"""
    code: int = Field(..., description="响应码 200 = 成功")
    msg: str = Field(..., description="响应消息")
    symbol: str = Field(..., description="交易对")
    margin: str = Field(..., description="更新后的仓位保证金")
    timestamp: int = Field(..., description="更新时间戳")
    
    model_config = ConfigDict()


class QueryFuturesTradeHistoryRequest(BaseModel):
    """查询合约账户成交历史请求模型"""
    symbol: str = Field(..., description="交易对")
    fromId: Optional[int] = Field(None, description="从TradeId开始（用来查询成交订单）")
    toId: Optional[int] = Field(None, description="到TradeId结束（用来查询成交订单）")
    startTime: Optional[int] = Field(None, description="开始时间戳")
    endTime: Optional[int] = Field(None, description="截止时间戳")
    limit: Optional[int] = Field(20, description="返回条数 默认20 最小1 最大1000")
    
    model_config = ConfigDict()


class FuturesTrade(BaseModel):
    """合约成交记录模型"""
    time: str = Field(..., description="成交时间")
    id: str = Field(..., description="成交ID")
    orderId: str = Field(..., description="订单ID")
    symbol: str = Field(..., description="交易对")
    price: str = Field(..., description="成交价格")
    qty: str = Field(..., description="成交数量")
    commissionAsset: str = Field(..., description="手续费类型（Token名称）")
    commission: str = Field(..., description="实际手续费")
    makerRebate: str = Field(..., description="负maker返佣")
    type: str = Field(..., description="订单类型（LIMIT、MARKET)")
    isMaker: bool = Field(..., description="是否是maker")
    side: str = Field(..., description="订单方向（BUY_OPEN、SELL_OPEN、BUY_CLOSE、SELL_CLOSE）")
    realizedPnl: str = Field(..., description="成交盈亏")
    ticketId: str = Field(..., description="ticketId")
    
    model_config = ConfigDict()


class QueryFuturesAccountFlowRequest(BaseModel):
    """查询合约账户流水请求模型"""
    symbol: Optional[str] = Field(None, description="资产")
    flowType: Optional[int] = Field(None, description="流水类型")
    fromId: Optional[int] = Field(None, description="顺向查询数据")
    endId: Optional[int] = Field(None, description="反向查询数据")
    startTime: Optional[int] = Field(None, description="开始时间")
    endTime: Optional[int] = Field(None, description="结束时间")
    limit: Optional[int] = Field(None, description="每页记录数")
    
    model_config = ConfigDict()


class FuturesAccountFlow(BaseModel):
    """合约账户流水模型"""
    id: int = Field(..., description="流水ID")
    accountId: int = Field(..., description="账户ID")
    coin: str = Field(..., description="资产")
    coinId: str = Field(..., description="资产ID")
    coinName: str = Field(..., description="资产名称")
    symbol: str = Field(..., description="交易对名称")
    symbolId: str = Field(..., description="交易对ID")
    flowTypeValue: int = Field(..., description="流水类型值")
    flowType: str = Field(..., description="流水类型名称")
    flowName: str = Field(..., description="流水类型说明")
    change: str = Field(..., description="变动值")
    total: str = Field(..., description="变动后当前tokenId总资产")
    created: int = Field(..., description="创建时间")
    
    model_config = ConfigDict()


class QueryFuturesUserFeeRateRequest(BaseModel):
    """查询合约用户手续费率请求模型"""
    symbol: str = Field(..., description="交易对")
    
    model_config = ConfigDict()


class FuturesUserFeeRate(BaseModel):
    """合约用户手续费率模型"""
    openMakerFee: str = Field(..., description="开仓挂单的手续费费率")
    openTakerFee: str = Field(..., description="开仓吃单的手续费费率")
    closeMakerFee: str = Field(..., description="平仓挂单的手续费费率")
    closeTakerFee: str = Field(..., description="平仓吃单的手续费费率")
    
    model_config = ConfigDict()


class FuturesTodayPnL(BaseModel):
    """合约今日盈亏模型"""
    dayProfit: str = Field(..., description="今日盈亏 UTC+0 时区")
    dayProfitRate: str = Field(..., description="今日盈亏率 UTC+0 时区")
    
    model_config = ConfigDict()


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
    orderId: Optional[int] = Field(None, description="订单ID")
    origClientOrderId: Optional[str] = Field(None, description="原始客户端订单ID")
    recvWindow: Optional[int] = Field(None, description="接收窗口")
    
    model_config = ConfigDict()


class Trade(BaseModel):
    """成交记录模型"""
    id: int = Field(..., description="成交ID")
    price: float = Field(..., description="成交价格")
    qty: float = Field(..., description="成交数量")
    commission: float = Field(..., description="手续费")
    commissionAsset: str = Field(..., description="手续费资产")
    time: int = Field(..., description="成交时间")
    isBuyer: bool = Field(..., description="是否买方")
    isMaker: bool = Field(..., description="是否挂单方")
    isBestMatch: bool = Field(..., description="是否最佳匹配")
    
    model_config = ConfigDict()


class ExchangeInfo(BaseModel):
    """交易所信息模型"""
    timezone: Optional[str] = Field(None, description="时区")
    serverTime: Optional[int] = Field(None, description="服务器时间")
    rateLimits: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="速率限制")
    brokerFilters: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="交易所过滤器")
    symbols: Optional[List[Dict[str, Any]]] = Field(default_factory=list, description="交易对列表")
    
    model_config = ConfigDict()


class Ticker24hr(BaseModel):
    """24小时价格变动模型"""
    t: int = Field(..., description="时间")
    a: str = Field(..., description="最高卖价")
    b: str = Field(..., description="最高买价")
    s: str = Field(..., description="交易对")
    c: str = Field(..., description="最新成交价")
    o: str = Field(..., description="开盘价")
    h: str = Field(..., description="最高价")
    l: str = Field(..., description="最低价")
    v: str = Field(..., description="成交量")
    qv: str = Field(..., description="成交额")
    pc: str = Field(..., description="24小时价格变动")
    pcp: str = Field(..., description="24小时价格变动百分比")
    
    model_config = ConfigDict()


class OrderBook(BaseModel):
    """订单簿模型"""
    t: Optional[int] = Field(None, description="最后更新ID")
    b: Optional[List[List[float]]] = Field(default_factory=list, description="买单 [价格, 数量]")
    a: Optional[List[List[float]]] = Field(default_factory=list, description="卖单 [价格, 数量]")
    
    model_config = ConfigDict()


class Kline(BaseModel):
    """K线模型"""
    openTime: int = Field(..., description="开盘时间")
    open: float = Field(..., description="开盘价")
    high: float = Field(..., description="最高价")
    low: float = Field(..., description="最低价")
    close: float = Field(..., description="收盘价")
    volume: float = Field(..., description="成交量")
    closeTime: int = Field(..., description="收盘时间")
    quoteAssetVolume: float = Field(..., description="成交额")
    numberOfTrades: int = Field(..., description="成交笔数")
    takerBuyBaseAssetVolume: float = Field(..., description="主动买入成交量")
    takerBuyQuoteAssetVolume: float = Field(..., description="主动买入成交额")
    
    model_config = ConfigDict() 