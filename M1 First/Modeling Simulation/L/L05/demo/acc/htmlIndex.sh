#!/bin/bash
 ##setting parameter
 #directory where figures are 
 DN1="./"
 DN2="./"
 HF="./index.html"
 #number of rows
 R=3
 ##definition of suffix
 SUFFIX1=".gif"
 SUFFIX2=".gif"
 #make directory DN2 if not exsit
 #if [[ ! -a $DN2  ]]
 #then
 #  mkdir $DN2
 #fi
 #
 #NPS=10
 #ip=0
 #for i in ${DN1}/*${SUFFIX1}
 #do
 #  (
 #    #FNN=`basename $i .eps`.re.eps
 #    #eps2eps $i $FNN
 #    #mv $FNN $i
 #    convert -density 200 $i `basename $i ${SUFFIX1}`${SUFFIX2} ;
 #    convert -density 300 $i `basename $i ${SUFFIX1}`.png ;
 #    #convert -density 400 $i `basename $i ${SUFFIX1}`${SUFFIX2} ;
 #  )&
 #  flg=$((ip%NPS))
 #  flg=$((flg+1))
 #  if [[ $flg -eq $NPS ]]
 #  then
 #    echo "*********************************************************"
 #    echo "waiting"
 #    echo "*********************************************************"
 #    wait
 #  fi
 #  ip=$((ip+1))
 #done
 #mv *${SUFFIX2} ${DN2} 

 wait

 ##script for tag 
 echo '<html><head><title>Index</title></head>' > ${HF}
 echo '<link rel="stylesheet" href="common.css" type="text/css">' >>${HF}
	
 echo '<div id ="title">'`pwd`'</div>' >> ${HF}
 echo '<div id="stitle2">
       <script language="javascript">
       <!--
                update = new Date(document.lastModified);
                theMonth = update.getMonth() + 1;
                theDate = update.getDate();
                theYear = update.getYear();
                theYear = "2" + theYear - "100";
                document.write("Last updated: " + theYear + "."+ theMonth + "." + theDate);
       -->
       </script>
       </div>
       <div id="space"></div> ' >> ${HF}
 
 echo '<table><tr>' >>${HF}
 let j=1
 for i in ${DN2}/*${SUFFIX2}
   do
     if [[ `expr $j % $R`  -eq 0  ]] ; then
       echo '<td><a href="'${DN1}'/'`basename ${i} ${SUFFIX2}`${SUFFIX1}'">'`basename ${i} ${SUFFIX2}`'</a><br><img src='${i} width=100%'></td></tr><tr>' >>${HF}
     else
       echo '<td><a href="'${DN1}'/'`basename ${i} ${SUFFIX2}`${SUFFIX1}'">'`basename ${i} ${SUFFIX2}`'</a><br><img src='${i} width=100%'></td>' >>${HF}
     fi
     let j=j+1
   done
 echo '</tr></table></div></body></html>' >>${HF}

