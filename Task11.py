import random

def kiem_tra_nguyen_to(n, k=5):
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

def tao_so_nguyen_to(bits):
    min_val = 1 << (bits - 1)
    max_val = (1 << bits) - 1
    while True:
        num = random.randint(min_val, max_val)
        if kiem_tra_nguyen_to(num):
            return num

def tim_10_so_nguyen_to_lon_nhat_duoi_mersenne():
    mersenne_primes = [3, 7, 31, 127, 8191, 131071, 524287, 2147483647, 2305843009213693951, 618970019642690137449562111]
    ket_qua = []
    for mp in mersenne_primes:
        gioi_han = mp - 1
        danh_sach = []
        for i in range(gioi_han, 0, -1):
            if kiem_tra_nguyen_to(i):
                danh_sach.append(i)
                if len(danh_sach) == 10:
                    break
        ket_qua.append((mp, danh_sach))
    return ket_qua

def ucln(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def luy_thua_modulo(a, x, p):
    return pow(a, x, p)

def main():
    print("1. Tạo số nguyên tố ngẫu nhiên:")
    print(f"8-bit: {tao_so_nguyen_to(8)}")
    print(f"16-bit: {tao_so_nguyen_to(16)}")
    print(f"64-bit: {tao_so_nguyen_to(64)}")

    print("\n2. 10 số nguyên tố lớn nhất dưới 10 số Mersenne đầu tiên:")
    ket_qua_mersenne = tim_10_so_nguyen_to_lon_nhat_duoi_mersenne()
    for mp, primes in ket_qua_mersenne:
        print(f"Dưới {mp}: {primes}")

    print("\n3. Kiểm tra số nguyên tố (nhập số < 2^89 - 1):")
    num = int(input("Nhập số: "))
    if num < 2**89 - 1:
        print(f"{num} {'là' if kiem_tra_nguyen_to(num) else 'không là'} số nguyên tố")
    else:
        print("Số phải nhỏ hơn 2^89 - 1")

    print("\n4. Tính UCLN của 2 số lớn:")
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    print(f"UCLN({a}, {b}) = {ucln(a, b)}")

    print("\n5. Tính lũy thừa modulo (a^x mod p):")
    a = int(input("Nhập cơ số (a): "))
    x = int(input("Nhập số mũ (x): "))
    p = int(input("Nhập modulo (p): "))
    print(f"{a}^{x} mod {p} = {luy_thua_modulo(a, x, p)}")

if __name__ == "__main__":
    main()