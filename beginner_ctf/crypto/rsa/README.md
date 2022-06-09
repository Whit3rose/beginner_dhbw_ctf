This challenge gives us our flag. The only issue is that every letter is encrypted using rsa. On the other hand the interesting thing is that we are allowed to encrypt and decrypt our own data.   
![rsa](/images/rsa9.png?raw=true "rsa")  
Now the first and obvious thing is to try to decrypt the given numbers and therefore simple get the flag. So let us try to decrypt the first letter:  
![rsa](/images/rsa7.png?raw=true "rsa")  
Looks like it checks if you did input one of the values of the flag and then does block the decryption. Good thing that we got some tricks. There is an issue in homomorphic encryption that essentialy works like the following:  
enc(m1) * enc(m2) = enc(m1 * m2)  
We already got enc(m1) which are the values of the cipher letters we got from the challenge itself. So let us simply decode a known character:  
![rsa](/images/rsa8.png?raw=true "rsa")  
Now we also got the cipher of f which in this case is enc(m2). We also know that the value of f is most likely ASCII value of 102.  
So let us now calculate enc(m1) * enc(m2) = 88668 * 77584 = 6879218112 = enc(m1 * m2)  
We can now use this value and decrypt it:  
![rsa](/images/rsa6.png?raw=true "rsa")  
So now we know that we get dec(enc(m1 * m2)) = 10200 = m1 * m2  
Since we can assume that m2 = f = 102, we get the value of m1 which is 100 and thereby actually fits the acsii value of d. If the flag follows the same pattern as all the other flags, it starts with dhbw{...} so we can assume that this method works.   
Repeating the process for every single letter, we get the flag:  
  
dhbw{homomorphic_encryption}  
