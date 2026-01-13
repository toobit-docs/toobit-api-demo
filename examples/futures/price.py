"""
TooBit Futures API SDK - Get Latest Price
Get Futures Latest Price
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_latest_price():
    """Get Latest Price"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        print(f"Request Parameters: symbol={symbol}")
        
        response = client.get_latest_price(symbol)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

def get_all_prices():
    """Get All Trading Pair of Latest Price"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("Request Parameters: {}")
        
        response = client.get_all_prices()
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_latest_price()
    get_all_prices()
