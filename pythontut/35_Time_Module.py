
import time

initial = time.time()
print(initial)
k=0
while k < 45:
    print("This is a harry bhai")
    k = k+1
print("While loop Time: ",time.time() - initial, "seconds")

initial2 = time.time()
for x in range(45):
    print("This is a harry bhai")
print("For loop Time: ",time.time() - initial2, "seconds")

print(time.sleep(3))

localtime = time.asctime(time.localtime())
print(localtime)