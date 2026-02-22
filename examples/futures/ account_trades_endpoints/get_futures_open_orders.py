"""
TooBit Futures API SDK - View all open orders
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_open_orders():
    """View all open orders"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "DOGE-SWAP-USDT"
        order_id = None      # Optional: Order ID
        order_type = "LIMIT" # Optional: Order type (LIMIT, STOP, STOP_PROFIT_LOSS)
        limit = 20           # Optional: Number of records (default 20, max 1000)
        category = "USDT"    # Optional: Category (USDC, USDT)
        
        print(f"Request Parameters: symbol={symbol}, order_id={order_id}, order_type={order_type}, limit={limit}, category={category}")
        
        response = client.get_futures_open_orders(
            symbol=symbol,
            order_id=order_id,
            order_type=order_type,
            limit=limit,
            category=category
        )
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_open_orders()
