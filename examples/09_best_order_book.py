"""
TooBit API SDK - 获取当前最优挂单接口示例
获取买一卖一价格和数量
"""

from open_api_sdk import TooBitClient, TooBitConfig
import time


def get_best_order_book():
    """获取当前最优挂单"""
    print("=== TooBit API 获取当前最优挂单接口测试 ===\n")
    
    # 创建配置 (不需要真实的API密钥来测试连接)
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        symbol = "BTCUSDT"
        
        print(f"💹 获取 {symbol} 当前最优挂单...")
        print()
        
        # 调用获取当前最优挂单接口
        best_order_book = client.get_best_order_book(symbol)
        
        print("✅ 当前最优挂单获取成功!")
        print()
        
        # 显示基本信息
        print("📋 基本信息:")
        print(f"   交易对: {best_order_book['symbol']}")
        print()
        
        # 显示买卖盘信息
        print("💹 最优挂单信息:")
        bid_price = float(best_order_book['bidPrice'])
        bid_qty = float(best_order_book['bidQty'])
        ask_price = float(best_order_book['askPrice'])
        ask_qty = float(best_order_book['askQty'])
        
        print(f"   🟢 买一价: {bid_price:>12,.4f} USDT")
        print(f"   🟢 买一量: {bid_qty:>12.6f} BTC")
        print(f"   🟢 买一金额: {bid_price * bid_qty:>10,.2f} USDT")
        print()
        print(f"   🔴 卖一价: {ask_price:>12,.4f} USDT")
        print(f"   🔴 卖一量: {ask_qty:>12.6f} BTC")
        print(f"   🔴 卖一金额: {ask_price * ask_qty:>10,.2f} USDT")
        print()
        
        # 计算价差分析
        print("📊 价差分析:")
        spread = ask_price - bid_price
        spread_percentage = (spread / bid_price) * 100
        mid_price = (bid_price + ask_price) / 2
        
        print(f"   价差: {spread:>14,.4f} USDT")
        print(f"   价差百分比: {spread_percentage:>10.4f}%")
        print(f"   中间价: {mid_price:>12,.4f} USDT")
        
        # 判断价差状态
        if spread_percentage < 0.01:
            spread_status = "优秀"
            spread_emoji = "✅"
        elif spread_percentage < 0.05:
            spread_status = "良好"
            spread_emoji = "✅"
        elif spread_percentage < 0.1:
            spread_status = "一般"
            spread_emoji = "⚠️"
        else:
            spread_status = "较差"
            spread_emoji = "❌"
        
        print(f"   价差状态: {spread_emoji} {spread_status}")
        print()
        
        # 流动性分析
        print("💧 流动性分析:")
        total_liquidity = (bid_price * bid_qty) + (ask_price * ask_qty)
        liquidity_imbalance = abs(bid_qty - ask_qty) / (bid_qty + ask_qty) * 100
        
        print(f"   买一流动性: {bid_price * bid_qty:>10,.2f} USDT")
        print(f"   卖一流动性: {ask_price * ask_qty:>10,.2f} USDT")
        print(f"   总流动性: {total_liquidity:>12,.2f} USDT")
        print(f"   流动性不平衡: {liquidity_imbalance:>8.2f}%")
        
        # 判断流动性状态
        if total_liquidity >= 100000:
            liquidity_status = "充足"
            liquidity_emoji = "✅"
        elif total_liquidity >= 50000:
            liquidity_status = "良好"
            liquidity_emoji = "✅"
        elif total_liquidity >= 10000:
            liquidity_status = "一般"
            liquidity_emoji = "⚠️"
        else:
            liquidity_status = "不足"
            liquidity_emoji = "❌"
        
        print(f"   流动性状态: {liquidity_emoji} {liquidity_status}")
        
        # 判断买卖不平衡
        if liquidity_imbalance < 10:
            balance_status = "平衡"
            balance_emoji = "✅"
        elif liquidity_imbalance < 30:
            balance_status = "轻微不平衡"
            balance_emoji = "⚠️"
        else:
            balance_status = "严重不平衡"
            balance_emoji = "❌"
        
        print(f"   买卖平衡: {balance_emoji} {balance_status}")
        
        print("\n🎉 获取当前最优挂单接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 获取当前最优挂单接口测试失败: {e}")
        return False
    
    finally:
        client.close()


