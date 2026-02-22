"""
TooBit Futures API SDK - Get Best Open Orders
Get Futures Best Open Orders Information
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_best_order_book():
    """Get Best Open Orders Information"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        print(f"Request Parameters: symbol={symbol}")
        
        response = client.get_best_order_book(symbol)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_best_order_book()
