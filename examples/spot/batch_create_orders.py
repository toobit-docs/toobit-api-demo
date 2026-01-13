"""
TooBit API SDK - Batch Create Order API
Batch Create Multiple Items Order (Requires API key)
"""
import uuid
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import OrderRequest, OrderSide, OrderType, TimeInForce

def batch_create_orders():
    """Batch Create Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Create multiple items order request
        orders = []
        
        # Order1: Limit priceBuy
        order1 = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            quantity=0.01,
            price=45000.0,
            time_in_force=TimeInForce.GTC,
            new_client_order_id=f"batch_buy_{uuid.uuid4().hex[:8]}"
        )
        orders.append(order1)
        
        # Order2: Limit priceSell
        order2 = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.SELL,
            type=OrderType.LIMIT,
            quantity=1,
            price=10000.0,
            time_in_force=TimeInForce.GTC,
            new_client_order_id=f"batch_sell_{uuid.uuid4().hex[:8]}"
        )
        orders.append(order2)
        
        print(f"Request Parameters: orders={orders}")
        
        # Call Batch Create Order API
        response = client.batch_create_orders(orders)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    batch_create_orders()
