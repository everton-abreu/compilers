# src/syntatic.sh

pasta="trees"

if [[ -d $pasta ]]
then
	TEST_PREFIX="syntatic/tests"
	for archive in $(ls $TEST_PREFIX)
	do
		python3 __syntatic__.py $TEST_PREFIX/$archive
		echo "------------------------------"
	done
	echo "se chegou aqui deve ter dado certo \o/"
else
	echo "Pasta '$pasta' não existe"
fi

