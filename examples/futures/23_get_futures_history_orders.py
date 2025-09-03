#!/usr/bin/env python3
"""
TooBit API Futures QueryHistorical ordersExample (23Number)
QueryHistorical ordersRecord
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesHistoryOrdersRequest

def get_futures_history_orders():
    """QueryHistorical ordersExample"""
    print("=== TooBit API Futures QueryHistorical ordersExample ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Historical Orders Test:")
        print()
        
        # Example1: QueryAllHistorical orders
        print("📊 Example 1: Query All Historical Orders")
        print("   API: GET /api/v1/futures/historyOrders")
        print("   Description: Query all historical orders from the most recent 3 days")
        print()
        
        request1 = QueryFuturesHistoryOrdersRequest()
        response1 = client.get_futures_history_orders(request1)
        print(f"   Return Order quantity: {len(response1)}")
        if response1:
            order = response1[0]
            print(f"   First Order: {order.symbol} {order.side} {order.type}")
        print()
        
        # Example2: QuerySpecifiedTrading pairofHistorical orders
        print("📊 Example 2: Query Specified Trading pair of Historical Orders")
        print("   Parameters: symbol='BTC-SWAP-USDT'")
        print("   API: GET /api/v1/futures/historyOrders")
        print("   Description: Query BTC-SWAP-USDT of Historical Orders")
        print()
        
        request2 = QueryFuturesHistoryOrdersRequest(symbol="BTC-SWAP-USDT")
        response2 = client.get_futures_history_orders(request2)
        print(f"   ReturnOrder quantity: {len(response2)}")
        if response2:
            order = response2[0]
            print(f"   First Order: {order.symbol} {order.side} {order.type}")
        print()
        
        # Example3: QuerySpecifiedOrderID
        print("📊 Example 3: Query Specified Order ID")
        print("   Parameters: orderId='123456789'")
        print("   API: GET /api/v1/futures/historyOrders")
        print("   Description: Query historical record of specified order ID")
        print()
        
        request3 = QueryFuturesHistoryOrdersRequest(orderId="123456789")
        response3 = client.get_futures_history_orders(request3)
        print(f"   ReturnOrder quantity: {len(response3)}")
        if response3:
            order = response3[0]
            print(f"   OrderDetails: {order.symbol} {order.side} {order.type} {order.status}")
        print()
        
        # Example4: QuerySpecifiedTimeRange
        print("📊 Example 4: Query Specified Time Range")
        print("   Parameters: startTime=1672531200000, endTime=1672617600000, limit=10")
        print("   API: GET /api/v1/futures/historyOrders")
        print("   Description: Query Specified Time Range Within of Historical Orders, Limit 10 records")
        print()
        
        request4 = QueryFuturesHistoryOrdersRequest(
            startTime=1672531200000,
            endTime=1672617600000,
            limit=10
        )
        response4 = client.get_futures_history_orders(request4)
        print(f"   ReturnOrder quantity: {len(response4)}")
        if response4:
            order = response4[0]
            print(f"   First Order: {order.symbol} {order.side} {order.type}")
        print()
        
        print("🎉 Query Historical Orders Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Historical Orders Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_history_orders()
