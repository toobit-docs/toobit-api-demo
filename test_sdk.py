#!/usr/bin/env python3
"""
TooBit API SDK 简单测试
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from open_api_sdk import TooBitClient, TooBitConfig


def test_public_apis():
    """测试公开API接口"""
    print("=== 测试公开API接口 ===")
    
    # 创建配置 (不需要API密钥)
    config = TooBitConfig(
        api_key="test",
        api_secret="test",
        base_url="https://api.toobit.com"
    )
    
    client = TooBitClient(config)
    
    try:
        # 测试连接
        print("1. 测试服务器连接...")
        if client.ping():
            print("   ✅ 服务器连接正常")
        else:
            print("   ❌ 服务器连接失败")
            return False
        
        # 获取服务器时间
        print("2. 获取服务器时间...")
        server_time = client.get_server_time()
        print(f"   ✅ 服务器时间: {server_time}")
        
        # 获取交易所信息
        print("3. 获取交易所信息...")
        exchange_info = client.get_exchange_info()
        print(f"   ✅ 时区: {exchange_info.timezone}")
        print(f"   ✅ 交易对数量: {len(exchange_info.symbols)}")
        
        # 获取价格信息
        print("4. 获取BTC/USDT价格...")
        try:
            price_info = client.get_price("BTCUSDT")
            print(f"   ✅ BTC/USDT 价格: {price_info['price']}")
        except Exception as e:
            print(f"   ⚠️  获取价格失败: {e}")
        
        # 获取深度信息
        print("5. 获取深度信息...")
        try:
            order_book = client.get_order_book("BTCUSDT", limit=3)
            print(f"   ✅ 买单前3档: {len(order_book.bids)}")
            print(f"   ✅ 卖单前3档: {len(order_book.asks)}")
        except Exception as e:
            print(f"   ⚠️  获取深度信息失败: {e}")
        
        print("\n✅ 公开API接口测试完成!")
        return True
        
    except Exception as e:
        print(f"   ❌ 测试失败: {e}")
        return False
    
    finally:
        client.close()


def test_config_validation():
    """测试配置验证"""
    print("\n=== 测试配置验证 ===")
    
    try:
        # 测试空配置
        print("1. 测试空配置...")
        try:
            config = TooBitConfig(api_key="", api_secret="")
            config.validate()
            print("   ❌ 应该抛出异常")
            return False
        except ValueError:
            print("   ✅ 正确抛出异常")
        
        # 测试有效配置
        print("2. 测试有效配置...")
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        config.validate()
        print("   ✅ 配置验证通过")
        
        # 测试环境变量配置
        print("3. 测试环境变量配置...")
        try:
            config = TooBitConfig.from_env()
            print("   ✅ 环境变量配置加载成功")
        except ValueError:
            print("   ⚠️  环境变量配置未设置 (这是正常的)")
        
        print("\n✅ 配置验证测试完成!")
        return True
        
    except Exception as e:
        print(f"   ❌ 测试失败: {e}")
        return False


def main():
    """主测试函数"""
    print("🚀 TooBit API SDK 测试开始\n")
    
    # 测试配置验证
    config_test_passed = test_config_validation()
    
    # 测试公开API
    api_test_passed = test_public_apis()
    
    # 输出测试结果
    print("\n" + "="*50)
    print("📊 测试结果汇总:")
    print(f"   配置验证: {'✅ 通过' if config_test_passed else '❌ 失败'}")
    print(f"   公开API: {'✅ 通过' if api_test_passed else '❌ 失败'}")
    
    if config_test_passed and api_test_passed:
        print("\n🎉 所有测试通过! SDK基本功能正常。")
        print("\n💡 下一步:")
        print("   1. 设置你的API密钥 (复制 config.example 为 .env)")
        print("   2. 运行 examples/basic_usage.py 进行完整测试")
        print("   3. 查看 README.md 了解详细使用方法")
    else:
        print("\n⚠️  部分测试失败，请检查网络连接和配置。")
    
    print("="*50)


if __name__ == "__main__":
    main() 