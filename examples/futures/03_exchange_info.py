"""
TooBit Futures API SDK - Get Trade Rules and Trading Pair Information Example
Get Futures Trade Rules, Trading Pair List etc (No API key needed)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_exchange_info():
    """Get Trade All Information"""
    print("=== TooBit Futures API Get Trade All Information ===\n")
    
    try:
        # Create Configuration (No need API Key)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # Create Client
        client = TooBitClient(config)
        
        print("🔄 Getting Trade All Information...")
        
        # Get Trade All Information
        response = client.get_exchange_info()
        
        print("✅ Trade All Information Get Success!")
        
        # Display basic information
        if hasattr(response, 'timezone'):
            print(f"   Timezone: {response.timezone}")
        
        if hasattr(response, 'serverTime'):
            print(f"   Server Time: {response.serverTime}")
        
        if hasattr(response, 'rateLimits'):
            print(f"   Rate Limit Quantity: {len(response.rateLimits) if response.rateLimits else 0}")
        
        if hasattr(response, 'symbols'):
            print(f"   Trading Pair Quantity: {len(response.symbols) if response.symbols else 0}")
        
        print("\n🎉 Trade All Information Get Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Get Trade All Information Failed: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit Futures API SDK Get Trade All Information Example ===\n")
    print("💡 This example does not need API key, can run directly")
    
    # Run Example
    get_exchange_info()
