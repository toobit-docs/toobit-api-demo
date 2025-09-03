#!/usr/bin/env python3
"""
TooBit API Futures QueryAccountTrade historyExample (26Number)
QueryFutures AccountTrade historyRecord
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesTradeHistoryRequest

def get_futures_trade_history():
    """QueryFutures AccountTrade historyExample"""
    print("=== TooBit API Futures QueryAccountTrade historyExample ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Futures Account Trade History Test:")
        print()
        
        # Example1: QuerySpecifiedTrading pairofTrade history
        print("📊 Example 1: Query Specified Trading pair of Trade History")
        print("   Parameters: symbol='BTC-SWAP-USDT'")
        print("   API: GET /api/v1/futures/userTrades")
        print("   Description: Query BTC-SWAP-USDT of Trade History")
        print()
        
        request1 = QueryFuturesTradeHistoryRequest(symbol="BTC-SWAP-USDT")
        response1 = client.get_futures_trade_history(request1)
        print(f"   Return Execution Record Quantity: {len(response1)}")
        if response1:
            trade = response1[0]
            print(f"   First Record: {trade.symbol} {trade.side} {trade.price} {trade.qty}")
        print()
        
        # Example2: QuerySpecifiedTimeRange
        print("📊 Example 2: Query Specified Time Range")
        print("   Parameters: symbol='BTC-SWAP-USDT', startTime=1672531200000, endTime=1672617600000")
        print("   API: GET /api/v1/futures/userTrades")
        print("   Description: Query Specified Time Range Within of Trade History")
        print()
        
        request2 = QueryFuturesTradeHistoryRequest(
            symbol="BTC-SWAP-USDT",
            startTime=1672531200000,
            endTime=1672617600000
        )
        response2 = client.get_futures_trade_history(request2)
        print(f"   ReturnExecutionRecordQuantity: {len(response2)}")
        if response2:
            trade = response2[0]
            print(f"   First Record: {trade.symbol} {trade.side} {trade.price} {trade.qty}")
        print()
        
        # Example3: QuerySpecifiedTradeIdRange
        print("📊 Example 3: Query Specified Trade ID Range")
        print("   Parameters: symbol='BTC-SWAP-USDT', fromId=1000, toId=2000, limit=10")
        print("   API: GET /api/v1/futures/userTrades")
        print("   Description: Query Specified Trade ID Range Within of Trade History, Limit 10 records")
        print()
        
        request3 = QueryFuturesTradeHistoryRequest(
            symbol="BTC-SWAP-USDT",
            fromId=1000,
            toId=2000,
            limit=10
        )
        response3 = client.get_futures_trade_history(request3)
        print(f"   ReturnExecutionRecordQuantity: {len(response3)}")
        if response3:
            trade = response3[0]
            print(f"   First Record: {trade.symbol} {trade.side} {trade.price} {trade.qty}")
        print()
        
        # Example4: QueryDetailedInformation
        print("📊 Example 4: Query Detailed Information")
        print("   Parameters: symbol='ETH-SWAP-USDT', limit=5")
        print("   API: GET /api/v1/futures/userTrades")
        print("   Description: Query ETH-SWAP-USDT of Detailed Execution Information")
        print()
        
        request4 = QueryFuturesTradeHistoryRequest(
            symbol="ETH-SWAP-USDT",
            limit=5
        )
        response4 = client.get_futures_trade_history(request4)
        print(f"   ReturnExecutionRecordQuantity: {len(response4)}")
        if response4:
            for i, trade in enumerate(response4[:3]):  # Only Display Before 3 records
                print(f"   Record {i+1}: {trade.symbol} {trade.side} {trade.type}")
                print(f"       Price: {trade.price}, Quantity: {trade.qty}")
                print(f"       Fee: {trade.commission} {trade.commissionAsset}")
                print(f"       Execution Time: {trade.time}")
                print()
        
        print("🎉 Query Futures Account Trade History Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Futures Account Trade History Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_trade_history()
