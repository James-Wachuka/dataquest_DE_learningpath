## 2. The * Wildcard ##

/home/dq/brats$ ls v*

## 3. The ? Wildcard ##

/home/dq/brats$ ls ????

## 4. Escaping Characters ##

/home/dq/brats$ ls "a*" "t?"

## 5. The Wildcard [] ##

/home/dq/brats$ ls *[!aeiou]

## 6. Other Wildcards ##

/home/dq/brats$ ls *[[:alnum:]]

## 7. Summary and Practice ##

/home/dq/practice/wildcards$ mv *.csv data/

## 8. Searching for Files ##

/home/dq/practice/wildcards$ find / -type f -name "*.b64" -exec mv {} /home/dq \;