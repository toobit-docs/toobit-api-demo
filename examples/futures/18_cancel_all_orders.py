"""
TooBit 合约API SDK - 撤销全部订单示例 (18)
撤销全部订单 (需要API密钥和签名)
接口: DELETE /api/v1/futures/order
"""
from open_api_sdk import TooBitClient, TooBitConfig
from open_api_sdk.models import CancelAllOrdersResponse

def cancel_all_orders():
    """撤销全部订单"""
    print("=== TooBit 合约API 撤销全部订单 ===\n")
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        symbol = "BTC-SWAP-USDT"  # 交易对
        print("🔄 正在撤销全部订单...")
        print(f"   交易对: {symbol}")
        print()
        print("⚠️  注意: 这是真实的交易操作，请谨慎使用!")
        print("⚠️  建议先在测试环境中验证")
        print()
        response = client.cancel_all_orders(symbol)
        print("✅ 撤销全部订单成功!")
        print()
        
        # 显示撤销结果
        print("📋 撤销结果:")
        if hasattr(response, 'code'):
            print(f"   📊 响应代码: {response.code}")
        if hasattr(response, 'message'):
            print(f"   💬 响应消息: {response.message}")
        if hasattr(response, 'timestamp'):
            print(f"   🕐 时间戳: {response.timestamp}")
        
        # 检查是否成功
        if hasattr(response, 'code') and response.code == 200:
            print("   ✅ 撤销操作成功完成")
        else:
            print("   ⚠️  撤销操作可能未完全成功")
        print("\n🎉 撤销全部订单完成!")
        return response
    except Exception as e:
        print(f"❌ 撤销全部订单失败: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    print("=== TooBit 合约API SDK 撤销全部订单示例 ===\n")
    print("💡 这个示例需要API密钥，请确保配置正确")
    print("💡 这是真实的交易操作，请谨慎使用!")
    print()
    print("📚 接口信息:")
    print("   - 接口: DELETE /api/v1/futures/order")
    print("   - 鉴权: 需要签名 (TRADE)")
    print("   - 功能: 撤销指定交易对的所有订单")
    print("   - 参数: symbol")
    print()
    print("⚠️  重要提醒:")
    print("   - 此操作不可逆")
    print("   - 将撤销所有未成交的订单")
    print("   - 请确保这是您想要的操作")
    cancel_all_orders()
