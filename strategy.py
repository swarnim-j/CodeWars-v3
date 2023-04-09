import random

a = random.randint(0, 3)

print("loop:")
for i in range(10):
    print("rf:10:")
    print("rs:4:")
    print("id:10:")
for i in range(10):
    print("rf:10:")
    print("id:20:")
    print("id:40:")
for i in range(30):
    print("rf:12:")
    print("id:15:")
    print("rf:6")
    print("id:20:")
for i in range(20):
    print("rf:4:")
    print("re:15:")
    print("ia:25:")
    print("id:20:")
    print("rt:10:")
for i in range(40):
    print("rf:4:")
    print("re:20:")
    print("ia:20:")
    print("id:30:")
    if i % 10 == 9:
        print(f"at:{(a + i) % 4}:97")
print("loop:")