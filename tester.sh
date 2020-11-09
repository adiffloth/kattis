#!/bin/bash
prob_id=$1
py_file=$prob_id/$prob_id.py
for in_file in $prob_id/*.in
    do 
        output=`python $py_file < $in_file`
        ans_file=${in_file%.*}.ans
        ans=`cat $ans_file`
        if [ "$output" = "$ans" ]
        then
            echo Pass
        else
            echo Fail
        fi
done