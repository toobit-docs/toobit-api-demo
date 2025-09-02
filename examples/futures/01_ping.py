"""
TooBit 合约API SDK - PING测试接口示例
测试服务器连通性 (无需API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def ping_test():
    """测试服务器连通性"""
    print("=== TooBit 合约API PING测试 ===\n")
    
    try:
        # 创建配置 (无需API密钥)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # 创建客户端
        client = TooBitClient(config)
        
        print("🔄 正在测试服务器连通性...")
        
        # 调用PING接口
        response = client.ping()
        
        print("✅ 服务器连通性测试成功!")
        print(f"   响应: {response}")
        print("\n🎉 PING测试完成!")
        
        return True
        
    except Exception as e:
        print(f"❌ 服务器连通性测试失败: {e}")
        return False
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit 合约API SDK PING测试示例 ===\n")
    print("💡 这个示例无需API密钥，可以直接运行")
    
    # 运行示例
    ping_test()
