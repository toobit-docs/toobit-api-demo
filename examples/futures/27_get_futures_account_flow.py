#!/usr/bin/env python3
"""
TooBit API 合约查询账户流水示例 (27号)
查询合约账户流水记录
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesAccountFlowRequest

def get_futures_account_flow():
    """查询合约账户流水示例"""
    print("=== TooBit API 合约查询账户流水示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询合约账户流水测试:")
        print()
        
        # 示例1: 查询所有流水
        print("📊 示例1: 查询所有流水")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   说明: 查询所有账户流水记录")
        print()
        
        request1 = QueryFuturesAccountFlowRequest()
        response1 = client.get_futures_account_flow(request1)
        print(f"   返回流水记录数量: {len(response1)}")
        if response1:
            flow = response1[0]
            print(f"   第一条记录: {flow.coin} {flow.flowType} {flow.change}")
        print()
        
        # 示例2: 查询指定资产流水
        print("📊 示例2: 查询指定资产流水")
        print("   参数: symbol='USDT'")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   说明: 查询USDT资产的流水记录")
        print()
        
        request2 = QueryFuturesAccountFlowRequest(symbol="USDT")
        response2 = client.get_futures_account_flow(request2)
        print(f"   返回流水记录数量: {len(response2)}")
        if response2:
            flow = response2[0]
            print(f"   第一条记录: {flow.coin} {flow.flowType} {flow.change}")
        print()
        
        # 示例3: 查询手续费流水
        print("📊 示例3: 查询手续费流水")
        print("   参数: flowType=10 (手续费)")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   说明: 查询手续费类型的流水记录")
        print()
        
        request3 = QueryFuturesAccountFlowRequest(flowType=10)
        response3 = client.get_futures_account_flow(request3)
        print(f"   返回流水记录数量: {len(response3)}")
        if response3:
            flow = response3[0]
            print(f"   第一条记录: {flow.coin} {flow.flowType} {flow.change}")
        print()
        
        # 示例4: 查询指定时间范围
        print("📊 示例4: 查询指定时间范围")
        print("   参数: startTime=1672531200000, endTime=1672617600000, limit=10")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   说明: 查询指定时间范围内的流水记录，限制10条")
        print()
        
        request4 = QueryFuturesAccountFlowRequest(
            startTime=1672531200000,
            endTime=1672617600000,
            limit=10
        )
        response4 = client.get_futures_account_flow(request4)
        print(f"   返回流水记录数量: {len(response4)}")
        if response4:
            flow = response4[0]
            print(f"   第一条记录: {flow.coin} {flow.flowType} {flow.change}")
        print()
        
        # 示例5: 查询详细信息
        print("📊 示例5: 查询详细信息")
        print("   参数: symbol='BTC', limit=5")
        print("   API: GET /api/v1/futures/balanceFlow")
        print("   说明: 查询BTC资产的详细流水信息")
        print()
        
        request5 = QueryFuturesAccountFlowRequest(
            symbol="BTC",
            limit=5
        )
        response5 = client.get_futures_account_flow(request5)
        print(f"   返回流水记录数量: {len(response5)}")
        if response5:
            for i, flow in enumerate(response5[:3]):  # 只显示前3条
                print(f"   记录{i+1}: {flow.coin} {flow.flowType}")
                print(f"       变动: {flow.change}, 余额: {flow.total}")
                print(f"       类型: {flow.flowName} ({flow.flowTypeValue})")
                print(f"       时间: {flow.created}")
                print()
        
        print("🎉 查询合约账户流水测试完成!")
        
    except Exception as e:
        print(f"❌ 查询合约账户流水测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_account_flow()
