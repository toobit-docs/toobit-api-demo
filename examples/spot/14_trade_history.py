"""
TooBit API SDK - 获取成交历史接口示例
获取账户的成交记录 (需要API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig
from datetime import datetime, timedelta


def get_trade_history():
    """获取成交历史"""
    print("=== TooBit API 获取成交历史接口测试 ===\n")
    
    # 注意: 这个示例需要真实的API密钥
    print("⚠️  注意: 此示例需要真实的API密钥才能运行")
    print("请先设置环境变量或直接配置API密钥\n")
    
    try:
        # 从环境变量创建配置
        config = TooBitConfig.from_env()
        print("✅ 从环境变量加载配置成功")
    except ValueError as e:
        print(f"❌ 环境变量配置失败: {e}")
        print("\n请设置以下环境变量:")
        print("export TOOBIT_API_KEY='your_api_key'")
        print("export TOOBIT_API_SECRET='your_api_secret'")
        return
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        symbol = "BTCUSDT"
        print(f"\n📊 获取 {symbol} 的成交历史...")
        
        # 调用获取成交历史接口
        trades = client.get_trade_history(symbol)
        
        print("✅ 成交历史获取成功!")
        print()
        
        # 显示基本信息
        print("📋 成交概览:")
        print(f"   总成交数量: {len(trades)}")
        
        if not trades:
            print(f"   ℹ️  {symbol} 没有成交记录")
            return trades
        
        # 按买卖方向分组统计
        buy_trades = [t for t in trades if t.is_buyer]
        sell_trades = [t for t in trades if not t.is_buyer]
        
        print(f"   买入成交: {len(buy_trades)} 笔")
        print(f"   卖出成交: {len(sell_trades)} 笔")
        print()
        
        # 计算成交统计
        total_qty = sum(t.qty for t in trades)
        total_quote_qty = sum(t.quote_qty for t in trades)
        total_commission = sum(t.commission for t in trades)
        
        print("💰 成交统计:")
        print(f"   总成交数量: {total_qty:.6f} BTC")
        print(f"   总成交金额: {total_quote_qty:,.2f} USDT")
        print(f"   总手续费: {total_commission:.6f}")
        
        # 计算平均成交价
        if total_qty > 0:
            avg_price = total_quote_qty / total_qty
            print(f"   平均成交价: {avg_price:,.2f} USDT")
        print()
        
        # 显示最近的成交详情
        print("📋 最近成交详情 (前10笔):")
        
        # 按时间排序，最新的在前
        trades.sort(key=lambda x: x.time, reverse=True)
        
        for i, trade in enumerate(trades[:10]):
            trade_time = datetime.fromtimestamp(trade.time/1000).strftime('%Y-%m-%d %H:%M:%S')
            side_emoji = "🟢" if trade.is_buyer else "🔴"
            side_text = "买入" if trade.is_buyer else "卖出"
            
            print(f"   {i+1:2d}. 成交ID: {trade.id}")
            print(f"       时间: {trade_time}")
            print(f"       方向: {side_emoji} {side_text}")
            print(f"       价格: {trade.price:,.4f} USDT")
            print(f"       数量: {trade.qty:.6f} BTC")
            print(f"       金额: {trade.quote_qty:,.2f} USDT")
            print(f"       手续费: {trade.commission:.6f} {trade.commission_asset}")
            
            # 显示是否为挂单方
            if trade.is_maker:
                maker_text = "✅ Maker (挂单方)"
            else:
                maker_text = "❌ Taker (吃单方)"
            print(f"       类型: {maker_text}")
            
            print()
        
        if len(trades) > 10:
            print(f"   ... 还有 {len(trades) - 10} 笔成交记录")
        
        print("\n🎉 获取成交历史接口测试完成!")
        return trades
        
    except Exception as e:
        print(f"❌ 获取成交历史接口测试失败: {e}")
        print("\n可能的原因:")
        print("   - API密钥无效或过期")
        print("   - API密钥权限不足")
        print("   - 网络连接问题")
        print("   - 签名验证失败")
        print("   - 交易对不存在")
        return None
    
    finally:
        client.close()


def analyze_trading_performance():
    """分析交易表现"""
    print("\n=== 交易表现分析 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        print(f"📊 分析 {symbol} 的交易表现...")
        
        # 获取成交历史
        trades = client.get_trade_history(symbol)
        
        if not trades:
            print("   ℹ️  没有成交记录可供分析")
            return
        
        # 分析买卖比例
        buy_trades = [t for t in trades if t.is_buyer]
        sell_trades = [t for t in trades if not t.is_buyer]
        
        buy_ratio = len(buy_trades) / len(trades) * 100
        sell_ratio = len(sell_trades) / len(trades) * 100
        
        print("📈 交易方向分析:")
        print(f"   买入交易: {len(buy_trades)} 笔 ({buy_ratio:.1f}%)")
        print(f"   卖出交易: {len(sell_trades)} 笔 ({sell_ratio:.1f}%)")
        
        # 判断交易偏好
        if buy_ratio > 60:
            preference = "偏向买入"
            preference_emoji = "🟢"
        elif sell_ratio > 60:
            preference = "偏向卖出"
            preference_emoji = "🔴"
        else:
            preference = "买卖均衡"
            preference_emoji = "⚖️"
        
        print(f"   交易偏好: {preference_emoji} {preference}")
        print()
        
        # 分析Maker/Taker比例
        maker_trades = [t for t in trades if t.is_maker]
        taker_trades = [t for t in trades if not t.is_maker]
        
        maker_ratio = len(maker_trades) / len(trades) * 100
        taker_ratio = len(taker_trades) / len(trades) * 100
        
        print("🏷️  交易类型分析:")
        print(f"   Maker交易: {len(maker_trades)} 笔 ({maker_ratio:.1f}%)")
        print(f"   Taker交易: {len(taker_trades)} 笔 ({taker_ratio:.1f}%)")
        
        # 判断交易策略
        if maker_ratio > 70:
            strategy = "主动挂单策略"
            strategy_emoji = "🎯"
        elif taker_ratio > 70:
            strategy = "主动吃单策略"
            strategy_emoji = "⚡"
        else:
            strategy = "混合交易策略"
            strategy_emoji = "🔄"
        
        print(f"   交易策略: {strategy_emoji} {strategy}")
        print()
        
        # 分析手续费
        total_commission = sum(t.commission for t in trades)
        maker_commission = sum(t.commission for t in maker_trades)
        taker_commission = sum(t.commission for t in taker_trades)
        
        print("💰 手续费分析:")
        print(f"   总手续费: {total_commission:.6f}")
        print(f"   Maker手续费: {maker_commission:.6f}")
        print(f"   Taker手续费: {taker_commission:.6f}")
        
        # 计算平均手续费率
        total_quote_qty = sum(t.quote_qty for t in trades)
        if total_quote_qty > 0:
            avg_fee_rate = (total_commission / total_quote_qty) * 10000  # 万分比
            print(f"   平均手续费率: {avg_fee_rate:.2f} 万分之")
        print()
        
        # 分析交易频率
        if trades:
            trade_times = [datetime.fromtimestamp(t.time/1000) for t in trades]
            earliest_trade = min(trade_times)
            latest_trade = max(trade_times)
            
            time_span = latest_trade - earliest_trade
            days_span = time_span.days if time_span.days > 0 else 1
            
            avg_trades_per_day = len(trades) / days_span
            
            print("⏰ 交易频率分析:")
            print(f"   交易时间跨度: {days_span} 天")
            print(f"   平均每日交易: {avg_trades_per_day:.1f} 笔")
            
            # 判断交易频率
            if avg_trades_per_day >= 10:
                frequency = "高频交易"
                frequency_emoji = "🔥"
            elif avg_trades_per_day >= 3:
                frequency = "中频交易"
                frequency_emoji = "⚡"
            elif avg_trades_per_day >= 1:
                frequency = "低频交易"
                frequency_emoji = "📊"
            else:
                frequency = "偶尔交易"
                frequency_emoji = "😴"
            
            print(f"   交易频率: {frequency_emoji} {frequency}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 交易表现分析失败: {e}")


def get_trade_history_with_time_range():
    """获取指定时间范围的成交历史"""
    print("\n=== 获取指定时间范围的成交历史 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        # 设置时间范围 (最近24小时)
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=24)
        
        start_timestamp = int(start_time.timestamp() * 1000)
        end_timestamp = int(end_time.timestamp() * 1000)
        
        print(f"🔍 获取 {symbol} 最近24小时的成交...")
        print(f"   时间范围: {start_time.strftime('%Y-%m-%d %H:%M:%S')} 到 {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # 调用获取指定时间范围的成交历史接口
        trades = client.get_trade_history(
            symbol=symbol,
            start_time=start_timestamp,
            end_time=end_timestamp
        )
        
        print(f"✅ 获取成功! 共 {len(trades)} 笔成交")
        print()
        
        if not trades:
            print("   ℹ️  指定时间范围内没有成交记录")
            return
        
        # 按小时分组统计
        hourly_count = {}
        hourly_volume = {}
        
        for trade in trades:
            trade_hour = datetime.fromtimestamp(trade.time/1000).strftime('%Y-%m-%d %H:00')
            hourly_count[trade_hour] = hourly_count.get(trade_hour, 0) + 1
            hourly_volume[trade_hour] = hourly_volume.get(trade_hour, 0) + trade.quote_qty
        
        print("📅 每小时成交分布:")
        for hour in sorted(hourly_count.keys())[-12:]:  # 显示最近12小时
            count = hourly_count[hour]
            volume = hourly_volume.get(hour, 0)
            print(f"   {hour}: {count} 笔, {volume:,.2f} USDT")
        print()
        
        # 分析24小时交易活跃度
        total_volume = sum(t.quote_qty for t in trades)
        avg_trade_size = total_volume / len(trades) if trades else 0
        
        print("📊 24小时交易分析:")
        print(f"   总成交笔数: {len(trades)}")
        print(f"   总成交金额: {total_volume:,.2f} USDT")
        print(f"   平均单笔金额: {avg_trade_size:,.2f} USDT")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 获取指定时间范围成交历史失败: {e}")


def analyze_trade_patterns():
    """分析交易模式"""
    print("\n=== 交易模式分析 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        print(f"🔍 分析 {symbol} 的交易模式...")
        
        # 获取成交历史
        trades = client.get_trade_history(symbol)
        
        if not trades:
            print("   ℹ️  没有成交记录可供分析")
            return
        
        # 分析交易时间模式
        hour_distribution = {}
        for trade in trades:
            hour = datetime.fromtimestamp(trade.time/1000).hour
            hour_distribution[hour] = hour_distribution.get(hour, 0) + 1
        
        print("⏰ 交易时间分布:")
        
        # 找出最活跃的时间段
        if hour_distribution:
            most_active_hour = max(hour_distribution, key=hour_distribution.get)
            most_active_count = hour_distribution[most_active_hour]
            
            print(f"   最活跃时间: {most_active_hour}:00-{most_active_hour+1}:00 ({most_active_count} 笔)")
            
            # 分析时间段偏好
            morning_trades = sum(count for hour, count in hour_distribution.items() if 6 <= hour < 12)
            afternoon_trades = sum(count for hour, count in hour_distribution.items() if 12 <= hour < 18)
            evening_trades = sum(count for hour, count in hour_distribution.items() if 18 <= hour < 24)
            night_trades = sum(count for hour, count in hour_distribution.items() if 0 <= hour < 6)
            
            print(f"   上午交易: {morning_trades} 笔")
            print(f"   下午交易: {afternoon_trades} 笔")
            print(f"   晚上交易: {evening_trades} 笔")
            print(f"   深夜交易: {night_trades} 笔")
        print()
        
        # 分析交易规模分布
        trade_sizes = [t.quote_qty for t in trades]
        if trade_sizes:
            min_size = min(trade_sizes)
            max_size = max(trade_sizes)
            avg_size = sum(trade_sizes) / len(trade_sizes)
            
            print("💰 交易规模分析:")
            print(f"   最小单笔: {min_size:,.2f} USDT")
            print(f"   最大单笔: {max_size:,.2f} USDT")
            print(f"   平均单笔: {avg_size:,.2f} USDT")
            
            # 分类交易规模
            small_trades = len([s for s in trade_sizes if s < 100])
            medium_trades = len([s for s in trade_sizes if 100 <= s < 1000])
            large_trades = len([s for s in trade_sizes if s >= 1000])
            
            print(f"   小额交易 (<100 USDT): {small_trades} 笔")
            print(f"   中额交易 (100-1000 USDT): {medium_trades} 笔")
            print(f"   大额交易 (≥1000 USDT): {large_trades} 笔")
        print()
        
        # 分析价格执行效果
        prices = [t.price for t in trades]
        if len(prices) > 1:
            price_volatility = (max(prices) - min(prices)) / min(prices) * 100
            
            print("📈 价格执行分析:")
            print(f"   最低成交价: {min(prices):,.4f} USDT")
            print(f"   最高成交价: {max(prices):,.4f} USDT")
            print(f"   价格波动率: {price_volatility:.2f}%")
            
            # 判断价格执行效果
            if price_volatility < 1:
                execution_quality = "优秀"
                execution_emoji = "✅"
            elif price_volatility < 3:
                execution_quality = "良好"
                execution_emoji = "✅"
            elif price_volatility < 5:
                execution_quality = "一般"
                execution_emoji = "⚠️"
            else:
                execution_quality = "较差"
                execution_emoji = "❌"
            
            print(f"   执行质量: {execution_emoji} {execution_quality}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 交易模式分析失败: {e}")


def trade_history_monitoring_demo():
    """成交历史监控演示"""
    print("\n=== 成交历史监控演示 ===\n")
    
    print("📊 成交历史监控功能说明:")
    print("   1. 实时跟踪成交记录")
    print("   2. 分析交易表现和模式")
    print("   3. 监控手续费支出")
    print("   4. 生成交易报告")
    print()
    
    print("💡 监控建议:")
    print("   - 定期分析交易表现")
    print("   - 关注手续费优化机会")
    print("   - 监控交易频率变化")
    print("   - 分析最佳交易时间")
    print()
    
    print("🔧 实现方式:")
    print("   - 定时调用 get_trade_history() 接口")
    print("   - 计算关键交易指标")
    print("   - 比较历史表现")
    print("   - 生成可视化报告")


if __name__ == "__main__":
    # 注意: 这个示例需要真实的API密钥才能执行
    # 请先设置你的API密钥，或者注释掉这些调用
    
    print("=== TooBit API SDK 获取成交历史接口示例 ===\n")
    print("⚠️  重要提醒: 此接口需要真实的API密钥!")
    print("⚠️  请确保在测试环境中验证，或使用小额测试\n")
    
    # 取消注释以下行来运行示例
    # get_trade_history()
    # analyze_trading_performance()
    # get_trade_history_with_time_range()
    # analyze_trade_patterns()
    
    trade_history_monitoring_demo()
    
    print("\n💡 提示:")
    print("   取消注释相应的函数调用来运行实际的成交历史查询测试")
    print("   确保已设置正确的API密钥")
    print("   此接口可以获取账户的详细成交记录和分析") 