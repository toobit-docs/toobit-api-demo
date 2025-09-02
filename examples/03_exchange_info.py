"""
TooBit API SDK - 获取交易所信息接口示例
获取交易规则和交易对信息
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_exchange_info():
    """获取交易所信息"""
    print("=== TooBit API 获取交易所信息接口测试 ===\n")
    
    # 创建配置 (不需要真实的API密钥来测试连接)
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        print("🏢 获取交易所信息...")
        
        # 调用获取交易所信息接口
        exchange_info = client.get_exchange_info()
        
        print("✅ 交易所信息获取成功!")
        print()
        
        # 显示基本信息
        print("📊 基本信息:")
        print(f"   时区: {exchange_info.timezone}")
        print(f"   服务器时间: {exchange_info.server_time}")
        print(f"   交易对总数: {len(exchange_info.symbols)}")
        print()
        
        # 显示速率限制信息
        print("⚡ 速率限制:")
        if exchange_info.rate_limits:
            for i, limit in enumerate(exchange_info.rate_limits):
                print(f"   {i+1}. 类型: {limit.get('rateLimitType', 'N/A')}")
                print(f"      限制: {limit.get('limit', 'N/A')}")
                print(f"      间隔: {limit.get('interval', 'N/A')}")
                print(f"      计数: {limit.get('count', 'N/A')}")
                print()
        else:
            print("   暂无速率限制信息")
        
        # 显示交易所过滤器
        print("🔍 交易所过滤器:")
        if exchange_info.broker_filters:
            for i, filter_info in enumerate(exchange_info.broker_filters):
                print(f"   {i+1}. 类型: {filter_info.get('filterType', 'N/A')}")
                print(f"      参数: {filter_info}")
                print()
        else:
            print("   暂无交易所过滤器")
        
        # 显示前几个交易对信息
        print("📈 交易对信息 (前10个):")
        for i, symbol_info in enumerate(exchange_info.symbols[:10]):
            symbol = symbol_info.get('symbol', 'N/A')
            status = symbol_info.get('status', 'N/A')
            base_asset = symbol_info.get('baseAsset', 'N/A')
            quote_asset = symbol_info.get('quoteAsset', 'N/A')
            
            print(f"   {i+1}. {symbol}")
            print(f"      状态: {status}")
            print(f"      基础资产: {base_asset}")
            print(f"      计价资产: {quote_asset}")
            
            # 显示交易状态
            if status == 'TRADING':
                print(f"      ✅ 可交易")
            else:
                print(f"      ❌ 不可交易")
            print()
        
        if len(exchange_info.symbols) > 10:
            print(f"   ... 还有 {len(exchange_info.symbols) - 10} 个交易对")
        
        # 统计交易对状态
        trading_count = sum(1 for s in exchange_info.symbols if s.get('status') == 'TRADING')
        break_count = sum(1 for s in exchange_info.symbols if s.get('status') == 'BREAK')
        other_count = len(exchange_info.symbols) - trading_count - break_count
        
        print("📊 交易对状态统计:")
        print(f"   可交易: {trading_count} 个")
        print(f"   暂停交易: {break_count} 个")
        print(f"   其他状态: {other_count} 个")
        
        print("\n🎉 获取交易所信息接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 获取交易所信息接口测试失败: {e}")
        return False
    
    finally:
        client.close()


if __name__ == "__main__":
    get_exchange_info() 