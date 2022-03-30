# dapp-supply-chain-coffee
DApp supply chain solution backed by the Ethereum platform.

## About
The application suits the interactions between farmers, distributors, retailers and consumers in an example of supply-chain.

The actors are represented by their ethereum addresses. The owner of the contract is initially in charge to add the addresses to the distributor, retailer, consumer roles respectively.

## Getting started

* Delete the build folder if any and migrate the contract to a chain (either a local ganache or ethereum based on the truffle-config.js file)

To deploy on a specific network: 

```bash
truffle console --network rinkeby
compile
migrate --reset
```

To deploy on the development network (local ganache): 

```bash
truffle compile
truffle test
truffle migrate --reset
```

```bash
Starting migrations...
======================
> Network name:    'development'
> Network id:      5777
> Block gas limit: 6721975 (0x6691b7)


1_initial_migration.js
======================

   Deploying 'Migrations'
   ----------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x5ad556b9e35020405ecfc04a1c67f3d5de35eb0a9b7531cdb5c4d83e602693d8
   > Blocks: 0            Seconds: 0
   > contract address:    0x78F714842aFcB32eBD29Ee0BeA2F5271Fd7B089C
   > block number:        81
   > block timestamp:     1648642502
   > account:             0xf4806C970DaF0fC9c21e7Bd732C71031732488F4
   > balance:             109.517970979999999998
   > gas used:            273208 (0x42b38)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00546416 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.00546416 ETH


2_deploy_contracts.js
=====================

   Deploying 'FarmerRole'
   ----------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0xe2e48d2ee5d65dea94e7a93b48081d0e032b028893d1954f7f3d5e6db2d43a94
   > Blocks: 0            Seconds: 0
   > contract address:    0xb2EbF66aB505d4F9AA84Ed3B5c71F382d24B32bd
   > block number:        83
   > block timestamp:     1648642508
   > account:             0xf4806C970DaF0fC9c21e7Bd732C71031732488F4
   > balance:             109.510505699999999998
   > gas used:            330726 (0x50be6)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00661452 ETH


   Deploying 'DistributorRole'
   ---------------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x5f62fa76a862bc71647ba563eea5be3c689a43fd757edca5ce2ee6bcdcc5908d
   > Blocks: 0            Seconds: 0
   > contract address:    0xB367763f621093a0528a095b5fa757049AE50Fe6
   > block number:        84
   > block timestamp:     1648642512
   > account:             0xf4806C970DaF0fC9c21e7Bd732C71031732488F4
   > balance:             109.503891179999999998
   > gas used:            330726 (0x50be6)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00661452 ETH


   Deploying 'RetailerRole'
   ------------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x91acd27dcbd38e6c779986ccf87058866212a94a5f3faa7b272c1cf136fe3e9c
   > Blocks: 0            Seconds: 0
   > contract address:    0x600432Aee14ed08250B0CcFddB5923f07f79186F
   > block number:        85
   > block timestamp:     1648642516
   > account:             0xf4806C970DaF0fC9c21e7Bd732C71031732488F4
   > balance:             109.497276659999999998
   > gas used:            330726 (0x50be6)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00661452 ETH


   Deploying 'ConsumerRole'
   ------------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x89062ac43f7a6f1e3b94d78076dcdb0160fcf9781079ef84821b529c916a98a9
   > Blocks: 0            Seconds: 0
   > contract address:    0xCC4DC75940231602eA8D9b86680890D0576Ec0d2
   > block number:        86
   > block timestamp:     1648642520
   > account:             0xf4806C970DaF0fC9c21e7Bd732C71031732488F4
   > balance:             109.490662139999999998
   > gas used:            330726 (0x50be6)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00661452 ETH


   Deploying 'SupplyChain'
   -----------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x7390f085c1603830dff7b892397467d2fcfe190b8c31364968d58d34f557f153
undefined
   > Blocks: 1            Seconds: 4
   > contract address:    0xb575a1616d282fb5D9f7121D8C57900B3C58B300
   > block number:        87
   > block timestamp:     1648642527
   > account:             0xf4806C970DaF0fC9c21e7Bd732C71031732488F4
   > balance:             109.435023599999999998
   > gas used:            2781927 (0x2a72e7)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.05563854 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.08209662 ETH

Summary
=======
> Total deployments:   6
> Final cost:          0.08756078 ETH
```

* Start the dapp:

```bash
npm run dev
```


* Deployment on the Rinkeby network:
   * Etherscan transaction: https://rinkeby.etherscan.io/tx/0x1560b45e821f469cda9ca317a0bead1f62603992f85645936ff54e0f3adb3de1
   * Contract address: 0x35C1FDdd4E1d5cc70890f150695e86dAee9dC7f5


* Libraries used in the projects:
   - truffle: to help compile, test and deploy the smart-contracts
   - mocha / chai: js testing framework / assertions
   - web3: to interact with ethereum nodes
