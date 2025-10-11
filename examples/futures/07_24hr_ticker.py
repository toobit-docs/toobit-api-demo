"""
TooBit Futures API SDK - Get 24 Hour Price Change Example
Get Futures 24 Hour Price Change statistics (No need API Key)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_24hr_ticker():
    """Get 24 Hour Price Change statistics"""
    print("=== TooBit Futures API Get 24 Hour Price Change statistics ===\n")
    
    try:
        # Create Configuration (No need API Key)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # Create Client
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        print(f"🔄 Getting {symbol} 24 Hour Price Change statistics...")
        
        # Get 24 Hour Price Change statistics
        response = client.get_24hr_ticker(symbol)
        
        print("✅ 24 Hour Price Change statistics Get Success!")
        print()
        
        # Display basic information
        print(f"🔍 Debug info: responseType={type(response)}, length={len(response) if response else 0}")
        
        if response and len(response) > 0:
            ticker = response[0]  # Get First item Element
            print(f"🔍 Debug info: tickerType={type(ticker)}, ticker content={ticker}")
            print(f"🔍 Debug info: ticker has s attribute={hasattr(ticker, 's')}")
            
            if hasattr(ticker, 's'):
                print(f"📋 Trading pair: {ticker.s}")

            if hasattr(ticker, 'c'):
                print(f"💰 Latest price: {ticker.c}")

            if hasattr(ticker, 'o'):
                print(f"📈 Open price: {ticker.o}")

            if hasattr(ticker, 'h'):
                print(f"🔺 High price: {ticker.h}")

            if hasattr(ticker, 'l'):
                print(f"🔻 Low price: {ticker.l}")

            if hasattr(ticker, 'v'):
                print(f"📊 Volume: {ticker.v}")

            if hasattr(ticker, 'pcp'):
                print(f"📈 24hr price change: {ticker.pcp}%")
        else:
            print("   ℹ️  No Retrieved Data")
        
        print("\n🎉 24 Hour Price Change statistics Get Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Get 24 Hour Price Change statistics Failed: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit Futures API SDK Get 24 Hour Price Change Example ===\n")
    print("💡 This example does not need API key, can run directly")
    
    # Run Example
    get_24hr_ticker()
