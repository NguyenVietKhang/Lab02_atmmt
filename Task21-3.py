import random

def snt_check(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def snt_gen(bits):
    while True:
        num = random.getrandbits(bits)
        if snt_check(num):
            return num

def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

def modu(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        return None
    return x % phi

def tao_khoa(p=None, q=None, e=None):
    if p is None or q is None or e is None:
        p = snt_gen(1024)
        q = snt_gen(1024)
        e = 65537
    n = p * q
    phi = (p - 1) * (q - 1)
    if ucln(e, phi) != 1:
        return None, None
    d = modu(e, phi)
    return (e, n), (d, n)

def enc(thong_diep, pu):
    e, n = pu
    if isinstance(thong_diep, str):
        thong_diep = int.from_bytes(thong_diep.encode('utf-8'), 'big')
    return pow(thong_diep, e, n)

def dec(thong_diep_ma_hoa, pr):
    d, n = pr
    thong_diep = pow(thong_diep_ma_hoa, d, n)
    if thong_diep < 256:
        return thong_diep
    return thong_diep.to_bytes((thong_diep.bit_length() + 7) // 8, 'big').decode('utf-8')

def main():
    print("Tạo khóa RSA:")
    p = int(input("Nhập p (để trống để tạo ngẫu nhiên): ") or 0)
    q = int(input("Nhập q (để trống để tạo ngẫu nhiên): ") or 0)
    e = int(input("Nhập e (để trống để dùng 65537): ") or 0)
    
    if p == 0 or q == 0 or e == 0:
        pu, pr = tao_khoa()
    else:
        pu, pr = tao_khoa(p, q, e)
    
    if pu is None:
        print("Không tạo được khóa, kiểm tra lại p, q, e")
        return
    
    print(f"Khóa công khai (e, n): {pu}")
    print(f"Khóa bí mật (d, n): {pr}")

    m = input("Nhập thông điệp (số hoặc chuỗi): ")
    try:
        m = int(m)
    except ValueError:
        pass

    m_enc = enc(m, pu)
    print(f"Thông điệp mã hóa: {m_enc}")

    m_dec = dec(m_enc, pr)
    print(f"Thông điệp giải mã: {m_dec}")

if __name__ == "__main__":
    main()