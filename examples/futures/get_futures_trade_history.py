"""
TooBit API Futures Query Account Trade history
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesTradeHistoryRequest

def get_futures_trade_history():
    """Query Futures Account Trade history"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        request = QueryFuturesTradeHistoryRequest(
            symbol="BTC-SWAP-USDT",
            limit=10
        )
        
        print(f"Request Parameters: {request}")
        
        response = client.get_futures_trade_history(request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_trade_history()
