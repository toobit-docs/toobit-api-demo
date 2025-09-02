"""
TooBit API SDK - 获取账户信息接口示例
获取账户基本信息和权限状态 (需要API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_account_info():
    """获取账户信息"""
    print("=== TooBit API 获取账户信息接口测试 ===\n")
    
    # 注意: 这个示例需要真实的API密钥
    print("⚠️  注意: 此示例需要真实的API密钥才能运行")
    print("请先设置环境变量或直接配置API密钥\n")
    
    try:
        # 方式1: 从环境变量创建配置
        config = TooBitConfig.from_env()
        print("✅ 从环境变量加载配置成功")
    except ValueError as e:
        print(f"❌ 环境变量配置失败: {e}")
        print("\n请设置以下环境变量:")
        print("export TOOBIT_API_KEY='your_api_key'")
        print("export TOOBIT_API_SECRET='your_api_secret'")
        print("\n或者直接修改代码中的配置:")
        print("config = TooBitConfig(")
        print("    api_key='your_api_key',")
        print("    api_secret='your_api_secret'")
        print(")")
        return
    
    # 方式2: 直接创建配置 (取消注释并填入你的API密钥)
    # config = TooBitConfig(
    #     api_key="your_api_key_here",
    #     api_secret="your_api_secret_here"
    # )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        print("\n👤 获取账户信息...")
        
        # 调用获取账户信息接口
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
        print(f"   挂单手续费: {account_info.maker_commission} (万分之{account_info.maker_commission/10:.1f})")
        print(f"   吃单手续费: {account_info.taker_commission} (万分之{account_info.taker_commission/10:.1f})")
        print(f"   买方手续费: {account_info.buyer_commission} (万分之{account_info.buyer_commission/10:.1f})")
        print(f"   卖方手续费: {account_info.seller_commission} (万分之{account_info.seller_commission/10:.1f})")
        print()
        
        # 判断手续费等级
        if account_info.maker_commission <= 10:  # 万分之1
            fee_level = "VIP"
            fee_emoji = "👑"
        elif account_info.maker_commission <= 15:  # 万分之1.5
            fee_level = "高级"
            fee_emoji = "⭐"
        elif account_info.maker_commission <= 20:  # 万分之2
            fee_level = "标准"
            fee_emoji = "📊"
        else:
            fee_level = "普通"
            fee_emoji = "👤"
        
        print(f"   手续费等级: {fee_emoji} {fee_level}")
        print()
        
        # 显示余额信息
        print("💳 账户余额:")
        
        # 显示所有有余额的资产
        balances_with_funds = []
        for balance in account_info.balances:
            free = float(balance['free'])
            locked = float(balance['locked'])
            if free > 0 or locked > 0:
                balances_with_funds.append(balance)
        
        if balances_with_funds:
            print(f"   找到 {len(balances_with_funds)} 个有余额的资产:")
            
            # 按总余额排序
            balances_with_funds.sort(key=lambda x: float(x['free']) + float(x['locked']), reverse=True)
            
            for i, balance in enumerate(balances_with_funds[:10]):  # 只显示前10个
                asset = balance['asset']
                free = float(balance['free'])
                locked = float(balance['locked'])
                total = free + locked
                
                print(f"   {i+1:2d}. {asset:<8}")
                print(f"       可用: {free:>15,.8f}")
                print(f"       冻结: {locked:>15,.8f}")
                print(f"       总计: {total:>15,.8f}")
                
                # 显示资产状态
                if locked > 0:
                    locked_percentage = (locked / total) * 100
                    print(f"       状态: ⚠️  有 {locked_percentage:.1f}% 资产被冻结")
                else:
                    print(f"       状态: ✅ 全部可用")
                print()
            
            if len(balances_with_funds) > 10:
                print(f"   ... 还有 {len(balances_with_funds) - 10} 个资产有余额")
        else:
            print("   ℹ️  账户中没有资产余额")
        
        # 账户安全分析
        print("🛡️  账户安全分析:")
        
        security_score = 0
        security_issues = []
        
        # 检查交易权限
        if account_info.can_trade:
            security_score += 1
            print("   ✅ 交易权限正常")
        else:
            security_issues.append("交易权限被限制")
            print("   ❌ 交易权限被限制")
        
        # 检查提现权限
        if account_info.can_withdraw:
            security_score += 1
            print("   ✅ 提现权限正常")
        else:
            security_issues.append("提现权限被限制")
            print("   ❌ 提现权限被限制")
        
        # 检查充值权限
        if account_info.can_deposit:
            security_score += 1
            print("   ✅ 充值权限正常")
        else:
            security_issues.append("充值权限被限制")
            print("   ❌ 充值权限被限制")
        
        # 检查是否有冻结资产
        total_locked_assets = sum(1 for balance in account_info.balances 
                                if float(balance['locked']) > 0)
        
        if total_locked_assets == 0:
            security_score += 1
            print("   ✅ 没有冻结资产")
        else:
            security_issues.append(f"有 {total_locked_assets} 种资产被冻结")
            print(f"   ⚠️  有 {total_locked_assets} 种资产被冻结")
        
        # 安全评分
        print(f"\n   安全评分: {security_score}/4")
        
        if security_score == 4:
            security_status = "优秀"
            security_emoji = "🟢"
        elif security_score >= 3:
            security_status = "良好"
            security_emoji = "🟡"
        else:
            security_status = "需要关注"
            security_emoji = "🔴"
        
        print(f"   安全状态: {security_emoji} {security_status}")
        
        if security_issues:
            print("   需要关注的问题:")
            for issue in security_issues:
                print(f"     - {issue}")
        
        print("\n🎉 获取账户信息接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 获取账户信息接口测试失败: {e}")
        print("\n可能的原因:")
        print("   - API密钥无效或过期")
        print("   - API密钥权限不足")
        print("   - 网络连接问题")
        print("   - 签名验证失败")
        return False
    
    finally:
        client.close()


def analyze_account_performance():
    """分析账户表现"""
    print("\n=== 账户表现分析 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("📊 分析账户表现...")
        
        # 获取账户信息
        account_info = client.get_account_info()
        
        # 计算总资产价值 (简化计算，实际需要获取价格)
        print("💰 资产分析:")
        
        # 统计资产种类
        total_assets = len([b for b in account_info.balances 
                          if float(b['free']) > 0 or float(b['locked']) > 0])
        
        # 统计主要资产
        major_assets = ['BTC', 'ETH', 'USDT', 'BNB']
        major_asset_count = 0
        
        for asset in major_assets:
            for balance in account_info.balances:
                if balance['asset'] == asset:
                    free = float(balance['free'])
                    locked = float(balance['locked'])
                    if free > 0 or locked > 0:
                        major_asset_count += 1
                        print(f"   {asset}: {free + locked:.8f}")
                    break
        
        print(f"\n   总资产种类: {total_assets}")
        print(f"   主要资产种类: {major_asset_count}/{len(major_assets)}")
        
        # 账户活跃度分析
        print("\n🔥 账户活跃度:")
        
        # 基于手续费等级判断活跃度
        if account_info.maker_commission <= 10:
            activity_level = "非常活跃"
            activity_emoji = "🔥"
        elif account_info.maker_commission <= 15:
            activity_level = "比较活跃"
            activity_emoji = "⚡"
        else:
            activity_level = "一般活跃"
            activity_emoji = "📊"
        
        print(f"   活跃度: {activity_emoji} {activity_level}")
        print(f"   (基于手续费等级判断)")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 账户表现分析失败: {e}")


if __name__ == "__main__":
    get_account_info()
    analyze_account_performance() 