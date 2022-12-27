import numpy as np

with open("./day25/input.txt", 'r') as file:
    lines = file.readlines()

digits = {"2": 2,"1": 1,"0": 0,"-": -1,"=": -2}
snafus = {2: "2", 1: "1", 0: "0", -1: "-", -2:"="}

def s2d(snafu): 
    res = 0.0
    for i, digit in enumerate(snafu[::-1]):
        res += 5**i*digits[digit]
    return res

# d2s = {}
# for d5 in np.arange(-2, 3):
#     for d4 in np.arange(-2, 3):
#         for d3 in np.arange(-2, 3):
#             for d2 in np.arange(-2, 3):
#                 for d1 in np.arange(-2, 3):
#                     for d0 in np.arange(-2, 3):
#                         decimal = 5**0*d0 + 5**1*d1 + 5**2*d2 + 5**3*d3 + 5**4*d4 + 5**5*d5
#                         res = snafus[d5] + snafus[d4] + snafus[d3] + snafus[d2] + snafus[d1] + snafus[d0]
#                         d2s[decimal] = res.lstrip("0")
#                         # print(decimal, d2s[decimal])

def sumup(digits):
    # don't use numpy for this job!
    res = 0
    for i, d in enumerate(digits):
        res += d*5**i
    return res


def d2s(decimal):
    # decimal = 2076940343811
    print(decimal)
    N = 25
    digits = np.zeros((N,), dtype=np.int64)
    # base = 5**np.arange(N, dtype=np.long)
    for i in range(N)[::-1]:
        d = decimal-sumup(digits)
        digit = d // 5**i
        digits[i] = digit
    for i, digit in enumerate(digits):
        if digit > 2:
            digits[i+1] += 1
            digits[i] = digits[i]-5
        print(5**i, digit)
    print(digits[::-1])
    res = ""
    for d in digits[::-1]:
        res += snafus[d]
    res = res.lstrip("0")
    return res
    
res = 0
for s in lines:
    d = s2d(s.strip())
    res += d
    
    print(s.strip(), d)
    print( d2s(s2d(s.strip())) == s.strip())
print(res)
print(d2s(res))
answer = "2-1-110-=01-1-0-0==2"
print(s2d(answer))
# 1=-=0121-=212000221
