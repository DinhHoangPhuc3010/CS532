# Tìm UCLN
def gcd (a,b) :
    while b != 0 :
        a,b = b, a % b
    return a

# Sử dụng Modulo để tính lũy thừa lớn
def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m # Mũ lẻ
        base = (base * base) % m   # Mũ chẳn
        expo = expo // 2
    return res

# Thuật toán Euclid Mở rộng để tìm nghịch đảo đồng dư (de mod phi = 1)
def ModInverse_ExtendedEuclid(e, phi) :
    r0, r1 = phi, e
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while r1 != 0 :
        q = r0 // r1
        r = r0 % r1
        r0, r1 = r1, r
        x = x0 - q*x1
        x0, x1 = x1, x 
        y = y0 - q*y1
        y0, y1 = y1, y 
    if y0 < 0 :           # Nếu đồng dư là số âm
        return y0 + phi   # Cộng thêm modulo phi vào 
    return y0


def CreateKey() :
    p = 10009
    q = 10093
    print(f"(p, q): ({p}, {q})")
    n = p*q
    phi = (p-1)*(q-1)
    e = 0
    # Select integer e : gcd(e,phi) = 1; 1 < e < phi 
    for i in range(2,phi) :
        if (gcd(i, phi) == 1) :
            e = i
            break
    d = ModInverse_ExtendedEuclid(e, phi)
    return n, e, d    

def encryption(M, e, n) :  # MÃ HÓA
    return power(M, e, n)

def decrypt(C, d, n) :     # GIẢI MÃ
    return power(C, d, n) 

if __name__ == "__main__" :
    # Create KEYs
    print(ModInverse_ExtendedEuclid(101,323)) 
    '''
    n, e, d = CreateKey()
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    #MESSAGE 
    M = int(input("Nhập vào bản rõ : "))
    
    #ENCRYPTION the message
    C = encryption(M,e,n)
    print(f"Bản mã là (Encrypted Message) : {C}")

    #DECRYPTION the message
    decrypted = decrypt(C, d, n)
    print(f"Bản rõ là (Decrypted Message) : {decrypted}")
    '''