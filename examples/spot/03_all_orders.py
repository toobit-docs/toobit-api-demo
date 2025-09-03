"""
TooBit API SDK - 查询所有订单接口示例 (03)
查询所有订单 (需要API密钥)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def get_all_orders():
    """查询所有订单"""
    print("=== TooBit API 查询所有订单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"  # 交易对
        
        print("🔄 正在查询所有订单...")
        print(f"   交易对: {symbol}")
        print()
        print("⚠️  注意: 这是真实的账户查询操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 调用查询所有订单接口
        all_orders = client.get_all_orders(symbol)
        
        print("✅ 所有订单查询成功!")
        print()
        
        # 显示订单信息
        if all_orders and len(all_orders) > 0:
            print(f"📊 所有订单信息 (共{len(all_orders)}个):")
            for i, order in enumerate(all_orders[:5]):  # 只显示前5个
                print(f"\n   订单 {i+1}:")
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
            
            if len(all_orders) > 5:
                print(f"\n   ... 还有 {len(all_orders) - 5} 个订单")
        else:
            print("   ℹ️  没有找到订单")
        
        print("\n🎉 查询所有订单完成!")
        return all_orders
        
    except Exception as e:
        print(f"❌ 查询所有订单失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 查询所有订单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的账户查询操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: GET /api/v1/spot/allOrders")
    print("   - 鉴权: 需要签名 (USER_DATA)")
    print("   - 功能: 查询所有订单")
    print("   - 参数: symbol")
    print()
    print("⚠️  重要提醒:")
    print("   - 建议先在测试环境中验证")
    print()
    
    get_all_orders()