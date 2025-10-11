"""
TooBit Futures API SDK - Get Transfer History Example (13)
Get Transfer History Record (Requires API key and signature)
API: GET /api/v1/futures/transfer/history
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_transfer_history():
    """Get Transfer History"""
    print("=== TooBit Futures API Get Transfer History ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # Query Parameters
        asset = "USDT"  # Asset type (Optional)
        from_account_type = "MAIN"  # Source account type (Optional)
        to_account_type = "FUTURES"  # Target account type (Optional)
        limit = 10  # Return quantity limit
        
        print("🔄 Getting Transfer History...")
        print(f"   Asset type: {asset}")
        print(f"   Source account type: {from_account_type}")
        print(f"   Target account type: {to_account_type}")
        print(f"   Return quantity: {limit}")
        print()
        print("⚠️  Note: This is a real account query operation, please use with caution!")
        print("⚠️  It is recommended to verify in the test environment first")
        print()
        
        response = client.get_transfer_history(
            asset=asset,
            from_account_type=from_account_type,
            to_account_type=to_account_type,
            limit=limit
        )
        
        print("✅ Transfer history retrieved successfully!")
        print()
        
        # Process response based on actual API return body structure
        if response and len(response) > 0:
            print(f"📊 Transfer history records (Total {len(response)} records):")
            for i, record in enumerate(response):
                print(f"\n   Record {i+1}:")
                if 'id' in record:
                    print(f"     🆔 Flow ID: {record['id']}")
                if 'accountId' in record:
                    print(f"     👤 Account ID: {record['accountId']}")
                if 'coin' in record:
                    print(f"     🪙 Coin type: {record['coin']}")
                if 'coinName' in record:
                    print(f"     📝 Coin Type Name: {record['coinName']}")
                if 'flowTypeValue' in record:
                    print(f"     🔢 Flow Type Value: {record['flowTypeValue']}")
                if 'flowType' in record:
                    print(f"     📋 Flow Type: {record['flowType']}")
                if 'flowName' in record:
                    print(f"     📖 Flow Description: {record['flowName']}")
                if 'change' in record:
                    print(f"     📊 Change Value: {record['change']}")
                if 'total' in record:
                    print(f"     💰 Total Assets After Change: {record['total']}")
                if 'created' in record:
                    print(f"     ⏰ Create Time: {record['created']}")
        else:
            print("   ℹ️  No transfer history data retrieved")
        
        print("\n🎉 Transfer history retrieval completed!")
        return response
        
    except Exception as e:
        print(f"❌ Get Transfer History Failed: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit Futures API SDK Get Transfer History Example ===\n")
    print("💡 This example requires API key, please ensure correct configuration")
    print("💡 This is a real account query operation, please use with caution!")
    print()
    print("📚 API Information:")
    print("   - API: GET /api/v1/account/balanceFlow")
    print("   - Auth: Requires signature (USER_DATA)")
    print("   - Function: Query Account Transfer history records")
    print("   - Parameters: asset(Optional), from Account Type(Optional), to Account Type(Optional), limit")
    print()
    print("💡 Query description:")
    print("   - Can filter by asset type")
    print("   - Can filter by account type")
    print("   - Supports paginated query")
    print("   - Return most recent transfer records")
    get_transfer_history()
