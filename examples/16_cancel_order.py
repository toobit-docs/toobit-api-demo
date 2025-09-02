"""
TooBit API SDK - 取消订单接口示例
取消指定的订单 (需要API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig
from datetime import datetime


def cancel_order():
    """取消订单"""
    print("=== TooBit API 取消订单接口测试 ===\n")
    
    # 注意: 这个示例需要真实的API密钥
    print("⚠️  注意: 此示例需要真实的API密钥才能运行")
    print("⚠️  注意: 这些操作会取消真实的订单，请谨慎使用!")
    print("⚠️  建议先在测试环境中验证\n")
    
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
        print("\n❌ 取消订单...")
        
        # 首先获取当前挂单
        print("📋 获取当前挂单...")
        open_orders = client.get_open_orders()
        
        if not open_orders:
            print("   ℹ️  当前没有未成交的订单，无法取消")
            return
        
        print(f"   找到 {len(open_orders)} 个挂单")
        print()
        
        # 显示挂单列表供用户选择
        print("📋 当前挂单列表:")
        for i, order in enumerate(open_orders):
            print(f"   {i+1:2d}. {order.symbol} | {order.side} | {order.type} | "
                  f"数量: {order.orig_qty} | 价格: {order.price} | "
                  f"时间: {datetime.fromtimestamp(int(order.time)/1000).strftime('%H:%M:%S')}")
        
        print()
        print("⚠️  注意: 以下演示将取消第一个挂单")
        print("   在实际使用中，请谨慎选择要取消的订单")
        print()
        
        # 选择要取消的订单 (这里演示取消第一个)
        target_order = open_orders[0]
        
        print(f"🎯 准备取消订单:")
        print(f"   订单ID: {target_order.order_id}")
        print(f"   交易对: {target_order.symbol}")
        print(f"   方向: {target_order.side}")
        print(f"   类型: {target_order.type}")
        print(f"   数量: {target_order.orig_qty}")
        print(f"   价格: {target_order.price}")
        print()
        
        # 调用取消订单接口
        print("🔄 正在取消订单...")
        response = client.cancel_order(
            symbol=target_order.symbol,
            order_id=target_order.order_id
        )
        
        print("✅ 订单取消成功!")
        print()
        
        # 显示取消结果
        print("📋 取消结果:")
        print(f"   订单ID: {response.order_id}")
        print(f"   客户端订单ID: {response.client_order_id}")
        print(f"   交易对: {response.symbol}")
        print(f"   原始数量: {response.orig_qty}")
        print(f"   已执行数量: {response.executed_qty}")
        print(f"   状态: {response.status}")
        
        # 判断取消状态
        if response.status == "CANCELED":
            status_emoji = "✅"
            status_text = "订单已成功取消"
        elif response.status == "PARTIALLY_CANCELED":
            status_emoji = "🟠"
            status_text = "订单部分取消 (部分已成交)"
        else:
            status_emoji = "❓"
            status_text = f"订单状态: {response.status}"
        
        print(f"   取消状态: {status_emoji} {status_text}")
        
        # 显示成交信息
        if float(response.executed_qty) > 0:
            fill_percentage = (float(response.executed_qty) / float(response.orig_qty)) * 100
            print(f"   成交比例: {fill_percentage:.1f}%")
            # print(f"累计成交金额: 字段不存在")
        
        print("\n🎉 取消订单接口测试完成!")
        return response.order_id
        
    except Exception as e:
        print(f"❌ 取消订单接口测试失败: {e}")
        print("\n可能的原因:")
        print("   - 订单不存在或已被取消")
        print("   - 订单已完成成交")
        print("   - API密钥权限不足")
        print("   - 订单不属于当前账户")
        return None
    
    finally:
        client.close()


def cancel_order_by_client_order_id():
    """通过客户端订单ID取消订单"""
    print("\n=== 通过客户端订单ID取消订单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🔍 通过客户端订单ID取消订单...")
        
        # 获取当前挂单
        open_orders = client.get_open_orders()
        
        if not open_orders:
            print("   ℹ️  当前没有未成交的订单")
            return
        
        # 查找有客户端订单ID的订单
        orders_with_client_id = [o for o in open_orders if hasattr(o, 'client_order_id') and o.client_order_id]
        
        if not orders_with_client_id:
            print("   ℹ️  没有找到带客户端订单ID的订单")
            return
        
        # 选择第一个有客户端订单ID的订单
        target_order = orders_with_client_id[0]
        
        print(f"🎯 准备取消订单:")
        print(f"   客户端订单ID: {target_order.client_order_id}")
        print(f"   交易对: {target_order.symbol}")
        print(f"   方向: {target_order.side}")
        print(f"   数量: {target_order.orig_qty}")
        print()
        
        # 通过客户端订单ID取消
        response = client.cancel_order(
            symbol=target_order.symbol,
            client_order_id=target_order.client_order_id
        )
        
        print("✅ 通过客户端订单ID取消成功!")
        print(f"   订单ID: {response.order_id}")
        print(f"   状态: {response.status}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 通过客户端订单ID取消订单失败: {e}")


def cancel_all_orders():
    """取消所有订单"""
    print("\n=== 取消所有订单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("⚠️  准备取消所有订单...")
        print("   此操作将取消账户中所有未成交的订单!")
        print("   请确认这是您想要的操作")
        print()
        
        # 获取当前挂单数量
        open_orders = client.get_open_orders()
        total_orders = len(open_orders)
        
        if total_orders == 0:
            print("   ℹ️  当前没有未成交的订单")
            return
        
        print(f"📊 当前挂单统计:")
        print(f"   总挂单数量: {total_orders}")
        
        # 按交易对统计
        symbol_count = {}
        for order in open_orders:
            symbol = order.symbol
            symbol_count[symbol] = symbol_count.get(symbol, 0) + 1
        
        print(f"   涉及交易对: {len(symbol_count)} 个")
        for symbol, count in symbol_count.items():
            print(f"     {symbol}: {count} 个")
        print()
        
        print("⚠️  注意: 以下演示将取消所有订单")
        print("   在实际使用中，请谨慎考虑此操作")
        print()
        
        # 取消所有订单
        print("🔄 正在取消所有订单...")
        
        canceled_count = 0
        failed_count = 0
        
        for order in open_orders:
            try:
                response = client.cancel_order(
                    symbol=order.symbol,
                    order_id=order.order_id
                )
                
                if response.status in ["CANCELED", "PARTIALLY_CANCELED"]:
                    canceled_count += 1
                    print(f"   ✅ {order.symbol} 订单取消成功")
                else:
                    failed_count += 1
                    print(f"   ❌ {order.symbol} 订单取消失败: {response.status}")
                    
            except Exception as e:
                failed_count += 1
                print(f"   ❌ {order.symbol} 订单取消失败: {e}")
        
        print()
        print("📊 取消结果统计:")
        print(f"   成功取消: {canceled_count} 个")
        print(f"   取消失败: {failed_count} 个")
        print(f"   成功率: {canceled_count/total_orders*100:.1f}%")
        
        # 验证取消结果
        remaining_orders = client.get_open_orders()
        print(f"   剩余挂单: {len(remaining_orders)} 个")
        
        print("\n🎉 批量取消订单完成!")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 批量取消订单失败: {e}")


def cancel_orders_by_symbol():
    """取消指定交易对的所有订单"""
    print("\n=== 取消指定交易对的所有订单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        print(f"🎯 准备取消 {symbol} 的所有订单...")
        
        # 获取指定交易对的挂单
        open_orders = client.get_open_orders(symbol)
        
        if not open_orders:
            print(f"   ℹ️  {symbol} 当前没有未成交的订单")
            return
        
        print(f"   找到 {len(open_orders)} 个 {symbol} 挂单")
        print()
        
        # 显示挂单详情
        print("📋 挂单详情:")
        for i, order in enumerate(open_orders):
            print(f"   {i+1}. {order.side} | {order.type} | "
                  f"数量: {order.orig_qty} | 价格: {order.price}")
        print()
        
        # 取消指定交易对的所有订单
        print(f"🔄 正在取消 {symbol} 的所有订单...")
        
        canceled_count = 0
        for order in open_orders:
            try:
                response = client.cancel_order(
                    symbol=order.symbol,
                    order_id=order.order_id
                )
                
                if response.status in ["CANCELED", "PARTIALLY_CANCELED"]:
                    canceled_count += 1
                    print(f"   ✅ 订单 {order.order_id} 取消成功")
                else:
                    print(f"   ❌ 订单 {order.order_id} 取消失败: {response.status}")
                    
            except Exception as e:
                print(f"   ❌ 订单 {order.order_id} 取消失败: {e}")
        
        print()
        print(f"📊 {symbol} 订单取消结果:")
        print(f"   成功取消: {canceled_count}/{len(open_orders)} 个")
        
        # 验证结果
        remaining_orders = client.get_open_orders(symbol)
        print(f"   剩余挂单: {len(remaining_orders)} 个")
        
        print("\n🎉 指定交易对订单取消完成!")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 取消指定交易对订单失败: {e}")


def cancel_order_safety_demo():
    """取消订单安全演示"""
    print("\n=== 取消订单安全演示 ===\n")
    
    print("🛡️  取消订单安全注意事项:")
    print("   1. 确认要取消的订单ID")
    print("   2. 验证订单属于当前账户")
    print("   3. 检查订单状态是否可取消")
    print("   4. 避免重复取消同一订单")
    print()
    
    print("💡 最佳实践:")
    print("   - 在取消前先查询订单状态")
    print("   - 使用客户端订单ID便于跟踪")
    print("   - 批量取消时注意API限制")
    print("   - 记录取消操作日志")
    print()
    
    print("⚠️  风险提醒:")
    print("   - 取消订单是不可逆操作")
    print("   - 可能影响交易策略执行")
    print("   - 建议在非交易高峰期操作")
    print("   - 重要订单取消前请再三确认")


if __name__ == "__main__":
    # 注意: 这个示例需要真实的API密钥才能执行
    # 请先设置你的API密钥，或者注释掉这些调用
    
    print("=== TooBit API SDK 取消订单接口示例 ===\n")
    print("⚠️  重要提醒: 所有取消操作都是真实的!")
    print("⚠️  请确保在测试环境中验证，或使用小额测试")
    print("⚠️  建议先运行无需API密钥的示例熟悉接口\n")
    
    # 取消注释以下行来运行示例
    cancel_order()
    # cancel_order_by_client_order_id()
    # cancel_all_orders()
    # cancel_orders_by_symbol()
    
    cancel_order_safety_demo()
    
    print("\n💡 提示:")
    print("   取消注释相应的函数调用来运行实际的取消订单测试")
    print("   确保已设置正确的API密钥和充足的账户余额")
    print("   取消订单是不可逆操作，请谨慎使用") 