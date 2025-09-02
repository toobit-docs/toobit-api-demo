"""
TooBit 合约API SDK - 获取24小时价格变动示例
获取合约24小时价格变动统计 (无需API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_24hr_ticker():
    """获取24小时价格变动统计"""
    print("=== TooBit 合约API 获取24小时价格变动统计 ===\n")
    
    try:
        # 创建配置 (无需API密钥)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # 创建客户端
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        print(f"🔄 正在获取 {symbol} 的24小时价格变动统计...")
        
        # 获取24小时价格变动统计
        response = client.get_24hr_ticker(symbol)
        
        print("✅ 24小时价格变动统计获取成功!")
        print()
        
        # 显示基本信息
        print(f"🔍 调试信息: response类型={type(response)}, 长度={len(response) if response else 0}")
        
        if response and len(response) > 0:
            ticker = response[0]  # 获取第一个元素
            print(f"🔍 调试信息: ticker类型={type(ticker)}, ticker内容={ticker}")
            print(f"🔍 调试信息: ticker是否有s属性={hasattr(ticker, 's')}")
            
            if hasattr(ticker, 's'):
                print(f"📋 交易对: {ticker.s}")

            if hasattr(ticker, 'c'):
                print(f"💰 最新价格: {ticker.c}")

            if hasattr(ticker, 'o'):
                print(f"📈 开盘价格: {ticker.o}")

            if hasattr(ticker, 'h'):
                print(f"🔺 最高价格: {ticker.h}")

            if hasattr(ticker, 'l'):
                print(f"🔻 最低价格: {ticker.l}")

            if hasattr(ticker, 'v'):
                print(f"📊 成交量: {ticker.v}")

            if hasattr(ticker, 'pcp'):
                print(f"📈 24小时涨跌幅: {ticker.pcp}%")
        else:
            print("   ℹ️  未获取到数据")
        
        print("\n🎉 24小时价格变动统计获取完成!")
        return response
        
    except Exception as e:
        print(f"❌ 获取24小时价格变动统计失败: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit 合约API SDK 获取24小时价格变动示例 ===\n")
    print("💡 这个示例无需API密钥，可以直接运行")
    
    # 运行示例
    get_24hr_ticker()
