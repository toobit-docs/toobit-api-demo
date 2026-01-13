"""
TooBit API Futures Query Leverage Multiple And Position Mode
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryLeverageRequest

def get_account_leverage():
    """Query Leverage Multiple And Position Mode"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        request = QueryLeverageRequest(symbol="BTC-SWAP-USDT")
        
        print(f"Request Parameters: {request}")
        
        response = client.get_account_leverage(request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_account_leverage()
