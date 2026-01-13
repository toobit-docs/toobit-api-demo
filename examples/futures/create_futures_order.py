"""
TooBit Futures API SDK - Futures Create Order
"""

import uuid
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import OrderRequest, OrderSide, OrderType, TimeInForce

def create_futures_order():
    """Futures Create Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTC-SWAP-USDT"
        side = OrderSide.BUY_OPEN
        order_type = OrderType.LIMIT
        quantity = "10"
        price = "50000"
        time_in_force = TimeInForce.GTC
        client_order_id = f"order_{uuid.uuid4().hex[:8]}"
        
        order_request = OrderRequest(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price,
            timeInForce=time_in_force,
            newClientOrderId=client_order_id
        )
        
        print(f"Request Parameters: {order_request}")
        
        response = client.create_futures_order(order_request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    create_futures_order()
