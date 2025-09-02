"""
TooBit 合约API SDK - 获取最优挂单示例
获取合约最优挂单信息 (无需API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_best_order_book():
    """获取最优挂单信息"""
    print("=== TooBit 合约API 获取最优挂单信息 ===\n")
    
    try:
        # 创建配置 (无需API密钥)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # 创建客户端
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        print(f"🔄 正在获取 {symbol} 的最优挂单信息...")
        
        # 获取最优挂单信息
        response = client.get_best_order_book(symbol)
        
        print("✅ 最优挂单信息获取成功!")
        print()
        
        # 显示基本信息
        if response and len(response) > 0:
            ticker = response[0]  # 获取第一个元素
            
            if 's' in ticker:
                print(f"📋 交易对: {ticker['s']}")
            
            if 't' in ticker:
                print(f"⏰ 时间: {ticker['t']}")
            
            # 显示买单信息
            if 'b' in ticker and 'bq' in ticker:
                print(f"\n📈 买单信息:")
                print(f"   价格: {ticker['b']} | 数量: {ticker['bq']}")
            
            # 显示卖单信息
            if 'a' in ticker and 'aq' in ticker:
                print(f"\n📉 卖单信息:")
                print(f"   价格: {ticker['a']} | 数量: {ticker['aq']}")
        else:
            print("   ℹ️  未获取到数据")
        
        print("\n🎉 最优挂单信息获取完成!")
        return response
        
    except Exception as e:
        print(f"❌ 获取最优挂单信息失败: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit 合约API SDK 获取最优挂单示例 ===\n")
    print("💡 这个示例无需API密钥，可以直接运行")
    
    # 运行示例
    get_best_order_book()
