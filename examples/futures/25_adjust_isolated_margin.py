#!/usr/bin/env python3
"""
TooBit API Futures AdjustIsolatedMarginExample (25Number)
AdjustIsolatedMargin
"""

from open_api_sdk import TooBitClient, TooBitConfig, AdjustIsolatedMarginRequest

def adjust_isolated_margin():
    """AdjustIsolatedMarginExample"""
    print("=== TooBit API Futures AdjustIsolatedMarginExample ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Adjust Isolated Margin Test:")
        print()
        
        # Example1: IncreaseMargin
        print("📊 Example 1: Increase Margin")
        print("   Parameters: symbol='BTC-SWAP-USDT', side='LONG', amount='10'")
        print("   API: POST /api/v1/futures/positionMargin")
        print("   Description: For BTC-SWAP-USDT of Long Position Increase 10 USDT Margin")
        print()
        
        request1 = AdjustIsolatedMarginRequest(
            symbol="BTC-SWAP-USDT",
            side="LONG",
            amount="10"
        )
        
        response1 = client.adjust_isolated_margin(request1)
        print(f"   Response Code: {response1.code}")
        print(f"   Response Message: {response1.msg}")
        print(f"   Trading pair: {response1.symbol}")
        print(f"   Update After Margin: {response1.margin}")
        print(f"   Time Timestamp: {response1.timestamp}")
        print()
        
        # Example2: DecreaseMargin
        print("📊 Example 2: Decrease Margin")
        print("   Parameters: symbol='ETH-SWAP-USDT', side='SHORT', amount='-5'")
        print("   API: POST /api/v1/futures/positionMargin")
        print("   Description: For ETH-SWAP-USDT of Short Position Decrease 5 USDT Margin")
        print()
        
        request2 = AdjustIsolatedMarginRequest(
            symbol="ETH-SWAP-USDT",
            side="SHORT",
            amount="-5"
        )
        
        response2 = client.adjust_isolated_margin(request2)
        print(f"   ResponseCode: {response2.code}")
        print(f"   ResponseMessage: {response2.msg}")
        print(f"   Trading pair: {response2.symbol}")
        print(f"   UpdateAfterMargin: {response2.margin}")
        print(f"   TimeTimestamp: {response2.timestamp}")
        print()
        
        # Example3: IncreaseEmptyHeaderMargin
        print("📊 Example 3: Increase Short Position Margin")
        print("   Parameters: symbol='BTC-SWAP-USDT', side='SHORT', amount='15'")
        print("   API: POST /api/v1/futures/position/margin")
        print("   Description: For BTC-SWAP-USDT of Short Position Increase 15 USDT Margin")
        print()
        
        request3 = AdjustIsolatedMarginRequest(
            symbol="BTC-SWAP-USDT",
            side="SHORT",
            amount="15"
        )
        
        response3 = client.adjust_isolated_margin(request3)
        print(f"   ResponseCode: {response3.code}")
        print(f"   ResponseMessage: {response3.msg}")
        print(f"   Trading pair: {response3.symbol}")
        print(f"   UpdateAfterMargin: {response3.margin}")
        print(f"   TimeTimestamp: {response3.timestamp}")
        print()
        
        print("🎉 Adjust Isolated Margin Test Complete!")
        
    except Exception as e:
        print(f"❌ Adjust Isolated Margin Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    adjust_isolated_margin()
