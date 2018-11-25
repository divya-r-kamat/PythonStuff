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
