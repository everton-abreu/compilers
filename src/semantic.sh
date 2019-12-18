# src/semantic.sh

pasta="logs/symbols"

if [[ -d $pasta ]]
then
  TEST_PREFIX="semantic/tests"
  arquivo="$TEST_PREFIX/sema-003.tpp"
  for archive in $(ls $TEST_PREFIX)
  do
    # python3 __semantic__.py $TEST_PREFIX/$archive
    # echo ""
    # echo "File $TEST_PREFIX/$archive"
    # echo ""
    python3 __semantic__.py $arquivo
    echo ""
    echo "File $arquivo"
    exit
  done
else
  echo "Pasta '$pasta' não existe"
fi

# python3 __semantic__.py semantic/tests/expressoes.tpp
