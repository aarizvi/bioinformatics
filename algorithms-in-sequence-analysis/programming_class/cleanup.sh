if [ -e 'sequence.txt' ]; then
	echo Your sequence.txt is in the right folder.
else
	echo I can\'t find your sequence.txt
	echo Repeat the previous steps
	exit -1
fi

value=$(cat sequence.txt)
if [ $value = "AATA" ]; then
	echo You edited the file correcly.
else
	echo You did not edit your sequence.txt
	echo Repeat the previous steps
	exit -1
fi

echo Cleaning up...
rm -rf exercise
rm -f sequence.txt
echo Well done.
