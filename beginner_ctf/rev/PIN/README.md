This program requests an unknown PIN to access the account and probably the flag. To analyze the file we can use Ghidra and see if we find anything interesing. When looking at the main function, we already see the important part:  
![safePin](/images/safePin.png?raw=true "safePin")  
The user-input gets compared to a simple numerical value which we can convert from hex to decimal format:  
0xc2e7b6c = 204372844  
By using this number as a PIN, we receive the flag.  
dhbw{i_hope_you_did_not_bruteforce_it}  
