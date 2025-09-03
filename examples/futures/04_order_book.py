"""
TooBit Futures API SDK - Get Depth Information Example
Get Order Book Depth Information (No need API Key)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_order_book():
    """Get Order Book Depth Information"""
    print("=== TooBit Futures API Get Depth Information ===\n")
    
    try:
        # Create Configuration (No need API Key)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # Create Client
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        limit = 10  # Depth levels
        
        print(f"🔄 Getting {symbol} Depth Information (Depth: {limit})...")
        
        # Get Order Book Depth
        response = client.get_order_book(symbol, limit)
        
        print("✅ Depth Information Get Success!")
        
        # Display basic information
        if hasattr(response, 'symbol'):
            print(f"   Trading Pair: {response.symbol}")
        
        # Display Buy Order Depth
        if hasattr(response, 'b') and response.b:
            print(f"\n📈 Buy Order Depth (Top {min(limit, len(response.b))} levels):")
            for i, bid in enumerate(response.b[:limit]):
                price = float(bid[0])
                quantity = float(bid[1])
                print(f"   {i+1:2d}. Price: {price:>10.2f} | Quantity: {quantity:>10.4f}")
        
        # Display Sell Order Depth
        if hasattr(response, 'a') and response.a:
            print(f"\n📉 Sell Order Depth (Top {min(limit, len(response.a))} levels):")
            for i, ask in enumerate(response.a[:limit]):
                price = float(ask[0])
                quantity = float(ask[1])
                print(f"   {i+1:2d}. Price: {price:>10.2f} | Quantity: {quantity:>10.4f}")
        
        print("\n🎉 Depth Information Get Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Get Depth Information Failed: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit Futures API SDK Get Depth Information Example ===\n")
    print("💡 This example does not need API key, can run directly")
    
    # Run Example
    get_order_book()
