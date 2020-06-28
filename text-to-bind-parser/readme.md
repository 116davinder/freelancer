# text-to-bind-parser
It will parse input text file and output bind format.

Input format:
```
Add Record
Domain
xmail.neocode.com
Record
x A
IP Address
207.230.229.27
Add Record
Domain
xmail.neocode1.com
Record
x A
IP Address
207.230.229.28
Add Record
Domain
xmail.neocode2.com
Record
x A
IP Address
207.230.229.29
```


Output:
```
mail.neocode.com. 1 IN A 207.230.229.27
mail.neocode1.com. 1 IN A 207.230.229.28
mail.neocode2.com. 1 IN A 207.230.229.29
```
