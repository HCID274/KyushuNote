#!/bin/bash

 REL="1 10 1000 10000"
 SCT=cavity.py
 SCT=cavityAns.py

 NPS=2
 ip=0
 for i in $REL
 do
   (
   RE=$i
   python3.9 $SCT $i
   #a2ps --medium=letter $SCT -o `basename $SCT .py`.ps
   ./htmlIndex.sh
   #mkdir $RE
   #cp $SCT 
   #mv *.gif *.png index.html $RE
   )&
   flg=$((ip%NPS))
   flg=$((flg+1))
   if [[ $flg -eq $NPS ]]
   then
     wait
   fi
   ip=$((ip+1))
 done
