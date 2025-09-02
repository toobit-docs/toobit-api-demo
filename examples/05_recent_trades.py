"""
TooBit API SDK - 获取最近成交接口示例
获取最近成交记录
"""

from open_api_sdk import TooBitClient, TooBitConfig
from datetime import datetime


def get_recent_trades():
    """获取最近成交记录"""
    print("=== TooBit API 获取最近成交接口测试 ===\n")
    
    # 创建配置 (不需要真实的API密钥来测试连接)
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        symbol = "BTCUSDT"
        limit = 20
        
        print(f"📊 获取 {symbol} 最近成交记录...")
        print(f"   记录数量: {limit} 条")
        print()
        
        # 调用获取最近成交接口
        trades = client.get_recent_trades(symbol, limit)
        
        print("✅ 最近成交记录获取成功!")
        print(f"   实际返回记录数: {len(trades)} 条")
        print()
        
        # 显示成交记录
        print("📝 最近成交记录:")
        for i, trade in enumerate(trades):
            trade_id = trade.get('id', 'N/A')
            price = trade.get('price', 0)
            quantity = trade.get('qty', 0)
            quote_qty = trade.get('quoteQty', 0)
            time = trade.get('time', 0)
            is_buyer_maker = trade.get('isBuyerMaker', False)
            
            # 转换时间戳
            time_str = datetime.fromtimestamp(time / 1000).strftime('%H:%M:%S')
            
            # 判断买卖方向
            side = "买入" if not is_buyer_maker else "卖出"
            side_emoji = "🟢" if not is_buyer_maker else "🔴"
            
            print(f"   {i+1:2d}. {side_emoji} {side}")
            print(f"       成交ID: {trade_id}")
            print(f"       价格: {price:>10,.2f} USDT")
            print(f"       数量: {quantity:>12.6f} BTC")
            print(f"       金额: {quote_qty:>12.2f} USDT")
            print(f"       时间: {time_str}")
            print()
        
        # 统计分析
        print("📊 成交统计分析:")
        
        # 价格分析
        prices = [float(trade.get('price', 0)) for trade in trades]
        if prices:
            min_price = min(prices)
            max_price = max(prices)
            avg_price = sum(prices) / len(prices)
            
            print(f"   最低价格: {min_price:,.2f} USDT")
            print(f"   最高价格: {max_price:,.2f} USDT")
            print(f"   平均价格: {avg_price:,.2f} USDT")
            print(f"   价格波动: {((max_price - min_price) / avg_price * 100):,.2f}%")
        
        # 数量分析
        quantities = [float(trade.get('qty', 0)) for trade in trades]
        if quantities:
            total_quantity = sum(quantities)
            avg_quantity = total_quantity / len(quantities)
            
            print(f"   总成交量: {total_quantity:.6f} BTC")
            print(f"   平均成交量: {avg_quantity:.6f} BTC")
        
        # 买卖方向分析
        buy_trades = [t for t in trades if not t.get('isBuyerMaker', False)]
        sell_trades = [t for t in trades if t.get('isBuyerMaker', False)]
        
        print(f"   买入成交: {len(buy_trades)} 笔")
        print(f"   卖出成交: {len(sell_trades)} 笔")
        
        # 计算买卖比例
        if trades:
            buy_ratio = len(buy_trades) / len(trades) * 100
            sell_ratio = len(sell_trades) / len(trades) * 100
            print(f"   买入比例: {buy_ratio:.1f}%")
            print(f"   卖出比例: {sell_ratio:.1f}%")
        
        print("\n🎉 获取最近成交接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 获取最近成交接口测试失败: {e}")
        return False
    
    finally:
        client.close()


def get_recent_trades_multiple_symbols():
    """获取多个交易对的最近成交记录"""
    print("\n=== 多交易对成交记录对比 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
        limit = 10
        
        print(f"📊 获取 {len(symbols)} 个交易对的最近成交记录...")
        print(f"   记录数量: {limit} 条")
        print()
        
        for symbol in symbols:
            try:
                print(f"🔍 {symbol}:")
                
                trades = client.get_recent_trades(symbol, limit)
                
                if trades:
                    # 计算平均价格
                    prices = [float(trade.get('price', 0)) for trade in trades]
                    avg_price = sum(prices) / len(prices)
                    
                    # 计算总成交量
                    quantities = [float(trade.get('qty', 0)) for trade in trades]
                    total_quantity = sum(quantities)
                    
                    # 统计买卖方向
                    buy_trades = [t for t in trades if not t.get('isBuyerMaker', False)]
                    sell_trades = [t for t in trades if t.get('isBuyerMaker', False)]
                    
                    print(f"   平均价格: {avg_price:,.4f}")
                    print(f"   总成交量: {total_quantity:.6f}")
                    print(f"   买入: {len(buy_trades)} 笔, 卖出: {len(sell_trades)} 笔")
                else:
                    print("   ❌ 无法获取成交记录")
                
                print()
                
            except Exception as e:
                print(f"   ❌ 获取 {symbol} 成交记录失败: {e}")
                print()
        
        print("🎉 多交易对成交记录对比完成!")
        
    except Exception as e:
        print(f"❌ 多交易对成交记录对比失败: {e}")
    
    finally:
        client.close()


if __name__ == "__main__":
    get_recent_trades()
    get_recent_trades_multiple_symbols() 