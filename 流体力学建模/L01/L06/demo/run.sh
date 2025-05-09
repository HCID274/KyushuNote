#!/bin/bash

 ##2dAns:steady state
 #cases="2duExp 2duImp 2dAns"
 cases="2duExpAns 2duImpAns"
 for i in $cases
 do
   SCT=$i.py
   python $SCT
   #a2ps --medium=letter $SCT -o `basename $i .py`.ps
 done
 ./htmlIndex.sh
