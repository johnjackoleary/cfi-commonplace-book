// Based on https://joschua.io/posts/2023/09/01/obsidian-publish-dataview/// Based on https://joschua.io/posts/2023/09/01/obsidian-publish-dataview/



<%*
const dv = app.plugins.plugins["dataview"].api;
const openPublishPanel = app.commands.commands["publish:view-changes"].callback;

const fileAndQuery = new Map([
  [
    "Filed/+ Created On",
    'LIST rows.file.link WHERE !contains(file.name, "+ ") AND !contains(file.name, "~ ") AND file.folder = "Filed" GROUP BY (file.cday) AS Date SORT Date DESC',
  ],
  ["+ Acronyms", 'TABLE WITHOUT ID file.link AS "Acronyms: ", meaning AS "Meaning" FROM #acronym AND !"Templates" SORT file.link ASC'],
  ["+ Glossary", 'TABLE WITHOUT ID file.link AS "", definition AS "Definition", source AS "Source" FROM #glossary AND !"Templates" SORT file.link'],
  ["+ Maneuvers", 'LIST FROM #maneuver AND !"Templates"']
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