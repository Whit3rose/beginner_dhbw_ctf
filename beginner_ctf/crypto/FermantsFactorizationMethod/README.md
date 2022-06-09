After connecting with netcat, we see that we only get the public key of an rsa encryption and something that looks like an encrypted flag.  
![rsa](/images/rsa.png?raw=true "rsa")  
In principle we could run a dictionary attack but with such a short string, it will likely not suceed. Therefore we should have a look at the code itself.   
Looking at the encryption itself, it looks kind of standard for RSA. The other big issue some encryption implementations have is the key generation itself. Incorrectly generated keys might be an interesting attack point. The keys themselfes look like they are big enough to prevent a bruteforce in a short time. So this might not be the issue. However, looking at the two fundamental primes p and q, there is a interesting implementation:  
![rsa](/images/rsa3.png?raw=true "rsa")  
It looks like the first prime gets generated kind of randomly but the second prime number is simply the following prime number after p. After some research you might find, that if the two primes p and q are too close to each other, you can use Fermats Factorization Method to easily and quickly calculate the private key.    
A script for this in part of the repository. Using this method, we can calculate the private key and decrypt the flag:  
dhbw{use_safe_keys}  
