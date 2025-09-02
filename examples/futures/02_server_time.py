"""
TooBit 合约API SDK - 获取服务器时间接口示例
获取服务器时间 (无需API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_server_time():
    """获取服务器时间"""
    print("=== TooBit 合约API 获取服务器时间 ===\n")
    
    try:
        # 创建配置 (无需API密钥)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # 创建客户端
        client = TooBitClient(config)
        
        print("🔄 正在获取服务器时间...")
        
        # 获取服务器时间
        response = client.get_server_time()
        
        print("✅ 服务器时间获取成功!")
        print(f"   服务器时间: {response}")
        
        print("\n🎉 服务器时间获取完成!")
        return response
        
    except Exception as e:
        print(f"❌ 获取服务器时间失败: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit 合约API SDK 获取服务器时间示例 ===\n")
    print("💡 这个示例无需API密钥，可以直接运行")
    
    # 运行示例
    get_server_time()
