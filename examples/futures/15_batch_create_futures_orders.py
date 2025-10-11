#!/usr/bin/env python3
"""
TooBit API Futures Batch Create Order Example (15 Number)
Batch Create Multiple Items Futures Order
"""

import uuid
from open_api_sdk import TooBitClient, TooBitConfig, FuturesOrderRequest, OrderSide, OrderType

def batch_create_futures_orders():
    """Futures Batch Create Order Example"""
    print("=== TooBit API Futures Batch Create Order Example ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Futures Batch Create Order Test:")
        print()
        
        # Create Multiple Items Futures Order Request
        orders = [
            FuturesOrderRequest(
                newClientOrderId=f"pl2023010712345678900_{uuid.uuid4().hex[:8]}",
                symbol="BTC-SWAP-USDT",
                side=OrderSide.BUY_OPEN,
                type=OrderType.LIMIT,
                price=16500,
                quantity=10,
                priceType="INPUT"
            ),
            FuturesOrderRequest(
                newClientOrderId=f"pl2023010712345678901_{uuid.uuid4().hex[:8]}",
                symbol="BTC-SWAP-USDT",
                side=OrderSide.BUY_OPEN,
                type=OrderType.LIMIT,
                price=16000,
                quantity=10,
                priceType="INPUT"
            ),
            FuturesOrderRequest(
                newClientOrderId=f"pl2023010712345678902_{uuid.uuid4().hex[:8]}",
                symbol="BTC-SWAP-USDT",
                side=OrderSide.SELL_OPEN,
                type=OrderType.LIMIT,
                price=17000,
                quantity=5,
                priceType="INPUT"
            )
        ]
        
        print("📊 Batch Create Order Parameters:")
        for i, order in enumerate(orders, 1):
            print(f"   Order{i}:")
            print(f"     Client Order ID: {order.newClientOrderId}")
            print(f"     Trading pair: {order.symbol}")
            print(f"     Side: {order.side}")
            print(f"     Type: {order.type}")
            print(f"     Price: {order.price}")
            print(f"     Quantity: {order.quantity}")
            print(f"     Price type: {order.priceType}")
            print()
        
        # Call Futures Batch Create Order API
        response = client.batch_create_futures_orders(orders)
        
        print("📊 Batch Create Order Response:")
        print(f"   Response Code: {response.code}")
        print(f"   Result Quantity: {len(response.result)}")
        print()
        
        # Display Each Items Order of Result
        for i, result in enumerate(response.result, 1):
            print(f"   Order{i}Result:")
            print(f"     Code: {result.code}")
            
            if result.code == 200:
                print("     ✅ Create Order Success")
                if result.order:
                    order = result.order
                    print(f"     Order ID: {order.orderId}")
                    print(f"     Client Order ID: {order.clientOrderId}")
                    print(f"     Trading pair: {order.symbol}")
                    print(f"     Price: {order.price}")
                    print(f"     Quantity: {order.origQty}")
                    print(f"     Status: {order.status}")
                    print(f"     Time: {order.time}")
            else:
                print("     ❌ Create Order Failed")
                if result.msg:
                    print(f"     Failed reason: {result.msg}")
            print()
        
        print("🎉 Futures Batch Create Order Test Complete!")
        
    except Exception as e:
        print(f"❌ Futures Batch Create Order Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    batch_create_futures_orders()
