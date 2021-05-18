
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

encrypted = []
cipher = []
spydict = {}

with open('./emessage.txt') as f:
    for a in f:
        if a != '\n':
            encrypted.append(a.strip('\n'))

def dcode_word():
    wlist = []
    word = input(str('Enter a code word:\f\t')).upper()
    for w in word:
        wlist.append(w)
    return wlist

for i in dcode_word():
    if i in alphabet:
        cipher.append(i)
        alphabet.remove(i)
    else:
        pass


for s in alphabet:
    cipher.append(s)


for sp in range(len(cipher)):
    spydict['%s' % cipher[sp] ] = '%s' % alphabet2[sp]


def classified():
    alist = []
    blist = []
    q = encrypted
    for lg in q:
        for og in lg:
            alist.append(og)
    for b in range(len(alist)):
        if alist[b] == ' ':
            blist.append(' ')
        else:
            blist.append(spydict['%s' % alist[b]])
    return blist


classified = classified()



file = open('./dmessage.txt', 'w+')
decryption_history =  open('./dhistory.txt', 'a+')

for k in classified:
    file.write('%s' % k)
    decryption_history.write('%s' % k)
file.write('\n\n')
decryption_history.write('\n\n')

file.close()
decryption_history.close()
