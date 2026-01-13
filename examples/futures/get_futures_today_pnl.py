"""
TooBit API Futures Query Today PnL
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_today_pnl():
    """Query Futures Today PnL"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("Request Parameters: {}")
        
        response = client.get_futures_today_pnl()
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_today_pnl()
