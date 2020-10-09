
'''
tell() => file pointer
seek() => stating file pointer
'''

f = open("Parth2.txt")
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(11)
print(f.readline())
print(f.tell())
f.close()
