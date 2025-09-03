"""
TooBit API SDK - 下单接口示例 (05)
创建各种类型的订单 (需要API密钥)
"""
import uuid
from open_api_sdk import (
    TooBitClient, TooBitConfig, OrderRequest, 
    OrderSide, OrderType, TimeInForce
)

def create_limit_order():
    """创建限价单"""
    print("=== TooBit API 创建限价单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 创建限价买入订单
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            quantity=0.001,  # 买入0.001 BTC
            price=50000.0,   # 限价50000 USDT
            time_in_force=TimeInForce.GTC,  # 一直有效直到取消
            client_order_id=f"order_{uuid.uuid4().hex[:8]}"  # 客户端订单ID
        )
        
        print("🔄 正在创建限价单...")
        print(f"   交易对: {order_request.symbol}")
        print(f"   方向: {order_request.side}")
        print(f"   类型: {order_request.type}")
        print(f"   数量: {order_request.quantity}")
        print(f"   价格: {order_request.price}")
        print()
        print("⚠️  注意: 这是真实的交易操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        
        # 调用创建订单接口
        order_response = client.create_order(order_request)
        
        print("✅ 限价单创建成功!")
        print()
        
        # 显示订单信息
        print("📋 订单信息:")
        print(f"   订单ID: {order_response.order_id}")
        print(f"   客户端订单ID: {order_response.client_order_id}")
        print(f"   交易对: {order_response.symbol}")
        print(f"   状态: {order_response.status}")
        print(f"   类型: {order_response.type}")
        print(f"   方向: {order_response.side}")
        print(f"   数量: {order_response.orig_qty}")
        print(f"   价格: {order_response.price}")
        print(f"   已执行数量: {order_response.executed_qty}")
        print(f"   交易时间: {order_response.transact_time}")
        
        print("\n🎉 创建限价单完成!")
        return order_response
        
    except Exception as e:
        print(f"❌ 创建限价单失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit API SDK 创建限价单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的交易操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: POST /api/v1/spot/order")
    print("   - 鉴权: 需要签名 (TRADE)")
    print("   - 功能: 创建限价单")
    print("   - 参数: symbol, side, type, quantity, price, timeInForce")
    print()
    print("⚠️  重要提醒:")
    print("   - 建议先在测试环境中验证")
    print("   - 订单创建后无法撤销")
    print()
    
    create_limit_order()