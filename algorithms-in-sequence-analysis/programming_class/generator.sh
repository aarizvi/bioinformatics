i=0
while [ $i -lt 500 ]
do
	i=$[$i+1]
	if [ $i -eq 151 ]; then
		echo 'AATG' > exercise/file_$i.seq
	else
		echo 'AAAA' > exercise/file_$i.seq
	fi
done
