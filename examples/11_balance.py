"""
TooBit API SDK - 获取账户余额接口示例
获取账户中所有资产的余额信息 (需要API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_balance():
    """获取账户余额"""
    print("=== TooBit API 获取账户余额接口测试 ===\n")
    
    # 注意: 这个示例需要真实的API密钥
    print("⚠️  注意: 此示例需要真实的API密钥才能运行")
    print("请先设置环境变量或直接配置API密钥\n")
    
    try:
        # 从环境变量创建配置
        config = TooBitConfig.from_env()
        print("✅ 从环境变量加载配置成功")
    except ValueError as e:
        print(f"❌ 环境变量配置失败: {e}")
        print("\n请设置以下环境变量:")
        print("export TOOBIT_API_KEY='your_api_key'")
        print("export TOOBIT_API_SECRET='your_api_secret'")
        return
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        print("\n💳 获取账户余额...")
        
        # 调用获取账户余额接口
        balance = client.get_balance()
        
        print("✅ 账户余额获取成功!")
        print()
        
        # 显示基本信息
        print("📋 余额概览:")
        print(f"   总资产种类: {len(balance)}")
        
        # 统计有余额的资产
        assets_with_balance = [b for b in balance if float(b['free']) > 0 or float(b['locked']) > 0]
        print(f"   有余额的资产: {len(assets_with_balance)}")
        print()
        
        # 显示所有有余额的资产
        if assets_with_balance:
            print("💰 资产余额详情:")
            
            # 按总余额排序
            assets_with_balance.sort(key=lambda x: float(x['free']) + float(x['locked']), reverse=True)
            
            for i, asset in enumerate(assets_with_balance):
                asset_name = asset['asset']
                free = float(asset['free'])
                locked = float(asset['locked'])
                total = free + locked
                
                print(f"   {i+1:2d}. {asset_name:<8}")
                print(f"       可用: {free:>15,.8f}")
                print(f"       冻结: {locked:>15,.8f}")
                print(f"       总计: {total:>15,.8f}")
                
                # 显示资产状态
                if locked > 0:
                    locked_percentage = (locked / total) * 100
                    print(f"       状态: ⚠️  有 {locked_percentage:.1f}% 资产被冻结")
                else:
                    print(f"       状态: ✅ 全部可用")
                
                # 显示资产类型判断
                if asset_name in ['USDT', 'USDC', 'BUSD', 'TUSD']:
                    asset_type = "稳定币"
                    type_emoji = "💵"
                elif asset_name in ['BTC', 'ETH', 'BNB']:
                    asset_type = "主流币"
                    type_emoji = "⭐"
                else:
                    asset_type = "其他币种"
                    type_emoji = "🪙"
                
                print(f"       类型: {type_emoji} {asset_type}")
                print()
            
            if len(assets_with_balance) > 20:
                print(f"   ... 还有 {len(assets_with_balance) - 20} 个资产有余额")
        else:
            print("   ℹ️  账户中没有资产余额")
        
        print("\n🎉 获取账户余额接口测试完成!")
        return balance
        
    except Exception as e:
        print(f"❌ 获取账户余额接口测试失败: {e}")
        print("\n可能的原因:")
        print("   - API密钥无效或过期")
        print("   - API密钥权限不足")
        print("   - 网络连接问题")
        print("   - 签名验证失败")
        return None
    
    finally:
        client.close()


def analyze_balance_distribution():
    """分析余额分布"""
    print("\n=== 余额分布分析 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("📊 分析余额分布...")
        
        # 获取账户余额
        balance = client.get_balance()
        
        # 统计有余额的资产
        assets_with_balance = [b for b in balance if float(b['free']) > 0 or float(b['locked']) > 0]
        
        if not assets_with_balance:
            print("   ℹ️  账户中没有资产余额")
            return
        
        # 按资产类型分类
        stable_coins = []
        major_coins = []
        other_coins = []
        
        for asset in assets_with_balance:
            asset_name = asset['asset']
            total = float(asset['free']) + float(asset['locked'])
            
            if asset_name in ['USDT', 'USDC', 'BUSD', 'TUSD']:
                stable_coins.append((asset_name, total))
            elif asset_name in ['BTC', 'ETH', 'BNB']:
                major_coins.append((asset_name, total))
            else:
                other_coins.append((asset_name, total))
        
        # 显示分类统计
        print("📈 资产分类统计:")
        print(f"   稳定币: {len(stable_coins)} 种")
        print(f"   主流币: {len(major_coins)} 种")
        print(f"   其他币: {len(other_coins)} 种")
        print()
        
        # 显示稳定币详情
        if stable_coins:
            print("💵 稳定币余额:")
            stable_coins.sort(key=lambda x: x[1], reverse=True)
            for name, amount in stable_coins:
                print(f"   {name:<6}: {amount:>15,.2f}")
            print()
        
        # 显示主流币详情
        if major_coins:
            print("⭐ 主流币余额:")
            major_coins.sort(key=lambda x: x[1], reverse=True)
            for name, amount in major_coins:
                print(f"   {name:<6}: {amount:>15,.8f}")
            print()
        
        # 显示其他币种详情
        if other_coins:
            print("🪙 其他币种余额 (前10个):")
            other_coins.sort(key=lambda x: x[1], reverse=True)
            for i, (name, amount) in enumerate(other_coins[:10]):
                print(f"   {i+1:2d}. {name:<8}: {amount:>15,.8f}")
            
            if len(other_coins) > 10:
                print(f"   ... 还有 {len(other_coins) - 10} 个其他币种")
            print()
        
        # 计算总价值 (简化计算，实际需要获取价格)
        print("💎 资产价值分析:")
        print("   (注: 以下计算基于假设价格，实际价值请查询实时价格)")
        
        # 假设价格 (实际使用时应该从API获取)
        assumed_prices = {
            'BTC': 50000, 'ETH': 3000, 'BNB': 300,
            'USDT': 1, 'USDC': 1, 'BUSD': 1, 'TUSD': 1
        }
        
        total_value_usdt = 0
        for asset in assets_with_balance:
            asset_name = asset['asset']
            total = float(asset['free']) + float(asset['locked'])
            
            if asset_name in assumed_prices:
                value_usdt = total * assumed_prices[asset_name]
                total_value_usdt += value_usdt
                print(f"   {asset_name:<6}: {total:>15,.8f} ≈ {value_usdt:>12,.2f} USDT")
            else:
                print(f"   {asset_name:<6}: {total:>15,.8f} ≈ {'未知':>12}")
        
        print(f"\n   总价值估算: {total_value_usdt:>12,.2f} USDT")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 余额分布分析失败: {e}")


def check_specific_asset_balance():
    """检查特定资产余额"""
    print("\n=== 特定资产余额检查 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 要检查的资产列表
        assets_to_check = ['BTC', 'ETH', 'USDT', 'BNB', 'ADA', 'DOT']
        
        print(f"🔍 检查 {len(assets_to_check)} 个特定资产的余额...")
        print()
        
        # 获取账户余额
        balance = client.get_balance()
        
        # 转换为字典便于查找
        balance_dict = {b['asset']: b for b in balance}
        
        for asset in assets_to_check:
            if asset in balance_dict:
                asset_info = balance_dict[asset]
                free = float(asset_info['free'])
                locked = float(asset_info['locked'])
                total = free + locked
                
                if total > 0:
                    print(f"✅ {asset}:")
                    print(f"   可用: {free:>15,.8f}")
                    print(f"   冻结: {locked:>15,.8f}")
                    print(f"   总计: {total:>15,.8f}")
                    
                    # 判断余额状态
                    if free == 0 and locked > 0:
                        status = "⚠️  全部冻结"
                    elif locked > 0:
                        status = "⚠️  部分冻结"
                    else:
                        status = "✅ 全部可用"
                    
                    print(f"   状态: {status}")
                else:
                    print(f"❌ {asset}: 无余额")
            else:
                print(f"❌ {asset}: 资产不存在")
            
            print()
        
        client.close()
        
    except Exception as e:
        print(f"❌ 特定资产余额检查失败: {e}")


def balance_monitoring_demo():
    """余额监控演示"""
    print("\n=== 余额监控演示 ===\n")
    
    print("📊 余额监控功能说明:")
    print("   1. 实时监控资产余额变化")
    print("   2. 设置余额预警阈值")
    print("   3. 跟踪冻结资产状态")
    print("   4. 生成余额变化报告")
    print()
    
    print("💡 监控建议:")
    print("   - 定期检查主要资产余额")
    print("   - 关注冻结资产的变化")
    print("   - 设置合理的预警阈值")
    print("   - 记录余额变化历史")
    print()
    
    print("🔧 实现方式:")
    print("   - 定时调用 get_balance() 接口")
    print("   - 比较前后余额变化")
    print("   - 记录变化日志")
    print("   - 发送预警通知")


if __name__ == "__main__":
    # 注意: 这个示例需要真实的API密钥才能执行
    # 请先设置你的API密钥，或者注释掉这些调用
    
    print("=== TooBit API SDK 获取账户余额接口示例 ===\n")
    print("⚠️  重要提醒: 此接口需要真实的API密钥!")
    print("⚠️  请确保在测试环境中验证，或使用小额测试\n")
    
    # 取消注释以下行来运行示例
    # get_balance()
    # analyze_balance_distribution()
    # check_specific_asset_balance()
    
    balance_monitoring_demo()
    
    print("\n💡 提示:")
    print("   取消注释相应的函数调用来运行实际的余额查询测试")
    print("   确保已设置正确的API密钥")
    print("   此接口可以获取账户中所有资产的详细余额信息") 