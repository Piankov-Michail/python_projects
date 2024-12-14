#python
def hash(s):
    q = (10**9 + 7)
    result = ord(s[0])
    base = 31
    for i in range(len(s) - 1):
        result = result * base + ord(s[i+1])
    return result % q
def RabinKarp(w,s):
    base = 31
    q = (10 ** 9 + 7)
    n = len(s)
    m = len(w)
    hash_s = hash(s[0:m])
    hash_w = hash(w)
    res = []
    i = 0
    while True:
        if hash_s == hash_w:
            if w == s[i:i+m]:
                res.append(i)
        if i + m >= n:
            break
        hash_s = ((hash_s - ord(s[i]) * base ** (m-1)) * base + ord(s[i + m])) % q
        i += 1
    return ' '.join(map(str, sorted(res)))

if __name__ == "__main__":
    m = input()
    s = input()
    print(RabinKarp(m, s))