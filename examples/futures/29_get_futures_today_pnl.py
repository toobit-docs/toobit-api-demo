#!/usr/bin/env python3
"""
TooBit API Futures QueryTodayPnLExample (29Number)
QueryFutures TodayPnL
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_today_pnl():
    """QueryFutures TodayPnLExample"""
    print("=== TooBit API Futures QueryTodayPnLExample ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Futures Today PnL Test:")
        print()
        print("   API: GET /api/v1/futures/todayPnL")
        print("   Description: Query futures today PnL (UTC+0 timezone)")
        print()
        
        pnl = client.get_futures_today_pnl()
        print(f"   Today PnL: {pnl.dayProfit}")
        print(f"   Today PnL Rate: {pnl.dayProfitRate}")
        print()
        
        # PnL analysis
        profit = float(pnl.dayProfit)
        profit_rate = float(pnl.dayProfitRate)
        
        if profit > 0:
            print("   📈 Today profit status:")
            print(f"      Profit amount: {pnl.dayProfit}")
            print(f"      Profit rate: {pnl.dayProfitRate} ({profit_rate*100:.2f}%)")
        elif profit < 0:
            print("   📉 Today loss status:")
            print(f"      Loss amount: {pnl.dayProfit}")
            print(f"      Loss rate: {pnl.dayProfitRate} ({profit_rate*100:.2f}%)")
        else:
            print("   📊 Today PnL balanced:")
            print(f"      PnL amount: {pnl.dayProfit}")
            print(f"      PnL rate: {pnl.dayProfitRate}")
        
        print()
        print("🎉 Query Futures Today PnL Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Futures Today PnL Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_today_pnl()
