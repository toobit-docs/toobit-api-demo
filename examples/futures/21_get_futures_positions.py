#!/usr/bin/env python3
"""
TooBit API 合约查询当前持仓示例 (21号)
查询当前持仓信息，支持按交易对和方向筛选
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_positions():
    """查询当前持仓示例"""
    print("=== TooBit API 合约查询当前持仓示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询当前持仓测试:")
        print()
        
        # 示例1: 查询所有持仓
        print("📊 示例1: 查询所有持仓")
        print("   参数: 无")
        print("   API: GET /api/v1/futures/positions")
        print("   说明: 查询账户下所有合约持仓")
        print()
        
        response1 = client.get_futures_positions()
        print(f"   响应数量: {len(response1)} 个持仓")
        if response1:
            print("   持仓列表:")
            for i, position in enumerate(response1, 1):
                print(f"     持仓{i}: {position.symbol} - {position.side}")
        print()
        
        # 示例2: 查询指定交易对的持仓
        print("📊 示例2: 查询指定交易对的持仓")
        print("   参数: symbol='BTC-SWAP-USDT'")
        print("   API: GET /api/v1/futures/positions?symbol=BTC-SWAP-USDT")
        print("   说明: 查询BTC-SWAP-USDT交易对的所有持仓")
        print()
        
        response2 = client.get_futures_positions(symbol='BTC-SWAP-USDT')
        print(f"   响应数量: {len(response2)} 个持仓")
        if response2:
            print("   持仓详情:")
            for position in response2:
                print(f"     交易对: {position.symbol}")
                print(f"     方向: {position.side}")
                print(f"     数量: {position.position} 张")
                print(f"     可平仓: {position.available} 张")
                print(f"     杠杆: {position.leverage}x")
                print(f"     平均价格: {position.avgPrice}")
                print(f"     最新价格: {position.lastPrice}")
                print(f"     标记价格: {position.markPrice}")
                print(f"     未实现盈亏: {position.unrealizedPnL}")
                print(f"     已实现盈亏: {position.realizedPnL}")
                print(f"     保证金: {position.margin}")
                print(f"     保证金率: {position.marginRate}")
                print(f"     强制平仓价: {position.flp}")
                print()
        
        # 示例3: 查询指定交易对和方向的持仓
        print("📊 示例3: 查询指定交易对和方向的持仓")
        print("   参数: symbol='BTC-SWAP-USDT', side='LONG'")
        print("   API: GET /api/v1/futures/positions?symbol=BTC-SWAP-USDT&side=LONG")
        print("   说明: 查询BTC-SWAP-USDT交易对的多头持仓")
        print()
        
        response3 = client.get_futures_positions(symbol='BTC-SWAP-USDT', side='LONG')
        print(f"   响应数量: {len(response3)} 个持仓")
        if response3:
            print("   多头持仓详情:")
            for position in response3:
                print(f"     交易对: {position.symbol}")
                print(f"     方向: {position.side}")
                print(f"     数量: {position.position} 张")
                print(f"     可平仓: {position.available} 张")
                print(f"     杠杆: {position.leverage}x")
                print(f"     平均价格: {position.avgPrice}")
                print(f"     最新价格: {position.lastPrice}")
                print(f"     未实现盈亏: {position.unrealizedPnL}")
                print(f"     已实现盈亏: {position.realizedPnL}")
                print(f"     保证金: {position.margin}")
                print(f"     保证金率: {position.marginRate}")
                print(f"     强制平仓价: {position.flp}")
                print()
        
        # 示例4: 查询指定方向的持仓
        print("📊 示例4: 查询指定方向的持仓")
        print("   参数: side='SHORT'")
        print("   API: GET /api/v1/futures/positions?side=SHORT")
        print("   说明: 查询所有空头持仓")
        print()
        
        response4 = client.get_futures_positions(side='SHORT')
        print(f"   响应数量: {len(response4)} 个持仓")
        if response4:
            print("   空头持仓列表:")
            for position in response4:
                print(f"     {position.symbol} - {position.side} - {position.position} 张")
        print()
        
        print("🎉 查询当前持仓测试完成!")
        
    except Exception as e:
        print(f"❌ 查询当前持仓测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_positions()
