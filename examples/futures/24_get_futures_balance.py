#!/usr/bin/env python3
"""
TooBit API 合约查询账户余额示例 (24号)
查询合约账户余额信息
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_balance():
    """查询合约账户余额示例"""
    print("=== TooBit API 合约查询账户余额示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 查询合约账户余额测试:")
        print()
        print("   API: GET /api/v1/futures/balance")
        print("   说明: 查询合约账户所有资产的余额信息")
        print()
        
        balances = client.get_futures_balance()
        print(f"   返回资产数量: {len(balances)}")
        print()
        
        for balance in balances:
            print(f"   📊 资产: {balance.asset}")
            print(f"      总余额: {balance.balance}")
            print(f"      可用保证金: {balance.availableBalance}")
            print(f"      仓位保证金: {balance.positionMargin}")
            print(f"      委托保证金: {balance.orderMargin}")
            print(f"      全仓未实现盈亏: {balance.crossUnRealizedPnl}")
            print()
        
        print("🎉 查询合约账户余额测试完成!")
        
    except Exception as e:
        print(f"❌ 查询合约账户余额测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_balance()
