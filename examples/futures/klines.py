"""
TooBit Futures API SDK - Get KLine Data
Get Futures KLine Data
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_klines():
    """Get KLine Data"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        interval = "1h"
        limit = 10
        print(f"Request Parameters: symbol={symbol}, interval={interval}, limit={limit}")
        
        response = client.get_klines(symbol, interval, limit)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_klines()
