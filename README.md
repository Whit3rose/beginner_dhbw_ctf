To set up the website and the environment, clone the repositiory and then navigate to the CTFd folder. There you simply type
sudo docker-compose up  
After loading all the resources, you should be able to connect to the website on localhost:8000.  
You should now get greeted by this setup webpage. It does not matter what information you use to complete the setup, but you will have to go through the different pages until the initial setup is completed.  
![Setup](images/setup.png?raw=true "Setup")
Now you see a basic welcome page that looks like this:
![Setup](images/setup2.png?raw=true "Setup")
What we now want to do, is to import the actual project for dhbw_ctf. Therefore, navigate to the Admin Panel in the navigation bar on the top.
![Setup](images/setup4.png?raw=true "Setup")
Here you get the option to view statistics if the event actually started. However, what we want to do is to go to the config tab.
![Setup](images/setup5.png?raw=true "Setup")
There are some options to configure the CTFd website. We now want to move to 'Backup'
![Setup](images/setup6.png?raw=true "Setup")
If you now click on import and select the given zip file on the home folder of the repository (DHBW_CTF*.zip) you can import the project.
![Setup](images/setup7.png?raw=true "Setup")
Now you will have to wait some time until you can log in again.
![Setup](images/setup8.png?raw=true "Setup")
As soon as you get redirected to the Login page, use the user credentials of  
> admin : admin  

to activate the website. You can then modify and change the website as well as you can now see all challenges.
There also is a default user account:  
> user : user  

This account allows you to see the website as a participant of the CTF. You can also register new users now.  

Have fun playing :D


Notes:
- There have been some issues with the sockets running in the virtual network. When you connect with netcat and then abruptly close the connection with ctrl+c the sockets closed. I fixed this by using multi-connection servers. Just in case that this problem still apprears, you will have to restart the docker-compose and it should work again
- Challenges were tested on Kali and Ubuntu Linux
- If there are problems with the IP-adresses of the virtual network or with the port of the CTFd website, feel free to make some changes to the docker-compose.yml file
- An explanation/short write-up on how each challange works can be found as the README of each challenge. To view them, just navigate to /beginner_ctf/*
