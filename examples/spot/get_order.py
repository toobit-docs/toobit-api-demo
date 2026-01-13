"""
TooBit API SDK - Query Order
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_order():
    """Query Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First query open orders list to get an order_id
        open_orders = client.get_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("No open orders found to query.")
            return None
        
        first_order = open_orders[0]
        symbol = first_order.symbol
        order_id = first_order.order_id
        
        print(f"Request Parameters: symbol={symbol}, order_id={order_id}")
        
        from open_api_sdk.models import OrderQueryRequest
        query_request = OrderQueryRequest(symbol=symbol, orderId=order_id)
        
        response = client.get_order(query_request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_order()
