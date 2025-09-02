"""
TooBit API SDK - 下单接口示例
创建各种类型的订单 (需要API密钥)
"""

from open_api_sdk import (
    TooBitClient, TooBitConfig, OrderRequest, 
    OrderSide, OrderType, TimeInForce
)


def create_limit_order():
    """创建限价单"""
    print("=== TooBit API 创建限价单接口测试 ===\n")
    
    # 注意: 这个示例需要真实的API密钥
    print("⚠️  注意: 此示例需要真实的API密钥才能运行")
    print("⚠️  注意: 这些操作会创建真实的订单，请谨慎使用!")
    print("⚠️  建议先在测试环境中验证\n")
    
    try:
        # 从环境变量创建配置
        config = TooBitConfig.from_env()
        print("✅ 从环境变量加载配置成功")
    except ValueError as e:
        print(f"❌ 环境变量配置失败: {e}")
        print("\n请设置以下环境变量:")
        print("export TOOBIT_API_KEY='your_api_key'")
        print("export TOOBIT_API_SECRET='your_api_secret'")
        return
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        print("\n💰 创建限价买入订单...")
        
        # 创建限价买入订单
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            quantity=0.001,  # 买入0.001 BTC
            price=50000.0,   # 限价50000 USDT (设置较低价格避免立即成交)
            time_in_force=TimeInForce.GTC  # 一直有效直到取消
        )
        
        print("📝 订单参数:")
        print(f"   交易对: {order_request.symbol}")
        print(f"   方向: {order_request.side}")
        print(f"   类型: {order_request.type}")
        print(f"   数量: {order_request.quantity} BTC")
        print(f"   价格: {order_request.price} USDT")
        print(f"   有效期: {order_request.time_in_force}")
        print()
        
        # 调用下单接口
        response = client.create_order(order_request)
        
        print("✅ 限价买入订单创建成功!")
        print()
        
        # 显示订单信息
        print("📋 订单信息:")
        print(f"   订单ID: {response.order_id}")
        print(f"   客户端订单ID: {response.client_order_id}")
        print(f"   交易对: {response.symbol}")
        print(f"   订单状态: {response.status}")
        print(f"   订单类型: {response.type}")
        print(f"   订单方向: {response.side}")
        print(f"   原始数量: {response.orig_qty}")
        print(f"   已执行数量: {response.executed_qty}")
        print(f"   价格: {response.price}")
        # 注意：实际API响应中没有这些字段，已从模型中移除
        # # print(f"累计成交金额: 字段不存在")
        # # print(f"订单时间: 字段不存在")
        # # print(f"是否在工作: 字段不存在")
        
        # 判断订单状态
        if response.status == "NEW":
            status_emoji = "🟡"
            status_text = "新订单，等待成交"
        elif response.status == "FILLED":
            status_emoji = "🟢"
            status_text = "订单已完全成交"
        elif response.status == "PARTIALLY_FILLED":
            status_emoji = "🟠"
            status_text = "订单部分成交"
        else:
            status_emoji = "⚪"
            status_text = "其他状态"
        
        print(f"   状态说明: {status_emoji} {status_text}")
        
        # 成交分析
        if float(response.executed_qty) > 0:
            fill_percentage = (float(response.executed_qty) / float(response.orig_qty)) * 100
            # 注意：实际API响应中没有cummulative_quote_qty字段
            # avg_price = response.cummulative_quote_qty / response.executed_qty if float(response.executed_qty) > 0 else 0
            
            print(f"\n📊 成交分析:")
            print(f"   成交比例: {fill_percentage:.2f}%")
            print(f"   平均成交价: 需要查询成交历史获取")
        
        print("\n🎉 创建限价单接口测试完成!")
        return response.order_id
        
    except Exception as e:
        print(f"❌ 创建限价单接口测试失败: {e}")
        print("\n可能的原因:")
        print("   - 账户余额不足")
        print("   - 订单参数不符合交易规则")
        print("   - API密钥权限不足")
        print("   - 交易对暂停交易")
        return None
    
    finally:
        client.close()


def create_market_order():
    """创建市价单"""
    print("\n=== TooBit API 创建市价单接口测试 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("💰 创建市价买入订单...")
        print("⚠️  注意: 市价单会立即按市场价格成交!")
        
        # 创建市价买入订单
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.MARKET,
            quantity=10,  # 买入10U
            time_in_force=TimeInForce.IOC  # 市价单使用IOC，立即成交或取消
        )
        
        print("\n📝 订单参数:")
        print(f"   交易对: {order_request.symbol}")
        print(f"   方向: {order_request.side}")
        print(f"   类型: {order_request.type}")
        print(f"   数量: {order_request.quantity} BTC")
        print(f"   有效期: {order_request.time_in_force}")
        print("   价格: 市价 (按当前市场价格成交)")
        print()
        
        # 调用下单接口
        response = client.create_order(order_request)
        
        print("✅ 市价买入订单创建成功!")
        print()
        
        # 显示订单信息
        print("📋 订单信息:")
        print(f"   订单ID: {response.order_id}")
        print(f"   订单状态: {response.status}")
        print(f"   原始数量: {response.orig_qty}")
        print(f"   已执行数量: {response.executed_qty}")
        # 注意：实际API响应中没有cummulative_quote_qty字段
        # # print(f"累计成交金额: 字段不存在")
        
        # 计算平均成交价
        if float(response.executed_qty) > 0:
            # 注意：实际API响应中没有cummulative_quote_qty字段
            # avg_price = response.cummulative_quote_qty / response.executed_qty
            print(f"   平均成交价: 需要查询成交历史获取")
        
        print("\n🎉 创建市价单接口测试完成!")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 创建市价单接口测试失败: {e}")


