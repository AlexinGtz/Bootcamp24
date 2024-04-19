#!/bin/bash

for contador in {1..5}
do
    echo $contador
done

var1=5
var2=5

if [ $var1 -le $var2 ]
then
    echo Las variables son iguales
else
    echo Las variables son diferentes
fi

# -eq igual
# -ne no igual
# -lt less than
# -gt greater than
# -le lower or equal
# -ge greater or equal

# -a and
# -o or

while getopts ":al:f:" opt; do
    case $opt in
        a)
            arg_a='todo'
        ;;
        l)
            arg_l='detalle'
            param_l=$OPTARG
        ;;
        f)
            arg_f='mando archivo'
            param_f=$OPTARG
        ;;
    esac
done

echo valor en L $param_l
echo El usuario quiere imprimir $arg_a y con $arg_l y $arg_f
echo El archivo que quiere accesar es es $param_f

while read line
do  
    mkdir pruebas/$line
done < $param_f


