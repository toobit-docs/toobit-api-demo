"""
TooBit Futures API SDK - Get 24 Hour Price Change
Get Futures 24 Hour Price Change statistics
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_24hr_ticker():
    """Get 24 Hour Price Change statistics"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        print(f"Request Parameters: symbol={symbol}")
        
        response = client.get_24hr_ticker(symbol)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_24hr_ticker()
