"""
TooBit API Query Sub Accounts Example
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_sub_accounts():
    """Query Sub Account List"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Optional: filter by userId or email
        # params = {"userId": 123456, "email": "test@example.com"}
        params = {}
        
        print(f"Request Parameters: {params}")
        
        response = client.get_sub_accounts(**params)
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    get_sub_accounts()
