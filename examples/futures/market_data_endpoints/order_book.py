"""
TooBit Futures API SDK - Get Depth Information
Get Order Book Depth Information
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_order_book():
    """Get Order Book Depth Information"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        limit = 10
        print(f"Request Parameters: symbol={symbol}, limit={limit}")
        
        response = client.get_order_book(symbol, limit)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_order_book()
