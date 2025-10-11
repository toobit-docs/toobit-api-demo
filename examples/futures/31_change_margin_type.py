#!/usr/bin/env python3
"""
TooBit API Futures Change to Cross Mode Example (31 Number)
Change to Cross Mode
"""

from open_api_sdk import TooBitClient, TooBitConfig, ChangeMarginTypeRequest, MarginType

def change_margin_type():
    """Change to Cross Mode Example"""
    print("=== TooBit API Futures Change to Cross Mode Example ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Change to Cross Mode Test:")
        print()
        print("   API: POST /api/v1/futures/marginType")
        print("   Description: Change to Cross Mode")
        print()
        
        # Example 1: Switch To Cross Mode
        print("   📋 Example 1: Switch To Cross Mode")
        request1 = ChangeMarginTypeRequest(
            symbol="BTC-SWAP-USDT",
            marginType=MarginType.CROSS
        )
        
        response1 = client.change_margin_type(request1)
        print(f"   Response Code: {response1.code}")
        print(f"   Trading pair: {response1.symbol}")
        print(f"   Margin Type: {response1.marginType}")
        print()
        
        # Example 2: Switch To Isolated Mode
        print("   📋 Example 2: Switch To Isolated Mode")
        request2 = ChangeMarginTypeRequest(
            symbol="BTC-SWAP-USDT",
            marginType=MarginType.ISOLATED
        )
        
        response2 = client.change_margin_type(request2)
        print(f"   ResponseCode: {response2.code}")
        print(f"   Trading pair: {response2.symbol}")
        print(f"   MarginType: {response2.marginType}")
        print()
        
        # Status Description
        print("   💡 Margin Type Description:")
        print("      CROSS: Cross Mode - All Positions Share Total Margin")
        print("      ISOLATED: Isolated Mode - Each Position Has Independent Margin")
        print()
        
        print("🎉 Change to Cross Mode Test Complete!")
        
    except Exception as e:
        print(f"❌ Change to Cross Mode Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    change_margin_type()
