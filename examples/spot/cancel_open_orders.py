#!/usr/bin/env python3
"""
TooBit API Spot Cancel Open Orders Example
Cancel Specified Trading Pair And Side of All Open Orders
"""

from open_api_sdk import TooBitClient, TooBitConfig, OrderSide

def cancel_open_orders():
    """Cancel Open Orders Example"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Example1: Cancel All Open Orders
        print("Request Parameters: None")
        response1 = client.cancel_open_orders()
        print(f"Response: {response1}")
        
        # Example2: Cancel Specified Trading pair of All Open Orders
        symbol = 'BTCUSDT'
        print(f"Request Parameters: symbol={symbol}")
        response2 = client.cancel_open_orders(symbol=symbol)
        print(f"Response: {response2}")
        
        # Example3: Cancel Specified Trading pair And Side of Open Orders
        side = OrderSide.BUY
        print(f"Request Parameters: symbol={symbol}, side={side}")
        response3 = client.cancel_open_orders(symbol=symbol, side=side)
        print(f"Response: {response3}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    cancel_open_orders()
