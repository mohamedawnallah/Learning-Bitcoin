# Types of Wallets:
- Just a Bunch Of Keys Wallet (JBOK Wallet) > Non-deterministic Wallet
- Hierachical Deterministic Wallet (HD Wallet) -> deterministic Wallet
# Full Blockchain Node vs Wallet Node vs Miner Node vs Network Routing Node

# What are SVP Nodes

# What is Regtest Node and Testnet Network

# What is RPC server in Bitcoin

# What is ZeroMQ in Bitcoin

# Bitcoin Core Binaries Files
- `bitcoin-cli`
- `bitcoin-qt`
- `bitcoin-tx`
- `bitcoin-util`
- `bitcoin-wallet`
- `bitcoind`
- `test_bitcoin`

# Testnet vs Mainnet
It's not a good idea to use Mainnet while learning about bitcoin core for three reasons to avoid:
- Transaction fees
- Blocktime (added to blockchain every 10 minutes)
- Save to play around


# What is Regtsest
For situations where interaction with random peers and blocks is unnecessary or unwanted, Bitcoin Core’s regression test mode (regtest mode) lets you instantly create a brand-new `private block chain` with the same basic rules as testnet—but one major difference: you choose when to create new blocks, so you have complete control over the environment.

# What are the applications (layer2) for bitcoin scripting
- Atomic Swap
- Lightning Network
- Ligtning Loop
- Multisig
# What is Atomic Swap
An atomic swap is an `exchange of cryptocurrencies from separate blockchains`. The swap is conducted between two entities without a third party's involvement. The idea is to remove centralized intermediaries like regulated exchanges and give token owners total control.

It uses at the core, `Hashed Time Locked Contract Transaction`:
- Time Locked
- Special Key
# What is Lightning Network and Ligtning Loop
Wikipedia said: "The Lightning Network (LN) is a "layer 2" payment protocol layered on top of Bitcoin (and other blockchains and cryptocurrencies). It is intended to enable fast transactions among participating nodes and has been proposed as a solution to the bitcoin scalability problem. It features a peer-to-peer system for making micropayments of cryptocurrency through a network of bidirectional payment channels without delegating custody of funds".

It's based as well on `Hashed Time Locked Contract Transaction` concept

# What is Multisig

# What is Raw Transaction Serialization
All nodes need to agree on how we serialize

# Transaction Fees
Transaction fees serve as an `incentive` to include (mine) a transaction into the next block and also as a `disincentive` against abuse of the system by imposing a small cost on every transaction. Transaction fees are collected by the miner who mines the block that records the transaction on the blockchain.

Transaction fees are calculated based on `the size of the transaction in kilobytes`, not the value of the transaction in bitcoin. Overall, transaction fees are set based on market forces within the bitcoin network. Miners prioritize transactions based on many different criteria, including fees, and might even process transactions for free under certain circumstances. Transaction fees affect the `processing priority`, meaning that a transaction with sufficient fees is likely to be included in the next block mined, whereas a transaction with insufficient or no fees might be delayed, processed on a best-effort basis after a few blocks, or not processed at all. Transaction fees are not mandatory, and transactions without fees might be processed eventually; however, including transaction fees encourages priority processing.

# Locking and Unlocking Script
Locking script is a spending condition based on `the transaction output` Histroically the locking script was called a `scriptPubKey` because it usally contained a public key or bitcoin address (public key hash) also it is refeered to as a `witness script` or `cryptographic puzzle` these all terms mean the same thing, at different levels of abstractions.

The Unlocking script that `solves` or `satisfies` the conditions based on the UTXO ouput by a locking script allows the output to be spent. Unlocking scripts are part of every `transaction input` Most of the time they contain `digital signature` produced by the user's wallet from his or her private key. Historically it was called `scriptSig` because it usually contained a digital signature also it refeered to `witness`.

![Locking and Unlocking Diagram](assets/locking-and-unlocking-script.png)

```
Script Construction = Locking Script + Unlocking Script
```

Separate execution of unlocking and locking scripts to avoid the vulnerability that allowed a malformed unlocking script to push data onto the stack and corrupt the locking script.

# Bitcoin Transaction Scripts
Why we need to many differnt Bitcoin Transaction Scripts? the short answer is that we have many use cases that each one fit into (for more information look at the Script Types Usage resource down below)

