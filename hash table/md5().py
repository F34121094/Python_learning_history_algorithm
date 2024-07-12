import hashlib

data = hashlib.md5()
data.update(b'Ming-Chi Institute of Technology')

print("Hash Value = ", data.digest())
print("hash Value(16進位) = ", data.hexdigest())
print(type(data))
print(type(data.hexdigest()))