"""
TooBit API SDK - 止损单示例
演示如何创建和管理止损单 (需要API密钥)
"""

from open_api_sdk import (
    TooBitClient, TooBitConfig, OrderRequest, 
    OrderSide, OrderType, TimeInForce
)
from datetime import datetime
import time


def create_stop_loss_order():
    """创建止损单"""
    print("=== TooBit API 止损单示例 ===\n")
    
    # 注意: 这个示例需要真实的API密钥
    print("⚠️  注意: 此示例需要真实的API密钥才能运行")
    print("⚠️  注意: 这些操作会创建真实的止损单，请谨慎使用!")
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
        print("\n🛑 创建止损单...")
        
        # 获取当前市场价格作为参考
        print("📊 获取当前市场价格...")
        try:
            best_order_book = client.get_best_order_book("BTCUSDT")
            current_price = float(best_order_book['askPrice'])  # 使用卖一价作为当前市价
            print(f"   当前市价: {current_price:,.2f} USDT")
        except Exception as e:
            print(f"   ⚠️  无法获取当前市价: {e}")
            current_price = 50000  # 使用假设价格
            print(f"   使用假设价格: {current_price:,.2f} USDT")
        
        # 计算止损价格 (假设当前持有BTC，设置止损价格低于市价)
        stop_price = current_price * 0.95  # 止损价格设为当前价格的95%
        
        print(f"\n📝 止损单参数:")
        print(f"   交易对: BTCUSDT")
        print(f"   方向: 卖出 (SELL)")
        print(f"   类型: 止损单 (STOP_LOSS)")
        print(f"   数量: 0.001 BTC")
        print(f"   止损价格: {stop_price:,.2f} USDT")
        print(f"   当前市价: {current_price:,.2f} USDT")
        print(f"   止损幅度: {((current_price - stop_price) / current_price * 100):.2f}%")
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
            
            if btc_balance < 0.001:
                print(f"   ❌ BTC余额不足: {btc_balance:.6f} BTC")
                print("   需要至少0.001 BTC才能创建止损单")
                return
            else:
                print(f"   ✅ BTC余额充足: {btc_balance:.6f} BTC")
        except Exception as e:
            print(f"   ⚠️  无法检查余额: {e}")
            print("   继续创建止损单演示...")
        
        print()
        print("⚠️  注意: 以下将创建真实的止损单")
        print("   止损单会在价格下跌到指定价格时自动触发")
        print("   请确认这是您想要的操作")
        print()
        
        # 创建止损单
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.SELL,
            type=OrderType.STOP_LOSS,
            quantity=0.001,
            stop_price=stop_price,
            time_in_force=TimeInForce.GTC
        )
        
        print("🔄 正在创建止损单...")
        response = client.create_order(order_request)
        
        print("✅ 止损单创建成功!")
        print()
        
        # 显示止损单信息
        print("📋 止损单信息:")
        print(f"   订单ID: {response.order_id}")
        print(f"   交易对: {response.symbol}")
        print(f"   方向: {response.side}")
        print(f"   类型: {response.type}")
        print(f"   数量: {response.orig_qty} BTC")
        print(f"   止损价格: {response.stop_price} USDT")
        print(f"   状态: {response.status}")
        print(f"   时间: {datetime.fromtimestamp(# response.time  # 字段不存在/1000).strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("\n💡 止损单说明:")
        print("   - 当市场价格达到或低于止损价格时，订单将被触发")
        print("   - 触发后将以市价卖出，可能产生滑点")
        print("   - 用于限制损失，保护投资")
        print("   - 订单会一直有效直到被触发或手动取消")
        
        print("\n🎉 止损单创建完成!")
        return response.order_id
        
    except Exception as e:
        print(f"❌ 创建止损单失败: {e}")
        print("\n可能的原因:")
        print("   - 账户余额不足")
        print("   - 该交易对不支持止损单")
        print("   - 止损价格设置不当")
        print("   - API密钥权限不足")
        return None
    
    finally:
        client.close()


def create_trailing_stop_order():
    """创建追踪止损单"""
    print("\n=== 创建追踪止损单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("📈 创建追踪止损单...")
        print("   追踪止损单会跟随价格上涨，自动调整止损价格")
        print()
        
        # 获取当前市价
        try:
            best_order_book = client.get_best_order_book("BTCUSDT")
            current_price = float(best_order_book['askPrice'])
            print(f"   当前市价: {current_price:,.2f} USDT")
        except:
            current_price = 50000
            print(f"   使用假设价格: {current_price:,.2f} USDT")
        
        # 设置追踪止损参数
        trailing_percent = 2.0  # 追踪2%的跌幅
        stop_price = current_price * (1 - trailing_percent / 100)
        
        print(f"📝 追踪止损单参数:")
        print(f"   交易对: BTCUSDT")
        print(f"   方向: 卖出 (SELL)")
        print(f"   类型: 追踪止损单")
        print(f"   数量: 0.001 BTC")
        print(f"   初始止损价格: {stop_price:,.2f} USDT")
        print(f"   追踪幅度: {trailing_percent}%")
        print()
        
        # 注意：TooBit可能不支持原生追踪止损单，这里演示概念
        print("💡 追踪止损单概念:")
        print("   - 初始止损价格: 当前价格 - 追踪幅度")
        print("   - 当价格上涨时，止损价格也会相应上调")
        print("   - 当价格下跌时，止损价格保持不变")
        print("   - 这样可以锁定更多利润")
        print()
        
        print("⚠️  注意: TooBit可能不支持原生追踪止损单")
        print("   实际应用中需要手动实现追踪逻辑")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 创建追踪止损单失败: {e}")


def manage_stop_loss_orders():
    """管理止损单"""
    print("\n=== 管理止损单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🔍 查找和管理止损单...")
        
        # 获取所有订单
        all_orders = client.get_all_orders("BTCUSDT")
        
        # 筛选止损单
        stop_loss_orders = [o for o in all_orders if hasattr(o, 'stop_price') and o.stop_price]
        
        if not stop_loss_orders:
            print("   ℹ️  没有找到止损单")
            return
        
        print(f"   找到 {len(stop_loss_orders)} 个止损单")
        print()
        
        # 显示止损单列表
        print("📋 止损单列表:")
        for i, order in enumerate(stop_loss_orders):
            print(f"   {i+1:2d}. 订单ID: {order.order_id}")
            print(f"       状态: {order.status}")
            print(f"       数量: {order.orig_qty} BTC")
            print(f"       止损价格: {order.stop_price} USDT")
            print(f"       创建时间: {datetime.fromtimestamp(# order.time  # 字段不存在/1000).strftime('%m-%d %H:%M')}")
            
            # 分析止损单状态
            if order.status == "NEW":
                status_emoji = "🟡"
                status_text = "等待触发"
            elif order.status == "FILLED":
                status_emoji = "🟢"
                status_text = "已触发成交"
            elif order.status == "CANCELED":
                status_emoji = "❌"
                status_text = "已取消"
            else:
                status_emoji = "⚪"
                status_text = order.status
            
            print(f"       状态说明: {status_emoji} {status_text}")
            print()
        
        # 提供管理选项
        print("🔧 管理选项:")
        print("   1. 取消止损单")
        print("   2. 修改止损价格")
        print("   3. 查看止损单详情")
        print("   4. 监控止损单状态")
        print()
        
        print("💡 止损单管理建议:")
        print("   - 定期检查止损单状态")
        print("   - 根据市场情况调整止损价格")
        print("   - 避免设置过于紧密的止损")
        print("   - 考虑使用分批止损策略")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 管理止损单失败: {e}")


def stop_loss_strategy_demo():
    """止损策略演示"""
    print("\n=== 止损策略演示 ===\n")
    
    print("📊 常见止损策略:")
    print()
    
    print("1. 🎯 固定价格止损:")
    print("   - 设置固定的止损价格")
    print("   - 优点: 简单明确")
    print("   - 缺点: 可能过早触发或过晚触发")
    print("   - 适用: 短期交易，明确风险承受能力")
    print()
    
    print("2. 📈 移动止损:")
    print("   - 随着价格上涨，止损价格也相应上调")
    print("   - 优点: 可以锁定更多利润")
    print("   - 缺点: 实现复杂，需要持续监控")
    print("   - 适用: 趋势交易，希望最大化利润")
    print()
    
    print("3. 💰 百分比止损:")
    print("   - 根据投资金额设置止损比例")
    print("   - 优点: 风险控制明确")
    print("   - 缺点: 可能忽略市场波动")
    print("   - 适用: 资金管理，风险控制")
    print()
    
    print("4. 🕐 时间止损:")
    print("   - 在一定时间内未达到目标则止损")
    print("   - 优点: 避免长期套牢")
    print("   - 缺点: 可能错过反转机会")
    print("   - 适用: 短线交易，时间敏感")
    print()
    
    print("5. 🔍 技术指标止损:")
    print("   - 基于技术指标设置止损")
    print("   - 优点: 更科学，适应市场")
    print("   - 缺点: 需要技术分析能力")
    print("   - 适用: 技术分析交易者")
    print()
    
    print("💡 止损策略选择建议:")
    print("   - 新手: 使用固定价格止损")
    print("   - 进阶: 结合移动止损")
    print("   - 专业: 多策略组合使用")
    print("   - 风险控制: 永远不要超过可承受的损失")


def stop_loss_risk_management():
    """止损风险管理"""
    print("\n=== 止损风险管理 ===\n")
    
    print("⚠️  止损单风险提醒:")
    print()
    
    print("1. 🚨 滑点风险:")
    print("   - 止损单触发时可能产生滑点")
    print("   - 在剧烈波动时滑点可能很大")
    print("   - 建议: 设置合理的止损价格，避免在极端市场使用")
    print()
    
    print("2. ⏰ 执行延迟风险:")
    print("   - 网络延迟可能导致执行延迟")
    print("   - 市场快速变化时可能错过最佳价格")
    print("   - 建议: 使用稳定的网络连接，监控执行情况")
    print()
    
    print("3. 💸 过度止损风险:")
    print("   - 设置过于紧密的止损可能频繁触发")
    print("   - 累积的手续费可能超过止损损失")
    print("   - 建议: 合理设置止损幅度，考虑交易成本")
    print()
    
    print("4. 📊 市场操纵风险:")
    print("   - 大额止损单可能被市场操纵者利用")
    print("   - 触发大量止损单可能导致价格剧烈波动")
    print("   - 建议: 分散止损单，避免集中触发")
    print()
    
    print("🛡️  风险控制措施:")
    print("   - 设置合理的止损幅度")
    print("   - 使用分批止损策略")
    print("   - 定期检查和调整止损单")
    print("   - 监控市场异常情况")
    print("   - 保持充足的账户余额")


if __name__ == "__main__":
    # 注意: 这些示例需要真实的API密钥才能执行
    # 请先设置你的API密钥，或者注释掉这些调用
    
    print("=== TooBit API SDK 止损单示例 ===\n")
    print("⚠️  重要提醒: 所有止损单操作都是真实的!")
    print("⚠️  请确保在测试环境中验证，或使用小额测试")
    print("⚠️  建议先运行无需API密钥的示例熟悉接口\n")
    
    # 取消注释以下行来运行示例
    # create_stop_loss_order()
    # create_trailing_stop_order()
    # manage_stop_loss_orders()
    
    stop_loss_strategy_demo()
    stop_loss_risk_management()
    
    print("\n💡 提示:")
    print("   取消注释相应的函数调用来运行实际的止损单测试")
    print("   确保已设置正确的API密钥和充足的账户余额")
    print("   止损单是重要的风险控制工具，请谨慎使用") 