#!/usr/bin/env python3
"""
TooBit API 合约调整开仓杠杆示例 (32号)
调整开仓杠杆
"""

from open_api_sdk import TooBitClient, TooBitConfig, AdjustLeverageRequest

def adjust_leverage():
    """调整开仓杠杆示例"""
    print("=== TooBit API 合约调整开仓杠杆示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 调整开仓杠杆测试:")
        print()
        print("   API: POST /api/v1/futures/leverage")
        print("   说明: 调整开仓杠杆")
        print()
        
        # 示例1: 调整到20倍杠杆
        print("   📋 示例1: 调整到20倍杠杆")
        request1 = AdjustLeverageRequest(
            symbol="BTC-SWAP-USDT",
            leverage=20
        )
        
        response1 = client.adjust_leverage(request1)
        print(f"   响应码: {response1.code}")
        print(f"   交易对: {response1.symbolId}")
        print(f"   杠杆倍数: {response1.leverage}")
        print()
        
        # 示例2: 调整到10倍杠杆
        print("   📋 示例2: 调整到10倍杠杆")
        request2 = AdjustLeverageRequest(
            symbol="BTC-SWAP-USDT",
            leverage=10
        )
        
        response2 = client.adjust_leverage(request2)
        print(f"   响应码: {response2.code}")
        print(f"   交易对: {response2.symbolId}")
        print(f"   杠杆倍数: {response2.leverage}")
        print()
        
        # 杠杆说明
        print("   💡 杠杆倍数说明:")
        print("      杠杆倍数越高，收益和风险都越大")
        print("      建议根据风险承受能力选择合适的杠杆")
        print("      常见杠杆倍数: 1x, 2x, 5x, 10x, 20x, 50x, 100x")
        print()
        
        print("🎉 调整开仓杠杆测试完成!")
        
    except Exception as e:
        print(f"❌ 调整开仓杠杆测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    adjust_leverage()
