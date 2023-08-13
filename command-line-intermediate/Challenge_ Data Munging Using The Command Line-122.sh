## 1. Data munging ##

/home/dq$ ls -l ~

## 2. Data exploration ##

/home/dq$ head -n 10 *.csv

## 3. Filtering ##

/home/dq$ tail -n +2 Hud_2005.csv >> combined_hud.csv

## 4. Consolidating datasets ##

/home/dq$ tail -n +2 Hud_2013.csv >> combined_hud.csv

## 5. Counting ##

/home/dq$ awk -F',' '$5 ~ /198[0-9]/ { count++ } END { print count }' combined_hud.csv