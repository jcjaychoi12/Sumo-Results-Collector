# Sumo Results Collector
### _Collects the latest available results from the [Japan Sumo Association](https://www.sumo.or.jp) site_


**Links**
* [Banzuke](https://www.sumo.or.jp/ResultBanzuke/table/)


**Basho Date Calcuation**

Since the start of the 6 basho per year era (1958 and onwards), the starting date has been the 2nd Sunday of every odd-numbered months

```
Earliest start = 8th (1st Sunday is the 1st)

Latest start = 14th (1st Sunday is the 7th)
```

The basho is held for 15 days, and the start and end dates can be calculated
1st Sunday | Start | End
:-: | :-: | :-:
1 | 8 | 23
2 | 9 | 24
3 | 10 | 25
4 | 11 | 26
5 | 12 | 27
6 | 13 | 28
7 | 14 | 29

Another way to calculate is to see which day of the week is the 1st of the month 
1st of the month | Start | End
:-: | :-: | :-:
Sun | 8 | 23
Sat | 9 | 24
Fri | 10 | 25
Thu | 11 | 26
Wed | 12 | 27
Tue | 13 | 28
Mon | 14 | 29