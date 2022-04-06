Title: A Program Manager's Approach to the Mechanical Side of the Hustle
Subtitle: how to use a daily sprint nested in a weekly sprint to focus on achieving your goals
Affiliate Line: As an Amazon Associate I earn from qualifying purchases. (maybe don't use this?)
Tags: #projectmanagement #learning #trello #obsidian #productrecommendation #tools


Takeaway: Nested sprints allow you to focus execution on top priority items.

Plausibly Useful Idea: Story points using Fibonicii sequence, and why that works well.

Area of Improvement: Multi-step writing process. (I'm testing out a timeline for blog posts -- if it works well, I'll likely write about it later! If it doesn't work well... We'll keep iterating)

### Affiliate Links
```
<a target="_blank" href="https://www.amazon.com/Guide-Project-Management-Knowledge-PMBOK-C2-AE-ebook-dp-B096KV7FXQ/dp/B096KV7FXQ/ref=mt_other?_encoding=UTF8&amp;me=&amp;qid=1649201975&_encoding=UTF8&tag=cfijack-20&linkCode=ur2&linkId=2e188a0a3417f874082d43c3117da95a&camp=1789&creative=9325">PMBOK</a>
```

### Outline
* Background on sprints and agile development
* Idea behind Nested Sprints
	* Include image here
* Use in practice
	* Story point sizes
	* Velocity of progress
	* Story point limits per day and per week
	* Contrasting with main use cases for Agile
		* No need to be able to estimate when things will be done, however can sanity check from velocity vs. list of all work remaining
	* Inbox for unplanned tasks
* Tools for this
	* Obsidian
	* Trello



### First Draft
Project management is a favorite topic for me. So much so that my friends and I formed a Discord community to bounce ideas off one another and see which approaches from our different industries can be useful to each other.

It's different in a blog than a discussion (although feel free to comment with your thoughts or experience!), but I hope this idea is useful in your projects.

While an Engineering Program Manager at Apple, I was pursuing two personal projects when I had a couple minutes free.(("fill the unforgiving minute" was my profile status)) The first was an overhaul in meeting structure and expectations, largely based on experimenting with ideas from \<maybe link book\>. This is a fun topic, but better for a future blog post.

The second was an attempt to use project management techniques to improve management of my own time and priorities. This was largely based off experimenting with Scrum and XP ideas.((There are many good posts written about these. If you're interested, consider checking out \<links\>)) I've found a system that works well for organizing/executing my tasks while working towards my flight instructor certificate. I hope you'll find it useful as well, or perhaps would like to pull some of the ideas.

#### System Overview
\<add image of flow, maybe from Trello\>

#### System Goals
Keep tasks for an individual organized in a way they can be prioritized and rough timelines established.

In other words, this is a system for one individual to execute a hobby project or work through coursework.

It is meant to ensure no tasks are accidentally dropped, and to allow you to focus on the most important subset each week/day without getting overwhelmed with the backlog.

* Keep it Simple(([KISS)](https://en.wikipedia.org/wiki/KISS_principle), a phrase "coined by Kelly Johnson, lead engineer at the Lockheed Skunk Works (creators of the Lockheed U-2 and SR-71 Blackbird spy planes)")): This should solve the problem. We don't want to accidentally end up with another JIRA.

#### Tools Used
* Board + Cards: I used [Trello](), although you could do post-its on a wall like the good ol' days, if you'd like.
* Record of tasks completed each day and each week: I used [Obsidian](), because that is where my other notes already reside. You could jot this anywhere, or use a tool for Trello like [Trello tool think (correlo I think?)]()

#### Board Structure
* Can I add a template link?

#### Terms
Cards: 
Boards:
Story Points: define ((To choose story point values, don't worry about it too much. a 1 should be a trivial task (whatever the smallest task is for your domain), and everything from there is relative))

#### Workflow
* As a new task is apparent:
	* CFI mentions a piece of information you weren't aware of, and you should read up more on it? Add a quick card to the "Weekly Backlog".
* Every (working) day: 
	* Record the story points for each column. This becomes a record of how many story points you can complete in a day and in a week.
	* Move all "Daily Done" cards to "Weekly Done".
	* Estimate story points for any cards in "Weekly Backlog".
	* Pull in your "Daily Sprint" cards based on the story point limit you have for the day.
		* The goal is to focus on priorities -- it's fine to pull more tasks in after you complete the existing Sprint work, but if you're constantly avoiding a task, either it's not a priority or it really does need the focus!
		* (if it's your first week, just pick a random budget)
* Start of the week:
	* After doing the everyday tasks...
		* Archive all  "Weekly Done"
		* Move all uncompleted tasks to their proper backlogs, roughly prioritized. (Note: This is also when you organize out the random tasks that popped up through the week, but which you aren't going to do for a while.)
			* Or don't. Sure, I'll keep a task in "Weekly Backlog" if it needs to be done this week. Just don't get in the habit of having a task sitting in the backlog week after week.
		* Your board should be clear now
		* Review the number of story points you were able to complete over however many weeks you have data (if it's your first week, just pick a random budget)
		* Pull in your "Weekly Backlog" cards from whichever backlogs you're currently prioritizing based on the story point budget for the week (maybe 80% of the budeet to allow for unexpected work)
			* I call this "Weekly Backlog" since it's not really a sprint. I've heard it called a (i think?) working area or somethign before, which is a fair description. just cutting down distractions
			* Give story points to any tickets missing them
	* And you're set for the week! Now just execute!
	* ((Sprint goals are a good idea, but...))
	* ((I use several prioritized backlogs, for instance "Instrument Rating Backlog" or "Blog Backlog". That way I can have a project roughly prioritized for when I want to pick it up, but . You can also have an "On Ice" backlog, which is a way of not loosing the idea, but also putting it in the freezer so you don't have to look at it all the time.))
	* Periodically review you're backlogs to keep them roughly prioritized, and move anything truly not going to happen to "On Ice"

If you decide to give it a try, I'd love to know what works and doesn't work for you!

Any in any case, for this post's plausibly useful idea: Story points are traditionally done in a Fibonacci sequence (or ascending prime numbers, but we won't go there). This solves two problems: human's are bad at absolute estimates, but great at relative estimates. And golden ratio increases in size are generally perceived as "notably bigger" (find article or something for this). So if a task is worth 5 points vs. 6 points, it's hard to say they're all that much different. But if a task is 5 points vs. 8 points, that's a relative step up. So we use 1,2,3,5,8,13,etc.