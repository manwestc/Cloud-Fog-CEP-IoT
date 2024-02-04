#! /bin/bash
#echo "$mhora"
alarmas=100

while [  $alarmas -lt 280 ]; do
./paso1.sh > aux2.txt &
suscriber=$!
echo "Loop $alarmas"
sleep 66
#./paso2.sh $alarmas paso0_5
python3 testgiotec.py $alarmas
kill $suscriber
let "alarmas += 25"
sleep 9
done

