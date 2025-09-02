"""
TooBit API SDK - 冰山订单示例
演示如何创建和管理冰山订单 (需要API密钥)
"""

from open_api_sdk import (
    TooBitClient, TooBitConfig, OrderRequest, 
    OrderSide, OrderType, TimeInForce
)
from datetime import datetime
import time


def create_iceberg_order():
    """创建冰山订单"""
    print("=== TooBit API 冰山订单示例 ===\n")
    
    # 注意: 这个示例需要真实的API密钥
    print("⚠️  注意: 此示例需要真实的API密钥才能运行")
    print("⚠️  注意: 这些操作会创建真实的冰山订单，请谨慎使用!")
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
        print("\n🧊 创建冰山订单...")
        
        # 获取当前市场价格作为参考
        print("📊 获取当前市场价格...")
        try:
            best_order_book = client.get_best_order_book("BTCUSDT")
            current_price = float(best_order_book['askPrice'])
            print(f"   当前市价: {current_price:,.2f} USDT")
        except Exception as e:
            print(f"   ⚠️  无法获取当前市价: {e}")
            current_price = 50000  # 使用假设价格
            print(f"   使用假设价格: {current_price:,.2f} USDT")
        
        # 设置冰山订单参数
        total_quantity = 0.01      # 总数量: 0.01 BTC
        iceberg_quantity = 0.001   # 每次显示数量: 0.001 BTC
        order_price = current_price * 0.99  # 价格略低于市价
        
        print(f"\n📝 冰山订单参数:")
        print(f"   交易对: BTCUSDT")
        print(f"   方向: 卖出 (SELL)")
        print(f"   类型: 限价单 (LIMIT)")
        print(f"   总数量: {total_quantity} BTC")
        print(f"   冰山数量: {iceberg_quantity} BTC")
        print(f"   价格: {order_price:,.2f} USDT")
        print(f"   当前市价: {current_price:,.2f} USDT")
        print(f"   价格差异: {((current_price - order_price) / current_price * 100):.2f}%")
        print()
        
        # 计算冰山订单的批次数量
        batch_count = int(total_quantity / iceberg_quantity)
        print(f"📊 冰山订单分析:")
        print(f"   总数量: {total_quantity} BTC")
        print(f"   冰山数量: {iceberg_quantity} BTC")
        print(f"   预计批次: {batch_count} 批")
        print(f"   每批价值: {iceberg_quantity * order_price:,.2f} USDT")
        print(f"   总订单价值: {total_quantity * order_price:,.2f} USDT")
        print()
        
        # 检查账户余额
        print("💳 检查账户余额...")
        try:
            balance = client.get_balance()
            btc_balance = 0
            for asset in balance:
                if asset['asset'] == 'BTC':
                    btc_balance = float(asset['free'])
                    break
            
            if btc_balance < total_quantity:
                print(f"   ❌ BTC余额不足: {btc_balance:.6f} BTC")
                print(f"   需要至少 {total_quantity} BTC 才能创建冰山订单")
                return
            else:
                print(f"   ✅ BTC余额充足: {btc_balance:.6f} BTC")
        except Exception as e:
            print(f"   ⚠️  无法检查余额: {e}")
            print("   继续创建冰山订单演示...")
        
        print()
        print("⚠️  注意: 以下将创建真实的冰山订单")
        print("   冰山订单会分批显示，避免对市场造成冲击")
        print("   请确认这是您想要的操作")
        print()
        
        # 创建冰山订单
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.SELL,
            type=OrderType.LIMIT,
            quantity=total_quantity,
            price=order_price,
            iceberg_qty=iceberg_quantity,
            time_in_force=TimeInForce.GTC
        )
        
        print("🔄 正在创建冰山订单...")
        response = client.create_order(order_request)
        
        print("✅ 冰山订单创建成功!")
        print()
        
        # 显示冰山订单信息
        print("📋 冰山订单信息:")
        print(f"   订单ID: {response.order_id}")
        print(f"   交易对: {response.symbol}")
        print(f"   方向: {response.side}")
        print(f"   类型: {response.type}")
        print(f"   总数量: {response.orig_qty} BTC")
        print(f"   冰山数量: {response.iceberg_qty} BTC")
        print(f"   价格: {response.price} USDT")
        print(f"   状态: {response.status}")
        print(f"   时间: {datetime.fromtimestamp(# response.time  # 字段不存在/1000).strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("\n💡 冰山订单说明:")
        print("   - 总数量: 整个订单的总数量")
        print("   - 冰山数量: 每次在订单簿中显示的数量")
        print("   - 当冰山数量被成交后，会自动显示下一批")
        print("   - 用于大额订单，避免对市场造成冲击")
        print("   - 享受Maker手续费优惠")
        
        print("\n🎉 冰山订单创建完成!")
        return response.order_id
        
    except Exception as e:
        print(f"❌ 创建冰山订单失败: {e}")
        print("\n可能的原因:")
        print("   - 账户余额不足")
        print("   - 该交易对不支持冰山订单")
        print("   - 冰山数量设置不当")
        print("   - API密钥权限不足")
        return None
    
    finally:
        client.close()


def create_buy_iceberg_order():
    """创建买入冰山订单"""
    print("\n=== 创建买入冰山订单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🟢 创建买入冰山订单...")
        print("   买入冰山订单用于分批买入，避免推高价格")
        print()
        
        # 获取当前市价
        try:
            best_order_book = client.get_best_order_book("BTCUSDT")
            current_price = float(best_order_book['bidPrice'])  # 使用买一价
            print(f"   当前市价: {current_price:,.2f} USDT")
        except:
            current_price = 50000
            print(f"   使用假设价格: {current_price:,.2f} USDT")
        
        # 设置买入冰山订单参数
        total_quantity = 0.01      # 总数量: 0.01 BTC
        iceberg_quantity = 0.001   # 每次显示数量: 0.001 BTC
        order_price = current_price * 1.01  # 价格略高于市价
        
        print(f"📝 买入冰山订单参数:")
        print(f"   交易对: BTCUSDT")
        print(f"   方向: 买入 (BUY)")
        print(f"   类型: 限价单 (LIMIT)")
        print(f"   总数量: {total_quantity} BTC")
        print(f"   冰山数量: {iceberg_quantity} BTC")
        print(f"   价格: {order_price:,.2f} USDT")
        print(f"   当前市价: {current_price:,.2f} USDT")
        print(f"   价格差异: {((order_price - current_price) / current_price * 100):.2f}%")
        print()
        
        # 检查USDT余额
        print("💳 检查USDT余额...")
        try:
            balance = client.get_balance()
            usdt_balance = 0
            for asset in balance:
                if asset['asset'] == 'USDT':
                    usdt_balance = float(asset['free'])
                    break
            
            required_usdt = total_quantity * order_price
            if usdt_balance < required_usdt:
                print(f"   ❌ USDT余额不足: {usdt_balance:,.2f} USDT")
                print(f"   需要至少 {required_usdt:,.2f} USDT")
                return
            else:
                print(f"   ✅ USDT余额充足: {usdt_balance:,.2f} USDT")
        except Exception as e:
            print(f"   ⚠️  无法检查余额: {e}")
            print("   继续创建买入冰山订单演示...")
        
        print()
        print("⚠️  注意: 以下将创建真实的买入冰山订单")
        print("   买入冰山订单会分批执行，避免推高价格")
        print("   请确认这是您想要的操作")
        print()
        
        # 创建买入冰山订单
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            quantity=total_quantity,
            price=order_price,
            iceberg_qty=iceberg_quantity,
            time_in_force=TimeInForce.GTC
        )
        
        print("🔄 正在创建买入冰山订单...")
        response = client.create_order(order_request)
        
        print("✅ 买入冰山订单创建成功!")
        print()
        
        print("📋 买入冰山订单信息:")
        print(f"   订单ID: {response.order_id}")
        print(f"   总数量: {response.orig_qty} BTC")
        print(f"   冰山数量: {response.iceberg_qty} BTC")
        print(f"   价格: {response.price} USDT")
        print(f"   状态: {response.status}")
        
        print("\n💡 买入冰山订单优势:")
        print("   - 避免一次性大额买入推高价格")
        print("   - 分批执行，获得更好的平均价格")
        print("   - 享受Maker手续费优惠")
        print("   - 适合大额资金分批建仓")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 创建买入冰山订单失败: {e}")


