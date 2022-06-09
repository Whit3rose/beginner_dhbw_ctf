In this challenge, it looks like we have to win a couple of shell games against the machine. By itself, that would be quite an easy challenge. For every round the change is 1/3 to win. However, according to the message, we have to win 10 times in a row which would probably need a lot of attempts. Therefore we need another solution. Let's look at the code using Ghidra:  
![shellgame](/images/shellgame.png?raw=true "shellgame")  
There is nothing too interesting in the main function. So let's have a look at the game function that probably shows us how the game itself is implemented:  
![shellgame](/images/safeRev.png?raw=true "shellgame")  
The important part here is that the user-input and the computer-choice get compared by the strstr() function. If we have a look at the documentation of this function, the issue get clear:  
![shellgame](/images/strstr.png?raw=true "shellgame")  
It looks like this function searches for a substring when comparing two strings. We can use that, to make sure that the solution always is part of the given answer by inputting "firstsecondthird" as our guess. This way, we win every round we play and get the flag:  
dhbw{looks_like_that_function_is_not_safe}  
