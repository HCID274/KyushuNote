#!/bin/bash

 CL="case1 case2 case3"
 PY=1dAnsCases.py

 for i in $CL
 do
   python3 $PY $i
 
 done
 
 ./htmlIndex.sh 
