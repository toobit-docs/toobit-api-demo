"""
TooBit Futures API SDK - Batch Cancel Order
"""

from open_api_sdk import TooBitClient, TooBitConfig

def batch_cancel_orders():
    """Batch Cancel Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTC-SWAP-USDT"
        order_ids = ["12345678", "87654321"]
        print(f"Request Parameters: symbol={symbol}, order_ids={order_ids}")
        
        response = client.batch_cancel_orders(symbol, order_ids)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    batch_cancel_orders()
