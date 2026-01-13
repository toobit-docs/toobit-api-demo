"""
TooBit API SDK - View Current Open Orders
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_open_orders():
    """View Current Open Orders"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        print(f"Request Parameters: symbol={symbol}")
        
        response = client.get_open_orders(symbol)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_open_orders()
