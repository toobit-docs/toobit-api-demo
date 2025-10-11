"""
TooBit Futures API SDK - Batch Cancel Order Example (20)
Batch Cancel Order (Requires API key and signature)
API: DELETE /api/v1/futures/batchOrders
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import BatchCancelOrdersResponse

def batch_cancel_orders():
    """Batch Cancel Order"""
    print("=== TooBit Futures API Batch Cancel Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First Query Open Orders List
        print("🔄 Getting Query Open Orders List...")
        open_orders = client.get_futures_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  Currently No Open Orders, No need to cancel")
            return None
        
        print(f"✅ Retrieved {len(open_orders)} Items Open Orders")
        print()
        
        # Select first few open orders to perform batch cancel (maximum 5 orders)
        max_orders = min(5, len(open_orders))
        orders_to_cancel = open_orders[:max_orders]
        order_ids = [order.orderId for order in orders_to_cancel]
        symbol = orders_to_cancel[0].symbol if orders_to_cancel else "BTC-SWAP-USDT"
        
        print("🔄 Getting Batch Cancel Order...")
        print(f"   Trading pair: {symbol}")
        print(f"   Order ID List: {order_ids}")
        print(f"   Order quantity: {len(order_ids)}")
        print()
        print("⚠️  Note: This is a real trading operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        response = client.batch_cancel_orders(symbol, order_ids)
        
        print("✅ Batch Cancel Order Request Success!")
        print()
        
        # Display Batch Cancel Orders Result
        print("📋 Batch Cancel Orders Result:")
        if hasattr(response, 'code'):
            print(f"   📊 Response Code: {response.code}")
        if hasattr(response, 'message'):
            print(f"   💬 Response Message: {response.message}")
        if hasattr(response, 'timestamp'):
            print(f"   🕐 Time Timestamp: {response.timestamp}")
        
        if hasattr(response, 'result'):
            if response.result and len(response.result) > 0:
                print(f"   📊 Cancel Order Result Details (Total {len(response.result)} Items Order):")
                success_count = 0
                failed_count = 0
                
                for i, result in enumerate(response.result):
                    print(f"\n   Order {i+1}:")
                    if hasattr(result, 'orderId'):
                        print(f"     🆔 Order ID: {result.orderId}")
                    if hasattr(result, 'code'):
                        print(f"     📊 Cancel Order Code: {result.code}")
                        
                        # Check cancel order result
                        if result.code == 200:
                            print(f"     ✅ Cancel Order Success")
                            success_count += 1
                        else:
                            print(f"     ❌ Cancel Order Failed")
                            failed_count += 1
                            
                            # Display common error code meaning
                            if result.code == -2013:
                                print(f"     💡 Error Description: Order does not exist")
                            elif result.code == -2011:
                                print(f"     💡 Error Description: Cancel order rejected")
                            elif result.code == -1142:
                                print(f"     💡 Error Description: Order already canceled")
                            else:
                                print(f"     💡 Error Description: Other error (Code: {result.code})")
                
                print(f"\n   📊 Cancel Order Statistics:")
                print(f"     ✅ Success: {success_count} Items")
                print(f"     ❌ Failed: {failed_count} Items")
                print(f"     📊 Total Count: {len(response.result)} Items")
            else:
                print("   ✅ All Order Cancel Success (result For Empty Array Represents All Success)")
        
        # Check overall response status
        if hasattr(response, 'code') and response.code == 200:
            print("\n   ✅ Batch Cancel Orders Operation Complete")
        else:
            print("\n   ⚠️  Batch cancel orders operation may have issues")
        
        print("\n🎉 Batch Cancel Order Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Batch Cancel Order Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit Futures API SDK Batch Cancel Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real trading operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: DELETE /api/v1/futures/batchOrders")
    print("   - Auth: Requires signature (TRADE)")
    print("   - Function: Batch Cancel Specified Order")
    print("   - Parameters: symbol, orderIds")
    print()
    print("💡 Batch Cancel Orders Description:")
    print("   - First Query Current Open Orders List")
    print("   - Select Before 5 Items Open Orders Perform Batch Cancel Orders")
    print("   - Use actually existing order IDs")
    print("   - Return Each Items Order of Cancel Order Result")
    print("   - Partial Success Partial Failed Is normal")
    print()
    print("📈 Response Result Description:")
    print("   - code: 200 Represents Request Success")
    print("   - result: Empty Array Represents All Cancel Order Success")
    print("   - result: Contains Result Represents Partial Or All Failed")
    print("   - Each Items Result Contains orderId And code")
    print()
    print("⚠️  Important reminder:")
    print("   - This Operation Irreversible")
    print("   - Will Cancel Current Open Orders List In of Before 5 Items Order")
    print("   - Based on actual open orders to perform operation, ensure orders exist")
    print()
    
    batch_cancel_orders()
