#!/usr/bin/env python3
"""
TooBit API 合约批量下单示例 (15号)
批量创建多个合约订单
"""

import uuid
from open_api_sdk import TooBitClient, TooBitConfig, FuturesOrderRequest, OrderSide, OrderType

def batch_create_futures_orders():
    """合约批量下单示例"""
    print("=== TooBit API 合约批量下单示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 合约批量下单测试:")
        print()
        
        # 创建多个合约订单请求
        orders = [
            FuturesOrderRequest(
                newClientOrderId=f"pl2023010712345678900_{uuid.uuid4().hex[:8]}",
                symbol="BTC-SWAP-USDT",
                side=OrderSide.BUY_OPEN,
                type=OrderType.LIMIT,
                price=16500,
                quantity=10,
                priceType="INPUT"
            ),
            FuturesOrderRequest(
                newClientOrderId=f"pl2023010712345678901_{uuid.uuid4().hex[:8]}",
                symbol="BTC-SWAP-USDT",
                side=OrderSide.BUY_OPEN,
                type=OrderType.LIMIT,
                price=16000,
                quantity=10,
                priceType="INPUT"
            ),
            FuturesOrderRequest(
                newClientOrderId=f"pl2023010712345678902_{uuid.uuid4().hex[:8]}",
                symbol="BTC-SWAP-USDT",
                side=OrderSide.SELL_OPEN,
                type=OrderType.LIMIT,
                price=17000,
                quantity=5,
                priceType="INPUT"
            )
        ]
        
        print("📊 批量下单参数:")
        for i, order in enumerate(orders, 1):
            print(f"   订单{i}:")
            print(f"     客户端订单ID: {order.newClientOrderId}")
            print(f"     交易对: {order.symbol}")
            print(f"     方向: {order.side}")
            print(f"     类型: {order.type}")
            print(f"     价格: {order.price}")
            print(f"     数量: {order.quantity}")
            print(f"     价格类型: {order.priceType}")
            print()
        
        # 调用合约批量下单接口
        response = client.batch_create_futures_orders(orders)
        
        print("📊 批量下单响应:")
        print(f"   响应代码: {response.code}")
        print(f"   结果数量: {len(response.result)}")
        print()
        
        # 显示每个订单的结果
        for i, result in enumerate(response.result, 1):
            print(f"   订单{i}结果:")
            print(f"     代码: {result.code}")
            
            if result.code == 200:
                print("     ✅ 下单成功")
                if result.order:
                    order = result.order
                    print(f"     订单ID: {order.orderId}")
                    print(f"     客户端订单ID: {order.clientOrderId}")
                    print(f"     交易对: {order.symbol}")
                    print(f"     价格: {order.price}")
                    print(f"     数量: {order.origQty}")
                    print(f"     状态: {order.status}")
                    print(f"     时间: {order.time}")
            else:
                print("     ❌ 下单失败")
                if result.msg:
                    print(f"     失败原因: {result.msg}")
            print()
        
        print("🎉 合约批量下单测试完成!")
        
    except Exception as e:
        print(f"❌ 合约批量下单测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    batch_create_futures_orders()
