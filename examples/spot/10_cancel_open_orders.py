#!/usr/bin/env python3
"""
TooBit API 现货撤销挂单示例
撤销指定交易对和方向的全部挂单
"""

from open_api_sdk import TooBitClient, TooBitConfig, OrderSide

def cancel_open_orders():
    """撤销挂单示例"""
    print("=== TooBit API 现货撤销挂单示例 ===\n")
    
    # 初始化配置
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 撤销挂单测试:")
        print()
        
        # 示例1: 撤销所有挂单
        print("📊 示例1: 撤销所有挂单")
        print("   参数: 无")
        print("   API: DELETE /api/v1/spot/openOrders")
        print("   说明: 撤销账户下所有现货挂单")
        print()
        
        response1 = client.cancel_open_orders()
        print(f"   响应: {response1.model_dump()}")
        print(f"   成功: {response1.success}")
        print()
        
        # 示例2: 撤销指定交易对的所有挂单
        print("📊 示例2: 撤销指定交易对的所有挂单")
        print("   参数: symbol='BTCUSDT'")
        print("   API: DELETE /api/v1/spot/openOrders?symbol=BTCUSDT")
        print("   说明: 撤销BTCUSDT交易对的所有挂单")
        print()
        
        response2 = client.cancel_open_orders(symbol='BTCUSDT')
        print(f"   响应: {response2.model_dump()}")
        print(f"   成功: {response2.success}")
        print()
        
        # 示例3: 撤销指定交易对和方向的挂单
        print("📊 示例3: 撤销指定交易对和方向的挂单")
        print("   参数: symbol='BTCUSDT', side='BUY'")
        print("   API: DELETE /api/v1/spot/openOrders?symbol=BTCUSDT&side=BUY")
        print("   说明: 撤销BTCUSDT交易对的所有买单")
        print()
        
        response3 = client.cancel_open_orders(symbol='BTCUSDT', side=OrderSide.BUY)
        print(f"   响应: {response3.model_dump()}")
        print(f"   成功: {response3.success}")
        print()
        
        # 示例4: 撤销指定方向的所有挂单
        print("📊 示例4: 撤销指定方向的所有挂单")
        print("   参数: side='SELL'")
        print("   API: DELETE /api/v1/spot/openOrders?side=SELL")
        print("   说明: 撤销所有卖单")
        print()
        
        response4 = client.cancel_open_orders(side=OrderSide.SELL)
        print(f"   响应: {response4.model_dump()}")
        print(f"   成功: {response4.success}")
        print()
        
        print("🎉 撤销挂单测试完成!")
        
    except Exception as e:
        print(f"❌ 撤销挂单测试失败: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    cancel_open_orders()
