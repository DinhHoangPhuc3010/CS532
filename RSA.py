#Khỏi tạo hàm lấy mã Ascii
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def get_ascii():
    '''Return a dict. for ASCII {A = 65, B = 66, ...}'''
    ascii = dict()
    offset = 65
    for l in alphabet:
        ascii[l] = offset
        offset += 1
    return ascii

#Hàm biến đổi kí tự sang mã Ascii
def to_ascii(text):
    ascii = get_ascii()
    s = "".join([str(ascii[l]) for l in text.upper()])
    return s

#Tách thành từng khối(cipher) để mã hóa
def to_block(text_num):
    ''' Split a numerical string into chunks of 8 '''
    cp = str(text_num)      
    blocklist = []
    while len(cp) > 7:
        blocklist.append(cp[:8])
        cp = cp[8:]
    if cp:
        blocklist.append(cp)
    return blocklist


#Từ từng khối biến đổi lại thành bản rõ
def to_letters(lst):
    ''' Transform numerical message back to alphabet'''
    s = "".join([str(block) for block in lst])
    plaintext = ""
    while s:
        plaintext += alphabet[int(s[:2])-65].upper()
        s = s[2:]
    return plaintext

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

#Tạo khóa
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

def decryption(C, d, n) :     # GIẢI MÃ
    return power(C, d, n) 


#Mã hóa theo khối
def encrypt(lst, e, n):
    retlist = []
    for block in lst:
        retlist.append(encryption(int(block), e, n))
    return retlist

#Giải mã theo khối
def decrypt(lst, d, n):
    retlist = []
    for block in lst:
        retlist.append(decryption(int(block), d, n))
    return retlist

if __name__ == "__main__" :
    # Create KEYs
    print(ModInverse_ExtendedEuclid(101,323)) 

    n, e, d = CreateKey()
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    #MESSAGE 
    M = input("Nhập vào bản rõ : ")

    #Từ MESSAGE -> MÃ ASCII(MESSAGE)
    text_num = to_ascii(M)

    #text_num -> list_num
    list_num = to_block(text_num)
    print('Text, Blocks of 8: ', list_num)
    
    #ENCRYPTION the message
    C = encrypt(list_num,e,n)
    print(f"Bản mã là (Encrypted Message) : {C}")

    #DECRYPTION the message
    list_num_after = decrypt(C, d, n)
    plaintext = to_letters(list_num_after)
    print('Text, Back to letters:', plaintext)
    print(f"Bản rõ là (Decrypted Message) : {plaintext}")

