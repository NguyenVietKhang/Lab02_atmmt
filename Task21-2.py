def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return gcd, x, y

def exec(e, phi_n):
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise Exception("Không có nghịch đảo modulo")
    return x % phi_n

def tinh(p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = exec(e, phi_n)
    return (e, n), (d, n)

p = 329520679814142392965336341297134588639
q = 308863399973593539130925275387286220623
e = 886979 

public_key, private_key = tinh(p, q, e)

print("Public key (e, n):", public_key)
print("Private key (d, n):", private_key)
