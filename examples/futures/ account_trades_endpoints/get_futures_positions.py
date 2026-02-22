"""
TooBit Futures API SDK - Query Current Position
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_positions():
    """Query Current Position"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "DOGE-SWAP-USDT"
        side = "LONG"      # Optional: Position side (LONG, SHORT)
        category = "USDT"  # Optional: Category (USDC, USDT)
        recv_window = 5000 # Optional: Receive window
        
        print(f"Request Parameters: symbol={symbol}, side={side}, category={category}, recv_window={recv_window}")
        
        response = client.get_futures_positions(
            symbol=symbol,
            side=side,
            category=category,
            recv_window=recv_window
        )
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_positions()
