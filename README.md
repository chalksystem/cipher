# cipher


 Cipher is a simple polyalphabetic cipher with two .py files in the first commit: encrypt.py and decrpyt.py

### How it works

 encrypt.py will ask for an alphabetical code word which will be placed at the front of the alphabet with any letter used removed from the remaining letter. If a code word uses a letter twice, it will not be repeated in the newly created alphabet. For example:


Alphabet before inputting code word
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

```
$ Enter a code word:
                    code word
```

Alphabet after inputting code word
['C', 'O', 'D', 'E', 'W', 'R', 'A', 'B', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

Notice that the string "code word" contains two o's and two d's. Because letters do not repeat, the new code (if separated into two words) is "code" and "wr"; the remaining letters remain in their original order minus the code word.

So if the letter "A" were to be used in a message, the letter "C" would be used in the encrypted word, if "B" then "O" would be used, and so on.


Next, the prompt "Enter a message:" will appear. After entering a message, it will be encrypted with the cipher then written to two files - one contains the encrypted history and the other the most recently encrypted word. For example:

```
$ Enter a message:
                  secret message
```
The encrypted message would be "QWDPWS JWQQCAW".

To decrypt the message, simply execute the decrypt.py file. The prompt "Enter a code word:" will appear and upon entering the last code word used, a decrypted message will be written to two file - one with the decrypted history and the other with the most recently decrypted word. For example:

```
$ Enter a code word:
                    code word
```
The decrypted message would be "SECRET MESSAGE". 

While being an incredibly simple excryption, this was fun to make and inspired me to study cryptography. I hope to write more advanced encryptions in the future, but I am happy that I have one under my belt. 

Enjoy!
