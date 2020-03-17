# src/clean.sh

# Remove pycache
rm -r **/__pycache__
rm -r **/**/__pycache__

# # Remove parser files
# rm syntatic/parse{r.out,tab.py}

# Remove log files
rm logs/marks/*.marks
# rm logs/{trees,symbols}/*.png

# Remove zips

rm **.zip
