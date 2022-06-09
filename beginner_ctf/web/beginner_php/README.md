When we try to access the given website, all that happens is that we get told that it is forbidden to visit it by an Apache 2.4.52 Server. It might be, that there just is not an index.html file. So what we can do is use gobuster or dirbuster to find paths on the server.  
Using the typical SecLists wordlists to discover content on these sites, we find http://192.168.187.100/safe:  
![beginner_php](/images/safe.png?raw=true "beginner_php")
This site requests a password from us to access what looks like a password safe. The description of the challenge already mentions that the website is written in php. Therefore we can try some common php mistakes when it comes to comparing two strings. One of them is, that if you change the datatypes, the string compare return true. So lets try this using burp suit.  
Actual request:  
![beginner_php](/images/safe2.png?raw=true "beginner_php")  
Our request:  
![beginner_php](/images/safe3.png?raw=true "beginner_php")  
This actually bypasses the authentication and we receive the flag:  
![beginner_php](/images/php.png?raw=true "beginner_php")  
dhbw{i_should_not_use_insecure_functions}  
