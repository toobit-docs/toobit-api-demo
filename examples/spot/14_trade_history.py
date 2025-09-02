"""
TooBit API SDK - 查询交易历史接口示例 (14)
查询交易历史 (需要API密钥)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_trade_history():
    """查询交易历史"""
    print("=== TooBit API 查询交易历史 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"  # 交易对
        
        print("🔄 正在查询交易历史...")
        print(f"   交易对: {symbol}")
        print()
        print("⚠️  注意: 这是真实的账户查询操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 调用查询交易历史接口
        trades = client.get_trade_history(symbol)
        
        print("✅ 交易历史查询成功!")
        print()
        
        # 显示交易信息
        if trades and len(trades) > 0:
            print(f"📊 交易历史信息 (共{len(trades)}条):")
            for i, trade in enumerate(trades[:5]):  # 只显示前5条
                print(f"\n   交易 {i+1}:")
                print(f"     🆔 交易ID: {trade.id}")
                print(f"     🆔 订单ID: {trade.order_id}")
                print(f"     📊 交易对: {trade.symbol}")
                print(f"     💰 价格: {trade.price}")
                print(f"     📊 数量: {trade.qty}")
                print(f"     💰 成交金额: {trade.quote_qty}")
                print(f"     📈 买卖方向: {trade.side}")
                print(f"     🕐 交易时间: {trade.time}")
            
            if len(trades) > 5:
                print(f"\n   ... 还有 {len(trades) - 5} 条交易记录")
        else:
            print("   ℹ️  没有找到交易记录")
        
        print("\n🎉 查询交易历史完成!")
        return trades
        
    except Exception as e:
        print(f"❌ 查询交易历史失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 查询交易历史示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的账户查询操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: GET /api/v1/spot/myTrades")
    print("   - 鉴权: 需要签名 (USER_DATA)")
    print("   - 功能: 查询交易历史")
    print("   - 参数: symbol")
    print()
    print("⚠️  重要提醒:")
    print("   - 建议先在测试环境中验证")
    print()
    
    get_trade_history()