"""
TooBit API SDK - 24hr Ticker Example (01)
Get 24-hour price change statistics
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_24hr_ticker():
    """Get 24-hour price change statistics"""
    print("=== TooBit API 24hr Ticker ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        print("🔄 Getting 24hr ticker data...")
        print(f"   Symbol: {symbol}")
        print()
        print("⚠️  Note: This is a real API call, please ensure correct configuration")
        print()
        
        response = client.get_24hr_ticker(symbol)
        
        print("✅ 24hr ticker data retrieved successfully!")
        print()

        # Display basic information
        print(f"🔍 Debug info: responseType={type(response)}, length={len(response) if response else 0}")

        if response and len(response) > 0:
            ticker = response[0]  # Get FirstitemsElement
            print(f"🔍 Debug info: tickerType={type(ticker)}, tickerContent={ticker}")
            print(f"🔍 Debug info: tickerHasS={hasattr(ticker, 's')}")

            if hasattr(ticker, 's'):
                print(f"📋 Symbol: {ticker.s}")

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
            print("   ℹ️  No data retrieved")

        print("\n🎉 24hr ticker statistics retrieved complete!")
        return response
        
    except Exception as e:
        print(f"❌ Get 24 hour price change failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK Get 24 Hour Price Change Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real API call, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: GET /quote/v1/ticker/24hr")
    print("   - Auth: No signature required")
    print("   - Function: Get 24 hour price change statistics")
    print("   - Parameters: symbol")
    print()
    print("⚠️  Important reminder:")
    print("   - It is recommended to verify in the test environment first")
    print()
    
    get_24hr_ticker() 