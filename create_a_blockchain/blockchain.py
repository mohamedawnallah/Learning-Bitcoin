import datetime
import hashlib
import json

class Blockchain:

    def __init__(self):
        """Initialize the blockchain with the Genesis block."""
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof: int, previous_hash: str):
        """Create a new block in the blockchain."""
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self) -> dict:
        """Get the previous block in the blockchain."""
        return self.chain[-1]
 
    def get_proof_of_work(self, previous_proof: int, target='0000') -> int:
        """Find a proof (nonce number) that solves the proof of work problem by meeting the target."""
        new_proof = 1
        while True:
            is_proof_of_work_valid: bool = self.is_proof_of_work_valid(previous_proof, new_proof, target)
            if is_proof_of_work_valid:
                break
            new_proof += 1
        return new_proof
 
    def is_chain_valid(self, chain, target='0000'):
        """Check if the blockchain is valid."""
        previous_block = chain[0]
        for current_block in chain[1:]:
            if current_block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof, current_proof = previous_block['proof'], current_block['proof']
            is_proof_of_work_valid: bool = self.is_proof_of_work_valid(previous_proof, current_proof, target)
            if not is_proof_of_work_valid:
                return False
            previous_block = current_block
        return True
    
    def hash(self, block):
        """Hash a block using SHA-256."""
        encoded_block = json.dumps(block, sort_keys = True).encode()
        hashed_block = hashlib.sha256(encoded_block).hexdigest()
        return hashed_block

    def is_proof_of_work_valid(self, previous_proof: int, current_proof: int, target='0000') -> bool:
        """Check if the proof of work is valid."""
        encoded_proof = str(current_proof**2 - previous_proof**2).encode("utf-8")
        new_hash = hashlib.sha256(encoded_proof).hexdigest()
        if new_hash[:4] != target:
            return False
        return True
        

    
