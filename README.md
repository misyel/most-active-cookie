# most-active-cookie
The program returns the most active cookie(s) for a given date.
### Usage
The program takes in two required flags (-d and -f): the date and the file name. The date should be formatted in YYYY-MM-DD and the file should either be the file path if it is in a seperate directory than the program or the file name if in the same directory. The file content in the file should be formatted as shown here:

```
cookie          ,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
```

Example Usage:
``` 
./most_active_cookie.py -d 2020-09-10 -f test.txt 
```
