#!/usr/bin/env python3
"""
TooBit API Spot Query Sub Account Example (12 Number)
Query Spot Sub Account List
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_spot_sub_accounts():
    """QuerySpotSubAccountExample"""
    print("=== TooBit API Spot Query Sub Account Example ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Spot Sub Account Test:")
        print()
        print("   API: GET /api/v1/account/subAccount")
        print("   Description: Query Spot Sub Account List")
        print()
        
        sub_accounts = client.get_spot_sub_accounts()
        print(f"   Sub account total count: {len(sub_accounts)}")
        print()
        
        if sub_accounts:
            print("   📋 Sub Account List:")
            for i, account in enumerate(sub_accounts, 1):
                print(f"   [{i}] Account ID: {account.accountId}")
                print(f"       Account Name: {account.accountName if account.accountName else '(NotSet)'}")
                print(f"       Account Type: {account.accountType}")
                print(f"       Account Index: {account.accountIndex}")
                print()
        else:
            print("   📭 None Sub Account")
        
        # Account Type Description
        print("   💡 Account Type Description:")
        print("      1: Spot account")
        print("      3: Futures Account")
        print()
        
        # Account Index Description
        print("   💡 Account Index Description:")
        print("      0: Default account")
        print("      >0: Create of Sub Account")
        print()
        
        print("🎉 Query Spot Sub Account Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Spot Sub Account Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_spot_sub_accounts()
