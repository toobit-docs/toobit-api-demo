#!/usr/bin/env python3
"""
TooBit API Futures QueryUser feeFee RateExample (28Number)
QueryFutures User feeFee Rate
"""

from open_api_sdk import TooBitClient, TooBitConfig, QueryFuturesUserFeeRateRequest

def get_futures_user_fee_rate():
    """QueryFutures User feeFee RateExample"""
    print("=== TooBit API Futures QueryUser feeFee RateExample ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Futures User Fee Rate Test:")
        print()
        
        # Example1: QueryBTC-SWAP-USDTFeeFee Rate
        print("📊 Example 1: Query BTC-SWAP-USDT Fee Rate")
        print("   Parameters: symbol='BTC-SWAP-USDT'")
        print("   API: GET /api/v1/futures/userFeeRate")
        print("   Description: Query BTC-SWAP-USDT of User Fee Rate")
        print()
        
        request1 = QueryFuturesUserFeeRateRequest(symbol="BTC-SWAP-USDT")
        response1 = client.get_futures_user_fee_rate(request1)
        print(f"   Open Maker Fee Rate: {response1.openMakerFee}")
        print(f"   Open Taker Fee Rate: {response1.openTakerFee}")
        print(f"   Close Maker Fee Rate: {response1.closeMakerFee}")
        print(f"   Close Taker Fee Rate: {response1.closeTakerFee}")
        print()
        
        # Example2: QueryETH-SWAP-USDTFeeFee Rate
        print("📊 Example 2: Query ETH-SWAP-USDT Fee Rate")
        print("   Parameters: symbol='ETH-SWAP-USDT'")
        print("   API: GET /api/v1/futures/userFeeRate")
        print("   Description: Query ETH-SWAP-USDT of User Fee Rate")
        print()
        
        request2 = QueryFuturesUserFeeRateRequest(symbol="ETH-SWAP-USDT")
        response2 = client.get_futures_user_fee_rate(request2)
        print(f"   OpenOpen OrdersFee Rate: {response2.openMakerFee}")
        print(f"   OpenTakerFee Rate: {response2.openTakerFee}")
        print(f"   CloseOpen OrdersFee Rate: {response2.closeMakerFee}")
        print(f"   CloseTakerFee Rate: {response2.closeTakerFee}")
        print()
        
        # Example3: QueryMultipleitemsTrading pairFeeFee Rate
        print("📊 Example 3: Query Multiple Trading pair Fee Rate")
        print("   API: GET /api/v1/futures/userFeeRate")
        print("   Description: Query Multiple Trading pair of User Fee Rate Compare")
        print()
        
        symbols = ["BTC-SWAP-USDT", "ETH-SWAP-USDT", "BNB-SWAP-USDT"]
        for symbol in symbols:
            try:
                request = QueryFuturesUserFeeRateRequest(symbol=symbol)
                response = client.get_futures_user_fee_rate(request)
                print(f"   {symbol}:")
                print(f"     Open Maker: {response.openMakerFee}, Open Taker: {response.openTakerFee}")
                print(f"     Close Maker: {response.closeMakerFee}, Close Taker: {response.closeTakerFee}")
                print()
            except Exception as e:
                print(f"   {symbol}: Query Failed - {e}")
                print()
        
        print("🎉 Query Futures User Fee Rate Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Futures User Fee Rate Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_user_fee_rate()
