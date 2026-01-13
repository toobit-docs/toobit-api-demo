"""
TooBit API Futures Adjust Isolated Margin
"""

from open_api_sdk import TooBitClient, TooBitConfig, AdjustIsolatedMarginRequest

def adjust_isolated_margin():
    """Adjust Isolated Margin"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        request = AdjustIsolatedMarginRequest(
            symbol="BTC-SWAP-USDT",
            side="LONG",
            amount="10"
        )
        
        print(f"Request Parameters: {request}")
        
        response = client.adjust_isolated_margin(request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    adjust_isolated_margin()
