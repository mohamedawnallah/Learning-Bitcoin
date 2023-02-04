# Understanding Mining Difficulty

Let's imagine how minig is so difficult by doing some calculations:

Probility:
Total possible 64-digit hexadecimal numbers: 16^64 = 10^77
Total valid hashes with 18 leading zeros: 16^46 = 2*10^55
Probability of picking a random valid hash: (2*10^55) / (10^77) = 2e-22 %

# How mining diffulty cacluated
```
Difficulty = current_target / maximum_target
```
Difficulty is adjusted by adding more leading zeros every 2016 blocks i.e(every 2 weeks) so it becomes difficult of solving the cryptographical puzzle
over the time that's how It's being undercontrol

# Mining Pool
Avoiding Double Work

# Nonce Range
32 bit number (unsigned): 0 -> ~4Billion

Assuming no collisions, this means 4 * 10^9 different hashes
Probability of picking a random vlid hash: 2 * 10 ^ -22
Probability that ONE of them will be valid: 4 * 10^9 * 2 * 10 ^ -22 = 10^-12

Although Nounce Range is finite doesn't mean we can't find the valid hash from the prospective of modest miner (100 Million Hashes per Second) because there is a timestamp unix time that change every single second so the hash of the block change continously re-using the same nounce range if needed.

But what about Mining Pool it is a capcity waste if it's waiting until the unix
timestamp's changed ?
Just change the Block Configurations so miner get transactions from **MEMPOOL** until timestamp gets updated

# Additional Resources
[Bitcoin Mining Now Consuming More Electricity](https://powercompare.co.uk/blog/bitcoin-mining-now-consuming-more-electricity/)
[Unix Time - Number of Seconds since 1st Jan 1970](https://time.is/Unix_time)
[How Bitcoin Mining Works](https://www.coindesk.com/learn/how-bitcoin-mining-works-2/)