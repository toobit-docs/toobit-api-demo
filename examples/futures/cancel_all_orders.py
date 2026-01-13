"""
TooBit Futures API SDK - Cancel All Order
"""

from open_api_sdk import TooBitClient, TooBitConfig

def cancel_all_orders():
    """Cancel All Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTC-SWAP-USDT"
        print(f"Request Parameters: symbol={symbol}")
        
        response = client.cancel_all_orders(symbol)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    cancel_all_orders()
