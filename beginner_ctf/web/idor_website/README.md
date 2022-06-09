When we visit the website, all direct information we get is that it is a note taking website. We then have to option to either login or register. Since we do not have any credentials for a user account, we can try to register our own  
![idor](/images/idor3.png?raw=true "idor")  
![idor](/images/idor2.png?raw=true "idor")  
![idor](/images/idor4.png?raw=true "idor")  
After logging in, we get to see the actual usecase of the website.   
![idor](/images/idor5.png?raw=true "idor")  
It looks like we can either view our notes, create new ones or logout. We do not have any notes yet, so let us simply try to create a new one.  
![idor](/images/idor6.png?raw=true "idor")  
After we save it, we get redirected to the page where we can view the note.  
![idor](/images/idor7.png?raw=true "idor")  
Now at the beginning, there is nothing too special about that. However, there is something interesting in the URL we see:  
![idor](/images/idor8.png?raw=true "idor")  
It looks like the website displays us the note with an ID or something with the number of 45. Let us have a look, if we get access to any other notes when using different IDs. To do this, we can use burp:  
![idor](/images/idor9.png?raw=true "idor")  
Send this request to the Intruder and modify the url:  
![idor](/images/idor10.png?raw=true "idor")  
![idor](/images/idor11.png?raw=true "idor")  
  
After starting the attack, it might take a while until we get a result but we can see if a note exists by looking at the status code of the server response:  
![idor](/images/idor12.png?raw=true "idor")  
As we can see, there are three pages available. 45 is our note and / is the home. So let us have a look at the note with the id 51:  
![idor](/images/idor13.png?raw=true "idor")  
