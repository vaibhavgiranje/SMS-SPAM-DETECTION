Your GitHub repository is created successfully, but only the README.md file got uploaded because the other project files were not added/committed before pushing.

Do these steps in VS Code terminal:

git status

This will show all untracked files.

Now add all project files:

git add .

Then commit them:

git commit -m "Added all project files"

Now push again:

git push origin main

After this, refresh your GitHub repository page and all files should appear.

Your full workflow should look like this:

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin YOUR_GITHUB_LINK
git push -u origin main

From your screenshot, you only added:

git add README.md

So only the README file was uploaded.

Also check:

Your project files are inside the SMS-Spam-Detection folder

You are running commands in the correct folder


You can verify by running:

dir

or

ls

If files are visible there, then git add . will upload everything.
