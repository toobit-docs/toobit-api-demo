#!/usr/bin/env python3
"""
TooBit API 获取所有订单示例
演示如何获取账户的历史订单信息
"""

import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from open_api_sdk import TooBitClient, TooBitConfig

def get_all_orders():
    """获取所有订单"""
    print("=== TooBit API 获取所有订单接口测试 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        limit = 20  # 限制返回数量
        
        print(f"🔍 获取 {symbol} 的所有订单 (限制 {limit} 个)...")
        
        # 调用获取所有订单接口
        all_orders = client.get_all_orders(symbol, limit=limit)
        
        print(f"✅ 获取成功! 共 {len(all_orders)} 个订单")
        print()
        
        if not all_orders:
            print("   ℹ️  没有找到订单")
            return
        
        # 显示前10个订单的详细信息
        print("📋 前10个订单详情:")
        for i, order in enumerate(all_orders[:10]):
            print(f"   {i+1:2d}. 订单ID: {order.order_id}")
            print(f"       客户端订单ID: {order.client_order_id}")
            print(f"       交易对: {order.symbol}")
            print(f"       方向: {order.side}")
            print(f"       类型: {order.type}")
            print(f"       状态: {order.status}")
            print(f"       数量: {order.orig_qty}")
            print(f"       已执行: {order.executed_qty}")
            print(f"       价格: {order.price}")
            print(f"       状态: {order.status}")
            
            # 显示成交信息
            if float(order.executed_qty) > 0:
                fill_percentage = (float(order.executed_qty) / float(order.orig_qty)) * 100
                # 注意：实际API响应中没有cummulative_quote_qty字段
                # avg_price = order.cummulative_quote_qty / order.executed_qty if float(order.executed_qty) > 0 else 0
                print(f"       成交: {order.executed_qty} ({fill_percentage:.1f}%)")
                print(f"       平均价格: 需要查询成交历史获取")
            
            print()
        
        if len(all_orders) > 10:
            print(f"   ... 还有 {len(all_orders) - 10} 个历史订单")
        
        print("\n🎉 获取所有订单接口测试完成!")
        return all_orders
        
    except Exception as e:
        print(f"❌ 获取所有订单接口测试失败: {e}")
        print("\n可能的原因:")
        print("   - API密钥无效或过期")
        print("   - API密钥权限不足")
        print("   - 网络连接问题")
        print("   - 签名验证失败")
        print("   - 交易对不存在")
        return None
    
    finally:
        client.close()


def get_orders_with_time_range():
    """获取指定时间范围的订单"""
    print("\n=== 获取指定时间范围的订单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        
        # 设置时间范围 (最近7天)
        end_time = datetime.now()
        start_time = end_time - timedelta(days=7)
        
        start_timestamp = int(start_time.timestamp() * 1000)
        end_timestamp = int(end_time.timestamp() * 1000)
        
        print(f"🔍 获取 {symbol} 最近7天的订单...")
        print(f"   时间范围: {start_time.strftime('%Y-%m-%d %H:%M:%S')} 到 {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # 调用获取指定时间范围的订单接口
        orders = client.get_all_orders(
            symbol=symbol,
            start_time=start_timestamp,
            end_time=end_timestamp
        )
        
        print(f"✅ 获取成功! 共 {len(orders)} 个订单")
        print()
        
        if not orders:
            print("   ℹ️  指定时间范围内没有订单")
            return
        
        # 按天分组统计
        daily_count = {}
        for order in orders:
            # 注意：实际API响应中没有time字段，使用transact_time
            order_date = datetime.fromtimestamp(int(order.transact_time)/1000).strftime('%Y-%m-%d')
            daily_count[order_date] = daily_count.get(order_date, 0) + 1
        
        print("📅 每日订单分布:")
        for date in sorted(daily_count.keys()):
            count = daily_count[date]
            print(f"   {date}: {count} 个订单")
        print()
        
        # 分析订单活跃度
        total_days = 7
        avg_orders_per_day = len(orders) / total_days
        
        print("📊 订单活跃度分析:")
        print(f"   总订单数: {len(orders)}")
        print(f"   平均每日订单: {avg_orders_per_day:.1f} 个")
        
        if avg_orders_per_day >= 10:
            activity_level = "非常活跃"
            activity_emoji = "🔥"
        elif avg_orders_per_day >= 5:
            activity_level = "比较活跃"
            activity_emoji = "⚡"
        elif avg_orders_per_day >= 1:
            activity_level = "一般活跃"
            activity_emoji = "📊"
        else:
            activity_level = "不太活跃"
            activity_emoji = "😴"
        
        print(f"   活跃度: {activity_emoji} {activity_level}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 获取指定时间范围订单失败: {e}")


def analyze_order_history():
    """分析订单历史"""
    print("\n=== 订单历史分析 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        limit = 100  # 获取更多订单进行分析
        
        print(f"📊 分析 {symbol} 的订单历史...")
        
        # 获取订单列表
        all_orders = client.get_all_orders(symbol, limit=limit)
        
        if not all_orders:
            print("   ℹ️  没有订单数据")
            return
        
        print(f"✅ 获取到 {len(all_orders)} 个订单")
        print()
        
        # 统计订单状态分布
        status_count = {}
        type_count = {}
        side_count = {}
        
        for order in all_orders:
            status_count[order.status] = status_count.get(order.status, 0) + 1
            type_count[order.type] = type_count.get(order.type, 0) + 1
            side_count[order.side] = side_count.get(order.side, 0) + 1
        
        print("📈 订单状态分布:")
        for status, count in sorted(status_count.items()):
            percentage = (count / len(all_orders)) * 100
            print(f"   {status}: {count} 个 ({percentage:.1f}%)")
        print()
        
        print("📊 订单类型分布:")
        for order_type, count in sorted(type_count.items()):
            percentage = (count / len(all_orders)) * 100
            print(f"   {order_type}: {count} 个 ({percentage:.1f}%)")
        print()
        
        print("📈 订单方向分布:")
        for side, count in sorted(side_count.items()):
            percentage = (count / len(all_orders)) * 100
            print(f"   {side}: {count} 个 ({percentage:.1f}%)")
        print()
        
        # 分析成交情况
        filled_orders = [o for o in all_orders if o.status == "FILLED"]
        partial_orders = [o for o in all_orders if o.status == "PARTIALLY_FILLED"]
        
        total_filled = len(filled_orders)
        total_partial = len(partial_orders)
        
        fill_rate = (total_filled / len(all_orders)) * 100 if all_orders else 0
        
        print("💹 成交情况分析:")
        print(f"   完全成交: {total_filled} 个")
        print(f"   部分成交: {total_partial} 个")
        print(f"   成交率: {fill_rate:.1f}%")
        
        if fill_rate >= 80:
            fill_level = "优秀"
            fill_emoji = "🟢"
        elif fill_rate >= 60:
            fill_level = "良好"
            fill_emoji = "🟡"
        elif fill_rate >= 40:
            fill_level = "一般"
            fill_emoji = "🟠"
        else:
            fill_level = "较差"
            fill_emoji = "🔴"
        
        print(f"   成交率评价: {fill_emoji} {fill_level}")
        print()
        
        # 分析交易金额
        total_buy_amount = 0
        total_sell_amount = 0
        total_buy_qty = 0
        total_sell_qty = 0
        
        for order in filled_orders:
            if order.side == "BUY":
                # 注意：实际API响应中没有cummulative_quote_qty字段
                # total_buy_amount += order.cummulative_quote_qty
                total_buy_qty += float(order.executed_qty)
            else:
                # 注意：实际API响应中没有cummulative_quote_qty字段
                # total_sell_amount += order.cummulative_quote_qty
                total_sell_qty += float(order.executed_qty)
        
        print("💰 交易数量分析:")
        print(f"   买入总数量: {total_buy_qty:.6f} BTC")
        print(f"   卖出总数量: {total_sell_qty:.6f} BTC")
        print(f"   净买入数量: {total_buy_qty - total_sell_qty:+.6f} BTC")
        print()
        
        # 分析订单时间分布
        if all_orders:
            # 注意：实际API响应中没有time字段，使用transact_time
            order_times = [datetime.fromtimestamp(int(o.transact_time)/1000) for o in all_orders]
            earliest_order = min(order_times)
            latest_order = max(order_times)
            
            print("⏰ 时间分布分析:")
            print(f"   最早订单: {earliest_order.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   最新订单: {latest_order.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   交易跨度: {(latest_order - earliest_order).days} 天")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 订单历史分析失败: {e}")


def get_orders_with_pagination():
    """分页获取订单"""
    print("\n=== 分页获取订单 ===\n")
    
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        limit = 10  # 每页10个订单
        
        print(f"📄 分页获取 {symbol} 的订单 (每页 {limit} 个)...")
        
        # 获取第一页订单
        orders_page1 = client.get_all_orders(symbol, limit=limit)
        
        print(f"✅ 第一页获取成功! 共 {len(orders_page1)} 个订单")
        
        if not orders_page1:
            print("   ℹ️  没有订单")
            return
        
        # 显示第一页订单
        print("\n📋 第一页订单:")
        for i, order in enumerate(orders_page1):
            # 注意：实际API响应中没有time字段，使用transact_time
            order_time = datetime.fromtimestamp(int(order.transact_time)/1000).strftime('%m-%d %H:%M')
            print(f"   {i+1:2d}. {order_time} | "
                  f"{order.side} | {order.type} | {order.status} | "
                  f"数量: {order.orig_qty} | 价格: {order.price}")
        
        # 如果有更多订单，获取第二页
        if len(orders_page1) == limit:
            print(f"\n📄 获取第二页订单...")
            
            # 使用最后一个订单的ID作为起始点
            last_order_id = orders_page1[-1].order_id
            
            orders_page2 = client.get_all_orders(
                symbol=symbol, 
                limit=limit,
                order_id=last_order_id
            )
            
            print(f"✅ 第二页获取成功! 共 {len(orders_page2)} 个订单")
            
            if orders_page2:
                print("\n📋 第二页订单:")
                for i, order in enumerate(orders_page2):
                    # 注意：实际API响应中没有time字段，使用transact_time
                    order_time = datetime.fromtimestamp(int(order.transact_time)/1000).strftime('%m-%d %H:%M')
                    print(f"   {i+1:2d}. {order_time} | "
                          f"{order.side} | {order.type} | {order.status} | "
                          f"数量: {order.orig_qty} | 价格: {order.price}")
        
        print("\n🎉 分页获取订单测试完成!")
        
        client.close()
        
    except Exception as e:
        print(f"❌ 分页获取订单失败: {e}")


def main():
    """主函数"""
    print("=== TooBit API SDK 获取所有订单示例 ===\n")
    
    # 测试基本功能
    get_all_orders()
    
    # 测试时间范围查询
    get_orders_with_time_range()
    
    # 测试订单历史分析
    analyze_order_history()
    
    # 测试分页功能
    get_orders_with_pagination()
    
    print("\n=== 所有测试完成 ===")


if __name__ == "__main__":
    main() 