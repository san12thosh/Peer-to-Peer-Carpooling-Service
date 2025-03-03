from web3 import Web3
from web3 import EthereumTesterProvider
from django.conf import settings

# Initialize Web3
w3 = Web3(EthereumTesterProvider())

def is_connected():
    return w3.isConnected()

def get_wallet_balance(address):
    try:
        # Check if the address is valid
        if not Web3.isAddress(address):
            return 'Invalid Ethereum address'
        
        balance_wei = w3.eth.get_balance(address)
        balance_eth = Web3.fromWei(balance_wei, 'ether')
        return balance_eth
    except Exception as e:
        return str(e)
