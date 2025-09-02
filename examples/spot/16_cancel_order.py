"""
TooBit API SDK - 撤销订单接口示例 (16)
撤销订单 (需要API密钥)
"""
from open_api_sdk import TooBitClient, TooBitConfig

def cancel_order():
    """撤销订单"""
    print("=== TooBit API 撤销订单 ===\n")
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
        
        # 选择第一个挂单进行撤单
        first_order = open_orders[0]
        symbol = first_order.symbol
        order_id = first_order.order_id
        
        print("🔄 正在撤销订单...")
        print(f"   交易对: {symbol}")
        print(f"   订单ID: {order_id}")
        print()
        print("⚠️  注意: 这是真实的交易操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 调用撤销订单接口
        cancel_response = client.cancel_order(symbol, order_id)
        
        print("✅ 订单撤销成功!")
        print()
        
        # 显示撤销结果
        print("📋 撤销结果:")
        print(f"   订单ID: {cancel_response.order_id}")
        print(f"   客户端订单ID: {cancel_response.client_order_id}")
        print(f"   交易对: {cancel_response.symbol}")
        print(f"   状态: {cancel_response.status}")
        print(f"   类型: {cancel_response.type}")
        print(f"   方向: {cancel_response.side}")
        print(f"   数量: {cancel_response.orig_qty}")
        print(f"   价格: {cancel_response.price}")
        print(f"   已执行数量: {cancel_response.executed_qty}")
        print(f"   交易时间: {cancel_response.transact_time}")
        
        print("\n🎉 撤销订单完成!")
        return cancel_response
        
    except Exception as e:
        print(f"❌ 撤销订单失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 撤销订单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的交易操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: DELETE /api/v1/spot/order")
    print("   - 鉴权: 需要签名 (TRADE)")
    print("   - 功能: 撤销订单")
    print("   - 参数: symbol, orderId")
    print()
    print("⚠️  重要提醒:")
    print("   - 建议先在测试环境中验证")
    print("   - 只能撤销未成交的订单")
    print()
    
    cancel_order()