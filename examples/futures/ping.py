"""
TooBit Futures API SDK - PING Test API
Test Server Connectivity
"""

from open_api_sdk import TooBitClient, TooBitConfig

def ping_test():
    """Test Server Connectivity"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("Request Parameters: {}")
        
        response = client.ping()
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        client.close()

if __name__ == "__main__":
    ping_test()
