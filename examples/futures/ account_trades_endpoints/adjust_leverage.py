"""
TooBit API Futures Adjust Open Leverage
"""

from open_api_sdk import TooBitClient, TooBitConfig, AdjustLeverageRequest

def adjust_leverage():
    """Adjust Open Leverage"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        request = AdjustLeverageRequest(
            symbol="DOGE-SWAP-USDT",
            leverage=10
        )
        
        print(f"Request Parameters: {request}")
        
        response = client.adjust_leverage(request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    adjust_leverage()
