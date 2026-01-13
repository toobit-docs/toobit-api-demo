"""
TooBit Futures API SDK - Query Order
"""

from open_api_sdk import TooBitClient, TooBitConfig

def query_futures_order():
    """Query Futures Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTC-SWAP-USDT"
        order_id = "12345678"
        print(f"Request Parameters: symbol={symbol}, order_id={order_id}")
        
        response = client.get_futures_order(symbol, order_id=order_id)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    query_futures_order()
