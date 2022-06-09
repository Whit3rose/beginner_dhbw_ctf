When we visit the website, we get greeted by this error message:  
![spring](/images/spring.png?raw=true "spring")  
This already gives us some useful information. We  now know that the server is running on Apache Tomcat 9.0.59. Once again, by using gobuster or a similar tool, we can discover some actual content on the website:  
http://192.168.187.140:8080/prototype/welcome gives us this screen:  
![spring](/images/spring2.png?raw=true "spring")  
So now, we know that the application works with spring and likely spring boot. The combination of spring and tomcat ist quite popular. Not only for good reasons. There is a spring4shell exploit for this version of tomcat which we might give a try. Part of this folder is an exploit.py that can be found online if you do not want to create your own exploit.  
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22965  
We can use this exploit to get a shell:  
![spring](/images/spring3.png?raw=true "spring")  
We can now modify the cmd parameter of the site as if it would be in a terminal and search around for a bit:  
![spring](/images/spring4.png?raw=true "spring")  
