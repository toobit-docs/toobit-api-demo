# TooBit API SDK 示例代码

本目录包含了 TooBit API SDK 的完整示例代码，分为现货交易和合约交易两个部分。

## 📁 目录结构

```
examples/
├── README.md           # 本说明文件
├── spot/              # 现货交易示例
│   ├── 01_ping.py                    # PING测试
│   ├── 02_server_time.py             # 获取服务器时间
│   ├── 03_exchange_info.py           # 获取交易所信息
│   ├── 04_order_book.py              # 获取深度信息
│   ├── 05_recent_trades.py           # 获取最近成交
│   ├── 06_klines.py                  # 获取K线数据
│   ├── 07_24hr_ticker.py             # 获取24小时价格变动
│   ├── 08_price.py                   # 获取最新价格
│   ├── 09_best_order_book.py         # 获取最优挂单
│   ├── 10_account_info.py            # 获取账户信息
│   ├── 11_balance.py                 # 获取账户余额
│   ├── 12_open_orders.py             # 查询当前挂单
│   ├── 13_all_orders.py              # 查询所有订单
│   ├── 14_trade_history.py           # 获取成交历史
│   ├── 15_create_order.py            # 创建订单
│   ├── 16_cancel_order.py            # 取消订单
│   ├── 17_get_order.py               # 查询订单
│   ├── 18_stop_loss_orders.py        # 止损订单
│   ├── 19_iceberg_orders.py          # 冰山订单
│   └── 20_maker_orders.py            # 挂单策略
└── futures/           # 合约交易示例
    ├── 01_ping.py                    # PING测试
    ├── 02_server_time.py             # 获取服务器时间
    ├── 03_exchange_info.py           # 获取交易所信息
    ├── 04_order_book.py              # 获取深度信息
    ├── 05_recent_trades.py           # 获取最近成交记录
    ├── 06_klines.py                  # 获取K线数据
    ├── 07_24hr_ticker.py             # 获取24小时价格变动
    ├── 08_price.py                   # 获取最新价格
    ├── 09_best_order_book.py         # 获取最优挂单
    ├── 10_account_info.py            # 获取账户信息
    ├── 11_get_order.py               # 查询订单
    ├── 12_trade_history.py           # 获取成交历史
    ├── 15_create_order.py            # 创建订单
    ├── 16_cancel_order.py            # 取消订单
    ├── 17_batch_orders.py            # 批量下单
    ├── 18_positions.py               # 持仓查询
    ├── 19_funding_rate.py            # 资金费率
    └── 20_batch_cancel.py            # 批量撤单
```

## 🎯 现货交易示例 (spot/)

现货交易示例涵盖了 TooBit 现货交易的所有主要功能：

### 🔗 基础接口
- **01_ping.py** - 测试服务器连通性
- **02_server_time.py** - 获取服务器时间
- **03_exchange_info.py** - 获取交易规则和交易对信息

### 📊 行情接口
- **04_order_book.py** - 获取订单簿深度信息
- **05_recent_trades.py** - 获取最近成交记录
- **06_klines.py** - 获取K线数据
- **07_24hr_ticker.py** - 获取24小时价格变动统计
- **08_price.py** - 获取最新价格
- **09_best_order_book.py** - 获取最优挂单

### 💰 账户接口
- **10_account_info.py** - 获取账户信息
- **11_balance.py** - 获取账户余额

### 📋 交易接口
- **12_open_orders.py** - 查询当前挂单
- **13_all_orders.py** - 查询所有订单
- **14_trade_history.py** - 获取成交历史
- **15_create_order.py** - 创建订单
- **16_cancel_order.py** - 取消订单
- **17_get_order.py** - 查询订单详情

### 🎛️ 高级功能
- **18_stop_loss_orders.py** - 止损订单策略
- **19_iceberg_orders.py** - 冰山订单策略
- **20_maker_orders.py** - 挂单策略

## 🚀 合约交易示例 (futures/)

合约交易示例涵盖了 TooBit U本位合约交易的主要功能：

### 🔗 基础接口
- **01_ping.py** - 测试服务器连通性
- **02_server_time.py** - 获取服务器时间
- **03_exchange_info.py** - 获取交易规则和交易对信息

