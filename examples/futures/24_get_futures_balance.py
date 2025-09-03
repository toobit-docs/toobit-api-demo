#!/usr/bin/env python3
"""
TooBit API Futures Query Account Balance Example (24 Number)
Query Futures Account Balance information
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_balance():
    """Query Futures Account Balance Example"""
    print("=== TooBit API Futures Query Account Balance Example ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Futures Account Balance Test:")
        print()
        print("   API: GET /api/v1/futures/balance")
        print("   Description: Query Futures Account All Asset of Balance information")
        print()
        
        balances = client.get_futures_balance()
        print(f"   Return Asset Quantity: {len(balances)}")
        print()
        
        for balance in balances:
            print(f"   📊 Asset: {balance.asset}")
            print(f"      Total Balance: {balance.balance}")
            print(f"      Available Balance: {balance.availableBalance}")
            print(f"      Position Margin: {balance.positionMargin}")
            print(f"      Order Margin: {balance.orderMargin}")
            print(f"      Cross Unrealized PnL: {balance.crossUnRealizedPnl}")
            print()
        
        print("🎉 Query Futures Account Balance Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Futures Account Balance Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_balance()
