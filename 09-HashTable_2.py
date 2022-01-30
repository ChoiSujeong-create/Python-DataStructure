# chaining 기법으로 충돌해결 코드를 추가해보기
# open Hashing
hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    # 별도로 hash_function을 사용하기 전 index_key 변수를 만들어서 hash 값을 저장함
    # hash 값은 hash_address(해쉬함수 값)의 위치에 있는 데이터들 중 일치하는 key값을 검색해 value를 가져옴
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:  # hash_table[hash_address]에 데이터가 있다면
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = list([index_key, value])


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None