def create_stop_loss_order():
    """创建止损单"""
    print("\n=== TooBit API 创建止损单接口测试 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🛑 创建止损单...")
        print("   当价格下跌到指定价格时自动卖出")
        
        # 创建止损单
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.SELL,
            type=OrderType.STOP_LOSS,
            quantity=0.001,
            stop_price=48000.0,  # 止损价格
            time_in_force=TimeInForce.GTC
        )
        
        print("\n📝 订单参数:")
        print(f"   交易对: {order_request.symbol}")
        print(f"   方向: {order_request.side}")
        print(f"   类型: {order_request.type}")
        print(f"   数量: {order_request.quantity} BTC")
        print(f"   止损价格: {order_request.stop_price} USDT")
        print()
        
        # 调用下单接口
        response = client.create_order(order_request)
        
        print("✅ 止损单创建成功!")
        print()
        
        print("📋 订单信息:")
        print(f"   订单ID: {response.order_id}")
        print(f"   订单状态: {response.status}")
        print(f"   止损价格: {response.stop_price}")
        print(f"   数量: {response.orig_qty}")
        
        print("\n💡 止损单说明:")
        print("   - 当市场价格达到或低于止损价格时，订单将被触发")
        print("   - 触发后将以市价卖出")
        print("   - 用于限制损失")
        
        print("\n🎉 创建止损单接口测试完成!")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 创建止损单接口测试失败: {e}")
        print("   可能原因: 该交易对不支持止损单")


def create_advanced_orders():
    """创建高级订单类型"""
    print("\n=== TooBit API 创建高级订单类型测试 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        # 1. 创建冰山订单
        print("🧊 创建冰山订单...")
        try:
            iceberg_order = OrderRequest(
                symbol="BTCUSDT",
                side=OrderSide.SELL,
                type=OrderType.LIMIT,
                quantity=0.01,      # 总数量
                price=52000.0,      # 价格
                iceberg_qty=0.001,  # 每次显示数量
                time_in_force=TimeInForce.GTC
            )
            
            response = client.create_order(iceberg_order)
            print(f"   ✅ 冰山订单创建成功! 订单ID: {response.order_id}")
            print(f"   总数量: {response.orig_qty}, 冰山数量: {response.iceberg_qty}")
            
        except Exception as e:
            print(f"   ❌ 冰山订单创建失败: {e}")
        
        # 2. 创建限价挂单 (Maker订单)
        print("\n🏷️  创建限价挂单...")
        try:
            maker_order = OrderRequest(
                symbol="BTCUSDT",
                side=OrderSide.BUY,
                type=OrderType.LIMIT_MAKER,
                quantity=0.001,
                price=49000.0,  # 低于市价
                time_in_force=TimeInForce.GTC
            )
            
            response = client.create_order(maker_order)
            print(f"   ✅ 限价挂单创建成功! 订单ID: {response.order_id}")
            print(f"   享受Maker手续费优惠")
            
        except Exception as e:
            print(f"   ❌ 限价挂单创建失败: {e}")
        
        # 3. 创建IOC订单
        print("\n⚡ 创建IOC订单...")
        try:
            ioc_order = OrderRequest(
                symbol="BTCUSDT",
                side=OrderSide.BUY,
                type=OrderType.LIMIT,
                quantity=0.001,
                price=50000.0,
                time_in_force=TimeInForce.IOC  # 立即成交或取消
            )
            
            response = client.create_order(ioc_order)
            print(f"   ✅ IOC订单创建成功! 订单ID: {response.order_id}")
            print(f"   已执行数量: {response.executed_qty}")
            
        except Exception as e:
            print(f"   ❌ IOC订单创建失败: {e}")
        
        print("\n🎉 高级订单类型测试完成!")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 高级订单类型测试失败: {e}")


def order_validation_demo():
    """订单参数验证演示"""
    print("\n=== 订单参数验证演示 ===\n")
    
    print("📝 订单参数验证规则:")
    print("   - 交易对必须存在且可交易")
    print("   - 数量必须符合最小/最大限制")
    print("   - 价格必须符合价格过滤器")
    print("   - 账户余额必须充足")
    print("   - 订单类型必须被支持")
    print()
    
    print("💡 常见错误及解决方案:")
    print("   1. 'Filter failure: LOT_SIZE'")
    print("      - 数量不符合步长规则")
    print("      - 检查交易对的最小/最大数量限制")
    print()
    print("   2. 'Filter failure: PRICE_FILTER'")
    print("      - 价格不符合价格过滤器")
    print("      - 检查最小价格变动单位")
    print()
    print("   3. 'Account has insufficient balance'")
    print("      - 账户余额不足")
    print("      - 检查可用余额")
    print()
    print("   4. 'Order would trigger immediately'")
    print("      - 止损价格设置不当")
    print("      - 检查当前市场价格")


if __name__ == "__main__":
    # 注意: 这些示例需要真实的API密钥才能执行
    # 请先设置你的API密钥，或者注释掉这些调用
    
    print("=== TooBit API SDK 下单接口示例 ===\n")
    print("⚠️  重要提醒: 所有订单操作都是真实的!")
    print("⚠️  请确保在测试环境中验证，或使用小额测试")
    print("⚠️  建议先运行无需API密钥的示例熟悉接口\n")
    
    # 取消注释以下行来运行示例
    create_limit_order()
    # create_market_order()
    # create_stop_loss_order() 暂不支持
    # create_advanced_orders() 暂不支持
    
    order_validation_demo()
    
    print("\n💡 提示:")
    print("   取消注释相应的函数调用来运行实际的下单测试")
    print("   确保已设置正确的API密钥和充足的账户余额") 