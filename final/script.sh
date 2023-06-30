#!/bin/bash
path=/home/dragos/Docker/Storage/this.cpp
#echo $path
cp $path main.cpp
docker build . -t cpp_test --progress=plain > build.txt 2>&1

if [[ $(cat build.txt | egrep -c "ERROR") -gt 0 ]]
then
	#echo eroare
	nrs=$(egrep -n "^\-\-\-\-\-\-$" build.txt | cut -f1 -d:)
	declare -i nr1=$(echo $nrs | cut -f1 -d " ")
	declare -i nr2=$(echo $nrs | cut -f2 -d " ")
	nr2=$nr2-$nr1+1
	tail -n +$nr1 build.txt | head -n +$nr2 > /home/dragos/Docker/time.txt
	cat /home/dragos/Docker/time.txt | cut -f3- -d" " | sed -r "s/^\[4\/4\] //g"  > /home/dragos/Docker/rezult.txt
	echo -n 0 > /home/dragos/Docker/error.txt
	exit
fi
( time docker run --rm -it cpp_test) > /home/dragos/Docker/rezult.txt 2> /home/dragos/Docker/time.txt
echo The program was executed in : +$(egrep -o "real.*" /home/dragos/Docker/time.txt | tr "\t" " " | cut -f2 -d " ")> /home/dragos/Docker/time.txt
if [[ $(cat /home/dragos/Docker/time.txt | egrep -c "m..,") -gt 0 ]]
then
	echo -n The program took too long to execute. > /home/dragos/Docker/rezult.txt
	echo -n 0 > /home/dragos/Docker/error.txt 
else
	cat /home/dragos/Docker/rezult.txt >> /home/dragos/Docker/time.txt
	cat /home/dragos/Docker/time.txt > /home/dragos/Docker/rezult.txt
	echo -n 1 > /home/dragos/Docker/error.txt
fi