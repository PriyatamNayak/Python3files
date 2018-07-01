import hashlib as hasher
import datetime as date

class Block:
        
	def __init__(self, index, timestamp, data, pre_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data 
		self.pre_hash = pre_hash 
		self.hash = self.hash_block()


	def hash_block(self):
		sha = hasher.sha256()
		sha.update(str(self.index).encode("utf-8")+str(self.timestamp).encode("utf-8")+str(self.data).encode("utf-8")+str(self.pre_hash).encode("utf-8"))
		return sha.hexdigest()	


def genesis_block():
        return Block(0, date.datetime.now(),"genesis block", "0")


def next_block(last_block):
	this_index = last_block.index + 1
	this_timestamp = date.datetime.now()
	this_data = "hiii, i am the block" + str(this_index)
	this_hash = last_block.hash
	return Block(this_index, this_timestamp, this_data, this_hash)

blockchain = [genesis_block()]
pre_block = blockchain[0]
n_blocks = 10
for i in range(0,n_blocks):
        add_block = next_block(pre_block)
        blockchain.append(add_block)
        pre_block = add_block

        print("Block #{} has been added to blockchain!".format(add_block.index))
        print("Hash: {}".format(add_block.hash))
    

input("press enter to exit")