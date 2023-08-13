## 1. Introduction to Remote Repositories ##

/home/dq$ git clone /dataquest/user/git/chatbot

## 2. Making Changes to Cloned Repositories ##

/home/dq/chatbot$ git commit -m "Updated README.md"

## 3. Overview of the Master Branch ##

/home/dq/chatbot$ git branch

## 4. Pushing Changes to the Remote ##

/home/dq/chatbot$ git push origin master

## 5. Viewing Individual Commits ##

/home/dq/chatbot$ git show ^C

## 6. Referring to the Most Recent Commit ##

/home/dq/chatbot$ git rev-parse HEAD~1

## 7. Commits and the Working Directory ##

/home/dq/chatbot$ git diff ^C

## 8. Switching to a Specific Commit ##

/home/dq/chatbot$ git reset --hard 2a8ef79bbdbb3e32b8ec2ecb1df42b20908c24c0

## 9. Pulling From a Remote Repo ##

/home/dq/chatbot$ git pull