# src/clean.sh

# Remove pycache
rm -r **/__pycache__
rm -r **/**/__pycache__

# Remove log files
rm logs/marks/*.marks
rm logs/{trees,symbols}/*.png

# Remove zips

rm **.zip
