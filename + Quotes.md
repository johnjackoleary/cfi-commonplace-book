```dataview
TABLE WITHOUT ID file.link AS Link, file.date AS Date, quote AS "Quote", author AS "Author" 
FROM #quote AND !"Templates"
SORT file.date
```

