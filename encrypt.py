import base64
import random
final = str("")
where = 0
step = 0
out = str("")
inpt = input("String to encrypt? :")
salt = str(input("Key? :").encode('utf-8'))[2:-1]
#Remove padding to prevent brute-forcing everything before it
b64 = str(base64.b64encode(inpt.encode('utf-8')))
while where < 1:
    where = random.randint(2, len(b64) - 1)
while not step - 1== where:
    out += b64[step]
    step += 1
out += salt
goal = len(b64) + len(salt)
while not len(out) == goal:
    out += b64[step]
    step += 1
print(str(base64.b64encode(out.encode('utf-8')))[2:-1])
