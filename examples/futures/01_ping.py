"""
TooBit Futures API SDK - PING Test API Example
Test Server Connectivity (No need API Key)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def ping_test():
    """Test Server Connectivity"""
    print("=== TooBit Futures API PING Test ===\n")
    
    try:
        # Create Configuration (No need API Key)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # Create Client
        client = TooBitClient(config)
        
        print("🔄 Getting Test Server Connectivity...")
        
        # Call PING API
        response = client.ping()
        
        print("✅ Server Connectivity Test Success!")
        print(f"   Response: {response}")
        print("\n🎉 PING Test Complete!")
        
        return True
        
    except Exception as e:
        print(f"❌ Server Connectivity Test Failed: {e}")
        return False
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit Futures API SDK PING Test Example ===\n")
    print("💡 This example does not need API key, can run directly")
    
    # Run Example
    ping_test()
