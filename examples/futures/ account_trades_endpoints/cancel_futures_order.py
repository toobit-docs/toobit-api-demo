"""
TooBit Futures API SDK - Cancel Order
"""

from open_api_sdk import TooBitClient, TooBitConfig

def cancel_futures_order():
    """Cancel Futures Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "DOGE-SWAP-USDT"
        order_id = "2127756290562218240"
        # client_order_id = "your_client_order_id" # Optional: origClientOrderId
        order_type = "LIMIT"   # Optional: Order type (LIMIT, STOP)
        category = "USDT"      # Optional: Category (USDC, USDT)
        
        print(f"Request Parameters: symbol={symbol}, order_id={order_id}, order_type={order_type}, category={category}")
        
        response = client.cancel_futures_order(
            symbol=symbol,
            order_id=order_id,
            # client_order_id=client_order_id,
            order_type=order_type,
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
    cancel_futures_order()
