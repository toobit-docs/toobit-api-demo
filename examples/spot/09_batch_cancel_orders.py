"""
TooBit API SDK - 批量撤销订单接口示例 (09)
批量撤销多个订单 (需要API密钥)
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import BatchCancelOrdersResponse, BatchCancelOrderResult

def batch_cancel_orders():
    """批量撤销订单"""
    print("=== TooBit API 批量撤销订单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 先查询挂单列表
        print("🔄 正在查询挂单列表...")
        open_orders = client.get_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  当前没有挂单，无需撤单")
            return None
        
        print(f"✅ 获取到 {len(open_orders)} 个挂单")
        print()
        
        # 选择前几个挂单进行批量撤单（最多5个）
        max_orders = min(5, len(open_orders))
        orders_to_cancel = open_orders[:max_orders]
        order_ids = [order.order_id for order in orders_to_cancel]
        symbol = orders_to_cancel[0].symbol if orders_to_cancel else "BTCUSDT"
        
        print("🔄 正在批量撤销订单...")
        print(f"   交易对: {symbol}")
        print(f"   订单ID列表: {order_ids}")
        print(f"   订单数量: {len(order_ids)}")
        print()
        
        # 显示要撤销的订单详情
        for i, order in enumerate(orders_to_cancel, 1):
            print(f"   订单 {i}:")
            print(f"     订单ID: {order.order_id}")
            print(f"     客户端订单ID: {order.client_order_id}")
            print(f"     交易对: {order.symbol}")
            print(f"     方向: {order.side}")
            print(f"     类型: {order.type}")
            print(f"     价格: {order.price}")
            print(f"     数量: {order.orig_qty}")
            print()
        
        print("⚠️  注意: 这是真实的交易操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 调用现货批量撤单接口
        response = client.batch_cancel_spot_orders(order_ids)
        
        print("✅ 批量撤单请求成功!")
        print()
        
        # 显示批量撤单结果
        print("📋 批量撤单结果:")
        if hasattr(response, 'code'):
            print(f"   📊 响应代码: {response.code}")
        if hasattr(response, 'message'):
            print(f"   💬 响应消息: {response.message}")
        if hasattr(response, 'timestamp'):
            print(f"   🕐 时间戳: {response.timestamp}")
        
        if hasattr(response, 'result'):
            if response.result and len(response.result) > 0:
                print(f"   📊 撤单结果详情 (共{len(response.result)}个订单):")
                success_count = 0
                failed_count = 0
                
                for i, result in enumerate(response.result):
                    status = "成功" if result.code == 200 else "失败"
                    if result.code == 200:
                        success_count += 1
                    else:
                        failed_count += 1
                    print(f"     - 订单 {result.orderId}: {status} (代码: {result.code})")
                    # 常见错误代码解释
                    if result.code == -2013:
                        print("       ℹ️  错误: 订单不存在")
                    elif result.code == -2011:
                        print("       ℹ️  错误: 取消订单被拒绝")
                    elif result.code == -1142:
                        print("       ℹ️  错误: 订单已被取消")
            else:
                print("   ✅ 所有订单撤销成功 (result为空数组表示全部成功)")
        
        # 检查整体响应状态
        if hasattr(response, 'code') and response.code == 200:
            print("\n   ✅ 批量撤单操作完成")
        else:
            print("\n   ⚠️  批量撤单操作可能未完全成功")
        
        return response
        
    except Exception as e:
        print(f"❌ 批量撤销订单失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 批量撤销订单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的交易操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: DELETE /api/v1/spot/cancelOrderByIds")
    print("   - 鉴权: 需要签名 (TRADE)")
    print("   - 功能: 批量撤销指定订单")
    print("   - 参数: orderIds")
    print()
    print("💡 批量撤单说明:")
    print("   - 先查询当前挂单列表")
    print("   - 选择前5个挂单进行批量撤单")
    print("   - 使用实际存在的订单ID")
    print("   - 返回每个订单的撤单结果")
    print("   - 部分成功部分失败是正常情况")
    print()
    print("📈 响应结果说明:")
    print("   - code: 200 表示请求成功")
    print("   - result: 空数组表示全部撤单成功")
    print("   - result: 包含结果表示部分或全部失败")
    print("   - 每个结果包含 orderId 和 code")
    print()
    print("⚠️  重要提醒:")
    print("   - 此操作不可逆")
    print("   - 将撤销当前挂单列表中的前5个订单")
    print("   - 基于实际挂单进行操作，确保订单存在")
    print()
    
    batch_cancel_orders()
