When looking at the given code, it looks like there is a flag with the length 14 and some data. There to strings are appended and then hashed using md5. This hash is then used as a signature. Then there is an input_hash that consists of the data "user", some hex values and the string "admin". The hash that is required to retrieve the flag is then the md5 hash of the secret (so the flag) + this input_hash. The input_hash is known but we do not know the flag and therefore we do not know the required input that get checked.     
This information perfectly fits the conditions of a Hash Length Extension Attack (https://book.hacktricks.xyz/crypto-and-stego/hash-length-extension-attack) since we know:  
- length of the secret
- the clear text data
- the algorithm (md5)
- the padding
This essentially means that we can append data to the hash and still create a valid signature.
The attack works like the following:  
  
After connecting to the server, we get some important information:  
![hash](/images/hash.png?raw=true "hash")  
We get the signature and the data which equals "user". The server then requests some kind of answer. To figure out what is wants, we have a look at the challenge.py file again:  
![hash](/images/hash2.png?raw=true "hash")  
It looks like the server takes the answer of the user and prepends the hex value of the flag. Then it takes this combination and tries to decode it as an md5 hash. The server then checks this input against the signature we got previously. However, without knowing the secret (so the flag), we do not know how we can create this exact signature. But there is an option to create this signature without knowing the secret.  
We need a function that uses md5 as well, but we start with the signature. Now we can simply use this function to append the used "admin" part to create a valid hash. This attack is called hash length extension attack because we basically append something to a signature and thereby get a correct hash. This only works, because we know that the md5 hash has a length of 64 bytes. The exact method of this attack is decribed here:  
https://blog.skullsecurity.org/2012/everything-you-need-to-know-about-hash-length-extension-attacks  
To create this kind of attack, you can use the hash_extender tool https://github.com/iagox86/hash_extender. Using this tool to create the extended hash and then inputting it to the server, we get the flag:  
dhbw{use_hmac}  
