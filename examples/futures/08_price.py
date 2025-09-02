"""
TooBit 合约API SDK - 获取最新价格示例
获取合约最新价格 (无需API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_latest_price():
    """获取最新价格"""
    print("=== TooBit 合约API 获取最新价格 ===\n")
    
    try:
        # 创建配置 (无需API密钥)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # 创建客户端
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        print(f"🔄 正在获取 {symbol} 的最新价格...")
        
        # 获取最新价格
        response = client.get_latest_price(symbol)
        
        print("✅ 最新价格获取成功!")
        print()
        
        # 显示价格信息
        if response and len(response) > 0:
            ticker = response[0]  # 获取第一个元素

            if 's' in ticker:
                print(f"📋 交易对: {ticker['s']}")
            
            if 'p' in ticker:
                print(f"💰 最新价格: {ticker['p']}")
        else:
            print("   ℹ️  未获取到数据")
        
        print("\n🎉 最新价格获取完成!")
        return response
        
    except Exception as e:
        print(f"❌ 获取最新价格失败: {e}")
        return None
    
    finally:
        client.close()


def get_all_prices():
    """获取所有交易对的最新价格"""
    print("\n=== 获取所有交易对的最新价格 ===\n")
    
    try:
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        client = TooBitClient(config)
        
        print("🔄 正在获取所有交易对的最新价格...")
        
        # 获取所有交易对的最新价格
        response = client.get_all_prices()
        
        if response:
            print(f"✅ 获取到 {len(response)} 个交易对的最新价格")
            print()
            
            # 显示前10个交易对
            print("📊 前10个交易对价格:")
            for i, price_info in enumerate(response[:10]):
                if 's' in price_info and  'p' in price_info:
                    symbol = price_info['s']
                    price = price_info['p']
                    print(f"   {i+1:2d}. {symbol}: {price}")
        
        return response
        
    except Exception as e:
        print(f"❌ 获取所有价格失败: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit 合约API SDK 获取最新价格示例 ===\n")
    print("💡 这个示例无需API密钥，可以直接运行")
    
    # 运行示例
    get_latest_price()
    get_all_prices()