def monitor_best_order_book():
    """监控最优挂单变化"""
    print("\n=== 最优挂单监控 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        symbol = "BTCUSDT"
        
        print(f"🔄 监控 {symbol} 最优挂单变化 (连续获取5次)...")
        print()
        
        previous_data = None
        
        for i in range(5):
            try:
                current_data = client.get_best_order_book(symbol)
                
                bid_price = float(current_data['bidPrice'])
                bid_qty = float(current_data['bidQty'])
                ask_price = float(current_data['askPrice'])
                ask_qty = float(current_data['askQty'])
                spread = ask_price - bid_price
                
                print(f"   {i+1}. 时间点 {i+1}:")
                print(f"      买一: {bid_price:,.4f} ({bid_qty:.6f})")
                print(f"      卖一: {ask_price:,.4f} ({ask_qty:.6f})")
                print(f"      价差: {spread:,.4f}")
                
                # 与上次对比
                if previous_data:
                    prev_bid = float(previous_data['bidPrice'])
                    prev_ask = float(previous_data['askPrice'])
                    
                    bid_change = bid_price - prev_bid
                    ask_change = ask_price - prev_ask
                    
                    bid_emoji = "🟢" if bid_change > 0 else "🔴" if bid_change < 0 else "⚪"
                    ask_emoji = "🟢" if ask_change > 0 else "🔴" if ask_change < 0 else "⚪"
                    
                    print(f"      变化: 买一{bid_emoji}({bid_change:+.4f}) 卖一{ask_emoji}({ask_change:+.4f})")
                
                print()
                
                previous_data = current_data
                
                if i < 4:  # 最后一次不等待
                    time.sleep(3)  # 等待3秒
                    
            except Exception as e:
                print(f"   {i+1}. ❌ 获取失败: {e}")
                print()
        
        print("🎉 最优挂单监控完成!")
        
    except Exception as e:
        print(f"❌ 最优挂单监控失败: {e}")
    
    finally:
        client.close()


def compare_best_order_books():
    """对比多个交易对的最优挂单"""
    print("\n=== 多交易对最优挂单对比 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOTUSDT"]
        
        print(f"💹 获取 {len(symbols)} 个交易对的最优挂单...")
        print()
        
        order_books_data = []
        
        for symbol in symbols:
            try:
                print(f"🔍 {symbol}:")
                
                best_order_book = client.get_best_order_book(symbol)
                
                bid_price = float(best_order_book['bidPrice'])
                bid_qty = float(best_order_book['bidQty'])
                ask_price = float(best_order_book['askPrice'])
                ask_qty = float(best_order_book['askQty'])
                spread = ask_price - bid_price
                spread_percentage = (spread / bid_price) * 100
                
                order_books_data.append({
                    'symbol': symbol,
                    'bid_price': bid_price,
                    'ask_price': ask_price,
                    'spread': spread,
                    'spread_percentage': spread_percentage,
                    'liquidity': (bid_price * bid_qty) + (ask_price * ask_qty)
                })
                
                print(f"   买一: {bid_price:,.4f} ({bid_qty:.6f})")
                print(f"   卖一: {ask_price:,.4f} ({ask_qty:.6f})")
                print(f"   价差: {spread:,.4f} ({spread_percentage:.4f}%)")
                print()
                
            except Exception as e:
                print(f"   ❌ 获取 {symbol} 最优挂单失败: {e}")
                print()
        
        # 排行榜分析
        if order_books_data:
            print("🏆 价差排行榜 (价差越小越好):")
            
            # 按价差百分比排序
            sorted_by_spread = sorted(order_books_data, key=lambda x: x['spread_percentage'])
            
            for i, data in enumerate(sorted_by_spread):
                emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "🏅"
                print(f"   {emoji} {data['symbol']}: {data['spread_percentage']:.4f}%")
            
            print("\n🏆 流动性排行榜:")
            
            # 按流动性排序
            sorted_by_liquidity = sorted(order_books_data, key=lambda x: x['liquidity'], reverse=True)
            
            for i, data in enumerate(sorted_by_liquidity):
                emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "🏅"
                print(f"   {emoji} {data['symbol']}: {data['liquidity']:,.0f} USDT")
        
        print("\n🎉 多交易对最优挂单对比完成!")
        
    except Exception as e:
        print(f"❌ 多交易对最优挂单对比失败: {e}")
    
    finally:
        client.close()


def arbitrage_opportunity_analysis():
    """套利机会分析"""
    print("\n=== 套利机会分析 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        # 分析相关交易对的套利机会
        base_symbols = ["BTCUSDT", "ETHUSDT"]
        
        print("🔍 分析套利机会...")
        print()
        
        for symbol in base_symbols:
            try:
                best_order_book = client.get_best_order_book(symbol)
                
                bid_price = float(best_order_book['bidPrice'])
                ask_price = float(best_order_book['askPrice'])
                spread = ask_price - bid_price
                spread_percentage = (spread / bid_price) * 100
                
                print(f"📊 {symbol}:")
                print(f"   买一价: {bid_price:,.4f}")
                print(f"   卖一价: {ask_price:,.4f}")
                print(f"   价差: {spread:,.4f} ({spread_percentage:.4f}%)")
                
                # 简单的套利机会判断
                if spread_percentage > 0.1:
                    opportunity = "高"
                    emoji = "🔥"
                elif spread_percentage > 0.05:
                    opportunity = "中"
                    emoji = "⚡"
                else:
                    opportunity = "低"
                    emoji = "😴"
                
                print(f"   套利机会: {emoji} {opportunity}")
                print()
                
            except Exception as e:
                print(f"   ❌ 分析 {symbol} 失败: {e}")
                print()
        
        print("💡 套利提示:")
        print("   - 价差大于0.1%可能存在套利机会")
        print("   - 需要考虑交易手续费和滑点")
        print("   - 实际套利需要快速执行")
        print("   - 风险自负，仅供参考")
        
        print("\n🎉 套利机会分析完成!")
        
    except Exception as e:
        print(f"❌ 套利机会分析失败: {e}")
    
    finally:
        client.close()


if __name__ == "__main__":
    get_best_order_book()
    monitor_best_order_book()
    compare_best_order_books()
    arbitrage_opportunity_analysis() 