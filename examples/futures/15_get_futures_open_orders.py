"""
TooBit 合约API SDK - 查看当前全部挂单示例 (15)
查看当前全部挂单 (需要API密钥和签名)
接口: GET /api/v1/futures/openOrders
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import FuturesOpenOrderResponse

def get_futures_open_orders():
    """查看当前全部挂单"""
    print("=== TooBit 合约API 查看当前全部挂单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 查询参数
        symbol = "BTC-SWAP-USDT"  # 交易对 (可选，不传则查询所有交易对的挂单)
        
        print("🔄 正在查询当前全部挂单...")
        if symbol:
            print(f"   交易对: {symbol}")
        else:
            print("   交易对: 全部")
        print()
        print("⚠️  注意: 这是真实的账户查询操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        response = client.get_futures_open_orders(symbol=symbol)
        
        print("✅ 挂单查询成功!")
        print()
        
        # 显示挂单信息
        if response and len(response) > 0:
            print(f"📊 当前挂单信息 (共{len(response)}个):")
            for i, order in enumerate(response):
                print(f"\n   挂单 {i+1}:")
                if hasattr(order, 'time'):
                    print(f"     ⏰ 订单生成时间: {order.time}")
                if hasattr(order, 'updateTime'):
                    print(f"     🔄 最后更新时间: {order.updateTime}")
                if hasattr(order, 'orderId'):
                    print(f"     🆔 订单ID: {order.orderId}")
                if hasattr(order, 'clientOrderId'):
                    print(f"     🔑 客户端订单ID: {order.clientOrderId}")
                if hasattr(order, 'symbol'):
                    print(f"     📊 交易对: {order.symbol}")
                if hasattr(order, 'price'):
                    print(f"     💰 订单价格: {order.price}")
                if hasattr(order, 'leverage'):
                    print(f"     📈 订单杠杆: {order.leverage}")
                if hasattr(order, 'origQty'):
                    print(f"     📊 订单数量: {order.origQty}")
                if hasattr(order, 'executedQty'):
                    print(f"     ✅ 已执行数量: {order.executedQty}")
                if hasattr(order, 'avgPrice'):
                    print(f"     📊 平均成交价格: {order.avgPrice}")
                if hasattr(order, 'marginLocked'):
                    print(f"     🔒 锁定保证金: {order.marginLocked}")
                if hasattr(order, 'type'):
                    print(f"     🔧 订单类型: {order.type}")
                if hasattr(order, 'side'):
                    print(f"     📈 买卖方向: {order.side}")
                if hasattr(order, 'timeInForce'):
                    print(f"     ⏰ 时效: {order.timeInForce}")
                if hasattr(order, 'status'):
                    print(f"     📈 订单状态: {order.status}")
                if hasattr(order, 'priceType'):
                    print(f"     🏷️  价格类型: {order.priceType}")
        else:
            print("   ℹ️  当前没有挂单")
        
        print("\n🎉 挂单查询完成!")
        return response
        
    except Exception as e:
        print(f"❌ 挂单查询失败: {e}")
        return None
    finally:
        client.close()

def cancel_order_from_open_orders():
    """基于挂单列表进行撤单操作"""
    print("=== TooBit 合约API 基于挂单列表撤单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 先获取挂单列表
        print("🔄 正在获取挂单列表...")
        open_orders = client.get_futures_open_orders()
        
        if not open_orders or len(open_orders) == 0:
            print("   ℹ️  当前没有挂单，无需撤单")
            return
        
        print(f"✅ 获取到 {len(open_orders)} 个挂单")
        print()
        
        # 选择第一个挂单进行撤单演示
        first_order = open_orders[0]
        print("🔄 正在撤销第一个挂单...")
        print(f"   订单ID: {first_order.orderId}")
        print(f"   交易对: {first_order.symbol}")
        print(f"   客户端订单ID: {first_order.clientOrderId}")
        print()
        print("⚠️  注意: 这是真实的撤单操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 执行撤单
        cancel_response = client.cancel_futures_order(
            symbol=first_order.symbol,
            order_id=first_order.orderId
        )
        
        print("✅ 撤单操作成功!")
        print()
        
        # 显示撤单结果
        print("📋 撤单结果:")
        if hasattr(cancel_response, 'orderId'):
            print(f"   🆔 订单ID: {cancel_response.orderId}")
        if hasattr(cancel_response, 'symbol'):
            print(f"   📊 交易对: {cancel_response.symbol}")
        if hasattr(cancel_response, 'status'):
            print(f"   📈 订单状态: {cancel_response.status}")
        
        print("\n🎉 撤单操作完成!")
        return cancel_response
        
    except Exception as e:
        print(f"❌ 撤单操作失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit 合约API SDK 查看当前全部挂单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的账户查询操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: GET /api/v1/futures/openOrders")
    print("   - 鉴权: 需要签名 (USER_DATA)")
    print("   - 功能: 查看当前全部挂单")
    print("   - 参数: symbol(可选)")
    print()
    print("💡 查询说明:")
    print("   - 不传symbol参数则查询所有交易对的挂单")
    print("   - 传入symbol参数则只查询指定交易对的挂单")
    print("   - 返回当前所有未成交的订单")
    print("   - 包括订单的详细信息和状态")
    print()
    print("📈 订单状态说明:")
    print("   - NEW: 新订单")
    print("   - PARTIALLY_FILLED: 部分成交")
    print("   - FILLED: 完全成交")
    print("   - CANCELED: 已取消")
    print("   - REJECTED: 已拒绝")
    print()
    print("⚠️  重要提醒:")
    print("   - 建议先在测试环境中验证")
    print("   - 挂单信息包含敏感的交易数据")
    print()

    get_futures_open_orders()
