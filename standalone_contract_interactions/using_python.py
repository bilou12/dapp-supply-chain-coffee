from web3 import Web3
from web3.middleware import geth_poa_middleware

CONTRACT_ADDRESS = '0xcec31315b8c453eae37d9d1b42a3842a69021812'

ACCOUNT_ADDRESS = '0xc6696eDf5e753f5B3009608F9e25ED2cb713C7fA'
f = open(".deployment_account_pk", "r")
ACCOUNT_PK = f.readline()

FARMER_ADDRESS = '0xAFE4B7Ea233758Ae11b7687e43eF97AB6F6407f9'

f = open("../.infura-key", "r")
INFURA_PROJECT_ID = f.readline()


def print_buffer():
    buffer_1 = contract_instance.functions.fetchItemBufferOne(1).call()
    print(f'buffer_1: {buffer_1}')
    buffer_2 = contract_instance.functions.fetchItemBufferTwo(1).call()
    print(f'buffer_2: {buffer_2}')


# init
w3 = Web3(Web3.HTTPProvider(
    'https://rinkeby.infura.io/v3/{INFURA_PROJECT_ID}'))
# to work around discrepancy in the block format between your private geth
# network (or a public test network like Rinkeby) and the main network
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract_address = w3.toChecksumAddress(CONTRACT_ADDRESS)
contract_abi = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "account",
         "type": "address"}], "name": "ConsumerAdded", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "account",
         "type": "address"}], "name": "ConsumerRemoved", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "account",
         "type": "address"}], "name": "DistributorAdded", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "account",
         "type": "address"}], "name": "DistributorRemoved", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "account",
         "type": "address"}], "name": "FarmerAdded", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "account",
         "type": "address"}], "name": "FarmerRemoved", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": False, "internalType": "uint256", "name": "upc",
         "type": "uint256"}], "name": "ForSale", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": False, "internalType": "uint256", "name": "upc",
         "type": "uint256"}], "name": "Harvested", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": False, "internalType": "uint256", "name": "upc",
         "type": "uint256"}], "name": "Packed", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": False, "internalType": "uint256", "name": "upc",
         "type": "uint256"}], "name": "Processed", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": False, "internalType": "uint256", "name": "upc",
         "type": "uint256"}], "name": "Purchased", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": False, "internalType": "uint256", "name": "upc",
         "type": "uint256"}], "name": "Received", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "account",
         "type": "address"}], "name": "RetailerAdded", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "account",
         "type": "address"}], "name": "RetailerRemoved", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": False, "internalType": "uint256", "name": "upc",
         "type": "uint256"}], "name": "Shipped", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": False, "internalType": "uint256", "name": "upc",
         "type": "uint256"}], "name": "Sold", "type": "event"},
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "oldOwner",
         "type": "address"},
        {"indexed": True, "internalType": "address", "name": "newOwner",
         "type": "address"}], "name": "TransferOwnership", "type": "event"},
    {"inputs": [
        {"internalType": "address", "name": "account", "type": "address"}],
        "name": "addConsumer", "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"}, {"inputs": [
            {"internalType": "address", "name": "account", "type": "address"}],
        "name": "addDistributor", "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"}, {"inputs": [
            {"internalType": "address", "name": "account", "type": "address"}],
        "name": "addFarmer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"}, {
        "inputs": [{"internalType": "address", "name": "account",
                    "type": "address"}], "name": "addRetailer",
        "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [
        {"internalType": "address", "name": "account", "type": "address"}],
        "name": "isConsumer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view", "type": "function", "constant": True}, {
        "inputs": [{"internalType": "address", "name": "account",
                    "type": "address"}], "name": "isDistributor",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view", "type": "function", "constant": True}, {
        "inputs": [{"internalType": "address", "name": "account",
                    "type": "address"}], "name": "isFarmer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view", "type": "function", "constant": True},
    {"inputs": [], "name": "isOwner",
     "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
     "stateMutability": "view", "type": "function", "constant": True}, {
        "inputs": [{"internalType": "address", "name": "account",
                    "type": "address"}], "name": "isRetailer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view", "type": "function", "constant": True},
    {"inputs": [], "name": "ownerOrig",
     "outputs": [{"internalType": "address", "name": "", "type": "address"}],
     "stateMutability": "view", "type": "function", "constant": True},
    {"inputs": [], "name": "renounceConsumer", "outputs": [],
     "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "renounceDistributor", "outputs": [],
     "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "renounceFarmer", "outputs": [],
     "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "renounceOwnership", "outputs": [],
     "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "renounceRetailer", "outputs": [],
     "stateMutability": "nonpayable", "type": "function"}, {"inputs": [
         {"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"},
    {"inputs": [], "name": "kill", "outputs": [],
     "stateMutability": "nonpayable", "type": "function"}, {"inputs": [
         {"internalType": "uint256", "name": "_upc", "type": "uint256"},
         {"internalType": "address", "name": "_originFarmerID",
             "type": "address"},
         {"internalType": "string", "name": "_originFarmName", "type": "string"},
         {"internalType": "string", "name": "_originFarmInformation",
             "type": "string"},
         {"internalType": "string", "name": "_originFarmLatitude",
             "type": "string"},
         {"internalType": "string", "name": "_originFarmLongitude",
             "type": "string"},
         {"internalType": "string", "name": "_productNotes", "type": "string"}],
        "name": "harvestItem",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"},
    {"inputs": [
        {"internalType": "uint256", "name": "_upc", "type": "uint256"}],
        "name": "processItem", "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"}, {"inputs": [
            {"internalType": "uint256", "name": "_upc", "type": "uint256"}],
        "name": "packItem", "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"}, {"inputs": [
            {"internalType": "uint256", "name": "_upc", "type": "uint256"},
            {"internalType": "uint256", "name": "_price", "type": "uint256"}],
        "name": "sellItem",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"}, {
        "inputs": [
            {"internalType": "uint256", "name": "_upc", "type": "uint256"}],
        "name": "buyItem", "outputs": [], "stateMutability": "payable",
        "type": "function", "payable": True}, {"inputs": [
            {"internalType": "uint256", "name": "_upc", "type": "uint256"}],
        "name": "shipItem",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"}, {
        "inputs": [
            {"internalType": "uint256", "name": "_upc", "type": "uint256"}],
        "name": "receiveItem", "outputs": [],
        "stateMutability": "nonpayable", "type": "function"}, {"inputs": [
            {"internalType": "uint256", "name": "_upc", "type": "uint256"}],
        "name": "purchaseItem",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function",
        "payable": True},
    {"inputs": [
        {"internalType": "uint256", "name": "_upc", "type": "uint256"}],
        "name": "fetchItemBufferOne", "outputs": [
        {"internalType": "uint256", "name": "itemSKU", "type": "uint256"},
        {"internalType": "uint256", "name": "itemUPC", "type": "uint256"},
        {"internalType": "address", "name": "ownerID", "type": "address"},
        {"internalType": "address", "name": "originFarmerID",
         "type": "address"},
        {"internalType": "string", "name": "originFarmName",
         "type": "string"},
        {"internalType": "string", "name": "originFarmInformation",
         "type": "string"},
        {"internalType": "string", "name": "originFarmLatitude",
         "type": "string"},
        {"internalType": "string", "name": "originFarmLongitude",
         "type": "string"}], "stateMutability": "view", "type": "function",
        "constant": True}, {"inputs": [
            {"internalType": "uint256", "name": "_upc", "type": "uint256"}],
        "name": "fetchItemBufferTwo", "outputs": [
            {"internalType": "uint256", "name": "itemSKU", "type": "uint256"},
            {"internalType": "uint256", "name": "itemUPC", "type": "uint256"},
            {"internalType": "uint256", "name": "productID", "type": "uint256"},
            {"internalType": "string", "name": "productNotes",
             "type": "string"},
            {"internalType": "uint256", "name": "productPrice",
             "type": "uint256"},
            {"internalType": "uint256", "name": "itemState", "type": "uint256"},
            {"internalType": "address", "name": "distributorID",
             "type": "address"},
            {"internalType": "address", "name": "retailerID",
             "type": "address"},
            {"internalType": "address", "name": "consumerID",
             "type": "address"}], "stateMutability": "view", "type": "function",
        "constant": True}
]
contract_instance = w3.eth.contract(address=contract_address, abi=contract_abi)

# call
print_buffer()

# send tx
_upc = int(1)
_origin_farmer_id = w3.toChecksumAddress(FARMER_ADDRESS)
_origin_farm_name = 'Ben'
_origin_farm_info = 'Hossegor'
_origin_farm_latitude = '-38'
_origin_farm_longitude = '12'
_product_notes = 'blablabla'

nonce = w3.eth.getTransactionCount(w3.toChecksumAddress(ACCOUNT_ADDRESS))
print(f'nonce: {nonce}')
key = contract_instance.functions \
    .harvestItem(_upc, _origin_farmer_id, _origin_farm_name, _origin_farm_info,
                 _origin_farm_latitude, _origin_farm_longitude,
                 _product_notes) \
    .buildTransaction({'nonce': nonce, 'from': ACCOUNT_ADDRESS})
print(f'key: {key}')
signed_tx = w3.eth.account.signTransaction(key, private_key=ACCOUNT_PK)
print(f'signed_tx: {signed_tx}')
w3.eth.sendRawTransaction(signed_tx.rawTransaction)

# call
print_buffer()
