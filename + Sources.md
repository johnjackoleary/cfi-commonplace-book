```dataview
TABLE WITHOUT ID file.link AS "Sources: ", choice(Description = [[Source Template]].Description, regexreplace(substring(Link, 1), "\].*", ""), Description) as "Description"
FROM #source
WHERE !contains(file.name, "+ ") AND !contains(file.name, "~ ")
SORT regexreplace(file.name, "Ch(\d)$", "Ch0$1")
```