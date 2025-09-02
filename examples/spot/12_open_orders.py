"""
TooBit API SDK - 获取当前挂单接口示例
获取账户中所有未成交的订单 (需要API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig
from datetime import datetime


def get_open_orders():
    """获取当前挂单"""
    print("=== TooBit API 获取当前挂单接口测试 ===\n")
    
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
        print("\n📋 获取当前挂单...")
        
        # 调用获取当前挂单接口
        open_orders = client.get_open_orders()
        
        print("✅ 当前挂单获取成功!")
        print()
        
        # 显示基本信息
        print("📊 挂单概览:")
        print(f"   总挂单数量: {len(open_orders)}")
        
        if not open_orders:
            print("   ℹ️  当前没有未成交的订单")
            return open_orders
        
        # 按交易对分组统计
        symbol_count = {}
        for order in open_orders:
            symbol = order.symbol
            symbol_count[symbol] = symbol_count.get(symbol, 0) + 1
        
        print(f"   涉及交易对: {len(symbol_count)} 个")
        print()
        
        # 显示每个交易对的挂单数量
        print("📈 交易对挂单分布:")
        sorted_symbols = sorted(symbol_count.items(), key=lambda x: x[1], reverse=True)
        for symbol, count in sorted_symbols:
            print(f"   {symbol}: {count} 个挂单")
        print()
        
        # 显示挂单详情
        print("📋 挂单详情:")
        
        # 按时间排序，最新的在前
        open_orders.sort(key=lambda x: x.time, reverse=True)
        
        for i, order in enumerate(open_orders):
            print(f"   {i+1:2d}. 订单ID: {order.order_id}")
            print(f"       交易对: {order.symbol}")
            print(f"       方向: {order.side}")
            print(f"       类型: {order.type}")
            print(f"       数量: {order.orig_qty}")
            print(f"       价格: {order.price}")
            # print(f"订单时间: 字段不存在")
            
            # 显示订单状态
            if order.status == "NEW":
                status_emoji = "🟡"
                status_text = "新订单，等待成交"
            elif order.status == "PARTIALLY_FILLED":
                status_emoji = "🟠"
                status_text = "部分成交"
            else:
                status_emoji = "⚪"
                status_text = order.status
            
            print(f"       状态: {status_emoji} {status_text}")
            
            # 显示成交信息
            if float(order.executed_qty) > 0:
                fill_percentage = (float(order.executed_qty) / float(order.orig_qty)) * 100
                print(f"       已成交: {order.executed_qty} ({fill_percentage:.1f}%)")
                # 注意：实际API响应中没有cummulative_quote_qty字段
        # # print(f"累计成交金额: 字段不存在")
            
            # 显示特殊参数
            if hasattr(order, 'stop_price') and order.stop_price:
                print(f"       止损价格: {order.stop_price}")
            if hasattr(order, 'iceberg_qty') and order.iceberg_qty:
                print(f"       冰山数量: {order.iceberg_qty}")
            
            print()
        
        print("\n🎉 获取当前挂单接口测试完成!")
        return open_orders
        
    except Exception as e:
        print(f"❌ 获取当前挂单接口测试失败: {e}")
        print("\n可能的原因:")
        print("   - API密钥无效或过期")
        print("   - API密钥权限不足")
        print("   - 网络连接问题")
        print("   - 签名验证失败")
        return None
    
    finally:
        client.close()


def get_open_orders_by_symbol():
    """获取指定交易对的当前挂单"""
    print("\n=== 获取指定交易对的当前挂单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        print(f"🔍 获取 {symbol} 的当前挂单...")
        
        # 调用获取指定交易对的当前挂单接口
        open_orders = client.get_open_orders(symbol)
        
        print(f"✅ 获取成功! 共 {len(open_orders)} 个挂单")
        print()
        
        if not open_orders:
            print(f"   ℹ️  {symbol} 当前没有未成交的订单")
            return
        
        # 按方向分组
        buy_orders = [o for o in open_orders if o.side == "BUY"]
        sell_orders = [o for o in open_orders if o.side == "SELL"]
        
        print("📊 挂单分析:")
        print(f"   买单数量: {len(buy_orders)}")
        print(f"   卖单数量: {len(sell_orders)}")
        print()
        
        # 显示买单
        if buy_orders:
            print("🟢 买单:")
            buy_orders.sort(key=lambda x: x.price, reverse=True)  # 价格从高到低
            for i, order in enumerate(buy_orders[:5]):  # 只显示前5个
                print(f"   {i+1}. 价格: {order.price:,.2f} | 数量: {order.orig_qty:.6f} | 时间: {datetime.fromtimestamp(# order.time  # 字段不存在/1000).strftime('%H:%M:%S')}")
            
            if len(buy_orders) > 5:
                print(f"   ... 还有 {len(buy_orders) - 5} 个买单")
            print()
        
        # 显示卖单
        if sell_orders:
            print("🔴 卖单:")
            sell_orders.sort(key=lambda x: x.price)  # 价格从低到高
            for i, order in enumerate(sell_orders[:5]):  # 只显示前5个
                print(f"   {i+1}. 价格: {order.price:,.2f} | 数量: {order.orig_qty:.6f} | 时间: {datetime.fromtimestamp(# order.time  # 字段不存在/1000).strftime('%H:%M:%S')}")
            
            if len(sell_orders) > 5:
                print(f"   ... 还有 {len(sell_orders) - 5} 个卖单")
            print()
        
        # 计算挂单总价值
        total_buy_value = sum(o.price * o.orig_qty for o in buy_orders)
        total_sell_value = sum(o.price * o.orig_qty for o in sell_orders)
        
        print("💰 挂单价值:")
        print(f"   买单总价值: {total_buy_value:,.2f} USDT")
        print(f"   卖单总价值: {total_sell_value:,.2f} USDT")
        print(f"   总挂单价值: {total_buy_value + total_sell_value:,.2f} USDT")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 获取指定交易对挂单失败: {e}")


def analyze_open_orders():
    """分析当前挂单"""
    print("\n=== 当前挂单分析 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("📊 分析当前挂单...")
        
        # 获取所有挂单
        open_orders = client.get_open_orders()
        
        if not open_orders:
            print("   ℹ️  当前没有未成交的订单")
            return
        
        # 按订单类型统计
        order_type_count = {}
        for order in open_orders:
            order_type = order.type
            order_type_count[order_type] = order_type_count.get(order_type, 0) + 1
        
        print("📈 订单类型分布:")
        for order_type, count in order_type_count.items():
            print(f"   {order_type}: {count} 个")
        print()
        
        # 按订单方向统计
        buy_count = len([o for o in open_orders if o.side == "BUY"])
        sell_count = len([o for o in open_orders if o.side == "SELL"])
        
        print("📊 订单方向分布:")
        print(f"   买单: {buy_count} 个 ({buy_count/len(open_orders)*100:.1f}%)")
        print(f"   卖单: {sell_count} 个 ({sell_count/len(open_orders)*100:.1f}%)")
        print()
        
        # 分析挂单时间分布
        now = datetime.now()
        time_distribution = {
            "1小时内": 0,
            "1-6小时": 0,
            "6-24小时": 0,
            "24小时以上": 0
        }
        
        for order in open_orders:
            order_time = datetime.fromtimestamp(# order.time  # 字段不存在/1000)
            time_diff = now - order_time
            
            if time_diff.total_seconds() < 3600:  # 1小时
                time_distribution["1小时内"] += 1
            elif time_diff.total_seconds() < 21600:  # 6小时
                time_distribution["1-6小时"] += 1
            elif time_diff.total_seconds() < 86400:  # 24小时
                time_distribution["6-24小时"] += 1
            else:
                time_distribution["24小时以上"] += 1
        
        print("⏰ 挂单时间分布:")
        for time_range, count in time_distribution.items():
            if count > 0:
                percentage = count / len(open_orders) * 100
                print(f"   {time_range}: {count} 个 ({percentage:.1f}%)")
        print()
        
        # 分析挂单价格分布
        if open_orders:
            prices = [float(o.price) for o in open_orders if o.price]
            if prices:
                min_price = min(prices)
                max_price = max(prices)
                avg_price = sum(prices) / len(prices)
                
                print("💰 挂单价格分析:")
                print(f"   最低价格: {min_price:,.4f}")
                print(f"   最高价格: {max_price:,.4f}")
                print(f"   平均价格: {avg_price:,.4f}")
                print(f"   价格区间: {max_price - min_price:,.4f}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 挂单分析失败: {e}")


def open_orders_monitoring_demo():
    """挂单监控演示"""
    print("\n=== 挂单监控演示 ===\n")
    
    print("📊 挂单监控功能说明:")
    print("   1. 实时监控挂单状态变化")
    print("   2. 跟踪挂单成交情况")
    print("   3. 设置挂单超时预警")
    print("   4. 生成挂单分析报告")
    print()
    
    print("💡 监控建议:")
    print("   - 定期检查挂单状态")
    print("   - 关注长时间未成交的订单")
    print("   - 监控挂单价格与市价的差距")
    print("   - 及时调整不合理的挂单")
    print()
    
    print("🔧 实现方式:")
    print("   - 定时调用 get_open_orders() 接口")
    print("   - 比较挂单数量变化")
    print("   - 检查挂单时间")
    print("   - 分析挂单价格合理性")


if __name__ == "__main__":
    # 注意: 这个示例需要真实的API密钥才能执行
    # 请先设置你的API密钥，或者注释掉这些调用
    
    print("=== TooBit API SDK 获取当前挂单接口示例 ===\n")
    print("⚠️  重要提醒: 此接口需要真实的API密钥!")
    print("⚠️  请确保在测试环境中验证，或使用小额测试\n")
    
    # 取消注释以下行来运行示例
    # get_open_orders()
    # get_open_orders_by_symbol()
    # analyze_open_orders()
    
    open_orders_monitoring_demo()
    
    print("\n💡 提示:")
    print("   取消注释相应的函数调用来运行实际的挂单查询测试")
    print("   确保已设置正确的API密钥")
    print("   此接口可以获取账户中所有未成交的订单信息") 