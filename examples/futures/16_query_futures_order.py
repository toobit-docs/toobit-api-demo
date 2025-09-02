"""
TooBit 合约API SDK - 查询订单示例 (16)
查询合约订单 (需要API密钥和签名)
接口: GET /api/v1/futures/order
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import QueryFuturesOrderResponse

def query_futures_order():
    """查询合约订单"""
    print("=== TooBit 合约API 查询订单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 先查询挂单列表
        print("🔄 正在查询挂单列表...")
        open_orders = client.get_futures_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  当前没有挂单，无法查询订单详情")
            return None
        
        print(f"✅ 获取到 {len(open_orders)} 个挂单")
        print()
        
        # 选择第一个挂单进行查询
        first_order = open_orders[0]
        symbol = first_order.symbol
        order_id = first_order.orderId
        client_order_id = first_order.clientOrderId
        
        print("🔄 正在查询合约订单详情...")
        print(f"   交易对: {symbol}")
        print(f"   订单ID: {order_id}")
        print(f"   客户端订单ID: {client_order_id}")
        print()
        print("⚠️  注意: 这是真实的账户查询操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        response = client.get_futures_order(
            symbol=symbol,
            order_id=order_id,
            client_order_id=client_order_id
        )
        
        print("✅ 合约订单查询成功!")
        print()
        
        # 显示订单信息
        print("📋 订单信息:")
        if hasattr(response, 'time'):
            print(f"   ⏰ 订单生成时间: {response.time}")
        if hasattr(response, 'updateTime'):
            print(f"   🔄 最后更新时间: {response.updateTime}")
        if hasattr(response, 'orderId'):
            print(f"   🆔 订单ID: {response.orderId}")
        if hasattr(response, 'clientOrderId'):
            print(f"   🔑 客户端订单ID: {response.clientOrderId}")
        if hasattr(response, 'symbol'):
            print(f"   📊 交易对: {response.symbol}")
        if hasattr(response, 'price'):
            print(f"   💰 订单价格: {response.price}")
        if hasattr(response, 'leverage'):
            print(f"   📈 订单杠杆: {response.leverage}")
        if hasattr(response, 'origQty'):
            print(f"   📊 订单数量: {response.origQty}")
        if hasattr(response, 'executedQty'):
            print(f"   ✅ 已执行数量: {response.executedQty}")
        if hasattr(response, 'avgPrice'):
            print(f"   📊 平均成交价格: {response.avgPrice}")
        if hasattr(response, 'marginLocked'):
            print(f"   🔒 锁定保证金: {response.marginLocked}")
        if hasattr(response, 'type'):
            print(f"   🔧 订单类型: {response.type}")
        if hasattr(response, 'side'):
            print(f"   📈 买卖方向: {response.side}")
        if hasattr(response, 'timeInForce'):
            print(f"   ⏰ 时效: {response.timeInForce}")
        if hasattr(response, 'status'):
            print(f"   📈 订单状态: {response.status}")
        if hasattr(response, 'priceType'):
            print(f"   🏷️  价格类型: {response.priceType}")
        
        print("\n🎉 合约订单查询完成!")
        return response
        
    except Exception as e:
        print(f"❌ 合约订单查询失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit 合约API SDK 查询订单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的账户查询操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: GET /api/v1/futures/order")
    print("   - 鉴权: 需要签名 (USER_DATA)")
    print("   - 功能: 查询合约订单")
    print("   - 参数: symbol(必需), orderId(可选), origClientOrderId(可选)")
    print()
    print("💡 查询说明:")
    print("   - 可以通过订单ID查询")
    print("   - 可以通过客户端订单ID查询")
    print("   - 返回订单的详细信息")
    print("   - 包括订单状态、执行情况等")
    print()
    print("📈 订单状态说明:")
    print("   - NEW: 新订单")
    print("   - PARTIALLY_FILLED: 部分成交")
    print("   - FILLED: 完全成交")
    print("   - CANCELED: 已取消")
    print("   - REJECTED: 已拒绝")
    print()
    print("⚠️  重要提醒:")
    print("   - 请确保订单ID或客户端订单ID正确")
    print("   - 建议先在测试环境中验证")
    query_futures_order()
