"""
TooBit Futures API SDK - Master Sub Account Universal Transfer Example
Master Sub Account Universal Transfer (Requires API key and signature)
API: POST /api/v1/futures/transfer
"""
from open_api_sdk import TooBitClient, TooBitConfig

def transfer_between_accounts():
    """Master Sub Account Universal Transfer"""
    print("=== TooBit Futures API Master Sub Account Universal Transfer ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Transfer Parameters
        from_account_type = "MAIN"  # Source account type: MAIN, FUTURES
        to_account_type = "FUTURES"  # Target account type: MAIN, FUTURES
        asset = "USDT"  # Transfer Asset
        quantity = "100"  # Transfer Quantity
        
        print("🔄 Executing Master Sub Account Transfer...")
        print(f"   Source account type: {from_account_type}")
        print(f"   Target account type: {to_account_type}")
        print(f"   Transfer Asset: {asset}")
        print(f"   Transfer Quantity: {quantity}")
        print()
        print("⚠️  Note: This is a real funds transfer operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        response = client.transfer_between_accounts(
            from_account_type=from_account_type,
            to_account_type=to_account_type,
            asset=asset,
            quantity=quantity
        )
        
        print("✅ Account Transfer Success!")
        print()
        
        # Process response based on actual API return structure
        if response and 'code' in response:
            if response['code'] == 200:
                print("🎉 Transfer Operation Success!")
                if 'msg' in response:
                    print(f"📝 Response Message: {response['msg']}")
            else:
                print(f"⚠️  Transfer operation returned non-success status code: {response['code']}")
                if 'msg' in response:
                    print(f"📝 Response Message: {response['msg']}")
        else:
            print("   ℹ️  No valid transfer response data retrieved")
        
        print("\n🎉 Account Transfer Complete!")
        return response
        
    except Exception as e:
        print(f"❌ Account Transfer Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit Futures API SDK Master Sub Account Universal Transfer Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real funds transfer operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: POST /api/v1/futures/transfer")
    print("   - Auth: Requires signature (TRADE)")
    print("   - Function: Funds transfer between Master Sub Account")
    print("   - Support: MainAccount↔Futures, MainAccount↔MainAccount, Futures↔Futures")
    print()
    print("⚠️  Important reminder:")
    print("   - Please ensure sufficient account balance")
    print("   - Please carefully verify transfer parameters")
    print("   - Transfer operation is irreversible")
    transfer_between_accounts()
