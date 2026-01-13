"""
TooBit API Spot Query Sub Account
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_spot_sub_accounts():
    """Query Spot Sub Account"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("Request Parameters: None")
        
        response = client.get_spot_sub_accounts()
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_spot_sub_accounts()
