## 1. Appending ##

/home/dq$ echo "Take one down, pass it around, 98 bottles of beer on the wall..." >> beer.t

## 2. Redirecting from a file ##

/home/dq$ sort -r beer.txt

## 3. The grep command ##

/home/dq$ grep "bottles of" beer.txt coffee.txt

## 4. Special characters ##

/home/dq$ grep "beer" beer?.txt

## 5. The star wildcard ##

/home/dq$ grep "beer" ~/path/to/home/directory/*.txt

## 6. Piping output ##

/home/dq$ python rand.py | grep "50"

## 7. Chaining commands ##

/home/dq$ echo "This is an additional line." >> beer.txt && cat beer.tx

## 8. Escaping characters ##

/home/dq$ echo '"' >> filename.txt