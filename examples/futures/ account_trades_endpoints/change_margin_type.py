"""
TooBit API Futures Change Margin Type
"""

from open_api_sdk import TooBitClient, TooBitConfig, ChangeMarginTypeRequest, MarginType

def change_margin_type():
    """Change Margin Type"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        request = ChangeMarginTypeRequest(
            symbol="DOGE-SWAP-USDT",
            marginType=MarginType.CROSS
        )
        
        print(f"Request Parameters: {request}")
        
        response = client.change_margin_type(request)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    change_margin_type()
