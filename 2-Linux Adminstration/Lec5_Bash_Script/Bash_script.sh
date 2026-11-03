#!/bin/bash

longname="/tmp/longname.txt"
touch longname

if [ $# -eq 0 ]; then
    echo "No arguments provided. Please provide options."
    exit 1
fi


while getopts ":a:b:c:" opt; do
  case $opt in
    a)
      echo "Option -a triggered with argument: $OPTARG"
      echo "Argument: $OPTARG" >> $longname
      ;;
    b)
      echo "Option -b triggered with argument: $OPTARG"
      echo "Argument: $OPTARG" >> $longname
      ;;
    c)
      echo "Option -c triggered with argument: $OPTARG"
      echo "Argument: $OPTARG" >> $longname
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;  
  esac
done

function print(){
  echo Hello $1
  return 5
}

msg=$(print Embinux)
echo $msg

for x in {1..6};do 
  echo "Looping ... number $x"
done
for ((i=0; i<5; i++)); do
  echo "C-style loop iteration $i"
done

cat test.txt | while read line; do
  echo "Read line: $line"
done 

fruits=("apple" "banana" "cherry")

echo ${fruits[@]}
echo ${!fruits[@]}

echo "First fruit: ${fruits[0]}"
