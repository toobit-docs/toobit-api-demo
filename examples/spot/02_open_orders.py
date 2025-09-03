"""
TooBit API SDK - 查看当前挂单接口示例 (02)
查看当前挂单 (需要API密钥)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_open_orders():
    """查看当前挂单"""
    print("=== TooBit API 查看当前挂单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"  # 交易对 (可选，不传则查询所有交易对的挂单)
        
        print("🔄 正在查看当前挂单...")
        if symbol:
            print(f"   交易对: {symbol}")
        else:
            print("   交易对: 全部")
        print()
        print("⚠️  注意: 这是真实的账户查询操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 调用查看挂单接口
        open_orders = client.get_open_orders(symbol)
        
        print("✅ 挂单查询成功!")
        print()
        
        # 显示挂单信息
        if open_orders and len(open_orders) > 0:
            print(f"📊 当前挂单信息 (共{len(open_orders)}个):")
            for i, order in enumerate(open_orders):
                print(f"\n   挂单 {i+1}:")
                print(f"     🆔 订单ID: {order.order_id}")
                print(f"     🔑 客户端订单ID: {order.client_order_id}")
                print(f"     📊 交易对: {order.symbol}")
                print(f"     💰 价格: {order.price}")
                print(f"     📊 数量: {order.orig_qty}")
                print(f"     ✅ 已执行数量: {order.executed_qty}")
                print(f"     🔧 订单类型: {order.type}")
                print(f"     📈 买卖方向: {order.side}")
                print(f"     📈 订单状态: {order.status}")
                print(f"     ⏰ 时效: {order.time_in_force}")
                print(f"     🕐 交易时间: {order.time}")
        else:
            print("   ℹ️  当前没有挂单")
        
        print("\n🎉 查看挂单完成!")
        return open_orders
        
    except Exception as e:
        print(f"❌ 查看挂单失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 查看当前挂单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的账户查询操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: GET /api/v1/spot/openOrders")
    print("   - 鉴权: 需要签名 (USER_DATA)")
    print("   - 功能: 查看当前挂单")
    print("   - 参数: symbol(可选)")
    print()
    print("⚠️  重要提醒:")
    print("   - 建议先在测试环境中验证")
    print()
    
    get_open_orders()