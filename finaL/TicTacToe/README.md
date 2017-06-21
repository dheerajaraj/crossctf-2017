# Writeup for GovTech's level 2 challenge - TicTacToe 

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
   0001
```
```
0110 1001 -> 0x69 -> i
```
Combining all the letters we will get: 
> GovTech{ABC} 


