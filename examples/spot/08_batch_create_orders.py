"""
TooBit API SDK - Batch Create Order API Example (08)
Batch Create Multiple Items Order (Requires API key)
"""
import uuid
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import OrderRequest, OrderSide, OrderType, TimeInForce

def batch_create_orders():
    """Batch Create Order"""
    print("=== TooBit API Batch Create Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Create multiple items order request
        orders = []
        
        # Order1: Limit priceBuy
        order1 = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            quantity=0.01,
            price=45000.0,
            time_in_force=TimeInForce.GTC,
            new_client_order_id=f"batch_buy_{uuid.uuid4().hex[:8]}"
        )
        orders.append(order1)
        
        # Order2: Limit priceSell
        order2 = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.SELL,
            type=OrderType.LIMIT,
            quantity=1,
            price=10000.0,
            time_in_force=TimeInForce.GTC,
            new_client_order_id=f"batch_sell_{uuid.uuid4().hex[:8]}"
        )
        orders.append(order2)
        
        # # Order3: Market buy
        order3 = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.MARKET,
            quantity=10,
            time_in_force=TimeInForce.IOC,
            new_client_order_id=f"batch_market_{uuid.uuid4().hex[:8]}"
        )
        orders.append(order3)
        
        print("🔄 Getting Batch Create Order...")
        print(f"   Order quantity: {len(orders)}")
        print()
        
        # DisplayOrderDetails
        for i, order in enumerate(orders, 1):
            print(f"   Order {i}:")
            print(f"     Trading pair: {order.symbol}")
            print(f"     Side: {order.side}")
            print(f"     Type: {order.type}")
            print(f"     Quantity: {order.quantity}")
            if order.price:
                print(f"     Price: {order.price}")
            print(f"     Client Order ID: {order.new_client_order_id}")
            print()
        
        print("⚠️  Note: This is a real trading operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Call Batch Create Order API
        response = client.batch_create_orders(orders)
        
        print("✅ Batch Create Order Success!")
        print()
        
        # Display Response Result
        print("📋 Batch Create Order Result:")
        print(f"   📊 Response Code: {response.code}")
        
        if response.result:
            print(f"   📊 Order Create Result (Total {len(response.result)} items Order):")
            for i, order_result in enumerate(response.result, 1):
                print(f"     - Order {i}:")
                print(f"       ResultCode: {order_result.code}")
                
                if order_result.code == 0 and order_result.order:
                    # Success case
                    order = order_result.order
                    print(f"       ✅ Create Success")
                    print(f"       Trading pair: {order.symbol}")
                    print(f"       Order ID: {order.order_id}")
                    print(f"       Client Order ID: {order.client_order_id}")
                    print(f"       Status: {order.status}")
                    print(f"       Price: {order.price}")
                    print(f"       Quantity: {order.orig_qty}")
                    print(f"       Executed quantity: {order.executed_qty}")
                else:
                    # Failed case
                    print(f"       ❌ Create Failed")
                    print(f"       Error Message: {order_result.msg}")
                print()
        
        print("\n🎉 Batch Create Order Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Batch Create Order Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK Batch Create Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real trading operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: POST /api/v1/spot/batchOrders")
    print("   - Auth: Requires signature (TRADE)")
    print("   - Function: Batch Create Multiple items Order")
    print("   - Parameters: Order array directly placed in request body")
    print()
    print("💡 Batch Create Order Description:")
    print("   - Support creating multiple different types of orders simultaneously")
    print("   - Each order has a unique client order ID")
    print("   - Return Each items Order of Create Result")
    print("   - Partial Success Partial Failed Is normal")
    print()
    print("📈 Response Result Description:")
    print("   - code: 200 Represents Request Success")
    print("   - result: Contains Each items Order of Create Result")
    print("   - Each items Result Contains Order ID、Status Etc Information")
    print()
    print("⚠️  Important reminder:")
    print("   - This Operation Irreversible")
    print("   - Will Create 3 items Test Order")
    print("   - Please ensure account has sufficient funds")
    print("   - It is recommended to verify in the test environment first")
    print()
    
    batch_create_orders()
