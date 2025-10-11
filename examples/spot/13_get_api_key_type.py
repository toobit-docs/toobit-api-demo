#!/usr/bin/env python3
"""
TooBit API Get API Key Type Example (13 Number)
Get API Key Type
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_api_key_type():
    """Get API KEYTypeExample"""
    print("=== TooBit API Get API KEY Type Example ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Get API KEY Type Test:")
        print()
        print("   API: GET /api/v1/account/apiKeyType")
        print("   Description: Get API KEY Type")
        print()
        
        api_key_type = client.get_api_key_type()
        print(f"   API Key Type: {api_key_type.accountType}")
        print()

        print("🎉 Get API KEY Type Test Complete!")
        
    except Exception as e:
        print(f"❌ Get API KEY Type Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_api_key_type()
