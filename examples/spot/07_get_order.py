"""
TooBit API SDK - Query Order API Example (07)
Query Order Status (Requires API key)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_order():
    """Query Order"""
    print("=== TooBit API Query Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First query open orders list
        print("🔄 Getting query open orders list...")
        open_orders = client.get_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  Currently no open orders, unable to query order details")
            return None
        
        print(f"✅ Get to {len(open_orders)} items open orders")
        print()
        
        # Select first items open orders perform query
        first_order = open_orders[0]
        symbol = first_order.symbol
        order_id = first_order.order_id
        
        print("🔄 Getting query order details...")
        print(f"   Trading pair: {symbol}")
        print(f"   Order ID: {order_id}")
        print()
        print("⚠️  Note: This is a real account query operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Call query order API
        from open_api_sdk.models import OrderQueryRequest
        query_request = OrderQueryRequest(symbol=symbol, orderId=int(order_id))
        order_response = client.get_order(query_request)
        
        print("✅ Order query success!")
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
        
        print("\n🎉 Query order complete!")
        return order_response
        
    except Exception as e:
        print(f"❌ Query order failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK Query Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real account query operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: GET /api/v1/spot/order")
    print("   - Auth: Requires signature (USER_DATA)")
    print("   - Function: Query order status")
    print("   - Parameters: symbol, orderId")
    print()
    print("⚠️  Important reminder:")
    print("   - It is recommended to verify in the test environment first")
    print()
    
    get_order()