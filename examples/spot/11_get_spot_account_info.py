#!/usr/bin/env python3
"""
TooBit API 现货账户信息示例 (11号)
查询现货账户信息
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_spot_account_info():
    """查询现货账户信息示例"""
    print("=== TooBit API 现货账户信息示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询现货账户信息测试:")
        print()
        print("   API: GET /api/v1/account")
        print("   说明: 查询现货账户信息")
        print()
        
        account_info = client.get_spot_account_info()
        balances = account_info.balances
        
        print(f"   资产种类数量: {len(balances)}")
        print()
        
        if balances:
            print("   📋 资产余额列表:")
            for i, balance in enumerate(balances, 1):
                print(f"   [{i}] 资产: {balance.asset}")
                print(f"       资产ID: {balance.assetId}")
                print(f"       资产名称: {balance.assetName}")
                print(f"       总数量: {balance.total}")
                print(f"       可用数: {balance.free}")
                print(f"       冻结数: {balance.locked}")
                print()
        else:
            print("   📭 暂无资产余额")
        
        # 资产统计
        if balances:
            total_assets = len(balances)
            non_zero_assets = [b for b in balances if float(b.total) > 0]
            print(f"   📊 资产统计:")
            print(f"       总资产种类: {total_assets}")
            print(f"       非零资产: {len(non_zero_assets)}")
            print()
        
        print("🎉 查询现货账户信息测试完成!")
        
    except Exception as e:
        print(f"❌ 查询现货账户信息测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_spot_account_info()
