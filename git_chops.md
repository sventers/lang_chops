

Create new github repo (repository) from local command line

    curl -u 'username' https://api.github.com/user/repos -d '{"name":"REPO"}'


other

    git merge dev --allow-unrelated-histories





Add local git to existing github repo

    touch README.md
    git init
    git add .
    git commit -m "message"
    git remote add origin https://github.com/user/nameofgit.git
    git pull <remote> master:dev
    git push -u origin master


License choice:
[github help page](https://help.github.com/en/articles/licensing-a-repository)

