This challenge provides us with a audio (.wav) file and an address to a website. The audio itself plays the sound of what seems like a phone conversation with a support hotline that wants an account number and a pin for authentication. We can also hear a user inputting his credentials.  
The website on the other hand looks very simple. It seems like it should be the website of a bank, however, there are not many options. Tough we can click on a Login page that asks for a username and a password.  
![phone](/images/login.png?raw=true "phone")  
So maybe there is  some way to use the audio file with the user inputting his credentials to extract the input and therefore receive the username and password. Some research shows us, that the numbers on a phone acutally have a default frequency that differs for all the numbers:  
https://blogs.unimelb.edu.au/sciencecommunication/2012/10/17/melody-behind-phone-numbers/  
![phone](/images/soundFrequency.png?raw=true "phone")  
Now we can use this information and analyse the audio file itself. For that we can use a tool called Sonic Visualiser that can help us to display the the frequency of each sound.  
![phone](/images/soundFrequency2.png?raw=true "phone")  
The red dots represent the sound of the numbers. By having a look at the frequency itself, we can get the necesarry credentails:  
username = 11649981  
password = 584948  
dhbw{you_probably_should_not_publish_your_phonecalls}  
