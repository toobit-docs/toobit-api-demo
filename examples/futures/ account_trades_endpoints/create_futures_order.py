"""
TooBit Futures API SDK - Futures Create Order
"""

import uuid
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import OrderRequest, OrderSide, OrderType, TimeInForce

def create_futures_limit_order():
    """Futures Create Limit Order (INPUT Price)"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "DOGE-SWAP-USDT"
        side = OrderSide.BUY_OPEN
        order_type = OrderType.LIMIT
        quantity = 100
        price = 0.1
        time_in_force = TimeInForce.GTC
        client_order_id = f"limit_{uuid.uuid4().hex[:8]}"
        
        # Optional parameters
        price_type = "INPUT" # INPUT: User input price
        take_profit = 0.15
        tp_trigger_by = "CONTRACT_PRICE"
        stop_loss = 0.08
        sl_trigger_by = "CONTRACT_PRICE"
        
        order_request = OrderRequest(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price,
            priceType=price_type,
            timeInForce=time_in_force,
            newClientOrderId=client_order_id,
            takeProfit=take_profit,
            tpTriggerBy=tp_trigger_by,
            stopLoss=stop_loss,
            slTriggerBy=sl_trigger_by
        )
        
        print(f"\n--- Creating Limit Order ---")
        print(f"Request Parameters: {order_request}")
        response = client.create_futures_order(order_request)
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

def create_futures_market_order():
    """
    Futures Create Market Order (MARKET Price)
    According to documentation: For market orders, set type=LIMIT and priceType=MARKET
    """
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "DOGE-SWAP-USDT"
        side = OrderSide.BUY_OPEN
        # For market orders: type=LIMIT, priceType=MARKET
        order_type = OrderType.LIMIT
        price_type = "MARKET"
        quantity = 100
        client_order_id = f"market_{uuid.uuid4().hex[:8]}"
        
        order_request = OrderRequest(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            priceType=price_type,
            newClientOrderId=client_order_id,
            timeInForce=None  # Market orders don't need timeInForce
        )
        
        print(f"\n--- Creating Market Order ---")
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
    # 1. Limit Order Example (INPUT Price)
    create_futures_limit_order()
    
    # 2. Market Order Example (MARKET Price)
    # Note: TooBit futures market order requires setting type=LIMIT and priceType=MARKET
    create_futures_market_order()
