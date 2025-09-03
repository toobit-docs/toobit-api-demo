"""
TooBit API SDK - 批量创建订单接口示例 (08)
批量创建多个订单 (需要API密钥)
"""
import uuid
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import OrderRequest, OrderSide, OrderType, TimeInForce

def batch_create_orders():
    """批量创建订单"""
    print("=== TooBit API 批量创建订单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 创建多个订单请求
        orders = []
        
        # 订单1: 限价买入
        order1 = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            quantity=0.01,
            price=45000.0,
            time_in_force=TimeInForce.GTC,
            new_client_order_id=f"batch_buy_{uuid.uuid4().hex[:8]}"
        )
        orders.append(order1)
        
        # 订单2: 限价卖出
        order2 = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.SELL,
            type=OrderType.LIMIT,
            quantity=1,
            price=10000.0,
            time_in_force=TimeInForce.GTC,
            new_client_order_id=f"batch_sell_{uuid.uuid4().hex[:8]}"
        )
        orders.append(order2)
        
        # # 订单3: 市价买入
        order3 = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.MARKET,
            quantity=10,
            time_in_force=TimeInForce.IOC,
            new_client_order_id=f"batch_market_{uuid.uuid4().hex[:8]}"
        )
        orders.append(order3)
        
        print("🔄 正在批量创建订单...")
        print(f"   订单数量: {len(orders)}")
        print()
        
        # 显示订单详情
        for i, order in enumerate(orders, 1):
            print(f"   订单 {i}:")
            print(f"     交易对: {order.symbol}")
            print(f"     方向: {order.side}")
            print(f"     类型: {order.type}")
            print(f"     数量: {order.quantity}")
            if order.price:
                print(f"     价格: {order.price}")
            print(f"     客户端订单ID: {order.new_client_order_id}")
            print()
        
        print("⚠️  注意: 这是真实的交易操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 调用批量下单接口
        response = client.batch_create_orders(orders)
        
        print("✅ 批量下单成功!")
        print()
        
        # 显示响应结果
        print("📋 批量下单结果:")
        print(f"   📊 响应代码: {response.code}")
        
        if response.result:
            print(f"   📊 订单创建结果 (共{len(response.result)}个订单):")
            for i, order_result in enumerate(response.result, 1):
                print(f"     - 订单 {i}:")
                print(f"       结果代码: {order_result.code}")
                
                if order_result.code == 0 and order_result.order:
                    # 成功的情况
                    order = order_result.order
                    print(f"       ✅ 创建成功")
                    print(f"       交易对: {order.symbol}")
                    print(f"       订单ID: {order.order_id}")
                    print(f"       客户端订单ID: {order.client_order_id}")
                    print(f"       状态: {order.status}")
                    print(f"       价格: {order.price}")
                    print(f"       数量: {order.orig_qty}")
                    print(f"       已执行数量: {order.executed_qty}")
                else:
                    # 失败的情况
                    print(f"       ❌ 创建失败")
                    print(f"       错误消息: {order_result.msg}")
                print()
        
        print("\n🎉 批量创建订单完成!")
        return response
        
    except Exception as e:
        print(f"❌ 批量创建订单失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 批量创建订单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的交易操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: POST /api/v1/spot/batchOrders")
    print("   - 鉴权: 需要签名 (TRADE)")
    print("   - 功能: 批量创建多个订单")
    print("   - 参数: 订单数组直接放在request body中")
    print()
    print("💡 批量下单说明:")
    print("   - 支持同时创建多个不同类型的订单")
    print("   - 每个订单都有唯一的客户端订单ID")
    print("   - 返回每个订单的创建结果")
    print("   - 部分成功部分失败是正常情况")
    print()
    print("📈 响应结果说明:")
    print("   - code: 200 表示请求成功")
    print("   - result: 包含每个订单的创建结果")
    print("   - 每个结果包含订单ID、状态等信息")
    print()
    print("⚠️  重要提醒:")
    print("   - 此操作不可逆")
    print("   - 将创建3个测试订单")
    print("   - 请确保账户有足够资金")
    print("   - 建议先在测试环境中验证")
    print()
    
    batch_create_orders()
