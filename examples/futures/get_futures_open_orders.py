"""
TooBit Futures API SDK - View all open orders
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_open_orders():
    """View all open orders"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTC-SWAP-USDT"
        print(f"Request Parameters: symbol={symbol}")
        
        response = client.get_futures_open_orders(symbol)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_open_orders()
