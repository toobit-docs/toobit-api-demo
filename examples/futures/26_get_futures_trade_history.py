#!/usr/bin/env python3
"""
TooBit API 合约查询账户成交历史示例 (26号)
查询合约账户成交历史记录
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesTradeHistoryRequest

def get_futures_trade_history():
    """查询合约账户成交历史示例"""
    print("=== TooBit API 合约查询账户成交历史示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询合约账户成交历史测试:")
        print()
        
        # 示例1: 查询指定交易对的成交历史
        print("📊 示例1: 查询指定交易对的成交历史")
        print("   参数: symbol='BTC-SWAP-USDT'")
        print("   API: GET /api/v1/futures/userTrades")
        print("   说明: 查询BTC-SWAP-USDT的成交历史")
        print()
        
        request1 = QueryFuturesTradeHistoryRequest(symbol="BTC-SWAP-USDT")
        response1 = client.get_futures_trade_history(request1)
        print(f"   返回成交记录数量: {len(response1)}")
        if response1:
            trade = response1[0]
            print(f"   第一条记录: {trade.symbol} {trade.side} {trade.price} {trade.qty}")
        print()
        
        # 示例2: 查询指定时间范围
        print("📊 示例2: 查询指定时间范围")
        print("   参数: symbol='BTC-SWAP-USDT', startTime=1672531200000, endTime=1672617600000")
        print("   API: GET /api/v1/futures/userTrades")
        print("   说明: 查询指定时间范围内的成交历史")
        print()
        
        request2 = QueryFuturesTradeHistoryRequest(
            symbol="BTC-SWAP-USDT",
            startTime=1672531200000,
            endTime=1672617600000
        )
        response2 = client.get_futures_trade_history(request2)
        print(f"   返回成交记录数量: {len(response2)}")
        if response2:
            trade = response2[0]
            print(f"   第一条记录: {trade.symbol} {trade.side} {trade.price} {trade.qty}")
        print()
        
        # 示例3: 查询指定TradeId范围
        print("📊 示例3: 查询指定TradeId范围")
        print("   参数: symbol='BTC-SWAP-USDT', fromId=1000, toId=2000, limit=10")
        print("   API: GET /api/v1/futures/userTrades")
        print("   说明: 查询指定TradeId范围内的成交历史，限制10条")
        print()
        
        request3 = QueryFuturesTradeHistoryRequest(
            symbol="BTC-SWAP-USDT",
            fromId=1000,
            toId=2000,
            limit=10
        )
        response3 = client.get_futures_trade_history(request3)
        print(f"   返回成交记录数量: {len(response3)}")
        if response3:
            trade = response3[0]
            print(f"   第一条记录: {trade.symbol} {trade.side} {trade.price} {trade.qty}")
        print()
        
        # 示例4: 查询详细信息
        print("📊 示例4: 查询详细信息")
        print("   参数: symbol='ETH-SWAP-USDT', limit=5")
        print("   API: GET /api/v1/futures/userTrades")
        print("   说明: 查询ETH-SWAP-USDT的详细成交信息")
        print()
        
        request4 = QueryFuturesTradeHistoryRequest(
            symbol="ETH-SWAP-USDT",
            limit=5
        )
        response4 = client.get_futures_trade_history(request4)
        print(f"   返回成交记录数量: {len(response4)}")
        if response4:
            for i, trade in enumerate(response4[:3]):  # 只显示前3条
                print(f"   记录{i+1}: {trade.symbol} {trade.side} {trade.type}")
                print(f"       价格: {trade.price}, 数量: {trade.qty}")
                print(f"       手续费: {trade.commission} {trade.commissionAsset}")
                print(f"       成交时间: {trade.time}")
                print()
        
        print("🎉 查询合约账户成交历史测试完成!")
        
    except Exception as e:
        print(f"❌ 查询合约账户成交历史测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_trade_history()
