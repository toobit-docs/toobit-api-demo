#!/usr/bin/env python3
"""
TooBit API Futures SetPositionTake ProfitStop LossExample (22Number)
SetPositionofTake ProfitStop LossPrice
"""

from open_api_sdk import TooBitClient, TooBitConfig, SetPositionTradingStopRequest

def set_position_trading_stop():
    """SetPositionTake ProfitStop LossExample"""
    print("=== TooBit API Futures SetPositionTake ProfitStop LossExample ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Set Position Take Profit Stop Loss Test:")
        print()
        
        # Example1: SetMultipleHeaderPositionofTake ProfitStop Loss
        print("📊 Example 1: Set Long Position of Take Profit Stop Loss")
        print("   Parameters: symbol='BTC-SWAP-USDT', side='LONG'")
        print("   Stop LossPrice: 16000, Take ProfitPrice: 18000")
        print("   API: POST /api/v1/futures/position/trading-stop")
        print("   Description: For BTC-SWAP-USDT of Long Position Set Take Profit Stop Loss")
        print()
        
        request1 = SetPositionTradingStopRequest(
            symbol="BTC-SWAP-USDT",
            side="LONG",
            stopLoss="16000",
            takeProfit="138000"
        )
        
        response1 = client.set_position_trading_stop(request1)
        print(f"   Trading pair: {response1.symbol}")
        print(f"   Position Side: {response1.side}")
        print(f"   Take Profit Price: {response1.takeProfit}")
        print(f"   Stop Loss Price: {response1.stopLoss}")
        print(f"   Take Profit Trigger Type: {response1.tpTriggerBy}")
        print(f"   Stop Loss Trigger Type: {response1.slTriggerBy}")
        print()
        
        # Example2: OnlySetStop LossPrice
        print("📊 Example 2: Only Set Stop Loss Price")
        print("   Parameters: symbol='ETH-SWAP-USDT', side='SHORT'")
        print("   Stop LossPrice: 2000")
        print("   API: POST /api/v1/futures/position/trading-stop")
        print("   Description: For ETH-SWAP-USDT of Short Position Only Set Stop Loss")
        print()
        
        request2 = SetPositionTradingStopRequest(
            symbol="ETH-SWAP-USDT",
            side="SHORT",
            stopLoss="2000"
        )
        
        response2 = client.set_position_trading_stop(request2)
        print(f"   Trading pair: {response2.symbol}")
        print(f"   PositionSide: {response2.side}")
        print(f"   Take ProfitPrice: {response2.takeProfit}")
        print(f"   Stop LossPrice: {response2.stopLoss}")
        print(f"   Take ProfitTriggerType: {response2.tpTriggerBy}")
        print(f"   Stop LossTriggerType: {response2.slTriggerBy}")
        print()
        
        # Example3: OnlySetTake ProfitPrice
        print("📊 Example 3: Only Set Take Profit Price")
        print("   Parameters: symbol='BTC-SWAP-USDT', side='LONG'")
        print("   Take ProfitPrice: 19000")
        print("   API: POST /api/v1/futures/position/trading-stop")
        print("   Description: For BTC-SWAP-USDT of Long Position Only Set Take Profit")
        print()
        
        request3 = SetPositionTradingStopRequest(
            symbol="BTC-SWAP-USDT",
            side="LONG",
            takeProfit="19000"
        )
        
        response3 = client.set_position_trading_stop(request3)
        print(f"   Trading pair: {response3.symbol}")
        print(f"   PositionSide: {response3.side}")
        print(f"   Take ProfitPrice: {response3.takeProfit}")
        print(f"   Stop LossPrice: {response3.stopLoss}")
        print(f"   Take ProfitTriggerType: {response3.tpTriggerBy}")
        print(f"   Stop LossTriggerType: {response3.slTriggerBy}")
        print()
        
        # Example4: SetWithTypeofTake ProfitStop Loss
        print("📊 Example 4: Set With Type of Take Profit Stop Loss")
        print("   Parameters: symbol='BTC-SWAP-USDT', side='LONG'")
        print("   Stop LossPrice: 15000, Take ProfitPrice: 20000")
        print("   TriggerType: MARK_PRICE(Mark Price), CONTRACT_PRICE(Futures Latest Price)")
        print("   API: POST /api/v1/futures/position/trading-stop")
        print("   Description: For BTC-SWAP-USDT of Long Position Set With Trigger Type of Take Profit Stop Loss")
        print()
        
        request4 = SetPositionTradingStopRequest(
            symbol="BTC-SWAP-USDT",
            side="LONG",
            stopLoss="15000",
            takeProfit="20000",
            slTriggerBy="MARK_PRICE",
            tpTriggerBy="MARK_PRICE"
        )
        
        response4 = client.set_position_trading_stop(request4)
        print(f"   Trading pair: {response4.symbol}")
        print(f"   PositionSide: {response4.side}")
        print(f"   Take ProfitPrice: {response4.takeProfit}")
        print(f"   Stop LossPrice: {response4.stopLoss}")
        print(f"   Take ProfitTriggerType: {response4.tpTriggerBy}")
        print(f"   Stop LossTriggerType: {response4.slTriggerBy}")
        print()
        
        print("🎉 Set Position Take Profit Stop Loss Test Complete!")
        
    except Exception as e:
        print(f"❌ Set Position Take Profit Stop Loss Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    set_position_trading_stop()
