"""
TooBit API Futures Query Historical orders
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesHistoryOrdersRequest

def get_futures_history_orders():
    """Query Historical orders"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        request = QueryFuturesHistoryOrdersRequest(
            symbol="BTC-SWAP-USDT",
            limit=10
        )
        
        print(f"Request Parameters: {request}")
        
        response = client.get_futures_history_orders(request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_history_orders()
