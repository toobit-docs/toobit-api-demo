"""
TooBit 合约API SDK - 获取深度信息示例
获取订单簿深度信息 (无需API密钥)
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_order_book():
    """获取订单簿深度信息"""
    print("=== TooBit 合约API 获取深度信息 ===\n")
    
    try:
        # 创建配置 (无需API密钥)
        config = TooBitConfig(
            api_key="test_key",
            api_secret="test_secret"
        )
        
        # 创建客户端
        client = TooBitClient(config)
        
        symbol = "BTCUSDT"
        limit = 10  # 深度档数
        
        print(f"🔄 正在获取 {symbol} 的深度信息 (深度: {limit})...")
        
        # 获取订单簿深度
        response = client.get_order_book(symbol, limit)
        
        print("✅ 深度信息获取成功!")
        
        # 显示基本信息
        if hasattr(response, 'symbol'):
            print(f"   交易对: {response.symbol}")
        
        # 显示买单深度
        if hasattr(response, 'b') and response.b:
            print(f"\n📈 买单深度 (前{min(limit, len(response.b))}档):")
            for i, bid in enumerate(response.b[:limit]):
                price = float(bid[0])
                quantity = float(bid[1])
                print(f"   {i+1:2d}. 价格: {price:>10.2f} | 数量: {quantity:>10.4f}")
        
        # 显示卖单深度
        if hasattr(response, 'a') and response.a:
            print(f"\n📉 卖单深度 (前{min(limit, len(response.a))}档):")
            for i, ask in enumerate(response.a[:limit]):
                price = float(ask[0])
                quantity = float(ask[1])
                print(f"   {i+1:2d}. 价格: {price:>10.2f} | 数量: {quantity:>10.4f}")
        
        print("\n🎉 深度信息获取完成!")
        return response
        
    except Exception as e:
        print(f"❌ 获取深度信息失败: {e}")
        return None
    
    finally:
        client.close()


if __name__ == "__main__":
    print("=== TooBit 合约API SDK 获取深度信息示例 ===\n")
    print("💡 这个示例无需API密钥，可以直接运行")
    
    # 运行示例
    get_order_book()
