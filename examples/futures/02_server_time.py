"""
TooBit Futures API SDK - Get Server Time API Example
Get Server Time (No need API Key)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_server_time():
    """Get Server Time"""
    print("=== TooBit Futures API Get Server Time ===\n")
    
    try:
        # Create Configuration (No need API Key)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # Create Client
        client = TooBitClient(config)
        
        print("🔄 Getting Server Time...")
        
        # Get Server Time
        response = client.get_server_time()
        
        print("✅ Server Time Get Success!")
        print(f"   Server Time: {response}")
        
        print("\n🎉 Server Time Get Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Get Server Time Failed: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit Futures API SDK Get Server Time Example ===\n")
    print("💡 This example does not need API key, can run directly")
    
    # Run Example
    get_server_time()
