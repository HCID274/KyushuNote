#!/bin/bash

 #CASES="Imp Exp"
 CASES="Comp"
 for i in $CASES
 do
   SC=1d$i.py
   python $SC
 done

 #python 2dhcehBC.py
 #a2ps --medium=letter poisson.py -o poisson.ps
 ./htmlIndex.sh
