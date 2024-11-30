

import collections
import hashlib
import random



    
    # Y^2=x^3-3x+b

p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    
a=0
b=7
#Base point
gx=0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy=0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
   

n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


def modinv(k, p):
   #tabe az internet
    if k == 0:
        raise ZeroDivisionError('division by zero')

    if k < 0:
      
        return p - modinv(-k, p)

    
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t
    

    assert gcd == 1
    assert (k * x) % p == 1

    return x % p
    #tebghe formol in tavabe ra neveshtam
def double(x1,y1):
       
        s=(((3 * (x1**2))+a) * modinv(2*y1,p)) % p
        x3=((s**2)-(2*x1))%p
        y3=(s*(x1-x3)-y1)% p
        return(x3,y3)
        
def addition(x1,y1,x2,y2):
        
        s = (y2 - y1) * modinv(x2-x1,p) % p
        x3 = (s**2 - x1 - x2) % p
        y3 = (s * (x1 - x3) - y1) % p
        #print(x3,y3)
        return(x3,y3)

def DoubleandAdd(d,gx1,gy1):
        d=bin(d)
        Q1=gx1
        Q2=gy1
        le=len(d)
        for i in range(0,le-1):
            (Q1,Q2)=double(Q1,Q2)
            
            if d[i]=='1' :
                (Q1,Q2)=addition(Q1,Q2,gx1,gy1)  
        return(Q1,Q2)
        


def make_keypair():
   
    private_key = random.randrange(1, n)
    public_key = DoubleandAdd(private_key, gx , gy)

    return private_key, public_key

#in tabe az internet
def hash_message(message):
    """Returns the truncated SHA521 hash of the message."""
    message_hash = hashlib.sha512(message).digest()
    e = int.from_bytes(message_hash, 'big')

    # FIPS 180 says that when a hash needs to be truncated, the rightmost bits
    # should be discarded.
    z = e >> (e.bit_length() - n.bit_length())

    assert z.bit_length() <= n.bit_length()

    return z

def sign_message(private_key, message):
    z = hash_message(message)

    r = 0
    s = 0

    while not r or not s:
        k = random.randrange(1, n)
        t = DoubleandAdd(k, gx , gy)

        r = t[0] % n #مقدار x آن
        s = ((z + r * private_key) * modinv(k, n)) % n

    return (r, s)

def verify_signature(public_key, message, signature):
    z = hash_message(message)

    r, s = signature
    ( f , d) = public_key
    w = modinv(s, n)
    u1 = (z * w) % n
    u2 = (r * w) % n

    c2,x5= DoubleandAdd(u1, gx, gy )
    t,r =   DoubleandAdd(u2, f, d )
    (x, y) = addition( c2,x5,t,r)
        

    if (r % n) == (x % n):
        return 'okeye'
    else:
        return 'invalid '




private, public = make_keypair()
print("Private key:", hex(private))
print("Public key: (0x{:x}, 0x{:x})".format(*public))

msg = b'behzad!'
msgb='behzad!'
signature = sign_message(private, msg)

print()
print('Message:', msgb)
print('Signature: (0x{:x}, 0x{:x})'.format(*signature))
print('Verification:', verify_signature(public, msg, signature))
# nemidanam chera (x,y) be onvan khoroji dar nazar nagereft va kole meghdar ra x dar nazar migrad.va yekseri taghirat dadam ama baz drost nashod
msg = b'i am behzad!'
msgb = 'i am behzad!'
print()
print('Message:', msgb)
print('Verification:', verify_signature(public, msg, signature))

private, public = make_keypair()

msg = b'behzad!'
msgb='behzad!'
print()
print('Message:', msgb)
print("Public key: (0x{:x}, 0x{:x})".format(*public))
print('Verification:', verify_signature(public, msg, signature))
