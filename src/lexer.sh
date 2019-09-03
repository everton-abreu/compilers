if [[ -d logs ]]
then
	echo "existe"
fi

for file in $(ls lexer/tests)
do
	echo "------------------------------"
	echo "File: $file"
done
