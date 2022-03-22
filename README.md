# dapp-supply-chain-coffee
DApp supply chain solution backed by the Ethereum platform.

1. Deployment

```bash
truffle console --network rinkeby

compile
migrate --reset
```

Etherscan transaction: https://rinkeby.etherscan.io/tx/0xcf46727ec4bcf6039b074a93473b12bd5a77417032cee0d624b0f9220202af39


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
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x1dd5eea06429bd1e363281953a59b1e3f1ae4fac1b6f37e766b04634a56598f4
   > Blocks: 0            Seconds: 0
   > contract address:    0x7973C8Db2c299686806b9eCa412fDB6019638d42
   > block number:        26
   > block timestamp:     1647945362
   > account:             0x9302E68232aDA1EC1368c9091e846ed59993eEEC
   > balance:             99.80713832
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
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0xc181c6e54fbde0f8ff489c71a5764ebe7f8b95aed29bc85e914bf40423d77b71
   > Blocks: 0            Seconds: 0
   > contract address:    0x8928D89711Cd144C9AE89d408e4B7CfC05F8e153
   > block number:        28
   > block timestamp:     1647945365
   > account:             0x9302E68232aDA1EC1368c9091e846ed59993eEEC
   > balance:             99.79967304
   > gas used:            330726 (0x50be6)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00661452 ETH


   Deploying 'DistributorRole'
   ---------------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x137a37f4a45ba1ce2e90c5f21a4431ee2d4524cf056b699943b76cce80fc3a12
   > Blocks: 0            Seconds: 0
   > contract address:    0xBB4e090Eba3A43CE42c04c013B672d75a25fD9d9
   > block number:        29
   > block timestamp:     1647945367
   > account:             0x9302E68232aDA1EC1368c9091e846ed59993eEEC
   > balance:             99.79305852
   > gas used:            330726 (0x50be6)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00661452 ETH


   Deploying 'RetailerRole'
   ------------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x7b148933ae4a7df2aa1782385eb15c6ccbbfc39536438ee92e43aeafc41db8b2
   > Blocks: 0            Seconds: 0
   > contract address:    0xfB0546721144d8C1C5A2c75E76628b813b16AC34
   > block number:        30
   > block timestamp:     1647945369
   > account:             0x9302E68232aDA1EC1368c9091e846ed59993eEEC
   > balance:             99.786444
   > gas used:            330726 (0x50be6)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00661452 ETH


   Deploying 'ConsumerRole'
   ------------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x636356378992b9e660fa9357f10ef2ce89619a0d20c9e0606609005cd556f73a
   > Blocks: 0            Seconds: 0
   > contract address:    0x22197AACEe585A2Cd676d5364eFBe2667EC03fB0
   > block number:        31
   > block timestamp:     1647945371
   > account:             0x9302E68232aDA1EC1368c9091e846ed59993eEEC
   > balance:             99.77982948
   > gas used:            330726 (0x50be6)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00661452 ETH


   Deploying 'SupplyChain'
   -----------------------
   ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0x0e3a6752266e6d9db2a78e3ce2c99ca57c5e6c579241d3b8d1213eeeb19f4bb0
   > Blocks: 0            Seconds: 0
   > contract address:    0x9b76Ad86511398D54549D54dFa92D3aA6A525ce9
   > block number:        32
   > block timestamp:     1647945375
   > account:             0x9302E68232aDA1EC1368c9091e846ed59993eEEC
   > balance:             99.72586388
   > gas used:            2698280 (0x292c28)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.0539656 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.08042368 ETH

Summary
=======
> Total deployments:   6
> Final cost:          0.08588784 ETH
```