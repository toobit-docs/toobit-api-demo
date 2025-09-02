"""
TooBit 合约API SDK - 母子账户万能划转示例
母子账户万能划转 (需要API密钥和签名)
接口: POST /api/v1/futures/transfer
"""
from open_api_sdk import TooBitClient, TooBitConfig

def transfer_between_accounts():
    """母子账户万能划转"""
    print("=== TooBit 合约API 母子账户万能划转 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 划转参数
        from_account_type = "MAIN"  # 源账户类型: MAIN, FUTURES
        to_account_type = "FUTURES"  # 目标账户类型: MAIN, FUTURES
        asset = "USDT"  # 划转资产
        quantity = "100"  # 划转数量
        
        print("🔄 正在执行母子账户划转...")
        print(f"   源账户类型: {from_account_type}")
        print(f"   目标账户类型: {to_account_type}")
        print(f"   划转资产: {asset}")
        print(f"   划转数量: {quantity}")
        print()
        print("⚠️  注意: 这是真实的资金划转操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        response = client.transfer_between_accounts(
            from_account_type=from_account_type,
            to_account_type=to_account_type,
            asset=asset,
            quantity=quantity
        )
        
        print("✅ 账户划转成功!")
        print()
        
        # 根据实际API返回体结构处理响应
        if response and 'code' in response:
            if response['code'] == 200:
                print("🎉 划转操作成功!")
                if 'msg' in response:
                    print(f"📝 响应消息: {response['msg']}")
            else:
                print(f"⚠️  划转操作返回非成功状态码: {response['code']}")
                if 'msg' in response:
                    print(f"📝 响应消息: {response['msg']}")
        else:
            print("   ℹ️  未获取到有效的划转响应数据")
        
        print("\n🎉 账户划转完成!")
        return response
        
    except Exception as e:
        print(f"❌ 账户划转失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit 合约API SDK 母子账户万能划转示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的资金划转操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: POST /api/v1/futures/transfer")
    print("   - 鉴权: 需要签名 (TRADE)")
    print("   - 功能: 母子账户之间的资金划转")
    print("   - 支持: 主账户↔合约, 主账户↔主账户, 合约↔合约")
    print()
    print("⚠️  重要提醒:")
    print("   - 请确保账户余额充足")
    print("   - 请仔细核对划转参数")
    print("   - 划转操作不可逆")
    transfer_between_accounts()
