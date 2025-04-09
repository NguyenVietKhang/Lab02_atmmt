
import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return g, x, y

def exec(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception("Không tồn tại nghịch đảo module")
    else:
        return x % phi


p2 = 20079993872842322116151219
q2 = 676717145751736242170789
e2 = 17

if not is_prime(p2):
    print("p2 KHÔNG phải số nguyên tố")
if not is_prime(q2):
    print("q2 KHÔNG phải số nguyên tố")

n = p2 * q2
phi = (p2 - 1) * (q2 - 1)

if gcd(e2, phi) != 1:
    print("e2 KHÔNG nguyên tố cùng nhau với phi(n)")
else:
    d = exec(e2, phi)
    print("Khóa công khai PU = (e, n):")
    print(f"PU = ({e2}, {n})\n")

    print("Khóa bí mật PR = (d, n):")
    print(f"PR = ({d}, {n})")
