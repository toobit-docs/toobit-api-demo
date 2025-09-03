# TooBit API SDK

A comprehensive Python SDK for TooBit cryptocurrency exchange API, supporting both spot and futures trading.

> **⚠️ Disclaimer**: This SDK is for reference only. Please refer to the official TooBit API documentation for the most up-to-date and accurate information.

## Features

- **Spot Trading**: Complete spot trading functionality
- **Futures Trading**: Full USDT-margined futures trading support
- **Type Safety**: Built with Pydantic for robust data validation
- **Easy to Use**: Simple and intuitive API design
- **Comprehensive Examples**: 46+ example files covering all major operations

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Configuration

```python
from open_api_sdk import TooBitClient, TooBitConfig

# Initialize configuration
config = TooBitConfig(
    api_key="your_api_key",
    api_secret="your_api_secret",
    base_url="https://api.toobit.com"
)

# Create client
client = TooBitClient(config)
```

### Spot Trading Example

```python
from open_api_sdk.models import OrderRequest, OrderSide, OrderType, TimeInForce

# Create a limit order
order = OrderRequest(
    symbol="BTCUSDT",
    side=OrderSide.BUY,
    type=OrderType.LIMIT,
    quantity=0.01,
    price=45000.0,
    time_in_force=TimeInForce.GTC
)

# Place the order
response = client.create_order(order)
print(f"Order created: {response.order_id}")
```

### Futures Trading Example

```python
from open_api_sdk.models import CreateFuturesOrderRequest, OrderSide

# Create a futures order
futures_order = CreateFuturesOrderRequest(
    symbol="BTC-SWAP-USDT",
    side=OrderSide.BUY_OPEN,
    type=OrderType.LIMIT,
    quantity=1,
    price=50000.0,
    leverage=10
)

# Place the futures order
response = client.create_futures_order(futures_order)
print(f"Futures order created: {response.orderId}")
```

## API Coverage

### Spot Trading APIs
- Market Data (Ping, Server Time, Exchange Info, Order Book, etc.)
- Account Management (Account Info, Sub-accounts, API Key Type)
- Order Management (Create, Cancel, Query Orders)
- Batch Operations (Batch Create/Cancel Orders)

### Futures Trading APIs
- Market Data (Same as spot + futures-specific data)
- Account Management (Balance, Positions, Leverage, Margin Type)
- Order Management (Create, Cancel, Query Futures Orders)
- Risk Management (Stop Loss, Take Profit, Margin Adjustment)
- Advanced Features (Transfer, History, Fee Rates, PnL)

## Examples

The project includes comprehensive examples in two directories:

### Spot Examples (`examples/spot/`)
- `01_24hr_ticker.py` - Get 24hr ticker statistics
- `02_open_orders.py` - Query open orders
- `03_all_orders.py` - Query all orders
- `04_trade_history.py` - Get trade history
- `05_create_order.py` - Create a new order
- `06_cancel_order.py` - Cancel an order
- `07_get_order.py` - Query specific order
- `08_batch_create_orders.py` - Batch create orders
- `09_batch_cancel_orders.py` - Batch cancel orders
- `10_cancel_open_orders.py` - Cancel open orders
- `11_get_spot_account_info.py` - Get account information
- `12_get_spot_sub_accounts.py` - Get sub-accounts
- `13_get_api_key_type.py` - Get API key type

### Futures Examples (`examples/futures/`)
- `01_ping.py` - Test server connectivity
- `02_server_time.py` - Get server time
- `03_exchange_info.py` - Get exchange information
- `04_order_book.py` - Get order book
- `05_recent_trades.py` - Get recent trades
- `06_klines.py` - Get kline data
- `07_24hr_ticker.py` - Get 24hr ticker
- `08_price.py` - Get latest price
- `09_best_order_book.py` - Get best order book
- `12_transfer_between_accounts.py` - Transfer between accounts
- `13_get_transfer_history.py` - Get transfer history
- `14_create_futures_order.py` - Create futures order
- `15_batch_create_futures_orders.py` - Batch create futures orders
- `16_get_futures_open_orders.py` - Get futures open orders
- `17_query_futures_order.py` - Query futures order
- `18_cancel_futures_order.py` - Cancel futures order
- `19_cancel_all_orders.py` - Cancel all orders
- `20_batch_cancel_orders.py` - Batch cancel orders
- `21_get_futures_positions.py` - Get futures positions
- `22_set_position_trading_stop.py` - Set position trading stop
- `23_get_futures_history_orders.py` - Get futures history orders
- `24_get_futures_balance.py` - Get futures balance
- `25_adjust_isolated_margin.py` - Adjust isolated margin
- `26_get_futures_trade_history.py` - Get futures trade history
- `27_get_futures_account_flow.py` - Get futures account flow
- `28_get_futures_user_fee_rate.py` - Get futures user fee rate
- `29_get_futures_today_pnl.py` - Get futures today PnL
- `31_change_margin_type.py` - Change margin type
- `32_adjust_leverage.py` - Adjust leverage
- `33_get_account_leverage.py` - Get account leverage

## Configuration

### Environment Variables
Create a `.env` file or set environment variables:

```bash
TOOBIT_API_KEY=your_api_key
TOOBIT_API_SECRET=your_api_secret
TOOBIT_BASE_URL=https://api.toobit.com
```

Or create a `config.example` file and copy it to your environment:

```bash
# Copy the example config file
cp config.example .env

# Edit the .env file with your API credentials
nano .env

# Source the environment variables (if using shell)
source .env
```

### API Key Permissions
- **Read Only**: For market data and account queries
- **Trade**: For order creation and cancellation
- **User Data**: For account information and history

## Error Handling

The SDK includes comprehensive error handling:

```python
from open_api_sdk.exceptions import TooBitAPIException

try:
    response = client.create_order(order)
except TooBitAPIException as e:
    print(f"API Error: {e.message}")
    print(f"Error Code: {e.code}")
```

## Authentication

The SDK uses HMAC SHA256 signature authentication:

```python
# Automatic signature generation
response = client.create_order(order)  # Signs automatically

# Manual timestamp control
config = TooBitConfig(
    api_key="your_key",
    api_secret="your_secret",
    recv_window=5000  # 5 second window
)
```

## Rate Limits

- **Request Weight**: Each endpoint has a specific weight
- **Order Limits**: Rate limits for order operations
- **IP Restrictions**: Configure IP whitelist for security

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Check the examples directory for usage patterns
- Review the TooBit API documentation
- Open an issue on GitHub

## Changelog

### v1.0.0
- Initial release
- Complete spot trading support
- Complete futures trading support
- 46+ example files
- Comprehensive error handling
- Type-safe data models
