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

# Additional Resources
[Bitcoin Mining Now Consuming More Electricity](https://powercompare.co.uk/blog/bitcoin-mining-now-consuming-more-electricity/)