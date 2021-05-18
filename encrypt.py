
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

unencrypted = []
cipher = []
spydict = {}

def ecode_word():
    wlist = []
    word = input(str('Enter a code word:\f\t')).upper()
    for w in word:
        wlist.append(w)
    return wlist

for i in ecode_word():
    if i in alphabet:
        unencrypted.append(i)
        alphabet.remove(i)
    else:
        pass

for k in unencrypted:
    cipher.append(k)
for s in alphabet:
    cipher.append(s)

print(alphabet2)
print(cipher)


for sp in range(len(cipher)):
    spydict['%s' % alphabet2[sp] ] = '%s' % cipher[sp]


def classified():
    alist = []
    blist = []
    q = input(str('Enter a message:\f\t')).upper()
    for lg in q:
        alist.append(lg)

    for b in range(len(alist)):
        if alist[b] == ' ':
            blist.append(' ')
        elif alist[b] not in alphabet2:
            pass
        else:
            blist.append(spydict['%s' % alist[b]])
    return blist

classified = classified()



file = open('./emessage.txt', 'w+')
encryption_history =  open('./ehistory.txt', 'a+')

for k in classified:
    file.write('%s' % k)
    encryption_history.write('%s' % k)
file.write('\n\n')
encryption_history.write('\n\n')

file.close()
encryption_history.close()

''' Need to specify files to write message to based on the code word'''