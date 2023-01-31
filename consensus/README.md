## Byzantine Fault Tolerance
To oversimplify this concept it basically a consensus which deside each general(node) command(transaction) to listen to:
- Up to f generals might behave malicously
- Honest generals don't know who the malicious ones are
- The malicious genreals may collude
- Nervertheless, hones generals must agree on plan
- Theorem: need 3f + 1 generals in total to tolerate f
  malicious generals (i.e: < 1/3 may be malicious) so for example if you have 3 generals and one of them is malicious you don't tolerate the fault but you should have at least 4 generals to tolerate that malicious one
<h1 align="center">
  <img alt="byzantine fault tolerance" src="assets/byzantine-fault-tolerance.png" width="800px" height="450px" /><br/>
</h1>

## Additional Resources
[Byzantine Fault Tolerance](https://medium.com/loom-network/understanding-blockchain-fundamentals-part-1-byzantine-fault-tolerance-245f46fe8419) This article explains the concept of Byzantine Fault Tolerance pretty well