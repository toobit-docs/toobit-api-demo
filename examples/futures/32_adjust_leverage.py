#!/usr/bin/env python3
"""
TooBit API Futures Adjust Open Leverage Example (32 Number)
Adjust Open Leverage
"""

from open_api_sdk import TooBitClient, TooBitConfig, AdjustLeverageRequest

def adjust_leverage():
    """Adjust Open Leverage Example"""
    print("=== TooBit API Futures Adjust Open Leverage Example ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Adjust Open Leverage Test:")
        print()
        print("   API: POST /api/v1/futures/leverage")
        print("   Description: Adjust Open Leverage")
        print()
        
        # Example 1: Adjust To 20 Multiple Leverage
        print("   📋 Example 1: Adjust To 20 Multiple Leverage")
        request1 = AdjustLeverageRequest(
            symbol="BTC-SWAP-USDT",
            leverage=20
        )
        
        response1 = client.adjust_leverage(request1)
        print(f"   Response Code: {response1.code}")
        print(f"   Trading pair: {response1.symbolId}")
        print(f"   Leverage Multiple: {response1.leverage}")
        print()
        
        # Example 2: Adjust To 10 Multiple Leverage
        print("   📋 Example 2: Adjust To 10 Multiple Leverage")
        request2 = AdjustLeverageRequest(
            symbol="BTC-SWAP-USDT",
            leverage=10
        )
        
        response2 = client.adjust_leverage(request2)
        print(f"   ResponseCode: {response2.code}")
        print(f"   Trading pair: {response2.symbolId}")
        print(f"   LeverageMultiple: {response2.leverage}")
        print()
        
        # Leverage Description
        print("   💡 Leverage Multiple Description:")
        print("      Higher Leverage Multiple means higher profit and risk")
        print("      Recommend selecting appropriate leverage based on risk tolerance")
        print("      Common Leverage Multiples: 1x, 2x, 5x, 10x, 20x, 50x, 100x")
        print()
        
        print("🎉 Adjust Open Leverage Test Complete!")
        
    except Exception as e:
        print(f"❌ Adjust Open Leverage Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    adjust_leverage()
