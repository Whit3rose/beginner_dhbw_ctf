We get presented a simple jpg file. As usual in steganography challenges, we mostly try to use different tools and filters on the image. In this case, the solution lies in outguess. Outguess is a tool that allows you to insert invisible information into redundant bits of data sources like this image. To exfiltrate this information, you can simply use outguess as well. By using the command:  
> outguess -k "" -r joke.jpg flag.txt  

we receive the flag:  
![outguess](/images/outguess.png?raw=true "outguess")  
  
  
dhbw{guess_i_got_outguessed} 
