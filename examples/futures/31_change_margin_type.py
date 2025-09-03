#!/usr/bin/env python3
"""
TooBit API 合约变换逐全仓模式示例 (31号)
变换逐全仓模式
"""

from open_api_sdk import TooBitClient, TooBitConfig, ChangeMarginTypeRequest, MarginType

def change_margin_type():
    """变换逐全仓模式示例"""
    print("=== TooBit API 合约变换逐全仓模式示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 变换逐全仓模式测试:")
        print()
        print("   API: POST /api/v1/futures/marginType")
        print("   说明: 变换逐全仓模式")
        print()
        
        # 示例1: 切换到全仓模式
        print("   📋 示例1: 切换到全仓模式")
        request1 = ChangeMarginTypeRequest(
            symbol="BTC-SWAP-USDT",
            marginType=MarginType.CROSS
        )
        
        response1 = client.change_margin_type(request1)
        print(f"   响应码: {response1.code}")
        print(f"   交易对: {response1.symbol}")
        print(f"   保证金类型: {response1.marginType}")
        print()
        
        # 示例2: 切换到逐仓模式
        print("   📋 示例2: 切换到逐仓模式")
        request2 = ChangeMarginTypeRequest(
            symbol="BTC-SWAP-USDT",
            marginType=MarginType.ISOLATED
        )
        
        response2 = client.change_margin_type(request2)
        print(f"   响应码: {response2.code}")
        print(f"   交易对: {response2.symbol}")
        print(f"   保证金类型: {response2.marginType}")
        print()
        
        # 状态说明
        print("   💡 保证金类型说明:")
        print("      CROSS: 全仓模式 - 所有仓位共享保证金")
        print("      ISOLATED: 逐仓模式 - 每个仓位独立保证金")
        print()
        
        print("🎉 变换逐全仓模式测试完成!")
        
    except Exception as e:
        print(f"❌ 变换逐全仓模式测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    change_margin_type()
