"""
TooBit Futures API SDK - Get Latest Price Example
Get Futures Latest Price (No need API Key)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_latest_price():
    """Get Latest Price"""
    print("=== TooBit Futures API Get Latest Price ===\n")
    
    try:
        # Create Configuration (No need API Key)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # Create Client
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        print(f"🔄 Getting {symbol} Latest Price...")
        
        # Get Latest Price
        response = client.get_latest_price(symbol)
        
        print("✅ Latest Price Get Success!")
        print()
        
        # Display Price Information
        if response and len(response) > 0:
            ticker = response[0]  # Get First Item Element

            if 's' in ticker:
                print(f"📋 Trading pair: {ticker['s']}")
            
            if 'p' in ticker:
                print(f"💰 Latest price: {ticker['p']}")
        else:
            print("   ℹ️  No Retrieved Data")
        
        print("\n🎉 Latest Price Get Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Get Latest Price Failed: {e}")
        return None
    
    finally:
        client.close()


def get_all_prices():
    """Get All Trading Pair of Latest Price"""
    print("\n=== Get All Trading Pair of Latest Price ===\n")
    
    try:
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        client = TooBitClient(config)
        
        print("🔄 Getting All Trading Pair of Latest Price...")
        
        # Get All Trading Pair of Latest Price
        response = client.get_all_prices()
        
        if response:
            print(f"✅ Retrieved {len(response)} Items Trading Pair of Latest Price")
            print()
            
            # Display Before 10 Items Trading Pair
            print("📊 Before 10 Items Trading Pair Price:")
            for i, price_info in enumerate(response[:10]):
                if 's' in price_info and  'p' in price_info:
                    symbol = price_info['s']
                    price = price_info['p']
                    print(f"   {i+1:2d}. {symbol}: {price}")
        
        return response
        
    except Exception as e:
        print(f"❌ Get All Price Failed: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit Futures API SDK Get Latest Price Example ===\n")
    print("💡 This example does not need API key, can run directly")
    
    # Run Example
    get_latest_price()
    get_all_prices()

