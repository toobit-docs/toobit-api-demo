"""
TooBit API SDK - 获取K线数据接口示例
获取不同时间周期的K线数据
"""

from open_api_sdk import TooBitClient, TooBitConfig
from datetime import datetime


def get_klines():
    """获取K线数据"""
    print("=== TooBit API 获取K线数据接口测试 ===\n")
    
    # 创建配置 (不需要真实的API密钥来测试连接)
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        symbol = "BTCUSDT"
        interval = "1h"  # 1小时K线
        limit = 24  # 获取24根K线
        
        print(f"📊 获取 {symbol} K线数据...")
        print(f"   时间周期: {interval}")
        print(f"   K线数量: {limit}")
        print()
        
        # 调用获取K线数据接口
        klines = client.get_klines(symbol, interval, limit)
        
        print("✅ K线数据获取成功!")
        print(f"   实际返回K线数: {len(klines)} 根")
        print()
        
        # 显示K线数据
        print("📈 K线数据详情:")
        for i, kline in enumerate(klines):
            # K线数据结构: [开盘时间, 开盘价, 最高价, 最低价, 收盘价, 成交量, 收盘时间, 成交额, 成交笔数, 主动买入成交量, 主动买入成交额]
            open_time = kline[0]
            open_price = float(kline[1])
            high_price = float(kline[2])
            low_price = float(kline[3])
            close_price = float(kline[4])
            volume = float(kline[5])
            close_time = kline[6]
            quote_volume = float(kline[7])
            trade_count = kline[8]
            
            # 转换时间
            open_time_str = datetime.fromtimestamp(open_time / 1000).strftime('%m-%d %H:%M')
            close_time_str = datetime.fromtimestamp(close_time / 1000).strftime('%m-%d %H:%M')
            
            # 计算涨跌幅
            price_change = close_price - open_price
            price_change_percent = (price_change / open_price) * 100
            
            # 判断涨跌
            if price_change > 0:
                change_emoji = "🟢"
                change_text = "上涨"
            elif price_change < 0:
                change_emoji = "🔴"
                change_text = "下跌"
            else:
                change_emoji = "⚪"
                change_text = "平盘"
            
            print(f"   {i+1:2d}. {change_emoji} {change_text}")
            print(f"       时间: {open_time_str} - {close_time_str}")
            print(f"       开盘: {open_price:>10,.2f} USDT")
            print(f"       最高: {high_price:>10,.2f} USDT")
            print(f"       最低: {low_price:>10,.2f} USDT")
            print(f"       收盘: {close_price:>10,.2f} USDT")
            print(f"       涨跌: {price_change:>+10,.2f} USDT ({price_change_percent:>+7.2f}%)")
            print(f"       成交量: {volume:>12.6f} BTC")
            print(f"       成交额: {quote_volume:>12.2f} USDT")
            print(f"       成交笔数: {trade_count}")
            print()
        
        # 统计分析
        print("📊 K线统计分析:")
        
        # 价格分析
        open_prices = [float(kline[1]) for kline in klines]
        high_prices = [float(kline[2]) for kline in klines]
        low_prices = [float(kline[3]) for kline in klines]
        close_prices = [float(kline[4]) for kline in klines]
        volumes = [float(kline[5]) for kline in klines]
        
        if close_prices:
            # 价格统计
            min_price = min(low_prices)
            max_price = max(high_prices)
            avg_price = sum(close_prices) / len(close_prices)
            
            print(f"   最低价格: {min_price:,.2f} USDT")
            print(f"   最高价格: {max_price:,.2f} USDT")
            print(f"   平均收盘价: {avg_price:,.2f} USDT")
            print(f"   价格区间: {((max_price - min_price) / avg_price * 100):,.2f}%")
            
            # 涨跌统计
            price_changes = [float(kline[4]) - float(kline[1]) for kline in klines]
            up_count = sum(1 for change in price_changes if change > 0)
            down_count = sum(1 for change in price_changes if change < 0)
            flat_count = sum(1 for change in price_changes if change == 0)
            
            print(f"   上涨K线: {up_count} 根")
            print(f"   下跌K线: {down_count} 根")
            print(f"   平盘K线: {flat_count} 根")
            
            # 成交量统计
            total_volume = sum(volumes)
            avg_volume = total_volume / len(volumes)
            max_volume = max(volumes)
            
            print(f"   总成交量: {total_volume:.6f} BTC")
            print(f"   平均成交量: {avg_volume:.6f} BTC")
            print(f"   最大成交量: {max_volume:.6f} BTC")
        
        print("\n🎉 获取K线数据接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 获取K线数据接口测试失败: {e}")
        return False
    
    finally:
        client.close()


def get_klines_multiple_intervals():
    """获取多个时间周期的K线数据"""
    print("\n=== 多时间周期K线数据对比 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        symbol = "BTCUSDT"
        intervals = ["1m", "5m", "15m", "1h", "4h", "1d"]
        limit = 10
        
        print(f"📊 获取 {symbol} 多个时间周期的K线数据...")
        print(f"   时间周期: {', '.join(intervals)}")
        print(f"   每个周期K线数: {limit}")
        print()
        
        for interval in intervals:
            try:
                print(f"🔍 {interval} 周期:")
                
                klines = client.get_klines(symbol, interval, limit)
                
                if klines:
                    # 计算平均价格
                    close_prices = [float(kline[4]) for kline in klines]
                    avg_price = sum(close_prices) / len(close_prices)
                    
                    # 计算总成交量
                    volumes = [float(kline[5]) for kline in klines]
                    total_volume = sum(volumes)
                    
                    # 计算涨跌
                    price_changes = [float(kline[4]) - float(kline[1]) for kline in klines]
                    up_count = sum(1 for change in price_changes if change > 0)
                    down_count = sum(1 for change in price_changes if change < 0)
                    
                    print(f"   平均价格: {avg_price:,.2f} USDT")
                    print(f"   总成交量: {total_volume:.6f} BTC")
                    print(f"   上涨: {up_count} 根, 下跌: {down_count} 根")
                else:
                    print("   ❌ 无法获取K线数据")
                
                print()
                
            except Exception as e:
                print(f"   ❌ 获取 {interval} 周期K线失败: {e}")
                print()
        
        print("🎉 多时间周期K线数据对比完成!")
        
    except Exception as e:
        print(f"❌ 多时间周期K线数据对比失败: {e}")
    
    finally:
        client.close()


if __name__ == "__main__":
    get_klines()
    get_klines_multiple_intervals() 