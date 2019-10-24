# src/lexer.sh

pasta="logs"

if [[ -d $pasta ]]
then
	TEST_PREFIX="lexer/tests"
	for archive in $(ls $TEST_PREFIX)
	do
		python3 __lexer__.py $TEST_PREFIX/$archive
	done
else
	echo "Pasta '$pasta' não existe"
fi
