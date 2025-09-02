"""
TooBit API SDK - 获取账户信息接口示例 (10)
获取账户基本信息和权限状态 (需要API密钥)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_account_info():
    """获取账户信息"""
    print("=== TooBit API 获取账户信息 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🔄 正在获取账户信息...")
        print()
        print("⚠️  注意: 这是真实的账户查询操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        account_info = client.get_account_info()
        
        print("✅ 账户信息获取成功!")
        print()
        
        # 显示基本信息
        print("📋 基本信息:")
        print(f"   账户类型: {account_info.account_type}")
        print(f"   更新时间: {account_info.update_time}")
        print()
        
        # 显示权限信息
        print("🔐 账户权限:")
        print(f"   是否可以交易: {'✅ 是' if account_info.can_trade else '❌ 否'}")
        print(f"   是否可以提现: {'✅ 是' if account_info.can_withdraw else '❌ 否'}")
        print(f"   是否可以充值: {'✅ 是' if account_info.can_deposit else '❌ 否'}")
        print()
        
        # 显示手续费信息
        print("💰 手续费信息:")
        print(f"   挂单手续费: {account_info.maker_commission}")
        print(f"   吃单手续费: {account_info.taker_commission}")
        print(f"   买方手续费: {account_info.buyer_commission}")
        print(f"   卖方手续费: {account_info.seller_commission}")
        print()
        
        # 显示余额信息
        print("💳 账户余额:")
        balances_with_funds = []
        for balance in account_info.balances:
            free = float(balance['free'])
            locked = float(balance['locked'])
            if free > 0 or locked > 0:
                balances_with_funds.append(balance)
        
        if balances_with_funds:
            print(f"   找到 {len(balances_with_funds)} 个有余额的资产:")
            for balance in balances_with_funds[:5]:  # 只显示前5个
                asset = balance['asset']
                free = float(balance['free'])
                locked = float(balance['locked'])
                total = free + locked
                print(f"   {asset}: 可用 {free}, 冻结 {locked}, 总计 {total}")
        else:
            print("   ℹ️  账户中没有资产余额")
        
        print("\n🎉 获取账户信息完成!")
        return account_info
        
    except Exception as e:
        print(f"❌ 获取账户信息失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 获取账户信息示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的账户查询操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: GET /api/v1/account")
    print("   - 鉴权: 需要签名 (USER_DATA)")
    print("   - 功能: 获取账户基本信息和权限状态")
    print("   - 参数: 无")
    print()
    print("⚠️  重要提醒:")
    print("   - 建议先在测试环境中验证")
    print()
    
    get_account_info() 