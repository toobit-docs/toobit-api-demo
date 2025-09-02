"""
TooBit API SDK - 获取订单簿接口示例
获取深度信息
"""

from open_api_sdk import TooBitClient, TooBitConfig


def get_order_book():
    """获取订单簿信息"""
    print("=== TooBit API 获取订单簿接口测试 ===\n")
    
    # 创建配置 (不需要真实的API密钥来测试连接)
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    # 创建客户端
    client = TooBitClient(config)
    
    try:
        symbol = "BTCUSDT"
        limit = 10
        
        print(f"📊 获取 {symbol} 订单簿信息...")
        print(f"   深度限制: {limit} 档")
        print()
        
        # 调用获取订单簿接口
        order_book = client.get_order_book(symbol, limit)
        
        print("✅ 订单簿信息获取成功!")
        print()
        
        # 显示基本信息
        print("📋 基本信息:")
        print(f"   交易对: {symbol}")
        print(f"   最后更新ID: {order_book.last_update_id}")
        print(f"   买单数量: {len(order_book.bids)} 档")
        print(f"   卖单数量: {len(order_book.asks)} 档")
        print()
        
        # 显示买单信息
        print("🟢 买单 (Bids):")
        total_bid_volume = 0
        for i, bid in enumerate(order_book.bids):
            price = bid.price
            quantity = bid.quantity
            total_bid_volume += quantity
            
            print(f"   {i+1:2d}. 价格: {price:>10,.2f} USDT")
            print(f"       数量: {quantity:>12.6f} BTC")
            print(f"       累计: {total_bid_volume:>12.6f} BTC")
            print()
        
        # 显示卖单信息
        print("🔴 卖单 (Asks):")
        total_ask_volume = 0
        for i, ask in enumerate(order_book.asks):
            price = ask.price
            quantity = ask.quantity
            total_ask_volume += quantity
            
            print(f"   {i+1:2d}. 价格: {price:>10,.2f} USDT")
            print(f"       数量: {quantity:>12.6f} BTC")
            print(f"       累计: {total_ask_volume:>12.6f} BTC")
            print()
        
        # 计算买卖价差
        if order_book.bids and order_book.asks:
            best_bid = order_book.bids[0].price
            best_ask = order_book.asks[0].price
            spread = best_ask - best_bid
            spread_percentage = (spread / best_bid) * 100
            
            print("💰 价差分析:")
            print(f"   最佳买价: {best_bid:,.2f} USDT")
            print(f"   最佳卖价: {best_ask:,.2f} USDT")
            print(f"   价差: {spread:,.2f} USDT")
            print(f"   价差百分比: {spread_percentage:.4f}%")
            
            # 判断价差状态
            if spread_percentage < 0.01:
                print("   ✅ 价差状态: 优秀")
            elif spread_percentage < 0.05:
                print("   ✅ 价差状态: 良好")
            elif spread_percentage < 0.1:
                print("   ⚠️  价差状态: 一般")
            else:
                print("   ❌ 价差状态: 较差")
            print()
        
        # 显示流动性分析
        print("💧 流动性分析:")
        print(f"   买单总流动性: {total_bid_volume:.6f} BTC")
        print(f"   卖单总流动性: {total_ask_volume:.6f} BTC")
        
        if total_bid_volume > 0 and total_ask_volume > 0:
            liquidity_ratio = total_bid_volume / total_ask_volume
            print(f"   买卖流动性比例: {liquidity_ratio:.2f}")
            
            if 0.8 <= liquidity_ratio <= 1.2:
                print("   ✅ 流动性平衡: 良好")
            else:
                print("   ⚠️  流动性平衡: 不平衡")
        
        print("\n🎉 获取订单簿接口测试完成!")
        return True
        
    except Exception as e:
        print(f"❌ 获取订单簿接口测试失败: {e}")
        return False
    
    finally:
        client.close()


def get_order_book_multiple_symbols():
    """获取多个交易对的订单簿信息"""
    print("\n=== 多交易对订单簿对比 ===\n")
    
    config = TooBitConfig(
        api_key="test_key",
        api_secret="test_secret"
    )
    
    client = TooBitClient(config)
    
    try:
        symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
        limit = 5
        
        print(f"📊 获取 {len(symbols)} 个交易对的订单簿信息...")
        print(f"   深度限制: {limit} 档")
        print()
        
        for symbol in symbols:
            try:
                print(f"🔍 {symbol}:")
                
                order_book = client.get_order_book(symbol, limit)
                
                if order_book.bids and order_book.asks:
                    best_bid = order_book.bids[0].price
                    best_ask = order_book.asks[0].price
                    spread = best_ask - best_bid
                    spread_percentage = (spread / best_bid) * 100
                    
                    print(f"   最佳买价: {best_bid:,.4f}")
                    print(f"   最佳卖价: {best_ask:,.4f}")
                    print(f"   价差: {spread_percentage:.4f}%")
                    
                    # 计算前5档总流动性
                    bid_volume = sum(bid.quantity for bid in order_book.bids[:5])
                    ask_volume = sum(ask.quantity for ask in order_book.asks[:5])
                    
                    print(f"   买单流动性: {bid_volume:.6f}")
                    print(f"   卖单流动性: {ask_volume:.6f}")
                else:
                    print("   ❌ 无法获取订单簿数据")
                
                print()
                
            except Exception as e:
                print(f"   ❌ 获取 {symbol} 订单簿失败: {e}")
                print()
        
        print("🎉 多交易对订单簿对比完成!")
        
    except Exception as e:
        print(f"❌ 多交易对订单簿对比失败: {e}")
    
    finally:
        client.close()


if __name__ == "__main__":
    get_order_book()
    get_order_book_multiple_symbols() 