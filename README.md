Most of the projects that we work on in corporate life is code that someone else wrote. Not only did someone else write it and start that project, for the grand majority of it, dozens of people (or more!) have touched the same code. MIT (and some of our partners here at Kenzie) identified the ability to work on someone else's code as one of the most important skills a new developer can have. After all, it's not necessary to always reinvent the wheel just because you don't like how the guy three hires ago wrote his classes!
 

What we're going to do is switch codebases for the Recipebox. You are responsible for drafting these new features and extending the codebase that you're given, but the catch is that you cannot refactor the existing application. You can do minor cleanup (in the same function that you touch, for example), but you cannot change any of the existing core ways that the application works. As an additional burden (though I'm not sure how much of a burden this will be), you cannot ask the person whose codebase you received any questions about it. This is an analogue for receiving a codebase that was written by someone who has since left the company; you have to figure it out on your own. (And with me. You're more than welcome, as always, to ask me stuff.)
 

Before You Begin
Once you get assigned a repo, be sure to fork it. You may need to add a new remote to your forked repo (https://help.github.com/en/github/using-git/adding-a-remote (Links to an external site.)Links to an external site.).  If you run the following command and get something similar, you'll definitely want to add a new remote that is pointing to your forked repo (not the creator's):

>> git remote -v
origin https://github.com/<creator's_github_username>/recipebox/ (fetch)
origin https://github.com/<creator's_github_username>/recipebox/ (push)
Why are we forking? Because it allows us to make a Pull Request on the original repo.

 

Your Task
The project manager has returned to you with a heavy sigh and a long face. "They want to add the ability to edit recipes and have a favorites collection." Here's how that breaks down:
  Edit Recipes

  • create a form for editing existing recipes that pre-populates with the information of the model being updated
  • the logged in user can edit their recipes
  • the admin user can edit all recipes
  Favorite Recipes
  • every user has a collection of favorite recipes
  • links to favorites viewable from author detail page
  • all recipes have a favorite button on them; after all, you might want to favorite your own amazing cookies
  • favorite button is visible only if logged in
  Misc
  • cannot ask questions about code base from creator
  • cannot break site, cannot widely refactor
  • can clean up code blocks touched
Recipebox Repo Assignments:
https://gist.github.com/itsthejoker/a949f21c436ba5811789dfd89035839a
Submission
Please submit a link to the Pull Request (PR) you create.

For example:

https://github.com/<creator's_github_username>/recipebox/pull/1
