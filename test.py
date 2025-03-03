# test_web3_connection.py
from web3 import Web3
from web3 import EthereumTesterProvider

# Initialize Web3 with the Ethereum tester provider
w3 = Web3(EthereumTesterProvider())

# Function to check connection status
def test_connection():
    if w3.is_connected():
        print("Web3 is connected!")
    else:
        print("Web3 is not connected.")

if __name__ == "__main__":
    test_connection()

# w3 = Web3(Web3.EthereumTesterProvider())

# # Generate a new account
# account = w3.eth.account.create()

# print(f"New address: {account.address}")

address = '0xE64547B26fa84aaBA8676B020ab804B117f4D7f2'

# Check if the address is valid
if not Web3.is_address(address):
    print("Invalid Ethereum address")
else:
    # Get balance in Wei
    balance_wei = w3.eth.get_balance(address)

    # Convert balance to Ether
    balance_eth = Web3.from_wei(balance_wei, 'ether')
    print(f"Address: {address}")
    print(f"Balance: {balance_eth} ETH")