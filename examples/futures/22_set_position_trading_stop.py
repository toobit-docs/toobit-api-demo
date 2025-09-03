#!/usr/bin/env python3
"""
TooBit API 合约设置持仓止盈止损示例 (22号)
设置持仓的止盈止损价格
"""

from open_api_sdk import TooBitClient, TooBitConfig, SetPositionTradingStopRequest

def set_position_trading_stop():
    """设置持仓止盈止损示例"""
    print("=== TooBit API 合约设置持仓止盈止损示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 设置持仓止盈止损测试:")
        print()
        
        # 示例1: 设置多头持仓的止盈止损
        print("📊 示例1: 设置多头持仓的止盈止损")
        print("   参数: symbol='BTC-SWAP-USDT', side='LONG'")
        print("   止损价格: 16000, 止盈价格: 18000")
        print("   API: POST /api/v1/futures/position/trading-stop")
        print("   说明: 为BTC-SWAP-USDT的多头持仓设置止盈止损")
        print()
        
        request1 = SetPositionTradingStopRequest(
            symbol="BTC-SWAP-USDT",
            side="LONG",
            stopLoss="16000",
            takeProfit="138000"
        )
        
        response1 = client.set_position_trading_stop(request1)
        print(f"   交易对: {response1.symbol}")
        print(f"   仓位方向: {response1.side}")
        print(f"   止盈价格: {response1.takeProfit}")
        print(f"   止损价格: {response1.stopLoss}")
        print(f"   止盈触发类型: {response1.tpTriggerBy}")
        print(f"   止损触发类型: {response1.slTriggerBy}")
        print()
        
        # 示例2: 只设置止损价格
        print("📊 示例2: 只设置止损价格")
        print("   参数: symbol='ETH-SWAP-USDT', side='SHORT'")
        print("   止损价格: 2000")
        print("   API: POST /api/v1/futures/position/trading-stop")
        print("   说明: 为ETH-SWAP-USDT的空头持仓只设置止损")
        print()
        
        request2 = SetPositionTradingStopRequest(
            symbol="ETH-SWAP-USDT",
            side="SHORT",
            stopLoss="2000"
        )
        
        response2 = client.set_position_trading_stop(request2)
        print(f"   交易对: {response2.symbol}")
        print(f"   仓位方向: {response2.side}")
        print(f"   止盈价格: {response2.takeProfit}")
        print(f"   止损价格: {response2.stopLoss}")
        print(f"   止盈触发类型: {response2.tpTriggerBy}")
        print(f"   止损触发类型: {response2.slTriggerBy}")
        print()
        
        # 示例3: 只设置止盈价格
        print("📊 示例3: 只设置止盈价格")
        print("   参数: symbol='BTC-SWAP-USDT', side='LONG'")
        print("   止盈价格: 19000")
        print("   API: POST /api/v1/futures/position/trading-stop")
        print("   说明: 为BTC-SWAP-USDT的多头持仓只设置止盈")
        print()
        
        request3 = SetPositionTradingStopRequest(
            symbol="BTC-SWAP-USDT",
            side="LONG",
            takeProfit="19000"
        )
        
        response3 = client.set_position_trading_stop(request3)
        print(f"   交易对: {response3.symbol}")
        print(f"   仓位方向: {response3.side}")
        print(f"   止盈价格: {response3.takeProfit}")
        print(f"   止损价格: {response3.stopLoss}")
        print(f"   止盈触发类型: {response3.tpTriggerBy}")
        print(f"   止损触发类型: {response3.slTriggerBy}")
        print()
        
        # 示例4: 设置带类型的止盈止损
        print("📊 示例4: 设置带类型的止盈止损")
        print("   参数: symbol='BTC-SWAP-USDT', side='LONG'")
        print("   止损价格: 15000, 止盈价格: 20000")
        print("   触发类型: MARK_PRICE(标记价格), CONTRACT_PRICE(合约最新价)")
        print("   API: POST /api/v1/futures/position/trading-stop")
        print("   说明: 为BTC-SWAP-USDT的多头持仓设置带触发类型的止盈止损")
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
        print(f"   交易对: {response4.symbol}")
        print(f"   仓位方向: {response4.side}")
        print(f"   止盈价格: {response4.takeProfit}")
        print(f"   止损价格: {response4.stopLoss}")
        print(f"   止盈触发类型: {response4.tpTriggerBy}")
        print(f"   止损触发类型: {response4.slTriggerBy}")
        print()
        
        print("🎉 设置持仓止盈止损测试完成!")
        
    except Exception as e:
        print(f"❌ 设置持仓止盈止损测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    set_position_trading_stop()
