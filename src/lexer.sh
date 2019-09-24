if [[ -d logs ]]
then
	echo "existe"
fi
TEST_PREFIX="lexer/tests"
for arc in $(ls $TEST_PREFIX)
do
	echo "------------------------------"
	echo $arc
	python3 __main__.py $TEST_PREFIX/$arc >> logs/"$arc".marks
done
