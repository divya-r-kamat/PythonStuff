Steps to create a GIT REPOSITORY and push/commit changes to repository

#Initialize empty git repository using - git init - command
#This creates .git directory


#Next, use - git add <file_name> - to make git notice the file
#Commit using - git commit -m "<comment>" <file_name>
#Connect to GitHub from local Repository with below commends
# git remote add origin https://github.com/divya-r-kamat/PythonStuff.git

# Check remote repositories
git remote -v

#Push the files to repository using
git push origin master

<<<<<<< HEAD
Tutorial Link for reference : https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners
=======

#Switch to new branch
git checkout EDA

#Command to check the files to be added
git status

#COmmand to add file
git add "filename"

#Command to commit the file to repository
git commit -m "comment" <file_name>

#Command to pust to new branch
git push origin EDA
>>>>>>> EDA
