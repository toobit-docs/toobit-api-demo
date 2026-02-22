"""
TooBit Futures API SDK - Get Trade Rules and Trading Pair Information
Get Futures Trade Rules, Trading Pair List etc
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_exchange_info():
    """Get Trade All Information"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("Request Parameters: {}")
        
        response = client.get_exchange_info()
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_exchange_info()
