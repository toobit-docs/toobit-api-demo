"""
TooBit 合约API SDK - 撤销全部订单示例
撤销全部订单 (需要API密钥和签名)
接口: DELETE /api/v1/futures/order
"""
from open_api_sdk import TooBitClient, TooBitConfig

def cancel_all_orders():
    """撤销全部订单"""
    print("=== TooBit 合约API 撤销全部订单 ===\n")
    try:
        config = TooBitConfig(api_key="test_key", api_secret="test_secret")
        client = TooBitClient(config)
        symbol = "BTCUSDT"  # 交易对
        print("🔄 正在撤销全部订单...")
        print(f"   交易对: {symbol}")
        print()
        print("⚠️  注意: 这是真实的交易操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        response = client.cancel_all_orders(symbol)
        print("✅ 撤销全部订单成功!")
        print()
        if response and len(response) > 0:
            print(f"📊 撤销结果 (共{len(response)}个订单):")
            for i, order in enumerate(response):
                print(f"\n   订单 {i+1}:")
                if 'symbol' in order:
                    print(f"     📋 交易对: {order['symbol']}")
                if 'orderId' in order:
                    print(f"     🆔 订单ID: {order['orderId']}")
                if 'clientOrderId' in order:
                    print(f"     🔑 客户端订单ID: {order['clientOrderId']}")
                if 'price' in order:
                    print(f"     💰 价格: {order['price']}")
                if 'origQty' in order:
                    print(f"     📊 原始数量: {order['origQty']}")
                if 'executedQty' in order:
                    print(f"     ✅ 已执行数量: {order['executedQty']}")
                if 'status' in order:
                    print(f"     📈 状态: {order['status']}")
                if 'timeInForce' in order:
                    print(f"     ⏰ 时效: {order['timeInForce']}")
                if 'type' in order:
                    print(f"     🔧 类型: {order['type']}")
                if 'side' in order:
                    print(f"     📈 方向: {order['side']}")
                if 'transactTime' in order:
                    print(f"     🕐 交易时间: {order['transactTime']}")
        else:
            print("   ℹ️  没有订单被撤销")
        print("\n🎉 撤销全部订单完成!")
        return response
    except Exception as e:
        print(f"❌ 撤销全部订单失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit 合约API SDK 撤销全部订单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的交易操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: DELETE /api/v1/futures/order")
    print("   - 鉴权: 需要签名 (TRADE)")
    print("   - 功能: 撤销指定交易对的所有订单")
    print("   - 参数: symbol")
    print()
    print("⚠️  重要提醒:")
    print("   - 此操作不可逆")
    print("   - 将撤销所有未成交的订单")
    print("   - 请确保这是您想要的操作")
    cancel_all_orders()
