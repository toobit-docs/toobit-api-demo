"""
TooBit API SDK - 获取24小时价格变动接口示例
获取24小时价格变动统计
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_24hr_ticker():
    """获取24小时价格变动"""
    print("=== TooBit API 获取24小时价格变动接口测试 ===\n")
    
    # 创建配置 (不需要真实的API密钥来测试连接)
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        symbol = "BTCUSDT"
        
        print(f"📊 获取 {symbol} 24小时价格变动...")
        print()
        
        # 调用获取24小时价格变动接口
        ticker = client.get_24hr_ticker(symbol)
        
        print("✅ 24小时价格变动获取成功!")
        print()
        
        # 显示基本信息
        print("📋 基本信息:")
        print(f"   交易对: {ticker.symbol}")
        print(f"   统计时间: {ticker.open_time} - {ticker.close_time}")
        print(f"   成交笔数: {ticker.count:,}")
        print()
        
        # 显示价格信息
        print("💰 价格信息:")
        print(f"   开盘价: {ticker.open_price:>12,.4f} USDT")
        print(f"   收盘价: {ticker.last_price:>12,.4f} USDT")
        print(f"   最高价: {ticker.high_price:>12,.4f} USDT")
        print(f"   最低价: {ticker.low_price:>12,.4f} USDT")
        print(f"   前收盘价: {ticker.prev_close_price:>10,.4f} USDT")
        print(f"   加权平均价: {ticker.weighted_avg_price:>8,.4f} USDT")
        print()
        
        # 显示价格变动
        print("📈 价格变动:")
        change_emoji = "🟢" if ticker.price_change >= 0 else "🔴"
        change_text = "上涨" if ticker.price_change >= 0 else "下跌"
        
        print(f"   {change_emoji} {change_text}")
        print(f"   价格变动: {ticker.price_change:>+12,.4f} USDT")
        print(f"   变动百分比: {ticker.price_change_percent:>+10.2f}%")
        
        # 判断涨跌幅度
        abs_change = abs(ticker.price_change_percent)
        if abs_change >= 10:
            volatility = "极高"
            volatility_emoji = "🔥"
        elif abs_change >= 5:
            volatility = "高"
            volatility_emoji = "⚡"
        elif abs_change >= 2:
            volatility = "中等"
            volatility_emoji = "📊"
        else:
            volatility = "低"
            volatility_emoji = "😴"
        
        print(f"   波动程度: {volatility_emoji} {volatility}")
        print()
        
        # 显示成交信息
        print("📊 成交信息:")
        print(f"   成交量: {ticker.volume:>15,.6f} BTC")
        print(f"   成交额: {ticker.quote_volume:>15,.2f} USDT")
        print(f"   最新成交量: {ticker.last_qty:>11,.6f} BTC")
        print()
        
        # 显示买卖盘信息
        print("💹 买卖盘信息:")
        print(f"   买一价: {ticker.bid_price:>12,.4f} USDT")
        print(f"   卖一价: {ticker.ask_price:>12,.4f} USDT")
        
        # 计算买卖价差
        spread = ticker.ask_price - ticker.bid_price
        spread_percentage = (spread / ticker.bid_price) * 100
        
        print(f"   价差: {spread:>14,.4f} USDT")
        print(f"   价差百分比: {spread_percentage:>10.4f}%")
        
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
        
        # 显示市场活跃度分析
        print("🔥 市场活跃度分析:")
        
        # 基于成交笔数判断活跃度
        if ticker.count >= 100000:
            activity = "极高"
            activity_emoji = "🔥"
        elif ticker.count >= 50000:
            activity = "高"
            activity_emoji = "⚡"
        elif ticker.count >= 10000:
            activity = "中等"
            activity_emoji = "📊"
        else:
            activity = "低"
            activity_emoji = "😴"
        
        print(f"   活跃度: {activity_emoji} {activity}")
        print(f"   平均每笔成交: {ticker.quote_volume / ticker.count:.2f} USDT")
        
        print("\n🎉 获取24小时价格变动接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 获取24小时价格变动接口测试失败: {e}")
        return False
    
    finally:
        client.close()


def get_24hr_ticker_multiple_symbols():
    """获取多个交易对的24小时价格变动"""
    print("\n=== 多交易对24小时价格变动对比 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOTUSDT"]
        
        print(f"📊 获取 {len(symbols)} 个交易对的24小时价格变动...")
        print()
        
        tickers_data = []
        
        for symbol in symbols:
            try:
                print(f"🔍 {symbol}:")
                
                ticker = client.get_24hr_ticker(symbol)
                tickers_data.append(ticker)
                
                # 判断涨跌
                change_emoji = "🟢" if ticker.price_change_percent >= 0 else "🔴"
                
                print(f"   {change_emoji} 价格: {ticker.last_price:,.4f}")
                print(f"   涨跌幅: {ticker.price_change_percent:+.2f}%")
                print(f"   成交量: {ticker.volume:,.2f}")
                print(f"   成交额: {ticker.quote_volume:,.0f} USDT")
                print()
                
            except Exception as e:
                print(f"   ❌ 获取 {symbol} 24小时数据失败: {e}")
                print()
        
        # 排行榜分析
        if tickers_data:
            print("🏆 涨跌幅排行榜:")
            
            # 按涨跌幅排序
            sorted_tickers = sorted(tickers_data, key=lambda x: x.price_change_percent, reverse=True)
            
            print("   📈 涨幅榜:")
            for i, ticker in enumerate(sorted_tickers[:3]):
                emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉"
                print(f"   {emoji} {ticker.symbol}: {ticker.price_change_percent:+.2f}%")
            
            print("\n   📉 跌幅榜:")
            for i, ticker in enumerate(sorted_tickers[-3:]):
                emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉"
                print(f"   {emoji} {ticker.symbol}: {ticker.price_change_percent:+.2f}%")
            
            # 成交量排行
            print("\n   💰 成交额排行:")
            volume_sorted = sorted(tickers_data, key=lambda x: x.quote_volume, reverse=True)
            for i, ticker in enumerate(volume_sorted[:3]):
                emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉"
                print(f"   {emoji} {ticker.symbol}: {ticker.quote_volume:,.0f} USDT")
        
        print("\n🎉 多交易对24小时价格变动对比完成!")
        
    except Exception as e:
        print(f"❌ 多交易对24小时价格变动对比失败: {e}")
    
    finally:
        client.close()


def get_all_24hr_tickers():
    """获取所有交易对的24小时价格变动"""
    print("\n=== 所有交易对24小时价格变动概览 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        print("📊 获取所有交易对的24小时价格变动...")
        
        # 获取所有交易对的24小时数据
        all_tickers = client.get_24hr_ticker()  # 不传symbol参数获取所有
        
        print(f"✅ 获取成功! 共 {len(all_tickers)} 个交易对")
        print()
        
        # 统计分析
        up_count = sum(1 for ticker in all_tickers if ticker.price_change_percent > 0)
        down_count = sum(1 for ticker in all_tickers if ticker.price_change_percent < 0)
        flat_count = sum(1 for ticker in all_tickers if ticker.price_change_percent == 0)
        
        print("📊 市场概况:")
        print(f"   上涨: {up_count} 个 ({up_count/len(all_tickers)*100:.1f}%)")
        print(f"   下跌: {down_count} 个 ({down_count/len(all_tickers)*100:.1f}%)")
        print(f"   平盘: {flat_count} 个 ({flat_count/len(all_tickers)*100:.1f}%)")
        
        # 市场情绪
        if up_count > down_count * 1.5:
            market_sentiment = "🟢 乐观"
        elif down_count > up_count * 1.5:
            market_sentiment = "🔴 悲观"
        else:
            market_sentiment = "⚪ 中性"
        
        print(f"   市场情绪: {market_sentiment}")
        print()
        
        # 极值分析
        max_gain_ticker = max(all_tickers, key=lambda x: x.price_change_percent)
        max_loss_ticker = min(all_tickers, key=lambda x: x.price_change_percent)
        max_volume_ticker = max(all_tickers, key=lambda x: x.quote_volume)
        
        print("🏆 市场极值:")
        print(f"   最大涨幅: {max_gain_ticker.symbol} {max_gain_ticker.price_change_percent:+.2f}%")
        print(f"   最大跌幅: {max_loss_ticker.symbol} {max_loss_ticker.price_change_percent:+.2f}%")
        print(f"   最大成交额: {max_volume_ticker.symbol} {max_volume_ticker.quote_volume:,.0f} USDT")
        
        print("\n🎉 所有交易对24小时价格变动概览完成!")
        
    except Exception as e:
        print(f"❌ 所有交易对24小时价格变动概览失败: {e}")
    
    finally:
        client.close()


if __name__ == "__main__":
    get_24hr_ticker()
    get_24hr_ticker_multiple_symbols()
    get_all_24hr_tickers() 