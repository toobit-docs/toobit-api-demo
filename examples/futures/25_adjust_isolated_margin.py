#!/usr/bin/env python3
"""
TooBit API 合约调整逐仓保证金示例 (25号)
调整逐仓保证金
"""

from open_api_sdk import TooBitClient, TooBitConfig, AdjustIsolatedMarginRequest

def adjust_isolated_margin():
    """调整逐仓保证金示例"""
    print("=== TooBit API 合约调整逐仓保证金示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 调整逐仓保证金测试:")
        print()
        
        # 示例1: 增加保证金
        print("📊 示例1: 增加保证金")
        print("   参数: symbol='BTC-SWAP-USDT', side='LONG', amount='10'")
        print("   API: POST /api/v1/futures/positionMargin")
        print("   说明: 为BTC-SWAP-USDT的多头仓位增加10 USDT保证金")
        print()
        
        request1 = AdjustIsolatedMarginRequest(
            symbol="BTC-SWAP-USDT",
            side="LONG",
            amount="10"
        )
        
        response1 = client.adjust_isolated_margin(request1)
        print(f"   响应代码: {response1.code}")
        print(f"   响应消息: {response1.msg}")
        print(f"   交易对: {response1.symbol}")
        print(f"   更新后保证金: {response1.margin}")
        print(f"   时间戳: {response1.timestamp}")
        print()
        
        # 示例2: 减少保证金
        print("📊 示例2: 减少保证金")
        print("   参数: symbol='ETH-SWAP-USDT', side='SHORT', amount='-5'")
        print("   API: POST /api/v1/futures/positionMargin")
        print("   说明: 为ETH-SWAP-USDT的空头仓位减少5 USDT保证金")
        print()
        
        request2 = AdjustIsolatedMarginRequest(
            symbol="ETH-SWAP-USDT",
            side="SHORT",
            amount="-5"
        )
        
        response2 = client.adjust_isolated_margin(request2)
        print(f"   响应代码: {response2.code}")
        print(f"   响应消息: {response2.msg}")
        print(f"   交易对: {response2.symbol}")
        print(f"   更新后保证金: {response2.margin}")
        print(f"   时间戳: {response2.timestamp}")
        print()
        
        # 示例3: 增加空头保证金
        print("📊 示例3: 增加空头保证金")
        print("   参数: symbol='BTC-SWAP-USDT', side='SHORT', amount='15'")
        print("   API: POST /api/v1/futures/position/margin")
        print("   说明: 为BTC-SWAP-USDT的空头仓位增加15 USDT保证金")
        print()
        
        request3 = AdjustIsolatedMarginRequest(
            symbol="BTC-SWAP-USDT",
            side="SHORT",
            amount="15"
        )
        
        response3 = client.adjust_isolated_margin(request3)
        print(f"   响应代码: {response3.code}")
        print(f"   响应消息: {response3.msg}")
        print(f"   交易对: {response3.symbol}")
        print(f"   更新后保证金: {response3.margin}")
        print(f"   时间戳: {response3.timestamp}")
        print()
        
        print("🎉 调整逐仓保证金测试完成!")
        
    except Exception as e:
        print(f"❌ 调整逐仓保证金测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    adjust_isolated_margin()
