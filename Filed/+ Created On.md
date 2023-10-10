```dataview
LIST rows.file.link
WHERE !contains(file.name, "+ ") AND !contains(file.name, "~ ") AND file.folder = "Filed"
GROUP BY (file.cday) AS Date
SORT Date DESC
```
