This first index website seems to be a simply bootstrap version of a website that has nothing to interesting. Discovering more content by using gobuster however reveals the actually interesting part:  

/admin has login for Admin  
![blog](/images/adminLogin2.png?raw=true "blog")

However, when you input some random creadentials you get redirected to /login and it says that the creds are invalid  
![blog](/images/invalidUsername.png?raw=true "blog")  
So it makes sense to have a look the JavaScript Code of the page  
  
![blog](/images/cookieJs.png?raw=true "blog")  
This part seems interesting. It looks like the code checks if there is a sessionUser and then passes that instead of the actual credentials. Setting the Cookie in the Console with "document.cookie="sessionUser=test"" and trying to log in again shows this message:  
  
![blog](/images/cookieStorage3.png?raw=true "blog") 
  
  
Setting the sessionUser Cookie to admin and trying to log in again might work:  
![blog](/images/cookieFlag.png?raw=true "blog")

