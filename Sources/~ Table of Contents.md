```dataview
TABLE file.description AS "Description"
WHERE !contains(file.name, "+ ") AND !contains(file.name, "~ ") AND file.folder = this.file.folder
SORT file.name
```