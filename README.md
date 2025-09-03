# TooBit API SDK

一个全面的Python SDK，用于TooBit加密货币交易所API，支持现货和期货交易。

> **⚠️ 免责声明**: 本SDK仅供参考。请以官方TooBit API文档为准，获取最新、最准确的信息。

## 功能特性

- **现货交易**: 完整的现货交易功能
- **期货交易**: 完整的USDT保证金期货交易支持
- **类型安全**: 使用Pydantic构建，提供强大的数据验证
- **易于使用**: 简单直观的API设计
- **全面示例**: 46+个示例文件，涵盖所有主要操作

## 安装

```bash
pip install -r requirements.txt
```

## 快速开始

### 基本配置

```python
from open_api_sdk import TooBitClient, TooBitConfig

# 初始化配置
config = TooBitConfig(
    api_key="your_api_key",
    api_secret="your_api_secret",
    base_url="https://api.toobit.com"
)

# 创建客户端
client = TooBitClient(config)
```

### 现货交易示例

```python
from open_api_sdk.models import OrderRequest, OrderSide, OrderType, TimeInForce

# 创建限价单
order = OrderRequest(
    symbol="BTCUSDT",
    side=OrderSide.BUY,
    type=OrderType.LIMIT,
    quantity=0.01,
    price=45000.0,
    time_in_force=TimeInForce.GTC
)

# 下单
response = client.create_order(order)
print(f"订单已创建: {response.order_id}")
```

### 期货交易示例

```python
from open_api_sdk.models import CreateFuturesOrderRequest, OrderSide

# 创建期货订单
futures_order = CreateFuturesOrderRequest(
    symbol="BTC-SWAP-USDT",
    side=OrderSide.BUY_OPEN,
    type=OrderType.LIMIT,
    quantity=1,
    price=50000.0,
    leverage=10
)

# 下期货订单
response = client.create_futures_order(futures_order)
print(f"期货订单已创建: {response.orderId}")
```

## API覆盖范围

### 现货交易API
- 市场数据 (Ping, 服务器时间, 交易所信息, 订单簿等)
- 账户管理 (账户信息, 子账户, API密钥类型)
- 订单管理 (创建, 取消, 查询订单)
- 批量操作 (批量创建/取消订单)

### 期货交易API
- 市场数据 (与现货相同 + 期货特定数据)
- 账户管理 (余额, 持仓, 杠杆, 保证金类型)
- 订单管理 (创建, 取消, 查询期货订单)
- 风险管理 (止损, 止盈, 保证金调整)
- 高级功能 (转账, 历史记录, 费率, 盈亏)

## 示例

项目包含两个目录中的全面示例：

### 现货示例 (`examples/spot/`)
- `01_24hr_ticker.py` - 获取24小时价格统计
- `02_open_orders.py` - 查询开放订单
- `03_all_orders.py` - 查询所有订单
- `04_trade_history.py` - 获取交易历史
- `05_create_order.py` - 创建新订单
- `06_cancel_order.py` - 取消订单
- `07_get_order.py` - 查询特定订单
- `08_batch_create_orders.py` - 批量创建订单
- `09_batch_cancel_orders.py` - 批量取消订单
- `10_cancel_open_orders.py` - 取消开放订单
- `11_get_spot_account_info.py` - 获取账户信息
- `12_get_spot_sub_accounts.py` - 获取子账户
- `13_get_api_key_type.py` - 获取API密钥类型

### 期货示例 (`examples/futures/`)
- `01_ping.py` - 测试服务器连接
- `02_server_time.py` - 获取服务器时间
- `03_exchange_info.py` - 获取交易所信息
- `04_order_book.py` - 获取订单簿
- `05_recent_trades.py` - 获取最近交易
- `06_klines.py` - 获取K线数据
- `07_24hr_ticker.py` - 获取24小时价格
- `08_price.py` - 获取最新价格
- `09_best_order_book.py` - 获取最佳订单簿
- `12_transfer_between_accounts.py` - 账户间转账
- `13_get_transfer_history.py` - 获取转账历史
- `14_create_futures_order.py` - 创建期货订单
- `15_batch_create_futures_orders.py` - 批量创建期货订单
- `16_get_futures_open_orders.py` - 获取期货开放订单
- `17_query_futures_order.py` - 查询期货订单
- `18_cancel_futures_order.py` - 取消期货订单
- `19_cancel_all_orders.py` - 取消所有订单
- `20_batch_cancel_orders.py` - 批量取消订单
- `21_get_futures_positions.py` - 获取期货持仓
- `22_set_position_trading_stop.py` - 设置持仓交易止损
- `23_get_futures_history_orders.py` - 获取期货历史订单
- `24_get_futures_balance.py` - 获取期货余额
- `25_adjust_isolated_margin.py` - 调整逐仓保证金
- `26_get_futures_trade_history.py` - 获取期货交易历史
- `27_get_futures_account_flow.py` - 获取期货账户流水
- `28_get_futures_user_fee_rate.py` - 获取期货用户费率
- `29_get_futures_today_pnl.py` - 获取期货今日盈亏
- `31_change_margin_type.py` - 更改保证金类型
- `32_adjust_leverage.py` - 调整杠杆
- `33_get_account_leverage.py` - 获取账户杠杆

## 配置

### 环境变量
创建`.env`文件或设置环境变量：

```bash
TOOBIT_API_KEY=your_api_key
TOOBIT_API_SECRET=your_api_secret
TOOBIT_BASE_URL=https://api.toobit.com
```

或者创建`config.example`文件并复制到您的环境：

```bash
# 复制示例配置文件
cp config.example .env

# 编辑.env文件，填入您的API凭据
nano .env

# 加载环境变量（如果使用shell）
source .env
```

### API密钥权限
- **只读**: 用于市场数据和账户查询
- **交易**: 用于订单创建和取消
- **用户数据**: 用于账户信息和历史记录

## 错误处理

SDK包含全面的错误处理：

```python
from open_api_sdk.exceptions import TooBitAPIException

try:
    response = client.create_order(order)
except TooBitAPIException as e:
    print(f"API错误: {e.message}")
    print(f"错误代码: {e.code}")
```

## 身份验证

SDK使用HMAC SHA256签名身份验证：

```python
# 自动签名生成
response = client.create_order(order)  # 自动签名

# 手动时间戳控制
config = TooBitConfig(
    api_key="your_key",
    api_secret="your_secret",
    recv_window=5000  # 5秒窗口
)
```

## 速率限制

- **请求权重**: 每个端点都有特定的权重
- **订单限制**: 订单操作的速率限制
- **IP限制**: 配置IP白名单以确保安全

## 贡献

1. Fork仓库
2. 创建功能分支
3. 进行更改
4. 如适用，添加测试
5. 提交拉取请求

## 许可证

本项目采用MIT许可证。

## 支持

如有问题和疑问：
- 查看examples目录了解使用模式
- 查阅TooBit API文档
- 在GitHub上提交问题

## 更新日志

### v1.0.0
- 初始版本
- 完整的现货交易支持
- 完整的期货交易支持
- 46+个示例文件
- 全面的错误处理
- 类型安全的数据模型