# src/semantic.sh

pasta="logs/symbols"

if [[ -d $pasta ]]
then
  TEST_PREFIX="semantic/tests"
  for archive in $(ls $TEST_PREFIX)
  do
    python3 __semantic__.py $TEST_PREFIX/$archive
    echo ""
    echo "File $archive"
    echo ""
  done
else
  echo "Pasta '$pasta' não existe"
fi

# python3 __semantic__.py semantic/tests/expressoes.tpp
