# Writeup for GovTech's level 2 challenge - TicTacToe 
URL: http://govtech-challenge.com/challenge/challenge1-second-puzzle.php?firstchallenge=base4 

The first part of the challenge contain the brief explanation of how the flag is encoded.
![first_part](https://github.com/0x0ffff5ec/crossctf-2017/blob/master/final/web/govtech2-web/screenshots/first-part.PNG)

The second part of the challenge contain the encoded flag
![second_part](https://github.com/0x0ffff5ec/crossctf-2017/blob/master/final/web/govtech2-web/screenshots/second-part.PNG)

The objective of this challenge is to decode the flag encoded in the TicTacToe. 

## Description:
Web based "crypto" challenge.   

P.S. A FUCK UP CHALLENGE FOR PEOPLE WHO ARE TOO FREEEEEE. JKJK 

## STEPS
FOR EACH OF THE PICTURE
1. Convert each of the number to its binary i.e. 1 -> 0001, 4 -> 0100, 3 -> 0011 
2. Using the truth table, perform the operation i.e.
``` 
  1  0001
  4  0100
  3  0011
     0110
```
```
  0 0000
  7 0111
  6 0110
    0001 
```
```
0110 0001 -> 0x61 -> a
```
3. In the event which the winning tiles is x, prepend a 1 on the msb 
```
 1 0001
 4 0100
 3 0011
   0110
```
```
   1
 0 0000
 7 0111
 6 0110
   1001
```
```
0110 1001 -> 0x69 -> i
```
Combining all the letters we will get: 
> GovTech{ABC} 


