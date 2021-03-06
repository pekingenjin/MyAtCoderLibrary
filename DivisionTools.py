# divisors(12) == [1,2,3,4,6,12]
# O(sqrt(n))
def divisors(n):
    #assert 1 <= n
    lis = []
    for i in range(1, n+1):
        if i * i >= n:
            if i * i == n:
                lis.append(i)
            break

        if n % i == 0:
            lis.append(i)
            lis.append(n // i)

    lis.sort()
    return lis


# prime_factorization(60) == {2:2, 3:1, 5:1}
# O(sqrt(n))
def prime_factorization(n):
    #assert 1 <= n
    dic = dict()
    for p in range(2, n+1):
        if p * p > n:
            break
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                cnt += 1
                n //= p
            dic[p] = cnt
    if n > 1:
        dic[n] = 1
    return dic


#dict_mult_dict({2:1,3:2}, {3:1,5:2}) == {2:1, 3:3, 5:2}
def dict_mult_dict(dic1, dic2):
    if len(dic1) < len(dic2):
        dic1, dic2 = dic2, dic1
    for key, value in dic2.items():
        if key in dic1:
            dic1[key] += value
        else:
            dic1[key] = value
    return dic1


# prime_numbers(n) == [p | (p ∈ prime numbers) and p < n]
# prime_numbers(10) == [2,3,5,7]
def prime_numbers(n):
    #assert 3 <= n
    lis = [2]
    for i in range(3, n, 2):
        for p in lis:
            if p * p > i:
                lis.append(i)
                break
            if i % p == 0:
                break
    return lis


# a*x + b*y == gcd(a,b)
# return gcd(a,b), x, y
def ext_Euclid(a, b):
    #assert 1 <= a and 1 <= b
    if b > 0:
        gcd_ab, x, y = ext_Euclid(b,a%b)
        return gcd_ab, y, x-(a//b)*y
    return a, 1, 0


# return sum([(a*i + b)//m for i in range(n)])
def floor_sum(n, m, a, b):
    ans = 0
    while True:
        ans += ((a // m) * n * (n-1)) // 2 + (b // m) * n
        a %= m
        b %= m
        if a*n + b < m:
            return ans
        new_n = (a*n + b) // m
        max_x = -(b - m*new_n) // a
        ans += (n - max_x) * new_n
        n, m, a, b = new_n, a, m, a*max_x - m*new_n + b