![Script Types Usage](assets/script-types-usage.png)

# Pay-to-public Key Hash Transaction Script (p2pkh script)
![Pay-to-public Key Hash Script](assets/p2pkh-script.png)
Combining scriptSig and scriptPubKey to evaluate a transaction script
![Pay-to-public Key Hash Script2](assets/p2pkh-script2.png)

# Pay-to-witness Public Key Hash Transaction Script (p2wpkh script)

# MultiSignature Script
Requires `M` out of `N` Keys to sign
![Multisignature Script](assets/multisignature-script.png)

**A Bug in CHECKMULTISIG execution**
There is a bug in CHECKMULTISIG's execution that requires a slight workaround. When CHECKMULTISIG executes, it should consume M+N+2 items on the stack as parameters. However, due to the bug, CHECKMULTISIG will pop an extra value or one value more than expected. `it will cause a stack error and script failure (marking the transaction as invalid`. so for now and on you will see signature script as following with leading zero in the beginning.
```
0<Signature B><Signature C>2<PublicKey A><PublicKey B><PublicKey C>3 CHECKMULTISIG
```
# Pay-to-script Hash Transaction Script (p2sh script)
Instead of Including all public keys in the case of `mutlisig script` we include the script hash instead so it becomes easier for the sender to send the locking script to the receiver. Locking Script:
```
OP_HASH160 <SCRIPT_HASH> OP_EQUAL
```

# Pay-to-witness Script Hash Transaction Script (p2wpkh script)

![Pay to Script Hash Script](assets/p2sh-script.png)

![Pay to Script Hash Script 2](assets/p2sh-script2.png)

# Time Lock Transaction Script
- Absolute Time Lock:
    - `nLocktime` has many limitations some of them is `double spending problem`  and being stored  on `transaction level` and the transaction can not be broadcasted until the time is passed
    - `CHECK LOCK TIME VERIFY` must be placed UTXO itself and be part of the locking script 
- Relative Time Lock:
    - `nSequence` can be specified in either blocks or seconds on the transaction level
    - `CHECK SEQUENCE VERIFY` must be placed UTXO itself and be part of the locking script with relative time either in blocks/seconds have passed since it was mined

Median-Time-Past

# What is Segwit ?
Investopedia said: "Segregated Witness (SegWit) refers to a change in the `transaction format` of Bitcoin. Its stated purpose as a protocol upgrade was to protect against `transaction malleability` and decrease transaction times by increasing `block capacity`. Transaction malleability refers to the possibility that tiny pieces of transaction information could be changed, invalidating new cryptocurrency blocks."

Witness Data structure is not part of calculation of the transaction hash

# What is Signing Transaction ?
Signing transaction means providing the `unlocking script` to the output transaction

# Bitcoin and Economics

## The Origins of Money
In the earliest human societies, trade between groups of people occurred through `barter`. A major disadvantage with barter-based trade is `the double coincidence of wants problem`. An apple grower may desire trade with a fisherman, for example, but if the fisherman does not desire apples at the same moment, the trade will not take place.

```
Collectible -> Store of value -> Medium of Exchange -> Unit of account
```

# Additional Resources
[Bitcoin Developer Documentation](https://developer.bitcoin.org/)

[Lightning Network Official Website](https://lightning.network/)

[Bitcoin IDE](https://siminchen.github.io/bitcoinIDE/build/editor.html)

[Bitcoin OP Codes](https://en.bitcoin.it/wiki/Script#Opcodes)

[Big endian and little endian](https://www.techtarget.com/searchnetworking/definition/big-endian-and-little-endian)

[Bitcoin Transaction Fees Estimator](https://bitcoinfees.earn.com/)

[Pay-to-Pubkey Hash](https://en.bitcoinwiki.org/wiki/Pay-to-Pubkey_Hash)

[Turing Incompleteness Bitcoin Script Language](https://river.com/learn/terms/t/turing-completeness)

[Script Types Usage](https://river.com/learn/terms/s/script-bitcoin/)

[Segregated Witness](https://www.investopedia.com/terms/s/segwit-segregated-witness.asp)

[Transaction malleability problem](https://en.wikipedia.org/wiki/Transaction_malleability_problem)

[The Origins of Money](https://nakamotoinstitute.org/shelling-out/)

[Lindy Effect](https://en.wikipedia.org/wiki/Lindy_effect)

