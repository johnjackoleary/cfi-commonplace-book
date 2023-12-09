# CFI Commonplace Book
## Viewing Project Files
There are two main options to view project files:
 1. [*Easiest*] Use the [published online view](https://publish.obsidian.md/cfi-commonplace-book/)
 2. [*Most Complete*] Download [Obsidian](https://obsidian.md/), then clone and open this repository

---

## Suggesting Changes
If you'd like to help improve this content, feel free to dive in anywhere! The GitHub is publicly visible at https://github.com/johnjackoleary/cfi-commonplace-book

If you want a starting point, any notes tagged with #todo are good candidates for some love. Check out [[Todo]] for a complete list.

And thank you!

### Make a Note of an Issue Without Making the Change
You can [submit issues on GitHub](https://github.com/johnjackoleary/cfi-commonplace-book/issues), and they'll show up similar to [this example](https://github.com/johnjackoleary/cfi-commonplace-book/issues/10).

Suggestions can be big or small, any observations or input are helpful!

### Editing Project Files
#### If You Haven't Used Git Before
##### Editing On Your Computer
1. Install [GitHub Desktop](https://desktop.github.com)
2. Clone the repository wherever GitHub desktop suggests
3. Open the top level folder with [Obsidian](https://obsidian.md/)

##### Editing Directly Online
1. Click on the file you'd like to edit in GitHub, and click the edit (pencil) button.
2. Next, 'propose' your changes. Feel free to change the message and description to explain the change and update the branch name. Or don't change anything, that's also fine :)
3. Finally, open a 'pull request' to show that the changes are ready to be reviewed and merged. You can see an example of this [here](https://github.com/johnjackoleary/cfi-commonplace-book/pull/9).

#### If You Have Used Git Before
There's a few branch protections in place and specific merge strategies. Generally, you should be good to go however you prefer to approach it.

---

## Project Details
### Structure
- Files starting with "~ " are meant to show up on top of the list, likely they are MOCs or overviews. 
- Files starting with "+ " are aggregator files, which have no custom content but pull information about the files using Dataview or the template in [[Update Publish Files]].
- Directories:
	- Filed: Published information. Should be clean enough to be useful, with *todo* tags indicated in any areas yet to tackle.
	- Lesson Plans: Ways of teaching key concepts. Should pull mostly from cards in Filed.
	- Media: **Small** images to help build out important filed information.

### Formating
- Tags
	- with multiple words should use a hyphen ('my-awesome-tag')
	- currently there are no nested tags ('my/awesome-tag'), although Obsidian has nice support for these, so may be a consideration later
- #todo:: standardize when to use which headings levels, maybe. Or just live with it? Variety is the spice of life...
- Blocks of Learning Sizes #todo :: Helpful info, seems not worth having on top readme though
	- 400px x 400px for cards
	- somethingx440px for labels
	- 80px between rows
	- 160 between columns
	- 20 between side edge of groups, 40 between top edge of groups

### Obsidian Plug-ins Used
All plugins are meant to be optional, although Dataview is heavily used.
- [Dataview](https://github.com/blacksmithgu/obsidian-dataview) is used heavily for aggregating files and reformatting raw data. Most unusual symbols in the Markdown, especially in files like Gait Charts (e.g. [[C152 Gait]]), are for Dataview.
	- #todo :: This is difficult for publishing, because Dataview doesn't work with publish. May need to pivot further away from Dataview, for now the publishing process includes generating some Dataview tables from queries in [[Update Publish Files]].
- [Advanced Tables](https://github.com/tgrosinger/advanced-tables-obsidian) is for convenience in editing tables. This is totally optional but very helpful.
- [Git](https://github.com/denolehov/obsidian-git) for easy vault backups. 
- [Text Format](https://github.com/Benature/obsidian-text-format) convenience for formatting with keyboard shortcuts.
- [Templater](https://silentvoid13.github.io/Templater/) for Obsidian Publish to work with Dataview (see article [here](https://joschua.io/posts/2023/09/01/obsidian-publish-dataview/))
- (Disabled) [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) for creating flashcards to study. This was useful for checkride prep, and could be revisited. Only disabled because it was no longer used.

---

## About The Contributors
| Contributor    | Blurb                                                              | URL                                                              |
| -------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------- |
| Edward Abraham | Bay Area native and flight instructor with emphasis on ADM and SRM | [LinkedIn](https://www.linkedin.com/in/edward-abraham-1ba117129) |
| Jack O'Leary   | Bay Area flight instructor with a passion for learning             | [cfijack.com](https://www.cfijack.com)                           |

---

## License
<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">CFI Commonplace Book</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

> [!important] 
> In particular, note these excepts from *[Section 5 – Disclaimer of Warranties and Limitation of Liability.](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en#s5)*
> 1. ...the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation... fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable....
> 2. To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages....