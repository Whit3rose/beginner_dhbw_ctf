Playing around on this website does not seem to reveal anything too interesting in the first place. All just looks like a usual bootstrap website where we cannot do anything special. Content discovery with gobuster also does not reveal anything too interesing. However there is something that we might have a look at. We can Download a portfolio pdf file from the website itself. Let us have a look at the http request using burp:  
![directory](/images/directory.png?raw=true "directory")  
As it looks like, the website simply sets the location of the file as a parameter in the url. This means it might be vulnerable to the a directory traversal attack. Trying the different typical files, we can actually get the /etc/passwd file:  
![directory](/images/directory2.png?raw=true "directory")  
At the end of this file, we can find the flag:  
![directory](/images/directory3.png?raw=true "directory")  
  
dhbw{check_the_path}  
