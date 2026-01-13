"""
TooBit API SDK - Create Order API
Create various types of orders (Requires API key)
"""
import uuid
from open_api_sdk import (
    TooBitClient, TooBitConfig, OrderRequest, 
    OrderSide, OrderType, TimeInForce
)

def create_limit_order():
    """Create Limit Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Create limit price buy order
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            quantity=0.001,  # Buy 0.001 BTC
            price=50000.0,   # Limit price 50000 USDT
            time_in_force=TimeInForce.GTC,  # Valid until canceled
            client_order_id=f"order_{uuid.uuid4().hex[:8]}"  # Client Order ID
        )
        
        print(f"Request Parameters: {order_request}")
        
        # Call create order API
        order_response = client.create_order(order_request)
        
        print(f"Response: {order_response}")
        return order_response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    create_limit_order()