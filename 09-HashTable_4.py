# practice hash function
import hashlib

data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(b'test')
# hash_object.updata(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)
