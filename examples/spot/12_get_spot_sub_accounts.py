#!/usr/bin/env python3
"""
TooBit API 现货查询子账户示例 (12号)
查询现货子账户列表
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_spot_sub_accounts():
    """查询现货子账户示例"""
    print("=== TooBit API 现货查询子账户示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询现货子账户测试:")
        print()
        print("   API: GET /api/v1/account/subAccount")
        print("   说明: 查询现货子账户列表")
        print()
        
        sub_accounts = client.get_spot_sub_accounts()
        print(f"   子账户总数: {len(sub_accounts)}")
        print()
        
        if sub_accounts:
            print("   📋 子账户列表:")
            for i, account in enumerate(sub_accounts, 1):
                print(f"   [{i}] 账户ID: {account.accountId}")
                print(f"       账户名称: {account.accountName if account.accountName else '(未设置)'}")
                print(f"       账户类型: {account.accountType}")
                print(f"       账户索引: {account.accountIndex}")
                print()
        else:
            print("   📭 暂无子账户")
        
        # 账户类型说明
        print("   💡 账户类型说明:")
        print("      1: 币币账户")
        print("      3: 合约账户")
        print()
        
        # 账户索引说明
        print("   💡 账户索引说明:")
        print("      0: 默认账户")
        print("      >0: 创建的子账户")
        print()
        
        print("🎉 查询现货子账户测试完成!")
        
    except Exception as e:
        print(f"❌ 查询现货子账户测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_spot_sub_accounts()
