#!/usr/bin/env python3
"""
TooBit API Futures QueryLeverageMultipleAndPositionModeExample (33Number)
QueryLeverageMultipleAndPositionMode
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryLeverageRequest

def get_account_leverage():
    """QueryLeverageMultipleAndPositionModeExample"""
    print("=== TooBit API Futures QueryLeverageMultipleAndPositionModeExample ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Leverage Multiple And Position Mode Test:")
        print()
        print("   API: GET /api/v1/futures/accountLeverage")
        print("   Description: Query Leverage Multiple And Position Mode")
        print()
        
        # Query BTC-SWAP-USDT of Leverage Information
        request = QueryLeverageRequest(
            symbol="BTC-SWAP-USDT"
        )
        
        leverages = client.get_account_leverage(request)
        print(f"   Query Result Quantity: {len(leverages)}")
        print()
        
        if leverages:
            print("   📋 Leverage Information List:")
            for i, leverage in enumerate(leverages, 1):
                print(f"   [{i}] Trading pair: {leverage.symbolId}")
                print(f"       Leverage Multiple: {leverage.leverage}")
                print(f"       Margin Type: {leverage.marginType}")
                print()
        else:
            print("   📭 No Leverage Information")
        
        # Margin Type Description
        print("   💡 Margin Type Description:")
        print("      CROSS: Cross mode - All positions share total margin")
        print("      ISOLATED: Isolated mode - Each position has independent margin")
        print()
        
        print("🎉 Query Leverage Multiple And Position Mode Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Leverage Multiple And Position Mode Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_account_leverage()
