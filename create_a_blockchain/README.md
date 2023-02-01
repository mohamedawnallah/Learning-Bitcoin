# Blockchain Application
This is a simple blockchain application implemented in Python using Flask. The application has three endpoints:
-`/mine_block`: Mines a new block by finding a proof that meets the target and appending the block to the blockchain.
-`/get_chain`: Returns the full blockchain.
-`/is_valid`: Checks if the blockchain is valid.

The blockchain is implemented as a linked list of blocks, where each block has the following properties:

- `index`: The index of the block in the blockchain.
- `timestamp`: The timestamp of when the block was created.
- `proof`: The proof that meets the target for the proof of work problem.
- `previous_hash`: The hash of the previous block in the blockchain.

The proof of work algorithm used in this application is based on the square difference of the previous proof and the current proof, and the `target is set to 0000`. The hash function used to hash the blocks is SHA-256.


## Getting started
To run the application, you need to have Flask installed. You can install it and other dependencies by running:
```bash
pip install -r requirements.txt
```
Then, simply run `main.py`:
```bash
python main.py
```
The application will start running on http://127.0.0.1:5000. You can access the endpoints by sending HTTP requests to the URL http://127.0.0.1:5000/<endpoint>.

## Conclusion
This application is meant to be a simple demonstration of how a blockchain works, and is not meant to be used in a real-world scenario. It lacks many important features that a real blockchain would have, such as network consensus, security, and scalability.

