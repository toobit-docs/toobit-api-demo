"""
TooBit API SDK - Ping接口示例
测试服务器连通性
"""

from open_api_sdk import TooBitClient, TooBitConfig


def test_ping():
    """测试ping接口"""
    print("=== TooBit API Ping接口测试 ===\n")
    
    # 创建配置 (不需要真实的API密钥来测试连接)
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        print("📡 测试服务器连通性...")
        
        # 调用ping接口
        if client.ping():
            print("✅ 服务器连接正常")
            print("   - 服务器响应成功")
            print("   - 网络连接正常")
            print("   - API服务可用")
        else:
            print("❌ 服务器连接失败")
            print("   - 可能原因:")
            print("     * 网络连接问题")
            print("     * 服务器暂时不可用")
            print("     * API地址配置错误")
            return False
        
        print("\n🎉 Ping接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ Ping接口测试失败: {e}")
        return False
    
    finally:
        client.close()


if __name__ == "__main__":
    test_ping() 