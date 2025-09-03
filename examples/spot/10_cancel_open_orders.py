#!/usr/bin/env python3
"""
TooBit API Spot Cancel Open Orders Example
Cancel Specified Trading Pair And Side of All Open Orders
"""

from open_api_sdk import TooBitClient, TooBitConfig, OrderSide

def cancel_open_orders():
    """Cancel Open OrdersExample"""
    print("=== TooBit API Spot Cancel Open Orders Example ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Cancel Open OrdersTest:")
        print()
        
        # Example1: Cancel All Open Orders
        print("📊 Example1: Cancel All Open Orders")
        print("   Parameters: None")
        print("   API: DELETE /api/v1/spot/openOrders")
        print("   Description: Cancel all spot open orders under account")
        print()
        
        response1 = client.cancel_open_orders()
        print(f"   Response: {response1.model_dump()}")
        print(f"   Success: {response1.success}")
        print()
        
        # Example2: Cancel Specified Trading pair of All Open Orders
        print("📊 Example2: Cancel Specified Trading pair of All Open Orders")
        print("   Parameters: symbol='BTCUSDT'")
        print("   API: DELETE /api/v1/spot/openOrders?symbol=BTCUSDT")
        print("   Description: Cancel BTCUSDT Trading pair of All Open Orders")
        print()
        
        response2 = client.cancel_open_orders(symbol='BTCUSDT')
        print(f"   Response: {response2.model_dump()}")
        print(f"   Success: {response2.success}")
        print()
        
        # Example3: Cancel Specified Trading pair And Side of Open Orders
        print("📊 Example3: Cancel Specified Trading pair And Side of Open Orders")
        print("   Parameters: symbol='BTCUSDT', side='BUY'")
        print("   API: DELETE /api/v1/spot/openOrders?symbol=BTCUSDT&side=BUY")
        print("   Description: Cancel BTCUSDT Trading pair of All Buy order")
        print()
        
        response3 = client.cancel_open_orders(symbol='BTCUSDT', side=OrderSide.BUY)
        print(f"   Response: {response3.model_dump()}")
        print(f"   Success: {response3.success}")
        print()
        
        # Example4: Cancel Specified Side of All Open Orders
        print("📊 Example4: Cancel Specified Side of All Open Orders")
        print("   Parameters: side='SELL'")
        print("   API: DELETE /api/v1/spot/openOrders?side=SELL")
        print("   Description: Cancel All Sell order")
        print()
        
        response4 = client.cancel_open_orders(side=OrderSide.SELL)
        print(f"   Response: {response4.model_dump()}")
        print(f"   Success: {response4.success}")
        print()
        
        print("🎉 Cancel Open Orders Test Complete!")
        
    except Exception as e:
        print(f"❌ Cancel Open Orders Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    cancel_open_orders()
