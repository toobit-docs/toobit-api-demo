"""
TooBit Futures API SDK - Futures Create Order Example (14)
Futures Create Order (Requires API key and signature)
API: POST /api/v1/futures/order
"""
import uuid
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import OrderRequest, OrderSide, OrderType, TimeInForce, CreateFuturesOrderResponse

def create_futures_order():
    """Futures Create Order"""
    print("=== TooBit Futures API Futures Create Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Order Parameters
        symbol = "BTC-SWAP-USDT"  # Trading pair
        side = OrderSide.BUY_OPEN  # Buy/Sell side: BUY_OPEN, SELL_OPEN, BUY_CLOSE, SELL_CLOSE
        order_type = OrderType.LIMIT  # Order type: LIMIT, MARKET
        quantity = "10"  # Quantity
        price = "50000"  # Price (not needed for market order)
        time_in_force = TimeInForce.GTC  # Time in force: GTC, IOC, FOK
        client_order_id = f"order_{uuid.uuid4().hex[:8]}"  # Client order ID (generated using UUID)
        
        print("🔄 Creating Futures Order...")
        print(f"   Trading pair: {symbol}")
        print(f"   Buy/Sell side: {side.value}")
        print(f"   Order type: {order_type.value}")
        print(f"   Quantity: {quantity}")
        print(f"   Price: {price}")
        print(f"   Time in force: {time_in_force.value}")
        print(f"   Client Order ID: {client_order_id}")
        print()
        print("⚠️  Note: This is a real trading operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Create Order Request
        order_request = OrderRequest(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price,
            timeInForce=time_in_force,
            newClientOrderId=client_order_id
        )
        
        response = client.create_futures_order(order_request)
        
        print("✅ Futures Order Create Success!")
        print()
        
        # Display Order Information
        print("📋 Order information:")
        if hasattr(response, 'time'):
            print(f"   ⏰ Order creation time: {response.time}")
        if hasattr(response, 'updateTime'):
            print(f"   🔄 Last update time: {response.updateTime}")
        if hasattr(response, 'orderId'):
            print(f"   🆔 Order ID: {response.orderId}")
        if hasattr(response, 'clientOrderId'):
            print(f"   🔑 Client Order ID: {response.clientOrderId}")
        if hasattr(response, 'symbol'):
            print(f"   📊 Trading pair: {response.symbol}")
        if hasattr(response, 'price'):
            print(f"   💰 Order price: {response.price}")
        if hasattr(response, 'leverage'):
            print(f"   📈 Order leverage: {response.leverage}")
        if hasattr(response, 'origQty'):
            print(f"   📊 Order Quantity: {response.origQty}")
        if hasattr(response, 'executedQty'):
            print(f"   ✅ Executed Quantity: {response.executedQty}")
        if hasattr(response, 'avgPrice'):
            print(f"   📊 Average Execution Price: {response.avgPrice}")
        if hasattr(response, 'marginLocked'):
            print(f"   🔒 Locked Margin: {response.marginLocked}")
        if hasattr(response, 'type'):
            print(f"   🔧 Order Type: {response.type}")
        if hasattr(response, 'side'):
            print(f"   📈 Buy/Sell Side: {response.side}")
        if hasattr(response, 'timeInForce'):
            print(f"   ⏰ Time In Force: {response.timeInForce}")
        if hasattr(response, 'status'):
            print(f"   📈 Order Status: {response.status}")
        if hasattr(response, 'priceType'):
            print(f"   🏷️  Price Type: {response.priceType}")
        
        print("\n🎉 Futures Order Create Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Futures Order Create Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit Futures API SDK Futures Create Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real trading operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: POST /api/v1/futures/order")
    print("   - Auth: Requires signature (TRADE)")
    print("   - Function: Create Futures Order")
    print("   - Support: Limit Order, Market Order")
    print()
    print("📈 Futures Side Type Description:")
    print("   - BUY_OPEN: Buy to open (long position)")
    print("   - SELL_OPEN: Sell to open (short position)")
    print("   - BUY_CLOSE: Buy to close (close short)")
    print("   - SELL_CLOSE: Sell to close (close long)")
    print()
    print("⚠️  Important reminder:")
    print("   - Please ensure sufficient account balance")
    print("   - Please carefully verify order parameters")
    print("   - Order cannot be canceled after creation")
    print("   - It is recommended to verify in the test environment first")
    create_futures_order()
