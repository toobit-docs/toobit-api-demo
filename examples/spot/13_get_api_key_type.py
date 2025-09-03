#!/usr/bin/env python3
"""
TooBit API 获取API KEY类型示例 (13号)
获取API KEY类型
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_api_key_type():
    """获取API KEY类型示例"""
    print("=== TooBit API 获取API KEY类型示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 获取API KEY类型测试:")
        print()
        print("   API: GET /api/v1/account/apiKeyType")
        print("   说明: 获取API KEY类型")
        print()
        
        api_key_type = client.get_api_key_type()
        print(f"   API Key类型: {api_key_type.accountType}")
        print()

        print("🎉 获取API KEY类型测试完成!")
        
    except Exception as e:
        print(f"❌ 获取API KEY类型测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_api_key_type()
