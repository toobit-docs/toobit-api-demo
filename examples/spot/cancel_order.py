"""
TooBit API SDK - Cancel Order API
Cancel Order (Requires API key)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def cancel_order():
    """Cancel Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First query open orders list
        open_orders = client.get_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("No open orders found to cancel.")
            return None
        
        # Select first items open orders for cancellation
        first_order = open_orders[0]
        symbol = first_order.symbol
        order_id = first_order.order_id
        
        print(f"Request Parameters: symbol={symbol}, order_id={order_id}")
        
        # Call cancel order API
        cancel_response = client.cancel_order(symbol, order_id)
        
        print(f"Response: {cancel_response}")
        return cancel_response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    cancel_order()