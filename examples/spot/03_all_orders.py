"""
TooBit API SDK - Query All Order API Example (03)
Query All Order (Requires API key)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_all_orders():
    """Query All Order"""
    print("=== TooBit API Query All Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"  # Trading pair
        
        print("🔄 Getting query all order...")
        print(f"   Trading pair: {symbol}")
        print()
        print("⚠️  Note: This is a real account query operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Call query all order API
        all_orders = client.get_all_orders(symbol)
        
        print("✅ All order query success!")
        print()
        
        # Display order information
        if all_orders and len(all_orders) > 0:
            print(f"📊 All order information (Total {len(all_orders)} items):")
            for i, order in enumerate(all_orders[:5]):  # Only display before 5 items
                print(f"\n   Order {i+1}:")
                print(f"     🆔 Order ID: {order.order_id}")
                print(f"     🔑 Client Order ID: {order.client_order_id}")
                print(f"     📊 Trading pair: {order.symbol}")
                print(f"     💰 Price: {order.price}")
                print(f"     📊 Quantity: {order.orig_qty}")
                print(f"     ✅ Executed quantity: {order.executed_qty}")
                print(f"     🔧 Order type: {order.type}")
                print(f"     📈 Buy/Sell side: {order.side}")
                print(f"     📈 Order status: {order.status}")
                print(f"     ⏰ Time in force: {order.time_in_force}")
                print(f"     🕐 Trade Time: {order.time}")
            
            if len(all_orders) > 5:
                print(f"\n   ... and {len(all_orders) - 5} more orders")
        else:
            print("   ℹ️  No orders found")
        
        print("\n🎉 Query all order complete!")
        return all_orders
        
    except Exception as e:
        print(f"❌ Query all order failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK Query All Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real account query operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: GET /api/v1/spot/allOrders")
    print("   - Auth: Requires signature (USER_DATA)")
    print("   - Function: Query all order")
    print("   - Parameters: symbol")
    print()
    print("⚠️  Important reminder:")
    print("   - It is recommended to verify in the test environment first")
    print()
    
    get_all_orders()