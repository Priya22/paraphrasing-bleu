#!/bin/bash

hyp="$1"
maximum=$2
ref="${3}"


if [ $# -lt 2 ]; then
    echo "Wrong number of arguments specified (expecting 2)"
    echo "Usage: $0 HYPOTHESIS REF1 [REF2 REF3...REFN]"
    exit
fi

head -n $maximum $hyp | sacrebleu -sl -b --width 5 -s exp $ref
