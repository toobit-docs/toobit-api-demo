"""
TooBit Futures API SDK - Cancel Order Example (18)
Cancel Futures Order (Requires API key and signature)
API: DELETE /api/v1/futures/order
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import QueryFuturesOrderResponse

def cancel_futures_order():
    """Cancel Futures Order"""
    print("=== TooBit Futures API Cancel Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First Query Open Orders List
        print("🔄 Getting Query Open Orders List...")
        open_orders = client.get_futures_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  Currently no Open Orders, No need to cancel")
            return None
        
        print(f"✅ Retrieved {len(open_orders)} items Open Orders")
        print()
        
        # Select first items Open Orders for cancellation
        first_order = open_orders[0]
        symbol = first_order.symbol
        order_id = first_order.orderId
        client_order_id = first_order.clientOrderId
        
        print("🔄 Getting Cancel Futures Order...")
        print(f"   Trading pair: {symbol}")
        print(f"   Order ID: {order_id}")
        print(f"   Client Order ID: {client_order_id}")
        print()
        print("⚠️  Note: This is a real trading operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        response = client.cancel_futures_order(
            symbol=symbol,
            order_id=order_id,
            client_order_id=client_order_id
        )
        
        print("✅ Futures Order Cancel Success!")
        print()
        
        # Display Order Information
        print("📋 Cancel Order information:")
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
        
        print("\n🎉 Futures Order Cancel Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Futures Order Cancel Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit Futures API SDK Cancel Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real trading operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: DELETE /api/v1/futures/order")
    print("   - Auth: Requires signature (TRADE)")
    print("   - Function: Cancel Futures Order")
    print("   - Parameters: symbol(Required), orderId(Optional), origClientOrderId(Optional)")
    print()
    print("💡 Cancel Description:")
    print("   - Can through Order ID Cancel")
    print("   - Can through Client Order ID Cancel")
    print("   - After cancel, order status changes to CANCELED")
    print("   - Already Partial Execution of Order can also Cancel")
    print()
    print("⚠️  Important reminder:")
    print("   - Please ensure Order ID or Client Order ID is correct")
    print("   - Cancel Operation is Irreversible")
    print("   - It is recommended to verify in the test environment first")
    cancel_futures_order()
