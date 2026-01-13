"""
TooBit API SDK - Query All Order API
Query All Order (Requires API key)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_all_orders():
    """Query All Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"  # Trading pair
        
        print(f"Request Parameters: symbol={symbol}")
        
        # Call query all order API
        all_orders = client.get_all_orders(symbol)
        
        print(f"Response: {all_orders}")
        return all_orders
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_all_orders()