def values():
    val1 = 10
    val2 = 20
    val3 = 30

    return (val1, val2, val3)

v1, v2, v3 = values()

print(v1)
print(v2)
print(v3)

for value in values():
    print(value)
