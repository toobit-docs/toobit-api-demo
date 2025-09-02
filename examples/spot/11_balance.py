"""
TooBit API SDK - 查询账户余额接口示例 (11)
查询账户余额 (需要API密钥)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_balance():
    """查询账户余额"""
    print("=== TooBit API 查询账户余额 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🔄 正在查询账户余额...")
        print()
        print("⚠️  注意: 这是真实的账户查询操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 调用查询余额接口
        balance = client.get_balance()
        
        print("✅ 账户余额查询成功!")
        print()
        
        # 显示余额信息
        print("💳 账户余额:")
        balances_with_funds = []
        for balance_item in balance:
            free = float(balance_item['free'])
            locked = float(balance_item['locked'])
            if free > 0 or locked > 0:
                balances_with_funds.append(balance_item)
        
        if balances_with_funds:
            print(f"   找到 {len(balances_with_funds)} 个有余额的资产:")
            for balance_item in balances_with_funds[:10]:  # 只显示前10个
                asset = balance_item['asset']
                free = float(balance_item['free'])
                locked = float(balance_item['locked'])
                total = free + locked
                print(f"   {asset}: 可用 {free}, 冻结 {locked}, 总计 {total}")
        else:
            print("   ℹ️  账户中没有资产余额")
        
        print("\n🎉 查询账户余额完成!")
        return balance
        
    except Exception as e:
        print(f"❌ 查询账户余额失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 查询账户余额示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的账户查询操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: GET /api/v1/account")
    print("   - 鉴权: 需要签名 (USER_DATA)")
    print("   - 功能: 查询账户余额")
    print("   - 参数: 无")
    print()
    print("⚠️  重要提醒:")
    print("   - 建议先在测试环境中验证")
    print()
    
    get_balance()