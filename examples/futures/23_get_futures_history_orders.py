#!/usr/bin/env python3
"""
TooBit API 合约查询历史订单示例 (23号)
查询历史订单记录
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesHistoryOrdersRequest

def get_futures_history_orders():
    """查询历史订单示例"""
    print("=== TooBit API 合约查询历史订单示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询历史订单测试:")
        print()
        
        # 示例1: 查询所有历史订单
        print("📊 示例1: 查询所有历史订单")
        print("   API: GET /api/v1/futures/historyOrders")
        print("   说明: 查询最近3天的所有历史订单")
        print()
        
        request1 = QueryFuturesHistoryOrdersRequest()
        response1 = client.get_futures_history_orders(request1)
        print(f"   返回订单数量: {len(response1)}")
        if response1:
            order = response1[0]
            print(f"   第一个订单: {order.symbol} {order.side} {order.type}")
        print()
        
        # 示例2: 查询指定交易对的历史订单
        print("📊 示例2: 查询指定交易对的历史订单")
        print("   参数: symbol='BTC-SWAP-USDT'")
        print("   API: GET /api/v1/futures/historyOrders")
        print("   说明: 查询BTC-SWAP-USDT的历史订单")
        print()
        
        request2 = QueryFuturesHistoryOrdersRequest(symbol="BTC-SWAP-USDT")
        response2 = client.get_futures_history_orders(request2)
        print(f"   返回订单数量: {len(response2)}")
        if response2:
            order = response2[0]
            print(f"   第一个订单: {order.symbol} {order.side} {order.type}")
        print()
        
        # 示例3: 查询指定订单ID
        print("📊 示例3: 查询指定订单ID")
        print("   参数: orderId='123456789'")
        print("   API: GET /api/v1/futures/historyOrders")
        print("   说明: 查询指定订单ID的历史记录")
        print()
        
        request3 = QueryFuturesHistoryOrdersRequest(orderId="123456789")
        response3 = client.get_futures_history_orders(request3)
        print(f"   返回订单数量: {len(response3)}")
        if response3:
            order = response3[0]
            print(f"   订单详情: {order.symbol} {order.side} {order.type} {order.status}")
        print()
        
        # 示例4: 查询指定时间范围
        print("📊 示例4: 查询指定时间范围")
        print("   参数: startTime=1672531200000, endTime=1672617600000, limit=10")
        print("   API: GET /api/v1/futures/historyOrders")
        print("   说明: 查询指定时间范围内的历史订单，限制10条")
        print()
        
        request4 = QueryFuturesHistoryOrdersRequest(
            startTime=1672531200000,
            endTime=1672617600000,
            limit=10
        )
        response4 = client.get_futures_history_orders(request4)
        print(f"   返回订单数量: {len(response4)}")
        if response4:
            order = response4[0]
            print(f"   第一个订单: {order.symbol} {order.side} {order.type}")
        print()
        
        print("🎉 查询历史订单测试完成!")
        
    except Exception as e:
        print(f"❌ 查询历史订单测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_history_orders()
