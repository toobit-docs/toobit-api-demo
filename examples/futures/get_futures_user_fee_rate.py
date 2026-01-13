"""
TooBit API Futures Query User Fee Rate
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesUserFeeRateRequest

def get_futures_user_fee_rate():
    """Query Futures User Fee Rate"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        request = QueryFuturesUserFeeRateRequest(symbol="BTC-SWAP-USDT")
        
        print(f"Request Parameters: {request}")
        
        response = client.get_futures_user_fee_rate(request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_user_fee_rate()
