```dataview
TABLE WITHOUT ID file.link AS "Sources: ", choice(Description = [[Source Template]].Description, Link, Description) as "Description"
WHERE !contains(file.name, "+ ") AND !contains(file.name, "~ ") AND file.folder = this.file.folder
SORT file.name
```