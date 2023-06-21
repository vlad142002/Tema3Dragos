#!/bin/bash
path=/home/dragos/Docker/Storage/this.cpp
#echo $path
cp $path main.cpp
sudo docker build . -t cpp_test --progress=plain > build.txt 2>&1

if [[ $(cat build.txt | egrep -c "ERROR") -gt 0 ]]
then
	#echo eroare
	nrs=$(egrep -n "^\-\-\-\-\-\-$" build.txt | cut -f1 -d:)
	declare -i nr1=$(echo $nrs | cut -f1 -d " ")
	declare -i nr2=$(echo $nrs | cut -f2 -d " ")
	nr2=$nr2-$nr1+1
	tail -n +$nr1 build.txt | head -n +$nr2 > /home/dragos/Docker/rezult.txt
	exit
fi
sudo docker run --rm -it cpp_test > /home/dragos/Docker/rezult.txt