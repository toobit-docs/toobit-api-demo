"""
TooBit API SDK - Batch Cancel Order API
Batch Cancel Multiple Items Order (Requires API key)
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import BatchCancelOrdersResponse, BatchCancelOrderResult

def batch_cancel_orders():
    """Batch Cancel Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # First Query Open Orders List
        open_orders = client.get_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("No open orders found to cancel.")
            return None
        
        # Select first few open orders to perform batch cancel (maximum 5 orders)
        max_orders = min(5, len(open_orders))
        orders_to_cancel = open_orders[:max_orders]
        order_ids = [order.order_id for order in orders_to_cancel]
        
        print(f"Request Parameters: order_ids={order_ids}")
        
        # Call Spot Batch Cancel order API
        response = client.batch_cancel_spot_orders(order_ids)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    batch_cancel_orders()
