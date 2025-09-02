"""
TooBit 合约API SDK - 获取交易规则和交易对信息示例
获取合约交易规则、交易对列表等 (无需API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_exchange_info():
    """获取交易所信息"""
    print("=== TooBit 合约API 获取交易所信息 ===\n")
    
    try:
        # 创建配置 (无需API密钥)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # 创建客户端
        client = TooBitClient(config)
        
        print("🔄 正在获取交易所信息...")
        
        # 获取交易所信息
        response = client.get_exchange_info()
        
        print("✅ 交易所信息获取成功!")
        
        # 显示基本信息
        if hasattr(response, 'timezone'):
            print(f"   时区: {response.timezone}")
        
        if hasattr(response, 'serverTime'):
            print(f"   服务器时间: {response.serverTime}")
        
        if hasattr(response, 'rateLimits'):
            print(f"   速率限制数量: {len(response.rateLimits) if response.rateLimits else 0}")
        
        if hasattr(response, 'symbols'):
            print(f"   交易对数量: {len(response.symbols) if response.symbols else 0}")
        
        print("\n🎉 交易所信息获取完成!")
        return response
        
    except Exception as e:
        print(f"❌ 获取交易所信息失败: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit 合约API SDK 获取交易所信息示例 ===\n")
    print("💡 这个示例无需API密钥，可以直接运行")
    
    # 运行示例
    get_exchange_info()
