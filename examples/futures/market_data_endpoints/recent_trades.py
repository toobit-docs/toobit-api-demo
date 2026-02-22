"""
TooBit Futures API SDK - Get Recent Trades Record
Get Futures Recent Trades Record
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_recent_trades():
    """Get Recent Trades Record"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        limit = 10
        print(f"Request Parameters: symbol={symbol}, limit={limit}")
        
        response = client.get_recent_trades(symbol, limit)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_recent_trades()
