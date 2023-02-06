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
# Additional Resources
[Bitcoin Developer Documentation](https://developer.bitcoin.org/)
[Lightning Network Official Website](https://lightning.network/)