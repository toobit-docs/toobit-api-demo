"""
TooBit API SDK - Cancel Order API Example (06)
Cancel Order (Requires API key)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def cancel_order():
    """Cancel Order"""
    print("=== TooBit API Cancel Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First query open orders list
        print("🔄 Getting query open orders list...")
        open_orders = client.get_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  Currently no open orders, no need to cancel")
            return None
        
        print(f"✅ Get to {len(open_orders)} items open orders")
        print()
        
        # Select first items open orders for cancellation
        first_order = open_orders[0]
        symbol = first_order.symbol
        order_id = first_order.order_id
        
        print("🔄 Getting cancel order...")
        print(f"   Trading pair: {symbol}")
        print(f"   Order ID: {order_id}")
        print()
        print("⚠️  Note: This is a real trading operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Call cancel order API
        cancel_response = client.cancel_order(symbol, order_id)
        
        print("✅ Order cancel success!")
        print()
        
        # Display cancel result
        print("📋 Cancel Result:")
        print(f"   Order ID: {cancel_response.order_id}")
        print(f"   Client Order ID: {cancel_response.client_order_id}")
        print(f"   Trading pair: {cancel_response.symbol}")
        print(f"   Status: {cancel_response.status}")
        print(f"   Type: {cancel_response.type}")
        print(f"   Side: {cancel_response.side}")
        print(f"   Quantity: {cancel_response.orig_qty}")
        print(f"   Price: {cancel_response.price}")
        print(f"   Executed quantity: {cancel_response.executed_qty}")
        print(f"   Trade Time: {cancel_response.transact_time}")
        
        print("\n🎉 Cancel order complete!")
        return cancel_response
        
    except Exception as e:
        print(f"❌ Cancel order failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK Cancel Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real trading operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: DELETE /api/v1/spot/order")
    print("   - Auth: Requires signature (TRADE)")
    print("   - Function: Cancel order")
    print("   - Parameters: symbol, orderId")
    print()
    print("⚠️  Important reminder:")
    print("   - It is recommended to verify in the test environment first")
    print("   - Can only cancel unexecuted orders")
    print()
    
    cancel_order()