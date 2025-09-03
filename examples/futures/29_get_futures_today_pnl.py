#!/usr/bin/env python3
"""
TooBit API 合约查询今日盈亏示例 (29号)
查询合约今日盈亏
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_today_pnl():
    """查询合约今日盈亏示例"""
    print("=== TooBit API 合约查询今日盈亏示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询合约今日盈亏测试:")
        print()
        print("   API: GET /api/v1/futures/todayPnL")
        print("   说明: 查询合约今日盈亏 (UTC+0 时区)")
        print()
        
        pnl = client.get_futures_today_pnl()
        print(f"   今日盈亏: {pnl.dayProfit}")
        print(f"   今日盈亏率: {pnl.dayProfitRate}")
        print()
        
        # 盈亏分析
        profit = float(pnl.dayProfit)
        profit_rate = float(pnl.dayProfitRate)
        
        if profit > 0:
            print("   📈 今日盈利状态:")
            print(f"      盈利金额: {pnl.dayProfit}")
            print(f"      盈利率: {pnl.dayProfitRate} ({profit_rate*100:.2f}%)")
        elif profit < 0:
            print("   📉 今日亏损状态:")
            print(f"      亏损金额: {pnl.dayProfit}")
            print(f"      亏损率: {pnl.dayProfitRate} ({profit_rate*100:.2f}%)")
        else:
            print("   📊 今日盈亏平衡:")
            print(f"      盈亏金额: {pnl.dayProfit}")
            print(f"      盈亏率: {pnl.dayProfitRate}")
        
        print()
        print("🎉 查询合约今日盈亏测试完成!")
        
    except Exception as e:
        print(f"❌ 查询合约今日盈亏测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_today_pnl()
