<%*
const dv = app.plugins.plugins["dataview"].api;
const openPublishPanel = app.commands.commands["publish:view-changes"].callback;
const exportCanvasToImage = app.commands.commands["canvas:export-as-image"].callback;

const fileAndQuery = new Map([
  [
    "+ Recently Updated",
    'LIST rows.file.link FROM "Filed" OR "Lesson Plans" WHERE !contains(file.name, "+ ") GROUP BY (file.mday) AS Modified SORT Modified DESC LIMIT 10',
  ],
  ["+ Acronyms", 'TABLE WITHOUT ID file.link AS "Acronyms: ", meaning AS "Meaning" FROM #acronym AND !"Templates" SORT file.link ASC'],
  ["+ Concepts", 'List FROM #concept AND "Filed" SORT file.name'],
  ["+ Glossary", 'TABLE WITHOUT ID file.link AS "", definition AS "Definition", source AS "Source" FROM #glossary AND !"Templates" SORT file.link'],
  ["+ Maneuvers", 'LIST FROM #maneuver AND !"Templates"'],
  ["+ Quotes", 'TABLE WITHOUT ID "[["+file.path+"|...]]" AS "", quote AS "Quote", author AS "Author" FROM #quote AND !"Templates" SORT file.mtime DESC'],
  ["+ Sources", 'TABLE WITHOUT ID file.link AS "Sources: ", choice(Description = [[Source Template]].Description, regexreplace(substring(Link, 1), "\].*", ""), Description) as "Description" FROM #source AND !"Templates" WHERE !contains(file.name, "+ ") AND !contains(file.name, "~ ") SORT regexreplace(file.name, "Ch(\d)$", "Ch0$1")'],
]);

await fileAndQuery.forEach(async (query, filename) => {
  if (!tp.file.find_tfile(filename)) {
    await tp.file.create_new("", filename);
    new Notice(`Created ${filename}.`);
  }
  const tFile = tp.file.find_tfile(filename);
  const queryOutput = await dv.queryMarkdown(query);
  const fileContent = `%% Update via "Update Publish Files" template %% \n\n${queryOutput.value}`;
  try {
    await app.vault.modify(tFile, fileContent);
    new Notice(`Updated ${tFile.basename}.`);
  } catch (error) {
    new Notice("⚠️ ERROR updating! Check console. Skipped file: " + filename + ": " + error, 0);
  }
});
openPublishPanel();
%>