def monitor_iceberg_order():
    """监控冰山订单执行情况"""
    print("\n=== 监控冰山订单执行情况 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🔍 监控冰山订单执行...")
        
        # 获取当前挂单
        open_orders = client.get_open_orders("BTCUSDT")
        
        # 筛选冰山订单
        iceberg_orders = [o for o in open_orders if hasattr(o, 'iceberg_qty') and o.iceberg_qty]
        
        if not iceberg_orders:
            print("   ℹ️  没有找到冰山订单")
            return
        
        print(f"   找到 {len(iceberg_orders)} 个冰山订单")
        print()
        
        # 显示冰山订单状态
        for i, order in enumerate(iceberg_orders):
            print(f"📋 冰山订单 {i+1}:")
            print(f"   订单ID: {order.order_id}")
            print(f"   方向: {order.side}")
            print(f"   总数量: {order.orig_qty}")
            print(f"   冰山数量: {order.iceberg_qty}")
            print(f"   已执行数量: {order.executed_qty}")
            print(f"   剩余数量: {order.orig_qty - order.executed_qty}")
            print(f"   价格: {order.price}")
            print(f"   状态: {order.status}")
            
            # 计算执行进度
            if float(order.orig_qty) > 0:
                progress = (float(order.executed_qty) / float(order.orig_qty)) * 100
                print(f"   执行进度: {progress:.1f}%")
                
                # 估算剩余批次
                remaining_quantity = order.orig_qty - order.executed_qty
                remaining_batches = int(remaining_quantity / order.iceberg_qty) + (1 if remaining_quantity % order.iceberg_qty > 0 else 0)
                print(f"   剩余批次: {remaining_batches}")
            
            print()
        
        # 提供监控建议
        print("💡 冰山订单监控建议:")
        print("   - 定期检查执行进度")
        print("   - 监控市场深度变化")
        print("   - 关注成交价格质量")
        print("   - 必要时调整冰山数量")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 监控冰山订单失败: {e}")


