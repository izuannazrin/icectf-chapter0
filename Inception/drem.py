# 0 smpai 235
data = []
for i in range(0,235+1):
    with open(f'drem/dream_{i}.txt', 'r') as f:
        data.append( f.read() )

binary = [bytes.fromhex(x) for x in data]

with open('dream.png', 'wb') as f:
    for bi in binary:
        f.write(bi)
