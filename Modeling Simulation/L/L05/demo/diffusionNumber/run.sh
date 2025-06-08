#!/bin/bash

 DNL="0.2 0.4 0.5 1.0 2.0"

 FL="1dImp.py 1dExp.py"

 for d in $DNL
 do
   for f in $FL
   do
      python $f $d
   done
 done
 
 ./htmlIndex.sh
