"""
TooBit Futures API SDK - Master Sub Account Universal Transfer
"""

from open_api_sdk import TooBitClient, TooBitConfig

def transfer_between_accounts():
    """Master Sub Account Universal Transfer"""
    try:
        config = TooBitConfig.from_env()
        client = TooBitClient(config)
        
        from_account_type = "SPOT"
        to_account_type = "FUTURES"
        asset = "USDT"
        quantity = "100"
        
        print(f"Request Parameters: from_account_type={from_account_type}, to_account_type={to_account_type}, asset={asset}, quantity={quantity}")
        
        response = client.transfer_between_accounts(
            from_account_type=from_account_type,
            to_account_type=to_account_type,
            asset=asset,
            quantity=quantity
        )
        
        print(f"Response: {response}")
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    transfer_between_accounts()
