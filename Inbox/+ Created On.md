```dataview
LIST rows.file.link
WHERE !contains(file.name, "+ ") AND !contains(file.name, "~ ") AND file.folder = "Inbox"
GROUP BY (file.cday) AS Date
SORT Date DESC
```