def iceberg_order_strategies():
    """冰山订单策略演示"""
    print("\n=== 冰山订单策略演示 ===\n")
    
    print("📊 冰山订单使用策略:")
    print()
    
    print("1. 🎯 大额卖出策略:")
    print("   - 适用场景: 大额持仓需要卖出")
    print("   - 优势: 避免一次性大额卖出冲击市场")
    print("   - 设置建议: 冰山数量设为市场深度的1-5%")
    print("   - 价格策略: 略低于市价，确保成交")
    print()
    
    print("2. 🟢 大额买入策略:")
    print("   - 适用场景: 大额资金需要建仓")
    print("   - 优势: 避免一次性大额买入推高价格")
    print("   - 设置建议: 冰山数量设为市场深度的1-5%")
    print("   - 价格策略: 略高于市价，确保成交")
    print()
    
    print("3. 📈 趋势跟踪策略:")
    print("   - 适用场景: 在趋势中分批建仓或减仓")
    print("   - 优势: 获得更好的平均价格")
    print("   - 设置建议: 根据趋势强度调整冰山数量")
    print("   - 价格策略: 动态调整价格跟随趋势")
    print()
    
    print("4. 💰 成本控制策略:")
    print("   - 适用场景: 需要控制平均成本")
    print("   - 优势: 分散风险，避免单点风险")
    print("   - 设置建议: 根据资金规模设置批次")
    print("   - 价格策略: 设置价格区间，分批执行")
    print()
    
    print("5. 🕐 时间分散策略:")
    print("   - 适用场景: 需要在特定时间段内完成交易")
    print("   - 优势: 避免在不利时间点集中交易")
    print("   - 设置建议: 根据时间跨度设置批次")
    print("   - 价格策略: 根据时间段调整价格策略")
    print()
    
    print("💡 策略选择建议:")
    print("   - 新手: 使用简单的分批策略")
    print("   - 进阶: 结合市场深度分析")
    print("   - 专业: 多策略组合，动态调整")
    print("   - 风险控制: 设置合理的冰山数量")


def iceberg_order_best_practices():
    """冰山订单最佳实践"""
    print("\n=== 冰山订单最佳实践 ===\n")
    
    print("✅ 最佳实践:")
    print()
    
    print("1. 📊 冰山数量设置:")
    print("   - 参考市场深度，避免过度冲击")
    print("   - 一般设为市场深度的1-5%")
    print("   - 考虑交易对的最小交易单位")
    print("   - 根据市场波动性调整")
    print()
    
    print("2. 💰 价格策略:")
    print("   - 卖出: 略低于市价，确保成交")
    print("   - 买入: 略高于市价，确保成交")
    print("   - 避免设置极端价格")
    print("   - 考虑手续费和滑点成本")
    print()
    
    print("3. ⏰ 时间管理:")
    print("   - 避免在市场开盘和收盘时使用")
    print("   - 选择流动性较好的时间段")
    print("   - 考虑时区差异")
    print("   - 设置合理的订单有效期")
    print()
    
    print("4. 🔍 市场监控:")
    print("   - 监控市场深度变化")
    print("   - 关注大额订单的出现")
    print("   - 观察价格异常波动")
    print("   - 及时调整策略")
    print()
    
    print("5. 🛡️  风险控制:")
    print("   - 设置最大订单数量限制")
    print("   - 监控执行进度")
    print("   - 准备应急取消方案")
    print("   - 记录交易日志")
    print()
    
    print("⚠️  注意事项:")
    print("   - 冰山订单可能被市场识别")
    print("   - 在极端市场条件下可能执行困难")
    print("   - 需要持续监控和调整")
    print("   - 考虑网络延迟和执行延迟")


if __name__ == "__main__":
    # 注意: 这些示例需要真实的API密钥才能执行
    # 请先设置你的API密钥，或者注释掉这些调用
    
    print("=== TooBit API SDK 冰山订单示例 ===\n")
    print("⚠️  重要提醒: 所有冰山订单操作都是真实的!")
    print("⚠️  请确保在测试环境中验证，或使用小额测试")
    print("⚠️  建议先运行无需API密钥的示例熟悉接口\n")
    
    # 取消注释以下行来运行示例
    # create_iceberg_order()
    # create_buy_iceberg_order()
    # monitor_iceberg_order()
    
    iceberg_order_strategies()
    iceberg_order_best_practices()
    
    print("\n💡 提示:")
    print("   取消注释相应的函数调用来运行实际的冰山订单测试")
    print("   确保已设置正确的API密钥和充足的账户余额")
    print("   冰山订单适合大额交易，请谨慎使用") 