"""
TooBit Futures API SDK - Get Transfer History
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_transfer_history():
    """Get Transfer History"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        asset = "USDT"
        limit = 10
        flow_type = 51 # Transfer flow type
        print(f"Request Parameters: asset={asset}, limit={limit}, flow_type={flow_type}")
        
        response = client.get_transfer_history(asset=asset, limit=limit, flow_type=flow_type)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_transfer_history()
