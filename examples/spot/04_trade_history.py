"""
TooBit API SDK - Query Trade History API Example (04)
Query Trade History (Requires API key)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_trade_history():
    """Query Trade History"""
    print("=== TooBit API Query Trade History ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"  # Trading pair
        
        print("🔄 Getting query trade history...")
        print(f"   Trading pair: {symbol}")
        print()
        print("⚠️  Note: This is a real account query operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        # Call query trade history API
        trades = client.get_trade_history(symbol)
        
        print("✅ Trade history query success!")
        print()
        
        # Display trade information
        if trades and len(trades) > 0:
            print(f"📊 Trade history information (Total {len(trades)} records):")
            for i, trade in enumerate(trades[:5]):  # Only display before 5 records
                print(f"\n   Trade {i+1}:")
                print(f"     🆔 Trade ID: {trade['id']}")
                print(f"     🆔 Order ID: {trade['orderId']}")
                print(f"     📊 Trading pair: {trade['symbol']}")
                print(f"     💰 Price: {trade['price']}")
                print(f"     📊 Quantity: {trade['qty']}")
                print(f"     🕐 Trade Time: {trade['time']}")
            
            if len(trades) > 5:
                print(f"\n   ... and {len(trades) - 5} more trade records")
        else:
            print("   ℹ️  No trade records found")
        
        print("\n🎉 Query trade history complete!")
        return trades
        
    except Exception as e:
        print(f"❌ Query trade history failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK Query Trade History Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real account query operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: GET /api/v1/spot/myTrades")
    print("   - Auth: Requires signature (USER_DATA)")
    print("   - Function: Query trade history")
    print("   - Parameters: symbol")
    print()
    print("⚠️  Important reminder:")
    print("   - It is recommended to verify in the test environment first")
    print()
    
    get_trade_history()