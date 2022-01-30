# 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 1. hash function : key % 8
# 2. Generating hash key : hash(data)

hash_table = list([0 for i in range(8)])
print(hash_table)  # [0, 0, 0, 0, 0, 0, 0, 0]


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


save_data("sally", "01020304102")
save_data("andy", "01023748283")
print("sally's phone number is", read_data("sally"))
print("sally's hash address is ", hash_function(get_key("sally")))
print(hash_table)
