def evklid(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return evklid(b, a % b)
a, b = map(int, input().split())
print(evklid(a, b))