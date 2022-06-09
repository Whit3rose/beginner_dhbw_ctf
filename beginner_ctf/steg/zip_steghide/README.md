This challenge requires two steps to get the flag. The first one is, that the .jpg file is not only an image is actually a zip file. So if we unzip it, we get the image file itself and a password.txt file which includes a password we can use with steghide:  
> steghide extract -sf big_challenge  
  
By completing these steps, we get the flag:  
![steghide](/images/steghide.png?raw=true "steghide")  
  
  
DHBW{g00d_c0mb1nation}
