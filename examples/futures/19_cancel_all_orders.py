"""
TooBit Futures API SDK - Cancel All Order Example (19)
Cancel All Order (Requires API key and signature)
API: DELETE /api/v1/futures/order
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import CancelAllOrdersResponse

def cancel_all_orders():
    """Cancel All Order"""
    print("=== TooBit Futures API Cancel All Order ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        symbol = "BTC-SWAP-USDT"  # Trading pair
        print("🔄 Getting Cancel All Order...")
        print(f"   Trading pair: {symbol}")
        print()
        print("⚠️  Note: This is a real trading operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        response = client.cancel_all_orders(symbol)
        print("✅ Cancel All Order Success!")
        print()
        
        # Display Cancel Result
        print("📋 Cancel Result:")
        if hasattr(response, 'code'):
            print(f"   📊 Response Code: {response.code}")
        if hasattr(response, 'message'):
            print(f"   💬 Response Message: {response.message}")
        if hasattr(response, 'timestamp'):
            print(f"   🕐 Time Timestamp: {response.timestamp}")
        
        # Check if successful
        if hasattr(response, 'code') and response.code == 200:
            print("   ✅ Cancel Operation Success Complete")
        else:
            print("   ⚠️  Cancel operation may not be completely successful")
        print("\n🎉 Cancel All Order Complete!")
        return response
    except Exception as e:
        print(f"❌ Cancel All Order Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit Futures API SDK Cancel All Order Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real trading operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: DELETE /api/v1/futures/order")
    print("   - Auth: Requires signature (TRADE)")
    print("   - Function: Cancel Specified Trading Pair of All Order")
    print("   - Parameters: symbol")
    print()
    print("⚠️  Important reminder:")
    print("   - This Operation Irreversible")
    print("   - Will Cancel All Not Execution of Order")
    print("   - Please ensure this is the operation you want")
    cancel_all_orders()
