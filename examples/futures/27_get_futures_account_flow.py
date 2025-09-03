#!/usr/bin/env python3
"""
TooBit API Futures QueryAccountFlowExample (27Number)
QueryFutures AccountFlowRecord
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesAccountFlowRequest

def get_futures_account_flow():
    """QueryFutures AccountFlowExample"""
    print("=== TooBit API Futures QueryAccountFlowExample ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Futures Account Flow Test:")
        print()
        
        # Example1: QueryAllFlow
        print("📊 Example 1: Query All Flow")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   Description: Query All Account Flow Record")
        print()
        
        request1 = QueryFuturesAccountFlowRequest()
        response1 = client.get_futures_account_flow(request1)
        print(f"   Return Flow Record Quantity: {len(response1)}")
        if response1:
            flow = response1[0]
            print(f"   First Record: {flow.coin} {flow.flowType} {flow.change}")
        print()
        
        # Example2: QuerySpecifiedAssetFlow
        print("📊 Example 2: Query Specified Asset Flow")
        print("   Parameters: symbol='USDT'")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   Description: Query USDT Asset of Flow Record")
        print()
        
        request2 = QueryFuturesAccountFlowRequest(symbol="USDT")
        response2 = client.get_futures_account_flow(request2)
        print(f"   ReturnFlowRecordQuantity: {len(response2)}")
        if response2:
            flow = response2[0]
            print(f"   First Record: {flow.coin} {flow.flowType} {flow.change}")
        print()
        
        # Example3: QueryFeeFlow
        print("📊 Example 3: Query Fee Flow")
        print("   Parameters: flowType=10 (Fee)")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   Description: Query Fee Type of Flow Record")
        print()
        
        request3 = QueryFuturesAccountFlowRequest(flowType=10)
        response3 = client.get_futures_account_flow(request3)
        print(f"   ReturnFlowRecordQuantity: {len(response3)}")
        if response3:
            flow = response3[0]
            print(f"   First Record: {flow.coin} {flow.flowType} {flow.change}")
        print()
        
        # Example4: QuerySpecifiedTimeRange
        print("📊 Example 4: Query Specified Time Range")
        print("   Parameters: startTime=1672531200000, endTime=1672617600000, limit=10")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   Description: Query Specified Time Range Within of Flow Record, Limit 10 records")
        print()
        
        request4 = QueryFuturesAccountFlowRequest(
            startTime=1672531200000,
            endTime=1672617600000,
            limit=10
        )
        response4 = client.get_futures_account_flow(request4)
        print(f"   ReturnFlowRecordQuantity: {len(response4)}")
        if response4:
            flow = response4[0]
            print(f"   First Record: {flow.coin} {flow.flowType} {flow.change}")
        print()
        
        # Example5: QueryDetailedInformation
        print("📊 Example 5: Query Detailed Information")
        print("   Parameters: symbol='BTC', limit=5")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   Description: Query BTC Asset of Detailed Flow Information")
        print()
        
        request5 = QueryFuturesAccountFlowRequest(
            symbol="BTC",
            limit=5
        )
        response5 = client.get_futures_account_flow(request5)
        print(f"   ReturnFlowRecordQuantity: {len(response5)}")
        if response5:
            for i, flow in enumerate(response5[:3]):  # Only Display Before 3 records
                print(f"   Record {i+1}: {flow.coin} {flow.flowType}")
                print(f"       Change: {flow.change}, Balance: {flow.total}")
                print(f"       Type: {flow.flowName} ({flow.flowTypeValue})")
                print(f"       Time: {flow.created}")
                print()
        
        print("🎉 Query Futures Account Flow Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Futures Account Flow Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_account_flow()
