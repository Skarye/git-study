#! /bin/bash
#echo "True"
#echo "False"
#if [[ x"$1" != x"manual" && x"$1" != x"preinstall" ]];then
base_name=$(dirname $0)
echo $base_name
echo $#
echo $*
echo $@

echo "-- \$* 演示 ---"
for i in "$*"; do
	echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
	echo $i
done

if [[ x"$1" != x"manual" && x"$1" != x"preinstall" ]];then
	echo "True"
else 
	echo "False"
fi
