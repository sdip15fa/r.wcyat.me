git config --global user.name "actions-bot"
git config --global user.email "actions-bot@wcyat.me"
git add -A
git commit -a -m update
git pull origin master
git pull azure master
git push origin master
git push azure master