In this challenge we are simply supposed to give feedback to the creator of this CTF. Or not?
Let us open the docm file:  
![feedback](/images/feedback.png?raw=true "feedback")  
It states that this is a questionary for the ctf. But to actually get the questions we have to enable the Macros. Kind of suspicous, but lets give it a try:  
![feedback](/images/feedback2.png?raw=true "feedback")  
There actually are some changes. We can now see the questions. Pretty easy right?  
The issue with this challenge is, that in the backgroud the macro created a malicious file but we were not able to see that. We cannot see the Macro itself but there are ways to analyze the macro with malware analysis tools. This way, we could have seen what actually happend. But for now, lets not on the system where the file is located:  
![feedback](/images/feedback3.png?raw=true "feedback")  
This is the Macro. It saves a file systems.txt in the current users profile. By detecting the creation of this  file, we can also retrieve the flag:  
  
dhbw{plz_dont_open_random_word_files}  
