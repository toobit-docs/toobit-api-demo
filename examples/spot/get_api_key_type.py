#!/usr/bin/env python3
"""
TooBit API Get API Key Type Example (13 Number)
Get API Key Type
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_api_key_type():
    """Get API KEY Type Example"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("Request Parameters: None")
        
        api_key_type = client.get_api_key_type()
        
        print(f"Response: {api_key_type}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_api_key_type()
