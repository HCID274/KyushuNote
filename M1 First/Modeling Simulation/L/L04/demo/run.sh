#!/bin/bash

 CASES="case1 case2 case3"
 for i in $CASES
 do
   python 2dAnsCase.py $i
 done

 #python 2dhcehBC.py
 #a2ps --medium=letter poisson.py -o poisson.ps
 ./htmlIndex.sh
