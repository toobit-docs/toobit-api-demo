"""
TooBit API SDK - Batch Cancel Order API Example (09)
Batch Cancel Multiple Items Order (Requires API key)
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import BatchCancelOrdersResponse, BatchCancelOrderResult

def batch_cancel_orders():
    """Batch Cancel Order"""
    print("=== TooBit API Batch Cancel Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First Query Open Orders List
        print("🔄 Getting Query Open Orders List...")
        open_orders = client.get_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  Currently no Open Orders, no need to cancel")
            return None
        
        print(f"✅ Get To {len(open_orders)} items Open Orders")
        print()
        
        # Select first few open orders to perform batch cancel (maximum 5 orders)
        max_orders = min(5, len(open_orders))
        orders_to_cancel = open_orders[:max_orders]
        order_ids = [order.order_id for order in orders_to_cancel]
        symbol = orders_to_cancel[0].symbol if orders_to_cancel else "BTCUSDT"
        
        print("🔄 Getting Batch Cancel Order...")
        print(f"   Trading pair: {symbol}")
        print(f"   Order ID List: {order_ids}")
        print(f"   Order quantity: {len(order_ids)}")
        print()
        
        # Display order details to cancel
        for i, order in enumerate(orders_to_cancel, 1):
            print(f"   Order {i}:")
            print(f"     Order ID: {order.order_id}")
            print(f"     Client Order ID: {order.client_order_id}")
            print(f"     Trading pair: {order.symbol}")
            print(f"     Side: {order.side}")
            print(f"     Type: {order.type}")
            print(f"     Price: {order.price}")
            print(f"     Quantity: {order.orig_qty}")
            print()
        
        print("⚠️  Note: This is a real trading operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Call Spot Batch Cancel order API
        response = client.batch_cancel_spot_orders(order_ids)
        
        print("✅ Batch Cancel order Request Success!")
        print()
        
        # Display Batch Cancel order Result
        print("📋 Batch Cancel order Result:")
        if hasattr(response, 'code'):
            print(f"   📊 Response Code: {response.code}")
        if hasattr(response, 'message'):
            print(f"   💬 Response Message: {response.message}")
        if hasattr(response, 'timestamp'):
            print(f"   🕐 Time Timestamp: {response.timestamp}")
        
        if hasattr(response, 'result'):
            if response.result and len(response.result) > 0:
                print(f"   📊 Cancel order Result Details (Total {len(response.result)} items Order):")
                success_count = 0
                failed_count = 0
                
                for i, result in enumerate(response.result):
                    status = "Success" if result.code == 200 else "Failed"
                    if result.code == 200:
                        success_count += 1
                    else:
                        failed_count += 1
                    print(f"     - Order {result.orderId}: {status} (Code: {result.code})")
                    # Common error code explanation
                    if result.code == -2013:
                        print("       ℹ️  Error: Order does not exist")
                    elif result.code == -2011:
                        print("       ℹ️  Error: Cancel order rejected")
                    elif result.code == -1142:
                        print("       ℹ️  Error: Order already canceled")
            else:
                print("   ✅ All Order Cancel Success (result For Empty Array Represents All Success)")
        
        # Check overall response status
        if hasattr(response, 'code') and response.code == 200:
            print("\n   ✅ Batch Cancel order Operation Complete")
        else:
            print("\n   ⚠️  Batch cancel order operation may not be completely successful")
        
        return response
        
    except Exception as e:
        print(f"❌ Batch Cancel Order Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK Batch Cancel Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real trading operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: DELETE /api/v1/spot/cancelOrderByIds")
    print("   - Auth: Requires signature (TRADE)")
    print("   - Function: Batch Cancel Specified Order")
    print("   - Parameters: orderIds")
    print()
    print("💡 Batch Cancel order Description:")
    print("   - First Query Current Open Orders List")
    print("   - Select Before 5 items Open Orders Perform Batch Cancel order")
    print("   - Use actually existing order IDs")
    print("   - Return Each items Order of Cancel order Result")
    print("   - Partial Success Partial Failed Is normal")
    print()
    print("📈 Response Result Description:")
    print("   - code: 200 Represents Request Success")
    print("   - result: Empty Array Represents All Cancel order Success")
    print("   - result: Contains Result Represents Partial Or All Failed")
    print("   - Each items Result Contains orderId And code")
    print()
    print("⚠️  Important reminder:")
    print("   - This Operation Irreversible")
    print("   - Will Cancel Current Open Orders List In of Before 5 items Order")
    print("   - Based on actual open orders to perform operation, ensure orders exist")
    print()
    
    batch_cancel_orders()
