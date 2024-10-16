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

#print b[7]
print '\n'

#B={'0x30': '0', '0x31': '1', '0x32': '2$'} swap middle, key/vals
#B={'': {'0': ['0x30']}, '': {'0x31': '1'}, '': {'0x32': '2$'} }
#B={'0': ['0x30'], '0x31': 1, '0x32': '2$'}

#B={'0x30':0, '0x31':1, '0x32':'2$'}
#B={ 0: {"['0x30']":0}, 0: {"['0x31']":0}, 0: {'0x32':'2$'} }

#B={48:{"['0']":"['0x30']"}, 49:{"['1']":"['0x31']"}, 50:{"['2']":"['0x32']"}}
#print B

#for i in range(len(a),100000):
#    if B['0x31']==True or B['0x31']==True:
#        print i

#for i in B.items():
#    print i

#for i in range(len(_),100000):
#    if B['0x30']==False or B['0x30']==False:
#        print i

#B={0:'0x18', '0x31':1, '0x32':'2$'}
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

#def example(a,n,option):
#    column=a+n
#    value=column+option
#    return hex(value)

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

#Copyright (C) 2023 Thomas McCammon
#The above software is a standard input/output system configuration tool. 
#Users may freely download, use, distribute, and modify this file.
#As of 10/01/2023 a service fee of 5% will be required for any commercial use of this code.
#Payable to Thomas McCammon. For inquiry please call 951.605.0805 or email me at westcoast.coders@mail.com.
