"""
TooBit 合约API SDK - 获取最近成交记录示例
获取合约最近成交记录 (无需API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_recent_trades():
    """获取最近成交记录"""
    print("=== TooBit 合约API 获取最近成交记录 ===\n")
    
    try:
        # 创建配置 (无需API密钥)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # 创建客户端
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        limit = 10  # 获取数量
        
        print(f"🔄 正在获取 {symbol} 的最近成交记录...")
        
        # 获取最近成交记录
        response = client.get_recent_trades(symbol, limit)
        
        print("✅ 最近成交记录获取成功!")
        print(f"   获取到 {len(response)} 笔成交")
        print()
        
        # 显示成交记录
        print("📊 最近成交记录:")
        for i, trade in enumerate(response):
            if hasattr(trade, 'price') and hasattr(trade, 'qty'):
                price = float(trade.price)
                qty = float(trade.qty)
                print(f"   {i+1:2d}. 价格: {price:>8.2f} | 数量: {qty:>8.4f}")
        
        print("\n🎉 最近成交记录获取完成!")
        return response
        
    except Exception as e:
        print(f"❌ 获取最近成交记录失败: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit 合约API SDK 获取最近成交记录示例 ===\n")
    print("💡 这个示例无需API密钥，可以直接运行")
    
    # 运行示例
    get_recent_trades()
