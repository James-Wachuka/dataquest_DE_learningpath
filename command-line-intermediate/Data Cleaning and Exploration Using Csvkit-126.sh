## 2. Csvstack ##

/home/dq$ head Combined_hud.csv

## 3. Csvlook ##

/home/dq$ csvgrep -c AGE1 -m -9 Combined_hud.csv | head -10 | csvlook

## 4. Csvcut ##

/home/dq$ head Combined_hud.csv

## 5. Csvstat ##

/home/dq$ csvstat --mean Combined_hud.csv

## 6. Csvcut | csvstat ##

/home/dq$ csvcut -c AGE1 Combined_hud.csv | csvstat

## 7. Csvgrep ##

/home/dq$ csvgrep -c AGE1 -m -9 Combined_hud.csv | head -11 | csvlook

## 8. Filtering out problematic rows ##

/home/dq$ csvgrep -c AGE1 -m -9 -i Combined_hud.csv > positive_ages_only.csv