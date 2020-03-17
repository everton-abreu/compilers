# src/lexer.sh

log_folder="logs"

if [[ -d $log_folder ]]
then
  test_folder="src/lexer/tests"
  for archive in $(ls $test_folder)
  do
    python3 src/__lexer__.py $test_folder/$archive
  done
else
  echo "Pasta '$log_folder' não existe"
fi
