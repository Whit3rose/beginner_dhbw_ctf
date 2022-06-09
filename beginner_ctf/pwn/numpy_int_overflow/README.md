In this challenge we receive a port to connect to and the code of the program that runs on this port. At first, we can have a look at the code itself that looks very simple.   
![numpy](/images/numpy.png?raw=true "numpy")  
The program states that it is a simple calculator which multiplies your input by the number of 4. If the solution then equals -4, we receive the flag. The issue with this however is, that the program does not allow negative input. Therefore we need another way to generate a negative number that we can use to achieve our goal.
Interestingly enough, the program does not use a typical integer as the number to calculate but it uses a numpy array value. So let us look up how numpy works when it comes to numbers:  
https://numpy.org/doc/stable/reference/arrays.dtypes.html  
As the documentation states, a numpy int has the default size of 2^64. If our integer ist bigger than that maximum number of 18446744073709551616, we achieve an integer overflow and start in the negative part again. So we just have to remember that the number gets multiplied by 4 and we can calculate that we need the number of 4611686018427387903 to receive a -4 and with that also get the flag.  
![numpy](/images/numpy2.png?raw=true "numpy")  
dhbw{you_overflowed_me}  
