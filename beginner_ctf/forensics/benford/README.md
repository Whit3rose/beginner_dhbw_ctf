The original idea of this challenge was to use Benford's Law to detect a deepfake. Benford's Law essentially states, that in a natural environment, the number 1 is more likely to appear as the first digit of a number than number 2. Number 2 is more likely to be the leading digit than number 3 and so on.  
https://en.wikipedia.org/wiki/Benford%27s_law  
  
This is also the case when it comes to original pictures. If you count the RGB values, the same distribution of leading digits should appear that what Benford's Law states. However, when you edit a picture, like adding a filter or somethink, this changes the value of the pixels in a unnatural way. So Benford's Law does not apply anymore. This means, that by reviewing if the pixel values of an image follow Benford's Law, you can in theory detect image manipulation:  
https://www.irjet.net/archives/V8/i10/IRJET-V8I10113.pdf  
  
The idea for this challenge was, to let the user apply Benford's Law on a dataset of images and therefore recognize the edited image. This idea did not work because I could not find a dataset that did completly fit the natural behaviour of Benford's Law. This way, there would have been multiple possible answers for the challenge which should never be the case when it comes to a CTF. However the idea was still applied to single images:  
![benford](/images/benford1.png?raw=true "benford")  
![benford](/images/benford2.png?raw=true "benford")  
