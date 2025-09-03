"""
TooBit Futures API SDK - View all open orders Example (16)
View all open orders (Requires API key and signature)
API: GET /api/v1/futures/openOrders
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import FuturesOpenOrderResponse

def get_futures_open_orders():
    """View all open orders"""
    print("=== TooBit Futures API View all open orders ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Query Parameters
        symbol = "BTC-SWAP-USDT"  # Trading pair (Optional, If not passed Query All Trading Pairs of Open Orders)
        
        print("🔄 Getting Query Current All Open Orders...")
        if symbol:
            print(f"   Trading pair: {symbol}")
        else:
            print("   Trading pair: All")
        print()
        print("⚠️  Note: This is a real account query operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        response = client.get_futures_open_orders(symbol=symbol)
        
        print("✅ Open Orders Query Success!")
        print()
        
        # Display Open Orders Information
        if response and len(response) > 0:
            print(f"📊 Current Open Orders Information (Total {len(response)} items):")
            for i, order in enumerate(response):
                print(f"\n   Open Orders {i+1}:")
                if hasattr(order, 'time'):
                    print(f"     ⏰ Order creation time: {order.time}")
                if hasattr(order, 'updateTime'):
                    print(f"     🔄 Last update time: {order.updateTime}")
                if hasattr(order, 'orderId'):
                    print(f"     🆔 Order ID: {order.orderId}")
                if hasattr(order, 'clientOrderId'):
                    print(f"     🔑 Client Order ID: {order.clientOrderId}")
                if hasattr(order, 'symbol'):
                    print(f"     📊 Trading pair: {order.symbol}")
                if hasattr(order, 'price'):
                    print(f"     💰 Order price: {order.price}")
                if hasattr(order, 'leverage'):
                    print(f"     📈 Order leverage: {order.leverage}")
                if hasattr(order, 'origQty'):
                    print(f"     📊 Order Quantity: {order.origQty}")
                if hasattr(order, 'executedQty'):
                    print(f"     ✅ Executed Quantity: {order.executedQty}")
                if hasattr(order, 'avgPrice'):
                    print(f"     📊 Average Execution Price: {order.avgPrice}")
                if hasattr(order, 'marginLocked'):
                    print(f"     🔒 Locked Margin: {order.marginLocked}")
                if hasattr(order, 'type'):
                    print(f"     🔧 Order Type: {order.type}")
                if hasattr(order, 'side'):
                    print(f"     📈 Buy/Sell Side: {order.side}")
                if hasattr(order, 'timeInForce'):
                    print(f"     ⏰ Time In Force: {order.timeInForce}")
                if hasattr(order, 'status'):
                    print(f"     📈 Order Status: {order.status}")
                if hasattr(order, 'priceType'):
                    print(f"     🏷️  Price Type: {order.priceType}")
        else:
            print("   ℹ️  Currently No Open Orders")
        
        print("\n🎉 Open Orders Query Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Open Orders Query Failed: {e}")
        return None
    finally:
        client.close()

def cancel_order_from_open_orders():
    """Based on Open Orders List for Cancellation Operation"""
    print("=== TooBit Futures API Based on Open Orders List Cancel Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First Get Open Orders List
        print("🔄 Getting Open Orders List...")
        open_orders = client.get_futures_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  Currently No Open Orders, No need to cancel")
            return
        
        print(f"✅ Retrieved {len(open_orders)} Items Open Orders")
        print()
        
        # Select First Items Open Orders for Cancellation Demo
        first_order = open_orders[0]
        print("🔄 Getting Cancel First Items Open Orders...")
        print(f"   Order ID: {first_order.orderId}")
        print(f"   Trading pair: {first_order.symbol}")
        print(f"   Client Order ID: {first_order.clientOrderId}")
        print()
        print("⚠️  Note: This is a real Cancel Order Operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Execute Cancel order
        cancel_response = client.cancel_futures_order(
            symbol=first_order.symbol,
            order_id=first_order.orderId
        )
        
        print("✅ Cancel Order Operation Success!")
        print()
        
        # Display Cancel Order Result
        print("📋 Cancel Order Result:")
        if hasattr(cancel_response, 'orderId'):
            print(f"   🆔 Order ID: {cancel_response.orderId}")
        if hasattr(cancel_response, 'symbol'):
            print(f"   📊 Trading pair: {cancel_response.symbol}")
        if hasattr(cancel_response, 'status'):
            print(f"   📈 Order Status: {cancel_response.status}")
        
        print("\n🎉 Cancel Order Operation Complete!")
        return cancel_response
        
    except Exception as e:
        print(f"❌ Cancel Order Operation Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit Futures API SDK View All Open Orders Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real account query operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: GET /api/v1/futures/openOrders")
    print("   - Auth: Requires signature (USER_DATA)")
    print("   - Function: View all open orders")
    print("   - Parameters: symbol(Optional)")
    print()
    print("💡 Query description:")
    print("   - Not passed symbol Parameters then Query All Trading Pairs of Open Orders")
    print("   - Passed symbol Parameters Then only Query Specified Trading Pair of Open Orders")
    print("   - Return Current All Not Execution of Order")
    print("   - Including Order of Detailed Information And Status")
    print()
    print("📈 Order Status Description:")
    print("   - NEW: New Order")
    print("   - PARTIALLY_FILLED: Partial Execution")
    print("   - FILLED: Fully filled")
    print("   - CANCELED: Canceled")
    print("   - REJECTED: Rejected")
    print()
    print("⚠️  Important reminder:")
    print("   - It is recommended to verify in the test environment first")
    print("   - Open Orders Information Contains Sensitive of Trade Data")
    print()

    get_futures_open_orders()
