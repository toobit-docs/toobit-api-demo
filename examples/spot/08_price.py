"""
TooBit API SDK - 获取最新价格接口示例
获取单个或多个交易对的最新价格
"""

from open_api_sdk import TooBitClient, TooBitConfig
import time


def get_price():
    """获取最新价格"""
    print("=== TooBit API 获取最新价格接口测试 ===\n")
    
    # 创建配置 (不需要真实的API密钥来测试连接)
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        symbol = "BTCUSDT"
        
        print(f"💰 获取 {symbol} 最新价格...")
        print()
        
        # 调用获取最新价格接口
        price_info = client.get_price(symbol)
        
        print("✅ 最新价格获取成功!")
        print()
        
        # 显示价格信息
        print("📋 价格信息:")
        print(f"   交易对: {price_info['symbol']}")
        print(f"   最新价格: {float(price_info['price']):,.4f} USDT")
        print()
        
        # 多次获取价格，观察变化
        print("🔄 价格监控 (连续获取5次):")
        prices = []
        
        for i in range(5):
            try:
                current_price_info = client.get_price(symbol)
                current_price = float(current_price_info['price'])
                prices.append(current_price)
                
                # 与第一次价格对比
                if i > 0:
                    price_diff = current_price - prices[0]
                    price_diff_percent = (price_diff / prices[0]) * 100
                    
                    if price_diff > 0:
                        change_emoji = "🟢"
                        change_text = "上涨"
                    elif price_diff < 0:
                        change_emoji = "🔴"
                        change_text = "下跌"
                    else:
                        change_emoji = "⚪"
                        change_text = "不变"
                    
                    print(f"   {i+1}. {current_price:,.4f} USDT {change_emoji} {change_text} "
                          f"({price_diff:+.4f}, {price_diff_percent:+.4f}%)")
                else:
                    print(f"   {i+1}. {current_price:,.4f} USDT (基准价格)")
                
                if i < 4:  # 最后一次不等待
                    time.sleep(2)  # 等待2秒
                    
            except Exception as e:
                print(f"   {i+1}. ❌ 获取失败: {e}")
        
        # 价格变化分析
        if len(prices) > 1:
            print("\n📊 价格变化分析:")
            min_price = min(prices)
            max_price = max(prices)
            avg_price = sum(prices) / len(prices)
            price_range = max_price - min_price
            
            print(f"   最低价: {min_price:,.4f} USDT")
            print(f"   最高价: {max_price:,.4f} USDT")
            print(f"   平均价: {avg_price:,.4f} USDT")
            print(f"   价格区间: {price_range:,.4f} USDT")
            print(f"   波动率: {(price_range / avg_price * 100):.4f}%")
        
        print("\n🎉 获取最新价格接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 获取最新价格接口测试失败: {e}")
        return False
    
    finally:
        client.close()


def get_multiple_prices():
    """获取多个交易对的最新价格"""
    print("\n=== 多交易对最新价格对比 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOTUSDT"]
        
        print(f"💰 获取 {len(symbols)} 个交易对的最新价格...")
        print()
        
        prices_data = []
        
        for symbol in symbols:
            try:
                print(f"🔍 {symbol}:")
                
                price_info = client.get_price(symbol)
                price = float(price_info['price'])
                prices_data.append({
                    'symbol': symbol,
                    'price': price
                })
                
                print(f"   💰 价格: {price:,.4f}")
                print()
                
            except Exception as e:
                print(f"   ❌ 获取 {symbol} 价格失败: {e}")
                print()
        
        # 价格排行
        if prices_data:
            print("🏆 价格排行榜:")
            
            # 按价格排序
            sorted_prices = sorted(prices_data, key=lambda x: x['price'], reverse=True)
            
            for i, data in enumerate(sorted_prices):
                emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "🏅"
                print(f"   {emoji} {data['symbol']}: {data['price']:,.4f}")
        
        print("\n🎉 多交易对最新价格对比完成!")
        
    except Exception as e:
        print(f"❌ 多交易对最新价格对比失败: {e}")
    
    finally:
        client.close()


