In this challenge we get a pcap file. This is alrady an indicator that we should open the file in wireshark to display its content. Wireshark usually is used to read network traffic and therefore read pcap files. When we open the file, we see something interesting:  
![keytrokes](/images/keytrokes.png?raw=true "keytrokes")  
It looks like we have the communication of a USB transfer or something else. However, every second packet from 3.3.1 to host is 000000000000. So these packets will probably not be useful at all. The others packets follow the same structure tough. It always looks like there is some hex value that the Data part represents. So now the question is, what this data actually means. After some research you might find that there is an option to save keytrokes, so the keyboard input in pcap files. This input follows the following structure:  
2: “PostFail”,  
4: “a”,  
5: “b”,  
6: “c”,  
7: “d”,  
8: “e”,  
9: “f”,  
10: “g”,  
11: “h”,  
12: “i”,  
13: “j”,  
14: “k”,  
15: “l”,  
16: “m”,  
17: “n”,  
18: “o”,  
19: “p”,  
20: “q”,  
21: “r”,  
22: “s”,  
23: “t”,  
24: “u”,  
25: “v”,  
26: “w”,  
27: “x”,  
28: “y”,  
29: “z”,  
30: “1”,  
31: “2”,  
32: “3”,  
33: “4”,  
34: “5”,  
35: “6”,  
36: “7”,  
37: “8”,  
38: “9”,  
39: “0”,  
40: “Enter”,  
41: “esc”,  
42: “del”,  
43: “tab”,  
44: “space”,  
45: “-”,  
47: “[“,  
48: “]”,  
56: “/”,  
57: “CapsLock”,  
79: “RightArrow”,  
80: “LetfArrow”
  
  
Now that we have this knowledge, we can easily write the contents that the user wrote to the host:  
  
  
"ach wie gut dass niemand weiss dass die flagge dhbw  youpcapedmykeystrokes  heisst"


Refactoring this to the correct format and we get  
dhbw{youpcapedmykeystrokes}  

So as you can see, pcap file are much more versitile than just for saving network traffic.
