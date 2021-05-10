# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from web3 import Web3
from eth_account import Account
from constants import ETH, BTC, BTCTEST
from bit import PrivateKeyTestnet
from bit import wif_to_key
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
 
# Create a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive):
    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --numderive="{numderive}" --coin="{coin}" --format=json' 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return json.loads(output)


# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {"eth", "btc-test","btc"}

keys = {}
for coin in coins:
    keys[coin]= derive_wallets(mnemonic, coin, numderive=3)

print(json.dumps(keys, indent=4, sort_keys=True))

