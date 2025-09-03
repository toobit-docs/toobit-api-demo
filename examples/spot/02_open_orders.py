"""
TooBit API SDK - View Current Open Orders API Example (02)
View Current Open Orders (Requires API key)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_open_orders():
    """View Current Open Orders"""
    print("=== TooBit API View Current Open Orders ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"  # Trading pair (Optional, if not passed query all trading pairs of open orders)
        
        print("🔄 Getting view current open orders...")
        if symbol:
            print(f"   Trading pair: {symbol}")
        else:
            print("   Trading pair: All")
        print()
        print("⚠️  Note: This is a real account query operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Call view open orders API
        open_orders = client.get_open_orders(symbol)
        
        print("✅ Open orders query success!")
        print()
        
        # Display open orders information
        if open_orders and len(open_orders) > 0:
            print(f"📊 Current open orders information (Total {len(open_orders)} items):")
            for i, order in enumerate(open_orders):
                print(f"\n   Open order {i+1}:")
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
        else:
            print("   ℹ️  Currently no open orders")
        
        print("\n🎉 View open orders complete!")
        return open_orders
        
    except Exception as e:
        print(f"❌ View open orders failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK View Current Open Orders Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real account query operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: GET /api/v1/spot/openOrders")
    print("   - Auth: Requires signature (USER_DATA)")
    print("   - Function: View current open orders")
    print("   - Parameters: symbol (Optional)")
    print()
    print("⚠️  Important reminder:")
    print("   - It is recommended to verify in the test environment first")
    print()
    
    get_open_orders()