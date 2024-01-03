def max(a,b,c):# -> Any:
    max = a
    if (max <= b ):
        max = b
    if (max <= c):
        max = c
    return max

print(max(1,3,1))