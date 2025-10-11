#!/usr/bin/env python3
"""
TooBit API Futures QueryCurrentPositionExample (21Number)
Query current position information, supports filtering by trading pair and side
"""

from open_api_sdk import TooBitClient, TooBitConfig

def get_futures_positions():
    """QueryCurrentPositionExample"""
    print("=== TooBit API Futures QueryCurrentPositionExample ===\n")
    
    # Initialize configuration
    config = TooBitConfig.from_env()
    client = TooBitClient(config)
    
    try:
        print("🔍 Query Current Position Test:")
        print()
        
        # Example1: QueryAllPosition
        print("📊 Example 1: Query All Position")
        print("   Parameters: None")
        print("   API: GET /api/v1/futures/positions")
        print("   Description: Query all futures positions under account")
        print()
        
        response1 = client.get_futures_positions()
        print(f"   Response Quantity: {len(response1)} items Position")
        if response1:
            print("   Position List:")
            for i, position in enumerate(response1, 1):
                print(f"     Position {i}: {position.symbol} - {position.side}")
        print()
        
        # Example2: QuerySpecifiedTrading pairofPosition
        print("📊 Example 2: Query Specified Trading pair of Position")
        print("   Parameters: symbol='BTC-SWAP-USDT'")
        print("   API: GET /api/v1/futures/positions?symbol=BTC-SWAP-USDT")
        print("   Description: Query BTC-SWAP-USDT Trading pair of All Position")
        print()
        
        response2 = client.get_futures_positions(symbol='BTC-SWAP-USDT')
        print(f"   Response Quantity: {len(response2)} items Position")
        if response2:
            print("   Position Details:")
            for position in response2:
                print(f"     Trading pair: {position.symbol}")
                print(f"     Side: {position.side}")
                print(f"     Quantity: {position.position} Contract")
                print(f"     Available to close: {position.available} Contract")
                print(f"     Leverage: {position.leverage}x")
                print(f"     Average price: {position.avgPrice}")
                print(f"     Latest price: {position.lastPrice}")
                print(f"     Mark price: {position.markPrice}")
                print(f"     Unrealized PnL: {position.unrealizedPnL}")
                print(f"     Realized PnL: {position.realizedPnL}")
                print(f"     Margin: {position.margin}")
                print(f"     MarginRate: {position.marginRate}")
                print(f"     Forced close price: {position.flp}")
                print()
        
        # Example3: QuerySpecifiedTrading pairAndSideofPosition
        print("📊 Example 3: Query Specified Trading pair And Side of Position")
        print("   Parameters: symbol='BTC-SWAP-USDT', side='LONG'")
        print("   API: GET /api/v1/futures/positions?symbol=BTC-SWAP-USDT&side=LONG")
        print("   Description: Query BTC-SWAP-USDT Trading pair of Long Position")
        print()
        
        response3 = client.get_futures_positions(symbol='BTC-SWAP-USDT', side='LONG')
        print(f"   Response Quantity: {len(response3)} items Position")
        if response3:
            print("   Long Position Details:")
            for position in response3:
                print(f"     Trading pair: {position.symbol}")
                print(f"     Side: {position.side}")
                print(f"     Quantity: {position.position} Contract")
                print(f"     Available to close: {position.available} Contract")
                print(f"     Leverage: {position.leverage}x")
                print(f"     Average price: {position.avgPrice}")
                print(f"     Latest price: {position.lastPrice}")
                print(f"     Unrealized PnL: {position.unrealizedPnL}")
                print(f"     Realized PnL: {position.realizedPnL}")
                print(f"     Margin: {position.margin}")
                print(f"     MarginRate: {position.marginRate}")
                print(f"     Forced close price: {position.flp}")
                print()
        
        # Example4: QuerySpecifiedSideofPosition
        print("📊 Example 4: Query Specified Side of Position")
        print("   Parameters: side='SHORT'")
        print("   API: GET /api/v1/futures/positions?side=SHORT")
        print("   Description: Query All Short Position")
        print()
        
        response4 = client.get_futures_positions(side='SHORT')
        print(f"   Response Quantity: {len(response4)} items Position")
        if response4:
            print("   Short Position List:")
            for position in response4:
                print(f"     {position.symbol} - {position.side} - {position.position} Contract")
        print()
        
        print("🎉 Query Current Position Test Complete!")
        
    except Exception as e:
        print(f"❌ Query Current Position Test Failed: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    get_futures_positions()
