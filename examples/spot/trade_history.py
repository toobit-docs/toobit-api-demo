"""
TooBit API SDK - Query Trade History
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_trade_history():
    """Query Trade History"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        print(f"Request Parameters: symbol={symbol}")
        
        response = client.get_trade_history(symbol)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_trade_history()
