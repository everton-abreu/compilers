if [[ -d logs ]]
then
	echo "existe"
fi
TEST_PREFIX="lexer/tests"
for archive in $(ls $TEST_PREFIX)
do
	echo "------------------------------"
	echo $archive
	python3 __main__.py $TEST_PREFIX/$archive
done
