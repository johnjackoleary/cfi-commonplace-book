<%*
const dv = app.plugins.plugins["dataview"].api;
const openPublishPanel = app.commands.commands["publish:view-changes"].callback;

const fileAndQuery = new Map([
  [
    "Recently edited",
    'TABLE WITHOUT ID file.link AS Note, dateformat(file.mtime, "ff") AS Modified FROM "50 Slipbox" OR "30 External" WHERE publish SORT file.mtime desc LIMIT 7',
  ],
  [
    "Recent new files",
    'TABLE WITHOUT ID file.link AS Note, dateformat(file.ctime, "DD") AS Added FROM "50 Slipbox" OR "30 External" WHERE publish SORT file.ctime desc LIMIT 7',
  ],
]);

await fileAndQuery.forEach(async (query, filename) => {

  const tFile = tp.file.find_tfile(filename);
  const queryOutput = await dv.queryMarkdown(query);

  // write query output to file
  await app.vault.modify(tFile, queryOutput.value);

});
%>