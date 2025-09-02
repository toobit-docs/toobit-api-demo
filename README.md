# TooBit API SDK

一个功能完整的TooBit加密货币交易所API SDK，支持现货交易、行情查询、账户管理等所有主要功能。

## 特性

- 🔐 **完整鉴权支持**: 支持HMAC SHA256签名鉴权
- 📊 **行情数据**: 实时价格、深度、K线、成交记录等
- 💰 **交易功能**: 支持限价单、市价单、止损单等多种订单类型
- 👤 **账户管理**: 查询余额、订单状态、成交历史等
- 🛡️ **错误处理**: 完善的错误码映射和异常处理
- ⚡ **性能优化**: 连接池、超时控制、重试机制
- 📝 **类型提示**: 完整的Python类型提示支持
- 🔧 **灵活配置**: 支持环境变量和代码配置

## 安装

```bash
# 克隆项目
git clone <repository-url>
cd open-api-sdk

# 安装依赖
pip install -r requirements.txt
```

## 快速开始

### 1. 配置API密钥

创建 `.env` 文件并配置你的API密钥：

```bash
# 复制配置示例文件
cp config.example .env

# 编辑配置文件，填入你的API密钥
TOOBIT_API_KEY=your_api_key_here
TOOBIT_API_SECRET=your_api_secret_here
```

### 2. 基本使用

```python
from open_api_sdk import TooBitClient, TooBitConfig

# 从环境变量创建配置
config = TooBitConfig.from_env()

# 创建客户端
client = TooBitClient(config)

# 测试连接
if client.ping():
    print("✅ 连接成功")

# 获取BTC价格
price_info = client.get_price("BTCUSDT")
print(f"BTC价格: {price_info['price']}")

# 获取账户信息
account = client.get_account_info()
print(f"账户类型: {account.account_type}")

# 关闭客户端
client.close()
```

### 3. 交易示例

```python
from open_api_sdk import OrderRequest, OrderSide, OrderType, TimeInForce

# 限价买入
order_request = OrderRequest(
    symbol="BTCUSDT",
    side=OrderSide.BUY,
    type=OrderType.LIMIT,
    quantity=0.001,
    price=50000.0,
    time_in_force=TimeInForce.GTC
)

response = client.create_order(order_request)
print(f"订单创建成功! ID: {response.order_id}")

# 使用便捷方法
response = client.buy_limit("BTCUSDT", 0.001, 50000.0)
response = client.sell_limit("BTCUSDT", 0.001, 51000.0)
```

## API 接口

### 公开接口 (无需鉴权)

- `ping()` - 测试服务器连通性
- `get_server_time()` - 获取服务器时间
- `get_exchange_info()` - 获取交易规则和交易对信息
- `get_order_book(symbol, limit)` - 获取深度信息
- `get_recent_trades(symbol, limit)` - 获取最近成交
- `get_klines(symbol, interval, limit)` - 获取K线数据
- `get_24hr_ticker(symbol)` - 获取24小时价格变动
- `get_price(symbol)` - 获取最新价格
- `get_best_order_book(symbol)` - 获取当前最优挂单

### 签名接口 (需要API密钥)

- `create_order(order_request)` - 下单
- `cancel_order(cancel_request)` - 撤销订单
- `get_order(query_request)` - 查询订单
- `get_open_orders(symbol)` - 查询当前挂单
- `get_all_orders(symbol, ...)` - 查询所有订单
- `get_account_info()` - 获取账户信息
- `get_trade_history(symbol, ...)` - 获取成交历史

### 便捷方法

- `buy_limit(symbol, quantity, price)` - 限价买入
- `sell_limit(symbol, quantity, price)` - 限价卖出
- `buy_market(symbol, quantity)` - 市价买入
- `sell_market(symbol, quantity)` - 市价卖出
- `cancel_order_by_id(symbol, order_id)` - 通过ID取消订单
- `get_balance(asset)` - 获取指定资产余额

## 订单类型

- **LIMIT**: 限价单
- **MARKET**: 市价单
- **STOP_LOSS**: 止损单
- **STOP_LOSS_LIMIT**: 限价止损单
- **TAKE_PROFIT**: 止盈单
- **TAKE_PROFIT_LIMIT**: 限价止盈单
- **LIMIT_MAKER**: 限价挂单

## 订单有效期

- **GTC**: Good Till Canceled (一直有效直到取消)
- **IOC**: Immediate or Cancel (立即成交或取消)
- **FOK**: Fill or Kill (全部成交或全部取消)

## 错误处理

SDK提供了完善的错误处理机制，包括：

- `TooBitException`: 基础异常类
- `AuthenticationError`: 认证错误
- `ValidationError`: 参数验证错误
- `OrderError`: 订单相关错误
- `RateLimitError`: 速率限制错误
- `NetworkError`: 网络错误

```python
from open_api_sdk import TooBitException, AuthenticationError

try:
    response = client.create_order(order_request)
except AuthenticationError as e:
    print(f"认证失败: {e}")
except TooBitException as e:
    print(f"API错误: {e}")
```

## 配置选项

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `api_key` | - | API密钥 (必需) |
| `api_secret` | - | API密钥 (必需) |
| `base_url` | https://api.toobit.com | API基础URL |
| `timeout` | 30 | 请求超时时间(秒) |
| `recv_window` | 5000 | 接收窗口时间(毫秒) |
| `max_retries` | 3 | 最大重试次数 |
| `retry_delay` | 1.0 | 重试延迟时间(秒) |

## 示例代码

查看 `examples/` 目录获取更多使用示例：

### 🔌 基础功能示例 (无需API密钥)
- `01_connection_test.py` - 连接测试示例
- `02_market_data.py` - 市场数据查询示例

### 👤 账户管理示例 (需要API密钥)
- `03_account_info.py` - 账户信息查询示例

### 💰 交易操作示例 (需要API密钥)
- `04_basic_trading.py` - 基本交易示例
- `05_advanced_trading.py` - 高级交易示例

### 🚀 快速开始

```bash
# 1. 测试连接 (无需API密钥)
python examples/01_connection_test.py

# 2. 获取市场数据 (无需API密钥)
python examples/02_market_data.py

# 3. 设置API密钥后运行其他示例
export TOOBIT_API_KEY='your_api_key'
export TOOBIT_API_SECRET='your_api_secret'

# 4. 查询账户信息
python examples/03_account_info.py

# 5. 基本交易操作
python examples/04_basic_trading.py

# 6. 高级交易操作
python examples/05_advanced_trading.py
```

详细说明请查看 [examples/README.md](examples/README.md)

## 安全注意事项

1. **永远不要泄露你的API密钥**
2. 建议设置IP白名单限制
3. 定期轮换API密钥
4. 使用最小权限原则配置API权限
5. 在生产环境中使用环境变量存储敏感信息

## 速率限制

TooBit API有严格的速率限制：

- 请求权重限制: 1200/分钟
- 订单限制: 10/秒
- 违反限制会收到429错误码

建议使用WebSocket获取实时数据以减少API调用。

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License

## 免责声明

本SDK仅供学习和研究使用，使用本SDK进行交易的风险由用户自行承担。作者不对任何交易损失负责。

## 支持

如有问题，请：

1. 查看 [TooBit官方API文档](https://toobit-docs.github.io/apidocs/spot/v1/cn/)
2. 提交GitHub Issue
3. 检查错误日志和异常信息 