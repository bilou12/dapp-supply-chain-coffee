// This method does not work because Infura does not support eth_sendTransaction.
// (For it to support that, it would need to know your private key, but it's a shared public node.)
// Prefer method 3.

const Web3 = require('web3');
const fs = require('fs');

const infuraKey = fs.readFileSync("../.infura-key").toString().trim();
const privateKey = fs.readFileSync(".owner_account_pk").toString().trim(); // fs.readFileSync(".owner_account_pk").toString().trim();

const MyContract = require('../build/contracts/SupplyChain.json');

const account_address = '0xAFE4B7Ea233758Ae11b7687e43eF97AB6F6407f9';
const UPC = 1;

const init = async () => {
  const web3 = new Web3(`https://rinkeby.infura.io/v3/${infuraKey}`);
  const networkId = await web3.eth.net.getId();
  const contract_supply_chain = new web3.eth.Contract(
    MyContract.abi,
    MyContract.networks[networkId].address
  );
  web3.eth.accounts.wallet.add(privateKey);

  // call 
  let buffer1 = await contract_supply_chain.methods.fetchItemBufferOne(UPC).call({
    from: account_address
  });
  console.log('buffer1 before: %j', buffer1)

  // send tx
  console.log('contract_supply_chain.options.address: ' + contract_supply_chain.options.address)
  const tx = contract_supply_chain.methods.processItem(UPC);
  let gas = await tx.estimateGas({
    from: account_address
  });
  // gas = web3.utils.toHex('21000')
  console.log('gas: ' + gas)
  let gasPrice = await web3.eth.getGasPrice();
  // gasPrice = web3.utils.toHex('25000000000')
  console.log('gasPrice: ' + gasPrice)
  const data = tx.encodeABI();
  const nonce = await web3.eth.getTransactionCount(account_address);
  console.log('nonce: ' + nonce)


  const txData = {
    from: account_address,
    to: contract_supply_chain.options.address,
    data: data,
    gas,
    gasPrice,
    nonce,
    chain: 'rinkeby'
  };

  // does not work because Infura does not support eth_sendTransaction 
  // (For it to support that, it would need to know your private key, but it's a shared public node.)
  const receipt = await web3.eth.sendTransaction(txData);
  console.log(`Transaction hash: ${receipt.transactionHash}`);

  // call
  buffer1 = await contract_supply_chain.methods.fetchItemBufferOne(UPC).call({
    from: account_address
  });
  console.log('buffer1 after: %j', buffer1)
}

init()