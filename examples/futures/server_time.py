"""
TooBit Futures API SDK - Get Server Time API
Get Server Time
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_server_time():
    """Get Server Time"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("Request Parameters: {}")
        
        response = client.get_server_time()
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_server_time()
