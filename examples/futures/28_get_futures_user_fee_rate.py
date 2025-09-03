#!/usr/bin/env python3
"""
TooBit API 合约查询用户手续费率示例 (28号)
查询合约用户手续费率
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesUserFeeRateRequest

def get_futures_user_fee_rate():
    """查询合约用户手续费率示例"""
    print("=== TooBit API 合约查询用户手续费率示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询合约用户手续费率测试:")
        print()
        
        # 示例1: 查询BTC-SWAP-USDT手续费率
        print("📊 示例1: 查询BTC-SWAP-USDT手续费率")
        print("   参数: symbol='BTC-SWAP-USDT'")
        print("   API: GET /api/v1/futures/userFeeRate")
        print("   说明: 查询BTC-SWAP-USDT的用户手续费率")
        print()
        
        request1 = QueryFuturesUserFeeRateRequest(symbol="BTC-SWAP-USDT")
        response1 = client.get_futures_user_fee_rate(request1)
        print(f"   开仓挂单费率: {response1.openMakerFee}")
        print(f"   开仓吃单费率: {response1.openTakerFee}")
        print(f"   平仓挂单费率: {response1.closeMakerFee}")
        print(f"   平仓吃单费率: {response1.closeTakerFee}")
        print()
        
        # 示例2: 查询ETH-SWAP-USDT手续费率
        print("📊 示例2: 查询ETH-SWAP-USDT手续费率")
        print("   参数: symbol='ETH-SWAP-USDT'")
        print("   API: GET /api/v1/futures/userFeeRate")
        print("   说明: 查询ETH-SWAP-USDT的用户手续费率")
        print()
        
        request2 = QueryFuturesUserFeeRateRequest(symbol="ETH-SWAP-USDT")
        response2 = client.get_futures_user_fee_rate(request2)
        print(f"   开仓挂单费率: {response2.openMakerFee}")
        print(f"   开仓吃单费率: {response2.openTakerFee}")
        print(f"   平仓挂单费率: {response2.closeMakerFee}")
        print(f"   平仓吃单费率: {response2.closeTakerFee}")
        print()
        
        # 示例3: 查询多个交易对手续费率
        print("📊 示例3: 查询多个交易对手续费率")
        print("   API: GET /api/v1/futures/userFeeRate")
        print("   说明: 查询多个交易对的用户手续费率对比")
        print()
        
        symbols = ["BTC-SWAP-USDT", "ETH-SWAP-USDT", "BNB-SWAP-USDT"]
        for symbol in symbols:
            try:
                request = QueryFuturesUserFeeRateRequest(symbol=symbol)
                response = client.get_futures_user_fee_rate(request)
                print(f"   {symbol}:")
                print(f"     开仓挂单: {response.openMakerFee}, 开仓吃单: {response.openTakerFee}")
                print(f"     平仓挂单: {response.closeMakerFee}, 平仓吃单: {response.closeTakerFee}")
                print()
            except Exception as e:
                print(f"   {symbol}: 查询失败 - {e}")
                print()
        
        print("🎉 查询合约用户手续费率测试完成!")
        
    except Exception as e:
        print(f"❌ 查询合约用户手续费率测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_user_fee_rate()
