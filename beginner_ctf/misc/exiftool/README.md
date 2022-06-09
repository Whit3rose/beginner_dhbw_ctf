In this challenge the only thing we get is a picture of some kind of monkey. The first thing we might do is to have a look at the metadata. For this we can use the tool exiftool that helps us to display the exif data of the jpg file:  
![exiftool](/images/exiftoolMonkey.png?raw=true "exiftool")
  
  
The interesting part here are the artists name (Photoh4acker) and the gps coordinates. Looking at the gps coordinates first, does not directly lead to an useful location. Searching for a profile on social media with the name photoh4cker however reveals an account on the platform imgur where you can post and share pictures. There is already one post that looks like a flag.   
![exiftool](/images/imgur.png?raw=true "exiftool")  
Playing around with the string a little bit reveals that it is in ROT13 format and actually means  
dhbw{look_at_the_metadata}  
