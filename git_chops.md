

Create new github repo (repository) from local command line
''' bash
curl -u 'username' https://api.github.com/user/repos -d '{"name":"REPO"}'
'''








Add local git to existing github repo
''' bash
touch README.md
git init
git add .
git commit -m "message"
git remote add origin https://github.com/user/nameofgit.git
git push -u origin master
'''

License choice:
[github help page](https://help.github.com/en/articles/licensing-a-repository)

