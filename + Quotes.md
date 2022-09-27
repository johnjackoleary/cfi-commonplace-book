```dataview
TABLE WITHOUT ID "[["+file.path+"|...]]" AS "Link ", quote AS "Quote", author AS "Author" 
FROM #quote AND !"Templates"
SORT file.mtime DESC
```

