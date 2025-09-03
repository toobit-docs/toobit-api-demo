"""
TooBit Futures API SDK - Get KLine Data Example
Get Futures KLine Data (No need API Key)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_klines():
    """Get KLine Data"""
    print("=== TooBit Futures API Get KLine Data ===\n")
    
    try:
        # Create Configuration (No need API Key)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # Create Client
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        interval = "1h"  # Time interval
        limit = 10  # Get Quantity
        
        print(f"🔄 Getting {symbol} KLine Data...")
        print(f"   Time interval: {interval}")
        print(f"   Quantity: {limit}")
        print()
        
        # Get KLine Data
        response = client.get_klines(symbol, interval, limit)
        
        print("✅ KLine Data Get Success!")
        print(f"   Retrieved {len(response)} KLine records")
        print()
        
        # Display KLine Data
        print("📊 KLine Data Details:")
        for i, kline in enumerate(response[-5:]):  # Display Most Recent 5 KLine records
            if hasattr(kline, 'open') and hasattr(kline, 'high') and hasattr(kline, 'low') and hasattr(kline, 'close'):
                open_price = float(kline.open)
                high_price = float(kline.high)
                low_price = float(kline.low)
                close_price = float(kline.close)
                print(f"   {i+1:2d}. Open: {open_price:>8.2f} | High: {high_price:>8.2f} | Low: {low_price:>8.2f} | Close: {close_price:>8.2f}")
        
        print("\n🎉 KLine Data Get Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Get KLine Data Failed: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit Futures API SDK Get KLine Data Example ===\n")
    print("💡 This example does not need API key, can run directly")
    
    # Run Example
    get_klines()
