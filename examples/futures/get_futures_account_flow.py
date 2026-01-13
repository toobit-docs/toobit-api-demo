"""
TooBit API Futures Query Account Flow
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesAccountFlowRequest

def get_futures_account_flow():
    """Query Futures Account Flow"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        request = QueryFuturesAccountFlowRequest(
            symbol="BTC-SWAP-USDT",
            limit=10
        )
        
        print(f"Request Parameters: {request}")
        
        response = client.get_futures_account_flow(request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_account_flow()
