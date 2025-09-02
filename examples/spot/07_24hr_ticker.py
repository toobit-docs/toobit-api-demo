"""
TooBit API SDK - 获取24小时价格变动接口示例 (07)
获取24小时价格变动统计
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_24hr_ticker():
    """获取24小时价格变动"""
    print("=== TooBit API 获取24小时价格变动 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        print("🔄 正在获取24小时价格变动...")
        print(f"   交易对: {symbol}")
        print()
        print("⚠️  注意: 这是真实的API调用，请确保配置正确")
        print()
        
        ticker = client.get_24hr_ticker(symbol)
        
        print("✅ 24小时价格变动获取成功!")
        print()
        
        # 显示基本信息
        print("📋 基本信息:")
        print(f"   交易对: {ticker.symbol}")
        print(f"   最新价格: {ticker.last_price}")
        print(f"   24h涨跌幅: {ticker.price_change_percent}%")
        print(f"   24h成交量: {ticker.volume}")
        print(f"   24h成交额: {ticker.quote_volume}")
        
        print("\n🎉 获取24小时价格变动完成!")
        return ticker
        
    except Exception as e:
        print(f"❌ 获取24小时价格变动失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 获取24小时价格变动示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的API调用，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: GET /quote/v1/ticker/24hr")
    print("   - 鉴权: 不需要签名")
    print("   - 功能: 获取24小时价格变动统计")
    print("   - 参数: symbol")
    print()
    print("⚠️  重要提醒:")
    print("   - 建议先在测试环境中验证")
    print()
    
    get_24hr_ticker() 