def get_all_prices():
    """获取所有交易对的最新价格"""
    print("\n=== 所有交易对最新价格概览 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        print("💰 获取所有交易对的最新价格...")
        
        # 获取所有交易对的价格
        all_prices = client.get_price()  # 不传symbol参数获取所有
        
        print(f"✅ 获取成功! 共 {len(all_prices)} 个交易对")
        print()
        
        # 转换为数值并排序
        price_data = []
        for price_info in all_prices:
            try:
                symbol = price_info['symbol']
                price = float(price_info['price'])
                price_data.append({
                    'symbol': symbol,
                    'price': price
                })
            except:
                continue
        
        # 价格统计
        if price_data:
            prices = [data['price'] for data in price_data]
            
            print("📊 价格统计:")
            print(f"   最高价格: {max(prices):,.4f}")
            print(f"   最低价格: {min(prices):,.8f}")
            print(f"   平均价格: {sum(prices)/len(prices):,.4f}")
            print()
            
            # 价格区间分布
            high_price_count = sum(1 for p in prices if p >= 1000)
            mid_price_count = sum(1 for p in prices if 1 <= p < 1000)
            low_price_count = sum(1 for p in prices if p < 1)
            
            print("📈 价格区间分布:")
            print(f"   高价区 (≥1000): {high_price_count} 个")
            print(f"   中价区 (1-1000): {mid_price_count} 个")
            print(f"   低价区 (<1): {low_price_count} 个")
            print()
            
            # 显示价格最高的前10个
            print("🏆 价格最高的前10个交易对:")
            sorted_by_price = sorted(price_data, key=lambda x: x['price'], reverse=True)
            for i, data in enumerate(sorted_by_price[:10]):
                print(f"   {i+1:2d}. {data['symbol']:<12} {data['price']:>15,.4f}")
            
            print()
            
            # 显示一些特定的交易对价格
            popular_symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOTUSDT"]
            print("⭐ 热门交易对价格:")
            for symbol in popular_symbols:
                for data in price_data:
                    if data['symbol'] == symbol:
                        print(f"   {symbol:<12} {data['price']:>15,.4f}")
                        break
                else:
                    print(f"   {symbol:<12} {'未找到':>15}")
        
        print("\n🎉 所有交易对最新价格概览完成!")
        
    except Exception as e:
        print(f"❌ 所有交易对最新价格概览失败: {e}")
    
    finally:
        client.close()


def price_comparison_analysis():
    """价格对比分析"""
    print("\n=== 价格对比分析 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        # 主要加密货币对比
        major_cryptos = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
        
        print("🔍 主要加密货币价格对比:")
        
        crypto_prices = {}
        for symbol in major_cryptos:
            try:
                price_info = client.get_price(symbol)
                price = float(price_info['price'])
                crypto_prices[symbol] = price
                
                # 简化显示
                crypto_name = symbol.replace("USDT", "")
                print(f"   {crypto_name:<5} {price:>12,.2f} USDT")
                
            except Exception as e:
                print(f"   {symbol} ❌ 获取失败: {e}")
        
        # 计算比值
        if "BTCUSDT" in crypto_prices and "ETHUSDT" in crypto_prices:
            eth_btc_ratio = crypto_prices["ETHUSDT"] / crypto_prices["BTCUSDT"]
            print(f"\n📊 ETH/BTC 比值: {eth_btc_ratio:.6f}")
            
            # 判断ETH相对BTC的强弱
            if eth_btc_ratio > 0.08:
                strength = "强势"
                emoji = "🟢"
            elif eth_btc_ratio > 0.06:
                strength = "中性"
                emoji = "⚪"
            else:
                strength = "弱势"
                emoji = "🔴"
            
            print(f"   ETH相对BTC: {emoji} {strength}")
        
        print("\n🎉 价格对比分析完成!")
        
    except Exception as e:
        print(f"❌ 价格对比分析失败: {e}")
    
    finally:
        client.close()


if __name__ == "__main__":
    get_price()
    get_multiple_prices()
    get_all_prices()
    price_comparison_analysis() 