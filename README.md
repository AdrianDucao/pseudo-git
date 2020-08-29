# pseudo-git
A proof of concept git like version control. Digging deep on how it works

### To do:
- [ ] initite using something like e.g. python3 pseudo.py -edit file.txt
- [ ] track changes by comparing checksums and saving every file whenever we do, e.g. python3 pseudo.py -save file.txt, on a local database, might use sql lite or database.c
- [ ] need to display a comprehensive history of every -save just like in the real git where you can view the previous commits and the changes done with the file. 

### commands
* ./pseudo.py -action save	: much like commit -a	
* ./pseudo.py -action edit	: much like when editing a file 
* ./pseudo.py -action history	: much like viewing commit history
