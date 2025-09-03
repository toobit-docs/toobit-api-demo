"""
TooBit API SDK - Create Order API Example (05)
Create various types of orders (Requires API key)
"""
import uuid
from open_api_sdk import (
    TooBitClient, TooBitConfig, OrderRequest, 
    OrderSide, OrderType, TimeInForce
)

def create_limit_order():
    """Create Limit Order"""
    print("=== TooBit API Create Limit Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Create limit price buy order
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            quantity=0.001,  # Buy 0.001 BTC
            price=50000.0,   # Limit price 50000 USDT
            time_in_force=TimeInForce.GTC,  # Valid until canceled
            client_order_id=f"order_{uuid.uuid4().hex[:8]}"  # Client Order ID
        )
        
        print("🔄 Getting create limit order...")
        print(f"   Trading pair: {order_request.symbol}")
        print(f"   Side: {order_request.side}")
        print(f"   Type: {order_request.type}")
        print(f"   Quantity: {order_request.quantity}")
        print(f"   Price: {order_request.price}")
        print()
        print("⚠️  Note: This is a real trading operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Call create order API
        order_response = client.create_order(order_request)
        
        print("✅ Limit order create success!")
        print()
        
        # Display order information
        print("📋 Order information:")
        print(f"   Order ID: {order_response.order_id}")
        print(f"   Client Order ID: {order_response.client_order_id}")
        print(f"   Trading pair: {order_response.symbol}")
        print(f"   Status: {order_response.status}")
        print(f"   Type: {order_response.type}")
        print(f"   Side: {order_response.side}")
        print(f"   Quantity: {order_response.orig_qty}")
        print(f"   Price: {order_response.price}")
        print(f"   Executed quantity: {order_response.executed_qty}")
        print(f"   Trade Time: {order_response.transact_time}")
        
        print("\n🎉 Create limit order complete!")
        return order_response
        
    except Exception as e:
        print(f"❌ Create limit order failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK Create Limit Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real trading operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: POST /api/v1/spot/order")
    print("   - Auth: Requires signature (TRADE)")
    print("   - Function: Create limit order")
    print("   - Parameters: symbol, side, type, quantity, price, timeInForce")
    print()
    print("⚠️  Important reminder:")
    print("   - It is recommended to verify in the test environment first")
    print("   - Order create after unable to cancel")
    print()
    
    create_limit_order()