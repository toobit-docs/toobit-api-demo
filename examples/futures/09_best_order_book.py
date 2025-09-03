"""
TooBit Futures API SDK - Get Best Open Orders Example
Get Futures Best Open Orders Information (No need API Key)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_best_order_book():
    """Get Best Open Orders Information"""
    print("=== TooBit Futures API Get Best Open Orders Information ===\n")
    
    try:
        # Create Configuration (No need API Key)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # Create Client
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        print(f"🔄 Getting {symbol} Best Open Orders Information...")
        
        # Get Best Open Orders Information
        response = client.get_best_order_book(symbol)
        
        print("✅ Best Open Orders Information Get Success!")
        print()
        
        # Display basic information
        if response and len(response) > 0:
            ticker = response[0]  # Get First Item Element
            
            if 's' in ticker:
                print(f"📋 Trading pair: {ticker['s']}")
            
            if 't' in ticker:
                print(f"⏰ Time: {ticker['t']}")
            
            # Display Buy Order Information
            if 'b' in ticker and 'bq' in ticker:
                print(f"\n📈 Buy Order Information:")
                print(f"   Price: {ticker['b']} | Quantity: {ticker['bq']}")
            
            # Display Sell Order Information
            if 'a' in ticker and 'aq' in ticker:
                print(f"\n📉 Sell Order Information:")
                print(f"   Price: {ticker['a']} | Quantity: {ticker['aq']}")
        else:
            print("   ℹ️  No Retrieved Data")
        
        print("\n🎉 Best Open Orders Information Get Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Get Best Open Orders Information Failed: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit Futures API SDK Get Best Open Orders Example ===\n")
    print("💡 This example does not need API key, can run directly")
    
    # Run Example
    get_best_order_book()
