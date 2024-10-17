#!/usr/bin/python

print "^S"      

_=[[0x30],[0x31],[0x32],[0x33],[0x34],[0x35],[0x36],[0x37],[0x38],[0x39]]

for i in range(len(_)):
    print _[i]
                    
a=[48,49,50,51,52,53,54,55,56,57]

b={}
d={}
                   
for i in range(len(a)):
    d [a[i]] = i
print d

for i in range(len(a)):
    b [a[i]] = oct(a[i])
print b

#for i in range(len(a)):
    #b [a[i]] = bin(a[i])
#print b

#for i in range(len(_)):
 #   if _[i]==(55) OR _[i]==55
#        print ''

for i in range(len(_)):
    b [a[i]] = oct(a[i]+2)
print b

for i in range(len(a)):
    b [a[i]] = hex(a[i])
print b

print '\n'

B={ 0:{"['0']":"['0x30']"}, 1:{"['1']":"['0x31']"}, 2:{"['2$']":"['0x32']"} }
for i in range(len(a),100000):
    if B[1]==True or B[0]==False:
        print i
#    if B[2]!=True:
#        print '2'
#        if B[2]!=False or B[2]!=True:
#            print '2'

# {'':{'':'0x18'}, '':{'':'0x19'}, '':{'':'0x1A'}, '':{'':'0x1B'}}

for i in B.items():
    print i

#while(1):
#    if B[1]==True or B[0]==False:
#        print ''
#    if B[2]!=True:
#        break

G={ 1:{"['U']":"['0x55']"}, 0:{"['u']":"['0x75']"}, 2:{"['']":"['0x20']"}}
for i in range(len(a),100000):
    if B[1]==True or B[0]==False:
        print i
    if B[2]!=True:
        print '\t0\t'
        if G[0]!=False or G[2]!=False:
            print '\n\t\t'

def dec(a,n,option):
    col=a+n
    val=col+option
    return hex(val)

#N={ 0:{"['n']":"['0x4E']"}, 1:{"['N']":"['0x6E']"}}
V={ 0:{"['x']":"['0x58']"}, 1:{"['X']":"['0x78']"}, 2:{"['']":"['0x20']"}}
for i in range(len(a),100000):
    if B[1]==True or B[0]==False:
        print i
    if B[2]!=True:
        print ''
        if V[0]!=False or V[1]!=False:
            print '\n\t00\t'
	    if i ==3 or i==5:
	        V[2]=dec(22,0,0)
            else:
	        V[2]="C"
	        V[2]=dec((255%i),0,16)

#def dec(a,b):
#    diff=(hex(a)-hex(b))
#    return (hex(a)-hex(diff))

D={ 0:{"['s']":"['0x53']"}, 1:{"['S']":"['0x73']"}, 2:{"['']":"['0x20']"} }
for i in range(len(a),100000):
    if B[0]==True or B[1]==False:
        print i
    if B[2]!=True:
        print ''
        if D[0]!=False or D[1]!=False:
            print '\033[36;47;91;5m \n\t00\t \033[00m' 
	    D[2]="C"
	    D[2]=dec(22,0,0)	   

import time, sys, tty, socket
time.clock()
print ' \n'
n = 1

print str(d) + ''#{e} 
print sys.argv[0]

def cd(d):
    return '\t\o\r' +d

def test():
    tty.setraw(sys.stdin)
    ch = (sys.stdin.read(1))
    while True:
        if ch>0:
	    for i in range(len(a),100):
	        D[2]=dec(32,0,i)
	        sys.stdout.write('\033[36;47;100;7;5m \n\t \033[00m'+ch+""+D[2])
	        sys.stdout.flush()
	        time.sleep(0.1)
	        if ch>255:
	            sys.stdout.write(ch)
	            sys.stdout.flush()
            break 
        else:
	    break

def testa():
    cnt=0
    ch=(sys.stdin.read(1)) 
    while(cnt<=1550):
        for i in range(26):
	    time.sleep(0.1)
	    ch=(sys.stdin.read(1))
            for j in range(10):
	        n=(i*j)
	        D[2]=dec(n,0,0)
	        sys.stdout.write('\033[36;47;92;5;94;36;94;63;255m \t\t \033[00m'+D[2])
	        if [0x55]:
		    D[2]=dec(32,0,11)
	            print ch
	            sys.stdout.write(ch)
		    sys.stdout.flush()
		    cnt=cnt+1

testa()
#test()
print sys.argv[0]

class rA(n):
    def __init__(s, foo):
        s._foo=foo

class rB(rA):
    def __init__(n, foo):
        rA.__init__(s=n, foo=foo)

try:
    if '':
        print '\n' + str(d)
except:
    SyntaxError("_*, Error(e)")

#
