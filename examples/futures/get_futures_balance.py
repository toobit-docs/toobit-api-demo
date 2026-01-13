"""
TooBit API Futures Query Account Balance
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_balance():
    """Query Futures Account Balance"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("Request Parameters: {}")
        
        response = client.get_futures_balance()
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_balance()
