#!/bin/bash

WORDS="harry,gryffindor,chair,wand,good,enter,on,school"
DATA="data"
RESULTS="results.txt"

> $RESULTS  

echo "======================================" | tee -a $RESULTS
echo "DIMENSIONALITY EXPERIMENTS" | tee -a $RESULTS
echo "======================================" | tee -a $RESULTS

for DIM in 10 50 100 1000; do
    for PCT in 5 10 20 50; do
        NZ=$(( DIM * PCT / 100 ))
        if [ $NZ -lt 1 ]; then NZ=1; fi

        OUTPUT="vectors_d${DIM}_nz${PCT}.txt"

        echo "" | tee -a $RESULTS
        echo "--- dim=$DIM nz=$NZ ($PCT%) ---" | tee -a $RESULTS

        python random_indexing.py -f $DATA -o $OUTPUT -d $DIM -nz $NZ -n
        python VectorTester.py -f $OUTPUT -w $WORDS | tee -a $RESULTS
    done
done

echo "" | tee -a $RESULTS
echo "======================================" | tee -a $RESULTS
echo "WINDOW SIZE EXPERIMENTS" | tee -a $RESULTS
echo "======================================" | tee -a $RESULTS

# Symmetric windows
for W in 0 3 10; do
    OUTPUT="vectors_w${W}_${W}.txt"

    echo "" | tee -a $RESULTS
    echo "--- window left=$W right=$W (symmetric) ---" | tee -a $RESULTS

    python random_indexing.py -f $DATA -o $OUTPUT -lws $W -rws $W -n
    python VectorTester.py -f $OUTPUT -w $WORDS | tee -a $RESULTS
done

# Asymmetric windows
for LW in 1 2 5; do
    for RW in 3 5 10; do
        if [ $LW -ne $RW ]; then
            OUTPUT="vectors_w${LW}_${RW}.txt"

            echo "" | tee -a $RESULTS
            echo "--- window left=$LW right=$RW (asymmetric) ---" | tee -a $RESULTS

            python random_indexing.py -f $DATA -o $OUTPUT -lws $LW -rws $RW -n
            python VectorTester.py -f $OUTPUT -w $WORDS | tee -a $RESULTS
        fi
    done
done

echo "" | tee -a $RESULTS
echo "======================================" | tee -a $RESULTS
echo "ALL EXPERIMENTS DONE" | tee -a $RESULTS
echo "Results saved in $RESULTS" | tee -a $RESULTS