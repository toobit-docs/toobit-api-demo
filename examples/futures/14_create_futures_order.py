"""
TooBit 合约API SDK - 合约下单示例
合约下单 (需要API密钥和签名)
接口: POST /api/v1/futures/order
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import OrderRequest, OrderSide, OrderType, TimeInForce, CreateFuturesOrderResponse

def create_futures_order():
    """合约下单"""
    print("=== TooBit 合约API 合约下单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 订单参数
        symbol = "BTC-SWAP-USDT"  # 交易对
        side = OrderSide.BUY_OPEN  # 买卖方向: BUY_OPEN, SELL_OPEN, BUY_CLOSE, SELL_CLOSE
        order_type = OrderType.LIMIT  # 订单类型: LIMIT, MARKET
        quantity = "10"  # 数量
        price = "50000"  # 价格 (市价单不需要)
        time_in_force = TimeInForce.GTC  # 时效: GTC, IOC, FOK
        client_order_id = "test_order_006"  # 客户端订单ID (可选)
        
        print("🔄 正在创建合约订单...")
        print(f"   交易对: {symbol}")
        print(f"   买卖方向: {side.value}")
        print(f"   订单类型: {order_type.value}")
        print(f"   数量: {quantity}")
        print(f"   价格: {price}")
        print(f"   时效: {time_in_force.value}")
        print(f"   客户端订单ID: {client_order_id}")
        print()
        print("⚠️  注意: 这是真实的交易操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 创建订单请求
        order_request = OrderRequest(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price,
            timeInForce=time_in_force,
            newClientOrderId=client_order_id
        )
        
        response = client.create_futures_order(order_request)
        
        print("✅ 合约订单创建成功!")
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
        
        print("\n🎉 合约订单创建完成!")
        return response
        
    except Exception as e:
        print(f"❌ 合约订单创建失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit 合约API SDK 合约下单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的交易操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: POST /api/v1/futures/order")
    print("   - 鉴权: 需要签名 (TRADE)")
    print("   - 功能: 创建合约订单")
    print("   - 支持: 限价单、市价单")
    print()
    print("📈 合约方向类型说明:")
    print("   - BUY_OPEN: 买入开仓 (做多)")
    print("   - SELL_OPEN: 卖出开仓 (做空)")
    print("   - BUY_CLOSE: 买入平仓 (平空)")
    print("   - SELL_CLOSE: 卖出平仓 (平多)")
    print()
    print("⚠️  重要提醒:")
    print("   - 请确保账户余额充足")
    print("   - 请仔细核对订单参数")
    print("   - 订单创建后不可撤销")
    print("   - 建议先在测试环境中验证")
    create_futures_order()
