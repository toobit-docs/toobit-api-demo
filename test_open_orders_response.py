#!/usr/bin/env python3
"""
测试修复后的OrderResponse模型
验证查询未成交订单API的实际返回值
"""

import os
import sys
from dotenv import load_dotenv

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from open_api_sdk import OrderResponse

def test_open_orders_response():
    """测试查询未成交订单响应模型"""
    print("=== 测试修复后的OrderResponse模型 ===\n")
    
    # 用户提供的真实查询未成交订单API返回值
    real_response = {
        "symbol": "LTCBTC",
        "orderId": "1",
        "clientOrderId": "t7921223K12",
        "price": "0.1",
        "origQty": "1.0",
        "executedQty": "0.0",
        "cummulativeQuoteQty": "0.0",
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "stopPrice": "0.0",
        "icebergQty": "0.0",
        "time": "1499827319559",
        "updateTime": "1499827319559",
        "isWorking": True
    }
    
    print("1. 真实API响应数据:")
    for key, value in real_response.items():
        print(f"  {key}: {value}")
    
    print(f"\n响应字段数量: {len(real_response)}")
    
    print("\n2. 尝试解析响应...")
    
    try:
        order_response = OrderResponse(**real_response)
        print("✅ 响应解析成功！")
        
        print(f"\n3. 测试所有字段访问:")
        print(f"  交易对: {order_response.symbol}")
        print(f"  订单ID: {order_response.order_id}")
        print(f"  客户端订单ID: {order_response.client_order_id}")
        print(f"  价格: {order_response.price}")
        print(f"  原始数量: {order_response.orig_qty}")
        print(f"  已执行数量: {order_response.executed_qty}")
        print(f"  累计成交金额: {order_response.cummulative_quote_qty}")
        print(f"  订单状态: {order_response.status}")
        print(f"  订单有效期: {order_response.time_in_force}")
        print(f"  订单类型: {order_response.type}")
        print(f"  订单方向: {order_response.side}")
        print(f"  止损价格: {order_response.stop_price}")
        print(f"  冰山数量: {order_response.iceberg_qty}")
        print(f"  订单时间: {order_response.time}")
        print(f"  更新时间: {order_response.update_time}")
        print(f"  是否在工作: {order_response.is_working}")
        
        print(f"\n4. 验证字段数量:")
        model_fields = set(order_response.model_fields.keys())
        print(f"  模型字段数量: {len(model_fields)}")
        print(f"  API响应字段数量: {len(real_response)}")
        print(f"  字段匹配: {'✅' if len(model_fields) == len(real_response) else '❌'}")
        
        print(f"\n5. 测试序列化:")
        serialized = order_response.model_dump()
        print(f"  序列化成功，包含 {len(serialized)} 个字段")
        
        print(f"\n6. 验证枚举值:")
        print(f"  状态: {order_response.status} (类型: {type(order_response.status)})")
        print(f"  有效期: {order_response.time_in_force} (类型: {type(order_response.time_in_force)})")
        print(f"  类型: {order_response.type} (类型: {type(order_response.type)})")
        print(f"  方向: {order_response.side} (类型: {type(order_response.side)})")
        
        print(f"\n7. 验证数据类型:")
        print(f"  订单ID类型: {type(order_response.order_id)} (应该是str)")
        print(f"  价格类型: {type(order_response.price)} (应该是str)")
        print(f"  数量类型: {type(order_response.orig_qty)} (应该是str)")
        print(f"  是否在工作类型: {type(order_response.is_working)} (应该是bool)")
        
        print(f"\n8. 测试数学计算:")
        if float(order_response.executed_qty) > 0:
            fill_percentage = (float(order_response.executed_qty) / float(order_response.orig_qty)) * 100
            print(f"  成交比例: {fill_percentage:.2f}%")
        else:
            print("  成交比例: 0% (未成交)")
        
        # 测试时间字段
        import datetime
        order_time = datetime.datetime.fromtimestamp(int(order_response.time)/1000)
        update_time = datetime.datetime.fromtimestamp(int(order_response.update_time)/1000)
        print(f"  订单时间: {order_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  更新时间: {update_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
    except Exception as e:
        print(f"❌ 响应解析失败: {e}")
        print(f"错误类型: {type(e).__name__}")
        
        if hasattr(e, 'errors'):
            print("验证错误详情:")
            for error in e.errors():
                print(f"  字段: {error['loc']}, 错误: {error['msg']}, 输入值: {error['input']}")
    
    print("\n=== 查询未成交订单响应模型测试完成 ===")

if __name__ == "__main__":
    test_open_orders_response() 