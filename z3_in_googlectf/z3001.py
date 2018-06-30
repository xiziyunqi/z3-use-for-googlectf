#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from z3 import *
import time
s=Solver()
hash =BitVec(0x5417,16)
password=[BitVec(('password%d'%i),16) for i in range(0,15)]
for i in range(0,15):
          s.add(password[i]>0x2f,password[i]<0x7a)
          hash^=password[i]
          #print "11",password[i]
          hash<<=1
          hash&=(0xffff)
s.add(hash==36346)
s.check()
if s.check()==sat:
        answer=s.model()
        #print(chr(answer[password[1]].as_long()))
        #print "%s" %(answer[3].as_long())
        s=''
        for i in range(0,15):
            print chr(answer[password[i]].as_long())
            s+=chr(answer[password[i]].as_long())
        print(s)
        answer1=s.model()
        #print(chr(answer[password[1]].as_long()))
        #print "%s" %(answer[3].as_long())
        s1=''
        for j in range(0,15):
            print chr(answer1[password[j]].as_long())
            s1+=chr(answer1[password[j]].as_long())
        print(s1)
