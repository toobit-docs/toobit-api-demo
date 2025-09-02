"""
TooBit API SDK - 查询订单接口示例
查询指定订单的详细信息 (需要API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig
from datetime import datetime


def get_order():
    """查询订单"""
    print("=== TooBit API 查询订单接口测试 ===\n")
    
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
        print("\n🔍 查询订单...")
        
        # 首先获取一个现有订单用于演示
        print("📋 获取现有订单用于演示...")
        
        # 先获取所有订单
        all_orders = client.get_all_orders("BTCUSDT", limit=5)
        
        if not all_orders:
            print("   ℹ️  没有找到现有订单，无法演示查询功能")
            print("   建议先创建一些订单后再运行此示例")
            return
        
        # 选择第一个订单进行查询
        target_order = all_orders[0]
        
        print(f"   找到订单用于演示: {target_order.order_id}")
        print()
        
        # 调用查询订单接口
        print("🔍 通过订单ID查询订单详情...")
        order_info = client.get_order(
            symbol=target_order.symbol,
            order_id=target_order.order_id
        )
        
        print("✅ 订单查询成功!")
        print()
        
        # 显示订单详细信息
        print("📋 订单详细信息:")
        print(f"   订单ID: {order_info.order_id}")
        print(f"   客户端订单ID: {order_info.client_order_id}")
        print(f"   交易对: {order_info.symbol}")
        print(f"   订单状态: {order_info.status}")
        print(f"   订单类型: {order_info.type}")
        print(f"   订单方向: {order_info.side}")
        print(f"   时间有效性: {order_info.time_in_force}")
        print()
        
        # 显示数量和价格信息
        print("💰 数量和价格信息:")
        print(f"   原始数量: {order_info.orig_qty}")
        print(f"   已执行数量: {order_info.executed_qty}")
        print(f"   价格: {order_info.price}")
        # 注意：实际API响应中没有cummulative_quote_qty字段
        # # print(f"累计成交金额: 字段不存在")
        
        # 计算成交比例
        if float(order_info.orig_qty) > 0:
            fill_percentage = (float(order_info.executed_qty) / float(order_info.orig_qty)) * 100
            print(f"   成交比例: {fill_percentage:.2f}%")
        print()
        
        # 显示时间信息
        print("⏰ 时间信息:")
        order_time = datetime.fromtimestamp(order_info.time/1000)
        # print(f"订单时间: 字段不存在")
        
        if hasattr(order_info, 'update_time') and order_info.update_time:
            update_time = datetime.fromtimestamp(order_info.update_time/1000)
            print(f"   更新时间: {update_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # 显示订单状态分析
        print("📊 订单状态分析:")
        
        if order_info.status == "NEW":
            status_emoji = "🟡"
            status_text = "新订单，等待成交"
            status_advice = "订单正在等待市场匹配"
        elif order_info.status == "FILLED":
            status_emoji = "🟢"
            status_text = "订单已完全成交"
            status_advice = "订单执行完成"
        elif order_info.status == "PARTIALLY_FILLED":
            status_emoji = "🟠"
            status_text = "订单部分成交"
            status_advice = "订单正在逐步执行中"
        elif order_info.status == "CANCELED":
            status_emoji = "❌"
            status_text = "订单已取消"
            status_advice = "订单被手动取消或系统取消"
        elif order_info.status == "REJECTED":
            status_emoji = "🚫"
            status_text = "订单被拒绝"
            status_advice = "订单参数不符合要求"
        else:
            status_emoji = "❓"
            status_text = f"其他状态: {order_info.status}"
            status_advice = "请查看具体状态说明"
        
        print(f"   状态: {status_emoji} {status_text}")
        print(f"   说明: {status_advice}")
        
        # 显示特殊参数
        if hasattr(order_info, 'stop_price') and order_info.stop_price:
            print(f"   止损价格: {order_info.stop_price}")
        
        if hasattr(order_info, 'iceberg_qty') and order_info.iceberg_qty:
            print(f"   冰山数量: {order_info.iceberg_qty}")
        
        # print(f"是否在工作: 字段不存在")
        
        # 显示成交信息
        if float(order_info.executed_qty) > 0:
            # 注意：实际API响应中没有cummulative_quote_qty字段
            # avg_price = # order_info.cummulative_quote_qty  # 字段不存在 / order_info.executed_qty
            print(f"\n💹 成交信息:")
            print(f"   平均成交价: 需要查询成交历史获取")
            print(f"   成交金额: 需要查询成交历史获取")
        
        print("\n🎉 查询订单接口测试完成!")
        return order_info
        
    except Exception as e:
        print(f"❌ 查询订单接口测试失败: {e}")
        print("\n可能的原因:")
        print("   - 订单ID不存在")
        print("   - API密钥权限不足")
        print("   - 订单不属于当前账户")
        print("   - 网络连接问题")
        return None
    
    finally:
        client.close()


def get_order_by_client_order_id():
    """通过客户端订单ID查询订单"""
    print("\n=== 通过客户端订单ID查询订单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🔍 通过客户端订单ID查询订单...")
        
        # 获取有客户端订单ID的订单
        all_orders = client.get_all_orders("BTCUSDT", limit=10)
        orders_with_client_id = [o for o in all_orders if hasattr(o, 'client_order_id') and o.client_order_id]
        
        if not orders_with_client_id:
            print("   ℹ️  没有找到带客户端订单ID的订单")
            return
        
        target_order = orders_with_client_id[0]
        
        print(f"   使用客户端订单ID: {target_order.client_order_id}")
        
        # 通过客户端订单ID查询
        order_info = client.get_order(
            symbol=target_order.symbol,
            client_order_id=target_order.client_order_id
        )
        
        print("✅ 通过客户端订单ID查询成功!")
        print()
        
        print("📋 订单信息:")
        print(f"   订单ID: {order_info.order_id}")
        print(f"   客户端订单ID: {order_info.client_order_id}")
        print(f"   交易对: {order_info.symbol}")
        print(f"   状态: {order_info.status}")
        print(f"   类型: {order_info.type}")
        print(f"   方向: {order_info.side}")
        
        print("\n💡 客户端订单ID的优势:")
        print("   - 便于业务系统跟踪")
        print("   - 支持自定义标识")
        print("   - 方便订单管理")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 通过客户端订单ID查询失败: {e}")


def batch_query_orders():
    """批量查询订单"""
    print("\n=== 批量查询订单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🔍 批量查询订单状态...")
        
        # 获取最近的订单列表
        recent_orders = client.get_all_orders("BTCUSDT", limit=5)
        
        if not recent_orders:
            print("   ℹ️  没有找到订单")
            return
        
        print(f"   准备查询 {len(recent_orders)} 个订单的详细信息")
        print()
        
        successful_queries = 0
        failed_queries = 0
        
        for i, order in enumerate(recent_orders):
            try:
                print(f"📋 查询订单 {i+1}/{len(recent_orders)}: {order.order_id}")
                
                # 查询订单详情
                order_info = client.get_order(
                    symbol=order.symbol,
                    order_id=order.order_id
                )
                
                # 显示简要信息
                order_time = datetime.fromtimestamp(order_info.time/1000)
                fill_percentage = (float(order_info.executed_qty) / float(order_info.orig_qty)) * 100 if float(order_info.orig_qty) > 0 else 0
                
                print(f"   ✅ {order_info.symbol} | {order_info.side} | {order_info.status}")
                print(f"      时间: {order_time.strftime('%m-%d %H:%M')} | 成交: {fill_percentage:.1f}%")
                
                successful_queries += 1
                
            except Exception as e:
                print(f"   ❌ 查询失败: {e}")
                failed_queries += 1
            
            print()
        
        # 显示批量查询结果
        print("📊 批量查询结果:")
        print(f"   成功查询: {successful_queries} 个")
        print(f"   查询失败: {failed_queries} 个")
        print(f"   成功率: {successful_queries/(successful_queries+failed_queries)*100:.1f}%")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 批量查询订单失败: {e}")


def monitor_order_status():
    """监控订单状态变化"""
    print("\n=== 监控订单状态变化 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🔄 监控订单状态变化...")
        
        # 获取当前挂单
        open_orders = client.get_open_orders("BTCUSDT")
        
        if not open_orders:
            print("   ℹ️  当前没有挂单可供监控")
            return
        
        # 选择第一个挂单进行监控
        target_order = open_orders[0]
        
        print(f"   监控订单: {target_order.order_id}")
        print(f"   初始状态: {target_order.status}")
        print()
        
        # 模拟监控过程 (实际应用中应该是定时循环)
        print("🔍 开始监控 (模拟5次查询)...")
        
        for i in range(5):
            try:
                # 查询订单当前状态
                current_order = client.get_order(
                    symbol=target_order.symbol,
                    order_id=target_order.order_id
                )
                
                current_time = datetime.now().strftime('%H:%M:%S')
                fill_percentage = (float(current_order.executed_qty) / float(current_order.orig_qty)) * 100 if float(current_order.orig_qty) > 0 else 0
                
                print(f"   {i+1}. [{current_time}] 状态: {current_order.status} | 成交: {fill_percentage:.1f}%")
                
                # 检查状态变化
                if current_order.status != target_order.status:
                    print(f"      🔔 状态变化: {target_order.status} → {current_order.status}")
                    target_order = current_order
                
                # 检查成交进度
                if float(current_order.executed_qty) > 0:
                    avg_price = current_# order.cummulative_quote_qty  # 字段不存在 / current_order.executed_qty
                    print(f"      💰 平均成交价: {avg_price:.4f}")
                
                # 如果订单完成，停止监控
                if current_order.status in ["FILLED", "CANCELED", "REJECTED"]:
                    print(f"      🏁 订单已完成: {current_order.status}")
                    break
                
                # 实际应用中应该有适当的延时
                import time
                time.sleep(2)
                
            except Exception as e:
                print(f"   ❌ 第{i+1}次查询失败: {e}")
        
        print("\n🎉 订单状态监控完成!")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 订单状态监控失败: {e}")


def order_query_best_practices():
    """订单查询最佳实践"""
    print("\n=== 订单查询最佳实践 ===\n")
    
    print("🎯 查询策略:")
    print("   1. 优先使用客户端订单ID")
    print("   2. 批量查询时控制频率")
    print("   3. 缓存查询结果避免重复")
    print("   4. 处理查询失败的情况")
    print()
    
    print("⚡ 性能优化:")
    print("   - 避免频繁查询同一订单")
    print("   - 使用合适的查询间隔")
    print("   - 批量操作时注意API限制")
    print("   - 缓存不变的订单信息")
    print()
    
    print("🛡️  错误处理:")
    print("   - 订单不存在的情况")
    print("   - 网络超时重试机制")
    print("   - API限制的处理")
    print("   - 权限不足的处理")
    print()
    
    print("📊 监控建议:")
    print("   - 关键订单实时监控")
    print("   - 异常状态及时告警")
    print("   - 记录查询操作日志")
    print("   - 定期检查订单状态")


if __name__ == "__main__":
    # 注意: 这个示例需要真实的API密钥才能执行
    # 请先设置你的API密钥，或者注释掉这些调用
    
    print("=== TooBit API SDK 查询订单接口示例 ===\n")
    print("⚠️  重要提醒: 此接口需要真实的API密钥!")
    print("⚠️  请确保在测试环境中验证，或使用小额测试\n")
    
    # 取消注释以下行来运行示例
    # get_order()
    # get_order_by_client_order_id()
    # batch_query_orders()
    # monitor_order_status()
    
    order_query_best_practices()
    
    print("\n💡 提示:")
    print("   取消注释相应的函数调用来运行实际的订单查询测试")
    print("   确保已设置正确的API密钥")
    print("   此接口可以查询订单的详细状态和执行情况") 