### 📊 行情接口
- **04_order_book.py** - 获取订单簿深度信息
- **05_recent_trades.py** - 获取最近成交记录
- **06_klines.py** - 获取K线/蜡烛图数据
- **07_24hr_ticker.py** - 获取24小时价格变动统计
- **08_price.py** - 获取最新价格
- **09_best_order_book.py** - 获取最优挂单信息

### 💰 账户接口
- **10_account_info.py** - 获取账户信息和余额

### 📋 交易接口
- **11_get_order.py** - 查询订单状态和详情
- **12_trade_history.py** - 获取成交历史记录
- **15_create_order.py** - 创建合约订单
- **16_cancel_order.py** - 取消合约订单
- **17_batch_orders.py** - 批量创建订单

### 🎯 高级功能
- **18_positions.py** - 查询持仓信息和风险分析
- **19_funding_rate.py** - 获取资金费率和套利分析
- **20_batch_cancel.py** - 批量取消订单

## 🚨 重要提醒

### ⚠️ 安全注意事项
1. **API密钥安全**: 所有示例都需要真实的API密钥，请妥善保管
2. **测试环境**: 建议先在测试环境中验证所有功能
3. **小额测试**: 首次使用请使用小额资金进行测试
4. **权限控制**: 根据实际需要设置API密钥的权限

### 🔐 API密钥配置

#### 现货交易示例
现货交易示例需要设置环境变量：

```bash
# 现货交易
export TOOBIT_API_KEY='your_api_key'
export TOOBIT_API_SECRET='your_api_secret'

# 可选配置
export TOOBIT_RECV_WINDOW=5000
export TOOBIT_MAX_RETRIES=3
export TOOBIT_RETRY_DELAY=1
```

#### 合约交易示例
合约交易示例已配置测试密钥，可直接运行。如需使用真实API密钥，请修改文件中的配置：
```python
config = TooBitConfig(
    api_key="your_real_api_key",
    api_secret="your_real_api_secret",
    base_url="https://api.toobit.com"
)
```

### 📚 使用说明

#### 1. 无需API密钥的示例
以下示例无需API密钥，可以直接运行：
- `01_ping.py` - 测试连通性
- `02_server_time.py` - 获取时间
- `03_exchange_info.py` - 获取交易所信息
- `04_order_book.py` - 获取深度信息

#### 2. 需要API密钥的示例
现货交易示例需要配置环境变量：
- 账户相关接口 (10-11)
- 交易相关接口 (12-20)

合约交易示例已配置测试密钥，可直接运行：
- 账户相关接口 (10)
- 交易相关接口 (11-20)

#### 3. 运行示例
```bash
# 运行现货示例
cd examples/spot
python3 01_ping.py

# 运行合约示例
cd examples/futures
python3 01_ping.py
```

## 🛠️ 开发建议

### 1. 学习顺序
1. 先运行无需API密钥的示例，熟悉接口
2. 配置API密钥后，运行账户查询示例
3. 使用小额资金测试交易接口
4. 逐步尝试高级功能

### 2. 错误处理
- 所有示例都包含完整的错误处理
- 注意查看错误信息和可能的原因
- 根据错误信息调整参数或检查配置

### 3. 性能优化
- 遵守API速率限制
- 合理设置请求间隔
- 使用适当的缓存策略

### 4. 监控和日志
- 记录所有API调用
- 监控错误率和响应时间
- 设置告警机制

## 📖 相关文档

- [TooBit 现货API文档](https://toobit-docs.github.io/apidocs/spot/v1/cn/)
- [TooBit 合约API文档](https://toobit-docs.github.io/apidocs/usdt_swap/v1/cn/)
- [TooBit API SDK 主文档](../README.md)

## 🤝 技术支持

如果在使用过程中遇到问题，请：

1. 检查环境变量配置
2. 查看错误信息和可能原因
3. 参考API官方文档
4. 检查网络连接和API服务状态

---

**⚠️ 风险提醒**: 加密货币交易存在风险，请谨慎投资，合理控制仓位，不要投入超出承受能力的资金。 