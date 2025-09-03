"""
TooBit Futures API SDK - Get Recent Trades Record Example
Get Futures Recent Trades Record (No need API Key)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_recent_trades():
    """Get Recent Trades Record"""
    print("=== TooBit Futures API Get Recent Trades Record ===\n")
    
    try:
        # Create Configuration (No need API Key)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # Create Client
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        limit = 10  # Get Quantity
        
        print(f"🔄 Getting {symbol} Recent Trades Record...")
        
        # Get Recent Trades Record
        response = client.get_recent_trades(symbol, limit)
        
        print("✅ Recent Trades Record Get Success!")
        print(f"   Retrieved {len(response)} Execution Records")
        print()
        
        # Display Execution Record
        print("📊 Recent Trades Record:")
        for i, trade in enumerate(response):
            if hasattr(trade, 'price') and hasattr(trade, 'qty'):
                price = float(trade.price)
                qty = float(trade.qty)
                print(f"   {i+1:2d}. Price: {price:>8.2f} | Quantity: {qty:>8.4f}")
        
        print("\n🎉 Recent Trades Record Get Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Get Recent Trades Record Failed: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit Futures API SDK Get Recent Trades Record Example ===\n")
    print("💡 This example does not need API key, can run directly")
    
    # Run Example
    get_recent_trades()
