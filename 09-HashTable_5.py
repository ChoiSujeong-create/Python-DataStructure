import hashlib

data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)

# 16진수로 변환
hex_dig = hash_object.hexdigest()

print(hex_dig)
