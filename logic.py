import math

#given
p = 499
q = 547
a = -57
b = 52
x = 159201
m = [1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0]

def encryption(msg):
    n = p * q
    k = int(math.log(n, 2))
    h = int(math.log(k, 2))
    
    encrypt_x = x
    for i in xrange(len(msg)/h):
        encrypt_x = pow(encrypt_x, 2, n)
        least = "{0:08b}".format(encrypt_x)[-h:]

        offset = i * h
        for j in xrange(h):
            msg[offset + j] = msg[offset + j] ^ int(least[j])
    encrypt_x = pow(encrypt_x, 2, n)
    return msg, encrypt_x

def decryption(msg, encrypt_x):
    n = p * q
    k = int(math.log(n, 2))
    h = int(math.log(k, 2))
    t = len(msg) / h
    d1 = pow((p+1) / 4, t+1, p-1)
    d2 = pow((q+1) / 4, t+1, q-1)
    u  = pow(encrypt_x, d1, p)
    v  = pow(encrypt_x, d2, q)

    decrypt_x = (v * a * p + u * b * q) % n

    for i in xrange(len(msg)/h):
        decrypt_x = pow(decrypt_x, 2, n)
        least = "{0:08b}".format(decrypt_x)[-h:]

        offset = i * h
        for j in xrange(h):
            msg[offset + j] = msg[offset + j] ^ int(least[j])
    return msg

print "Original ", m
encrypted, encrypt_x = encryption(m)
print "Encrypted", encrypted
decrypted = decryption(encrypted, encrypt_x)
print "Decrypted", decrypted
assert decrypted == m
print "Original == Decrypted"
