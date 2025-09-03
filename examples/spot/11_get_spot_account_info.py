#!/usr/bin/env python3
"""
TooBit API Spot Account Information Example (11 Number)
Query Spot Account Information
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_spot_account_info():
    """QuerySpotAccount informationExample"""
    print("=== TooBit API Spot Account information Example ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Spot Account information Test:")
        print()
        print("   API: GET /api/v1/account")
        print("   Description: Query Spot Account information")
        print()
        
        account_info = client.get_spot_account_info()
        balances = account_info.balances
        
        print(f"   Asset type quantity: {len(balances)}")
        print()
        
        if balances:
            print("   📋 Asset Balance List:")
            for i, balance in enumerate(balances, 1):
                print(f"   [{i}] Asset: {balance.asset}")
                print(f"       Asset ID: {balance.assetId}")
                print(f"       Asset Name: {balance.assetName}")
                print(f"       Total Quantity: {balance.total}")
                print(f"       Available: {balance.free}")
                print(f"       Locked: {balance.locked}")
                print()
        else:
            print("   📭 None Asset Balance")
        
        # Asset Statistics
        if balances:
            total_assets = len(balances)
            non_zero_assets = [b for b in balances if float(b.total) > 0]
            print(f"   📊 Asset Statistics:")
            print(f"       Total asset types: {total_assets}")
            print(f"       Non-zero assets: {len(non_zero_assets)}")
            print()
        
        print("🎉 Query Spot Account information Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Spot Account information Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_spot_account_info()
