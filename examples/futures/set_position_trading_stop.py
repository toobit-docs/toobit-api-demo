"""
TooBit API Futures Set Position Take Profit Stop Loss
"""

from open_api_sdk import TooBitClient, TooBitConfig, SetPositionTradingStopRequest

def set_position_trading_stop():
    """Set Position Take Profit Stop Loss"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        request = SetPositionTradingStopRequest(
            symbol="BTC-SWAP-USDT",
            side="LONG",
            takeProfit="60000",
            stopLoss="40000"
        )
        
        print(f"Request Parameters: {request}")
        
        response = client.set_position_trading_stop(request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    set_position_trading_stop()
