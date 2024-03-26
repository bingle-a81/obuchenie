
import hashlib
# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
md51 = hashlib.sha1()
md52= hashlib.sha1()
with open('55.txt', 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md51.update(data)
p1=md51.hexdigest()
print(f"MD5: {p1}")


with open('66.txt', 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md52.update(data)
p2=md52.hexdigest()

print(f"MD5: {p2}")
print(p1==p2)
