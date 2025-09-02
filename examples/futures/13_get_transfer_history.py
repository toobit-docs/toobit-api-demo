"""
TooBit 合约API SDK - 获取划转历史示例 (13)
获取划转历史记录 (需要API密钥和签名)
接口: GET /api/v1/futures/transfer/history
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_transfer_history():
    """获取划转历史"""
    print("=== TooBit 合约API 获取划转历史 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 查询参数
        asset = "USDT"  # 资产类型 (可选)
        from_account_type = "MAIN"  # 源账户类型 (可选)
        to_account_type = "FUTURES"  # 目标账户类型 (可选)
        limit = 10  # 返回数量限制
        
        print("🔄 正在获取划转历史...")
        print(f"   资产类型: {asset}")
        print(f"   源账户类型: {from_account_type}")
        print(f"   目标账户类型: {to_account_type}")
        print(f"   返回数量: {limit}")
        print()
        print("⚠️  注意: 这是真实的账户查询操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        response = client.get_transfer_history(
            asset=asset,
            from_account_type=from_account_type,
            to_account_type=to_account_type,
            limit=limit
        )
        
        print("✅ 划转历史获取成功!")
        print()
        
        # 根据实际API返回体结构处理响应
        if response and len(response) > 0:
            print(f"📊 划转历史记录 (共{len(response)}条):")
            for i, record in enumerate(response):
                print(f"\n   记录 {i+1}:")
                if 'id' in record:
                    print(f"     🆔 流水ID: {record['id']}")
                if 'accountId' in record:
                    print(f"     👤 账户ID: {record['accountId']}")
                if 'coin' in record:
                    print(f"     🪙 币种: {record['coin']}")
                if 'coinName' in record:
                    print(f"     📝 币种名称: {record['coinName']}")
                if 'flowTypeValue' in record:
                    print(f"     🔢 流水类型值: {record['flowTypeValue']}")
                if 'flowType' in record:
                    print(f"     📋 流水类型: {record['flowType']}")
                if 'flowName' in record:
                    print(f"     📖 流水说明: {record['flowName']}")
                if 'change' in record:
                    print(f"     📊 变动值: {record['change']}")
                if 'total' in record:
                    print(f"     💰 变动后总资产: {record['total']}")
                if 'created' in record:
                    print(f"     ⏰ 创建时间: {record['created']}")
        else:
            print("   ℹ️  未获取到划转历史数据")
        
        print("\n🎉 划转历史获取完成!")
        return response
        
    except Exception as e:
        print(f"❌ 获取划转历史失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit 合约API SDK 获取划转历史示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的账户查询操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: GET /api/v1/account/balanceFlow")
    print("   - 鉴权: 需要签名 (USER_DATA)")
    print("   - 功能: 查询账户划转历史记录")
    print("   - 参数: asset(可选), fromAccountType(可选), toAccountType(可选), limit")
    print()
    print("💡 查询说明:")
    print("   - 可以按资产类型筛选")
    print("   - 可以按账户类型筛选")
    print("   - 支持分页查询")
    print("   - 返回最近的划转记录")
    get_transfer_history()
