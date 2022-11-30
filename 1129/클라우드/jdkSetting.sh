#!/bin/bash

x=`rpm -qa|grep java-1.8.0-openjdk-devel`
if [ ${#x} -eq 0 ];then 
	sudo yum -y install java-1.8.0-openjdk-devel
fi


x=`cat ~/.bashrc |grep JAVA_HOME`
# Description
if [ ${#x} -eq 0 ]; then
	  a=`which java`
        x=`readlink -f $a`
        y=`echo $x | awk '{print $NF}'`
        z=`echo ${y/\/jre\/bin\/java/}`
        echo 'export JAVA_HOME='$z >> ~/.bashrc
fi

