"""
TooBit 合约API SDK - 获取K线数据示例
获取合约K线数据 (无需API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_klines():
    """获取K线数据"""
    print("=== TooBit 合约API 获取K线数据 ===\n")
    
    try:
        # 创建配置 (无需API密钥)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # 创建客户端
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        interval = "1h"  # 时间间隔
        limit = 10  # 获取数量
        
        print(f"🔄 正在获取 {symbol} 的K线数据...")
        print(f"   时间间隔: {interval}")
        print(f"   数量: {limit}")
        print()
        
        # 获取K线数据
        response = client.get_klines(symbol, interval, limit)
        
        print("✅ K线数据获取成功!")
        print(f"   获取到 {len(response)} 根K线")
        print()
        
        # 显示K线数据
        print("📊 K线数据详情:")
        for i, kline in enumerate(response[-5:]):  # 显示最后5根K线
            if hasattr(kline, 'open') and hasattr(kline, 'high') and hasattr(kline, 'low') and hasattr(kline, 'close'):
                open_price = float(kline.open)
                high_price = float(kline.high)
                low_price = float(kline.low)
                close_price = float(kline.close)
                print(f"   {i+1:2d}. 开盘: {open_price:>8.2f} | 最高: {high_price:>8.2f} | 最低: {low_price:>8.2f} | 收盘: {close_price:>8.2f}")
        
        print("\n🎉 K线数据获取完成!")
        return response
        
    except Exception as e:
        print(f"❌ 获取K线数据失败: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit 合约API SDK 获取K线数据示例 ===\n")
    print("💡 这个示例无需API密钥，可以直接运行")
    
    # 运行示例
    get_klines()
