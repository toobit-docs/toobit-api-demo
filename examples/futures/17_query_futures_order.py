"""
TooBit Futures API SDK - QueryOrder Example (17)
QueryFutures Order (Requires API key and signature)
API: GET /api/v1/futures/order
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import QueryFuturesOrderResponse

def query_futures_order():
    """Query Futures Order"""
    print("=== TooBit Futures API Query Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First Query Open Orders List
        print("🔄 Getting Query Open Orders List...")
        open_orders = client.get_futures_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  Currently No Open Orders, Unable to Query Order Details")
            return None
        
        print(f"✅ Retrieved {len(open_orders)} Items Open Orders")
        print()
        
        # Select First Items Open Orders Perform Query
        first_order = open_orders[0]
        symbol = first_order.symbol
        order_id = first_order.orderId
        client_order_id = first_order.clientOrderId
        
        print("🔄 Getting Query Futures Order Details...")
        print(f"   Trading pair: {symbol}")
        print(f"   Order ID: {order_id}")
        print(f"   Client Order ID: {client_order_id}")
        print()
        print("⚠️  Note: This is a real account query operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        response = client.get_futures_order(
            symbol=symbol,
            order_id=order_id,
            client_order_id=client_order_id
        )
        
        print("✅ Futures Order Query Success!")
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
        
        print("\n🎉 Futures Order Query Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Futures Order Query Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit Futures API SDK Query Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real account query operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: GET /api/v1/futures/order")
    print("   - Auth: Requires signature (USER_DATA)")
    print("   - Function: Query Futures Order")
    print("   - Parameters: symbol(Required), orderId(Optional), origClientOrderId(Optional)")
    print()
    print("💡 Query description:")
    print("   - Can through Order ID Query")
    print("   - Can through Client Order ID Query")
    print("   - Return Order of Detailed Information")
    print("   - Including Order Status, execution situation etc")
    print()
    print("📈 Order Status Description:")
    print("   - NEW: New Order")
    print("   - PARTIALLY_FILLED: Partial Execution")
    print("   - FILLED: Fully filled")
    print("   - CANCELED: Canceled")
    print("   - REJECTED: Rejected")
    print()
    print("⚠️  Important reminder:")
    print("   - Please ensure Order ID Or Client Order ID is correct")
    print("   - It is recommended to verify in the test environment first")
    query_futures_order()
