const Web3 = require('web3');
const fs = require('fs');
const Provider = require('truffle-hdwallet-provider');

const infuraKey = fs.readFileSync("../.infura-key").toString().trim();
const privateKey = fs.readFileSync(".owner_account_pk").toString().trim(); // fs.readFileSync(".deployment_account_pk").toString().trim();

const MyContract = require('../build/contracts/SupplyChain.json');

const account_address = '0xAFE4B7Ea233758Ae11b7687e43eF97AB6F6407f9' // '0xc6696eDf5e753f5B3009608F9e25ED2cb713C7fA';
const farmer_address = '0xAFE4B7Ea233758Ae11b7687e43eF97AB6F6407f9'
const UPC = 1;

// console.log('contract_supply_chain: %j', contract_supply_chain)

//Easy way (Web3 + truffle-hdwallet-provider)
const init = async () => {
  const provider = new Provider(privateKey, `https://rinkeby.infura.io/v3/${infuraKey}`);
  const web3 = new Web3(provider);
  const networkId = await web3.eth.net.getId();
  console.log('networkId: ' + networkId)
  const contract_supply_chain = new web3.eth.Contract(
    MyContract.abi,
    MyContract.networks[networkId].address
  );

  let buffer1 = await contract_supply_chain.methods.fetchItemBufferOne(UPC).call({
    from: account_address
  });
  console.log('buffer1: %j', buffer1)

  // send tx
  // originFarmerID = farmer_address;
  // originFarmName = "Ben";
  // originFarmInformation = "Node";
  // originFarmLatitude = "-20";
  // originFarmLongitude = "36";
  // productNotes = "bla";

  var receipt = await contract_supply_chain.methods
    .processItem(UPC)
    .send({
      from: account_address
    });
  console.log('receipt: %j', receipt)
  console.log(`Transaction hash: ${receipt.transactionHash}`);

  // call
  contract_supply_chain.methods.fetchItemBufferOne(UPC).call({
    from: account_address
  }, (err, res) => {
    console.log(res);
  })
}

init()