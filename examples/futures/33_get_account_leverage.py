#!/usr/bin/env python3
"""
TooBit API 合约查询杠杆倍数和仓位模式示例 (33号)
查询杠杆倍数和仓位模式
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryLeverageRequest

def get_account_leverage():
    """查询杠杆倍数和仓位模式示例"""
    print("=== TooBit API 合约查询杠杆倍数和仓位模式示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询杠杆倍数和仓位模式测试:")
        print()
        print("   API: GET /api/v1/futures/accountLeverage")
        print("   说明: 查询杠杆倍数和仓位模式")
        print()
        
        # 查询BTC-SWAP-USDT的杠杆信息
        request = QueryLeverageRequest(
            symbol="BTC-SWAP-USDT"
        )
        
        leverages = client.get_account_leverage(request)
        print(f"   查询结果数量: {len(leverages)}")
        print()
        
        if leverages:
            print("   📋 杠杆信息列表:")
            for i, leverage in enumerate(leverages, 1):
                print(f"   [{i}] 交易对: {leverage.symbolId}")
                print(f"       杠杆倍数: {leverage.leverage}")
                print(f"       保证金类型: {leverage.marginType}")
                print()
        else:
            print("   📭 暂无杠杆信息")
        
        # 保证金类型说明
        print("   💡 保证金类型说明:")
        print("      CROSS: 全仓模式 - 所有仓位共享保证金")
        print("      ISOLATED: 逐仓模式 - 每个仓位独立保证金")
        print()
        
        print("🎉 查询杠杆倍数和仓位模式测试完成!")
        
    except Exception as e:
        print(f"❌ 查询杠杆倍数和仓位模式测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_account_leverage()
