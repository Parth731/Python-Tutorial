s = {10,20,30,40}
fs = frozenset(s)
print(fs)
for x in fs: print(x)

# error
# fs.add(70)
# fs.remove(10)