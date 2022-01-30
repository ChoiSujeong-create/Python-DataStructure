# create a hash table
hash_table = list([i for i in range(10)])
print(hash_table)

# create a simple hash function


def hash_func(key):
    return key % 5


# save data to hash table
data1 = "Sally"
data2 = "crystal"
data3 = "yeone"
data4 = "alan"
# ord(): return ASCII code of charactor
print(ord(data1[0]), ord(data2[0]), ord(data3[0]), ord(data4[0]))
print("ASCII data1 :", ord(data1[0]))
print("hash func data1 :", hash_func(ord(data1[0])))

# storage data to hash table


def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


# Create a function that fetches data from a specific address from the hash table.
storage_data("andy", "01029392929")
storage_data("sujeong", "2930402994")
storage_data("sally", "12345678938")
storage_data("alan", "22222222222")

# save a data and read it.


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


print(get_data("andy"))
print(get_data("sujeong"))
print(get_data("alan"))
print(get_data("s"))
print(hash_table)
