import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def modinv(a,m):

    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x
    raise Exception('The modular inverse does not exist.')


def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


primes = []
with open('./primes100.txt') as f:
    for prime in f:
        primes.append(int(prime))


p = primes[random.randint(0, len(primes))]
q = primes[random.randint(0, len(primes))]

while(p == q):
    q = primes[random.randint(0, len(primes))]

n = p * q
phi_n = compute_lcm((p - 1), (q - 1))
e = random.randint(1, phi_n)
while (gcd(phi_n, e) != 1):
    e = random.randint(1, phi_n)

d = modinv(e, phi_n)

def encypt(message: str):
    cipher = ""
    for char in message:
        cipher_letter = pow(ord(char), e, n)
        cipher += str(cipher_letter) + " "
    return cipher


print("Welcome to my RSA encryption tool")
print("Here is your flag: ")
encypted_flag = encypt("dhbw{homomorphic_encryption}")
print(encypted_flag)

def menu():
    print("\n Options:")
    print("1: Encrypt message")
    print("2: Decrypt message")
    option = input("Please select one of the options? ")


    if option == '1':
        print("-----Encryption-----")
        message = input("Please enter your message: ")
        print(encypt(message))
        menu()
    elif option == '2':
        print("-----Decryption-----")
        message = input("Please enter your encrypted numerical message: ")
        message = message.split(" ")
        for element in message:
            if element in encypted_flag:
                print("invalid character: " + element + "\n please choose a character that is not part of the flag")
                menu()
        plaintext = ""
        for char in message:
            mes = (int(char) ** d) % n
            print("decrypted value: " + str(mes))
            plaintext += chr(mes)
        print(plaintext)
        menu()
    else:
        print("Please select a valid Option")

menu()

