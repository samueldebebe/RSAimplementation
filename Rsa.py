import math

# Accept to prime number for the user let say 3 and 11

p = input("Enter your value of 'p': ")
q = input("Enter your value of 'q': ")

 
# compute 'N' 
n = p*q
print("n value is =", n)
 
# Calculate phi(n) = (p-1)*(q-1)
phi = (p-1)*(q-1)
 
# Choose a value of e such that 1<e<phi(n) and gcd(phi(n), e) = 1
e = 2
while(e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1
 
print(" Encription key e =", e)
# Calculate d such that d = (e^-1) mod phi(n).
k = 2
d = ((k*phi)+1)/e
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
 
# Inset your message
msg = input("Enter your message: ")
print(f'Original message:{msg}')
 
# encryption
C = pow(msg, e)
C = math.fmod(C, n)
print(f'Encrypted message: {C}')
 
# decryption
M = pow(C, d)
M = math.fmod(M, n)
 
print(f'Decrypted message: {M}')   