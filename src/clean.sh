# src/clean.sh

# Remove pycache
rm -r **/__pycache__
rm -r **/**/__pycache__

# Remove log files
rm **/*.marks

# Remove tree files
rm **/*.tree
rm trees/*.png

# Remove zips

rm **.zip
