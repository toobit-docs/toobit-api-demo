"""
TooBit API Futures Batch Create Order
"""

import uuid
from open_api_sdk import TooBitClient, TooBitConfig, FuturesOrderRequest, OrderSide, OrderType

def batch_create_futures_orders():
    """Futures Batch Create Order"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "DOGE-SWAP-USDT"
        
        order_requests = [
            FuturesOrderRequest(
                symbol=symbol,
                side=OrderSide.BUY_OPEN,
                type=OrderType.LIMIT,
                quantity=100,
                price=0.11,
                priceType="INPUT",
                newClientOrderId=f"order_{uuid.uuid4().hex[:8]}"
            ),
            FuturesOrderRequest(
                symbol=symbol,
                side=OrderSide.BUY_OPEN,
                type=OrderType.LIMIT,
                quantity=200,
                price=0.1,
                priceType="INPUT",
                newClientOrderId=f"order_{uuid.uuid4().hex[:8]}"
            )
        ]
        
        print(f"Request Parameters: orders={order_requests}")
        
        response = client.batch_create_futures_orders(order_requests)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    batch_create_futures_orders()
