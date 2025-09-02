"""
TooBit API SDK - Maker订单示例
演示如何创建Maker订单以享受手续费优惠 (需要API密钥)
"""

from open_api_sdk import (
    TooBitClient, TooBitConfig, OrderRequest, 
    OrderSide, OrderType, TimeInForce
)
from datetime import datetime
import time


def create_maker_order():
    """创建Maker订单"""
    print("=== TooBit API Maker订单示例 ===\n")
    
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
        print("\n🏷️  创建Maker订单...")
        
        # 获取当前市场价格作为参考
        print("📊 获取当前市场价格...")
        try:
            best_order_book = client.get_best_order_book("BTCUSDT")
            bid_price = float(best_order_book['bidPrice'])    # 买一价
            ask_price = float(best_order_book['askPrice'])    # 卖一价
            mid_price = (bid_price + ask_price) / 2          # 中间价
            
            print(f"   买一价: {bid_price:,.2f} USDT")
            print(f"   卖一价: {ask_price:,.2f} USDT")
            print(f"   中间价: {mid_price:,.2f} USDT")
            print(f"   价差: {ask_price - bid_price:,.2f} USDT")
        except Exception as e:
            print(f"   ⚠️  无法获取当前市价: {e}")
            mid_price = 50000  # 使用假设价格
            print(f"   使用假设价格: {mid_price:,.2f} USDT")
        
        # 设置Maker订单参数 (价格远离市价，确保不会立即成交)
        order_side = OrderSide.BUY  # 买入订单
        order_price = mid_price * 0.98  # 价格设为中间价的98%，确保不会立即成交
        order_quantity = 0.001  # 数量: 0.001 BTC
        
        print(f"\n📝 Maker订单参数:")
        print(f"   交易对: BTCUSDT")
        print(f"   方向: 买入 (BUY)")
        print(f"   类型: 限价单 (LIMIT)")
        print(f"   数量: {order_quantity} BTC")
        print(f"   价格: {order_price:,.2f} USDT")
        print(f"   中间价: {mid_price:,.2f} USDT")
        print(f"   价格差异: {((mid_price - order_price) / mid_price * 100):.2f}%")
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
            
            required_usdt = order_quantity * order_price
            if usdt_balance < required_usdt:
                print(f"   ❌ USDT余额不足: {usdt_balance:,.2f} USDT")
                print(f"   需要至少 {required_usdt:,.2f} USDT")
                return
            else:
                print(f"   ✅ USDT余额充足: {usdt_balance:,.2f} USDT")
        except Exception as e:
            print(f"   ⚠️  无法检查余额: {e}")
            print("   继续创建Maker订单演示...")
        
        print()
        print("⚠️  注意: 以下将创建真实的Maker订单")
        print("   Maker订单会挂单等待成交，享受手续费优惠")
        print("   请确认这是您想要的操作")
        print()
        
        # 创建Maker订单
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=order_side,
            type=OrderType.LIMIT,
            quantity=order_quantity,
            price=order_price,
            time_in_force=TimeInForce.GTC
        )
        
        print("🔄 正在创建Maker订单...")
        response = client.create_order(order_request)
        
        print("✅ Maker订单创建成功!")
        print()
        
        # 显示Maker订单信息
        print("📋 Maker订单信息:")
        print(f"   订单ID: {response.order_id}")
        print(f"   交易对: {response.symbol}")
        print(f"   方向: {response.side}")
        print(f"   类型: {response.type}")
        print(f"   数量: {response.orig_qty} BTC")
        print(f"   价格: {response.price} USDT")
        print(f"   状态: {response.status}")
        print(f"   时间: {datetime.fromtimestamp(# response.time  # 字段不存在/1000).strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("\n💡 Maker订单说明:")
        print("   - Maker订单会挂单等待成交")
        print("   - 享受较低的手续费 (Maker费率)")
        print("   - 不会立即成交，需要等待市场匹配")
        print("   - 适合不急于成交的交易者")
        
        print("\n🎉 Maker订单创建完成!")
        return response.order_id
        
    except Exception as e:
        print(f"❌ 创建Maker订单失败: {e}")
        print("\n可能的原因:")
        print("   - 账户余额不足")
        print("   - 订单参数不符合交易规则")
        print("   - API密钥权限不足")
        print("   - 交易对暂停交易")
        return None
    
    finally:
        client.close()


def create_sell_maker_order():
    """创建卖出Maker订单"""
    print("\n=== 创建卖出Maker订单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        print("🔴 创建卖出Maker订单...")
        print("   卖出Maker订单用于挂单卖出，享受手续费优惠")
        print()
        
        # 获取当前市价
        try:
            best_order_book = client.get_best_order_book("BTCUSDT")
            bid_price = float(best_order_book['bidPrice'])
            ask_price = float(best_order_book['askPrice'])
            mid_price = (bid_price + ask_price) / 2
            
            print(f"   买一价: {bid_price:,.2f} USDT")
            print(f"   卖一价: {ask_price:,.2f} USDT")
            print(f"   中间价: {mid_price:,.2f} USDT")
        except:
            mid_price = 50000
            print(f"   使用假设价格: {mid_price:,.2f} USDT")
        
        # 设置卖出Maker订单参数
        order_price = mid_price * 1.02  # 价格设为中间价的102%，确保不会立即成交
        order_quantity = 0.001  # 数量: 0.001 BTC
        
        print(f"📝 卖出Maker订单参数:")
        print(f"   交易对: BTCUSDT")
        print(f"   方向: 卖出 (SELL)")
        print(f"   类型: 限价单 (LIMIT)")
        print(f"   数量: {order_quantity} BTC")
        print(f"   价格: {order_price:,.2f} USDT")
        print(f"   中间价: {mid_price:,.2f} USDT")
        print(f"   价格差异: {((order_price - mid_price) / mid_price * 100):.2f}%")
        print()
        
        # 检查BTC余额
        print("💳 检查BTC余额...")
        try:
            balance = client.get_balance()
            btc_balance = 0
            for asset in balance:
                if asset['asset'] == 'BTC':
                    btc_balance = float(asset['free'])
                    break
            
            if btc_balance < order_quantity:
                print(f"   ❌ BTC余额不足: {btc_balance:.6f} BTC")
                print(f"   需要至少 {order_quantity} BTC")
                return
            else:
                print(f"   ✅ BTC余额充足: {btc_balance:.6f} BTC")
        except Exception as e:
            print(f"   ⚠️  无法检查余额: {e}")
            print("   继续创建卖出Maker订单演示...")
        
        print()
        print("⚠️  注意: 以下将创建真实的卖出Maker订单")
        print("   卖出Maker订单会挂单等待成交")
        print("   请确认这是您想要的操作")
        print()
        
        # 创建卖出Maker订单
        order_request = OrderRequest(
            symbol="BTCUSDT",
            side=OrderSide.SELL,
            type=OrderType.LIMIT,
            quantity=order_quantity,
            price=order_price,
            time_in_force=TimeInForce.GTC
        )
        
        print("🔄 正在创建卖出Maker订单...")
        response = client.create_order(order_request)
        
        print("✅ 卖出Maker订单创建成功!")
        print()
        
        print("📋 卖出Maker订单信息:")
        print(f"   订单ID: {response.order_id}")
        print(f"   数量: {response.orig_qty} BTC")
        print(f"   价格: {response.price} USDT")
        print(f"   状态: {response.status}")
        
        print("\n💡 卖出Maker订单优势:")
        print("   - 享受Maker手续费优惠")
        print("   - 可以设置理想的价格")
        print("   - 不会立即成交，避免滑点")
        print("   - 适合长期持有者")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 创建卖出Maker订单失败: {e}")


def compare_maker_vs_taker():
    """比较Maker和Taker订单"""
    print("\n=== 比较Maker和Taker订单 ===\n")
    
    print("📊 Maker vs Taker 订单对比:")
    print()
    
    print("🏷️  Maker订单 (挂单方):")
    print("   ✅ 优势:")
    print("      - 手续费较低 (Maker费率)")
    print("      - 可以设置理想价格")
    print("      - 避免滑点")
    print("      - 适合不急于成交的交易")
    print("   ❌ 劣势:")
    print("      - 可能不会立即成交")
    print("      - 需要等待市场匹配")
    print("      - 在快速市场中可能错过机会")
    print()
    
    print("⚡ Taker订单 (吃单方):")
    print("   ✅ 优势:")
    print("      - 立即成交")
    print("      - 确保执行")
    print("      - 适合快速交易")
    print("      - 在趋势市场中表现更好")
    print("   ❌ 劣势:")
    print("      - 手续费较高 (Taker费率)")
    print("      - 可能产生滑点")
    print("      - 价格执行质量较差")
    print()
    
    print("💰 手续费对比:")
    print("   - Maker费率: 通常为0.1% (万分之10)")
    print("   - Taker费率: 通常为0.1% (万分之10)")
    print("   - 注意: 实际费率可能因VIP等级而异")
    print()
    
    print("🎯 使用建议:")
    print("   - 长期投资: 优先使用Maker订单")
    print("   - 短线交易: 考虑使用Taker订单")
    print("   - 大额交易: 使用Maker订单避免冲击")
    print("   - 紧急交易: 使用Taker订单确保执行")


def maker_order_strategies():
    """Maker订单策略演示"""
    print("\n=== Maker订单策略演示 ===\n")
    
    print("📈 Maker订单使用策略:")
    print()
    
    print("1. 🎯 网格交易策略:")
    print("   - 适用场景: 震荡市场，价格在一定区间波动")
    print("   - 实现方式: 在支撑位挂买单，在阻力位挂卖单")
    print("   - 优势: 自动执行，享受Maker费率")
    print("   - 风险: 单边趋势市场可能亏损")
    print()
    
    print("2. 🕐 时间分散策略:")
    print("   - 适用场景: 需要在特定时间段内完成交易")
    print("   - 实现方式: 在不同时间点设置Maker订单")
    print("   - 优势: 分散风险，获得更好的平均价格")
    print("   - 风险: 市场快速变化时可能错过机会")
    print()
    
    print("3. 💰 价格分散策略:")
    print("   - 适用场景: 大额资金需要分批建仓或减仓")
    print("   - 实现方式: 在不同价格点设置Maker订单")
    print("   - 优势: 避免单点风险，获得更好的价格")
    print("   - 风险: 资金利用率可能较低")
    print()
    
    print("4. 📊 市场深度策略:")
    print("   - 适用场景: 需要根据市场深度调整策略")
    print("   - 实现方式: 分析订单簿，在合适位置挂单")
    print("   - 优势: 提高成交概率，获得更好价格")
    print("   - 风险: 需要持续监控市场变化")
    print()
    
    print("5. 🔄 动态调整策略:")
    print("   - 适用场景: 市场快速变化的环境")
    print("   - 实现方式: 根据市场变化动态调整订单价格")
    print("   - 优势: 适应市场变化，提高成交概率")
    print("   - 风险: 需要快速响应，可能增加交易成本")
    print()
    
    print("💡 策略选择建议:")
    print("   - 新手: 使用简单的网格策略")
    print("   - 进阶: 结合时间分散和价格分散")
    print("   - 专业: 多策略组合，动态调整")
    print("   - 风险控制: 设置合理的止损和止盈")


def maker_order_best_practices():
    """Maker订单最佳实践"""
    print("\n=== Maker订单最佳实践 ===\n")
    
    print("✅ 最佳实践:")
    print()
    
    print("1. 📊 价格设置:")
    print("   - 买入: 价格略低于当前买一价")
    print("   - 卖出: 价格略高于当前卖一价")
    print("   - 避免设置极端价格")
    print("   - 考虑市场波动性")
    print()
    
    print("2. ⏰ 时间管理:")
    print("   - 避免在市场开盘和收盘时使用")
    print("   - 选择流动性较好的时间段")
    print("   - 设置合理的订单有效期")
    print("   - 定期检查和调整订单")
    print()
    
    print("3. 🔍 市场监控:")
    print("   - 监控市场深度变化")
    print("   - 关注价格趋势变化")
    print("   - 观察成交量变化")
    print("   - 及时调整策略")
    print()
    
    print("4. 🛡️  风险控制:")
    print("   - 设置合理的订单数量")
    print("   - 避免过度集中")
    print("   - 准备应急取消方案")
    print("   - 记录交易日志")
    print()
    
    print("5. 💰 成本控制:")
    print("   - 计算总交易成本")
    print("   - 考虑机会成本")
    print("   - 平衡成交概率和价格")
    print("   - 优化手续费支出")
    print()
    
    print("⚠️  注意事项:")
    print("   - Maker订单可能长时间不成交")
    print("   - 需要持续监控市场变化")
    print("   - 在极端市场条件下可能失效")
    print("   - 考虑网络延迟和系统延迟")


if __name__ == "__main__":
    # 注意: 这些示例需要真实的API密钥才能执行
    # 请先设置你的API密钥，或者注释掉这些调用
    
    print("=== TooBit API SDK Maker订单示例 ===\n")
    print("⚠️  重要提醒: 所有Maker订单操作都是真实的!")
    print("⚠️  请确保在测试环境中验证，或使用小额测试")
    print("⚠️  建议先运行无需API密钥的示例熟悉接口\n")
    
    # 取消注释以下行来运行示例
    # create_maker_order()
    # create_sell_maker_order()
    
    compare_maker_vs_taker()
    maker_order_strategies()
    maker_order_best_practices()
    
    print("\n💡 提示:")
    print("   取消注释相应的函数调用来运行实际的Maker订单测试")
    print("   确保已设置正确的API密钥和充足的账户余额")
    print("   Maker订单适合长期投资和网格交易策略") 