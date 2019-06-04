# Markdown Chops

* [source cheatsheat](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf) </br>
* [github api](https://developer.github.com/v3/markdown/) </br>
* [mkdocs proj documentation](https://github.com/mkdocs/mkdocs)

#### Images, Pictures, jpeg, svg, png
```
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
```

#### Preview, local, write, test, lazy reload, auto-reload
[grip github link] (https://github.com/joeyespo/grip) \
pip install --user grip
```bash
grip FILENAME.md
#defaults to README.md in current directory
```

#### line breaks, bold, italic, color, font size, font type,
```
</br> or \  line breaks
# h1 (with space after #)
## h2 
###### h6 
```


#### List, index, items, ordered, bullets, points, numbers
* list
* ex
    * indent with tab
        * extra indent

- [x] x it dawg
- [ ] item up next
- [x] @mentions, #refs, [links](),
**formatting**, and <del>tags</del>
supported
    - [ ] list syntax required (any
unordered or ordered

```
* list
* above
    * indent with tab

- [x] this is a complete item
- [ ] this is an incomplete item
- [x] @mentions, #refs, [links](),
**formatting**, and <del>tags</del>
supported
- [x] list syntax required (any
unordered or ordered
```


#### Links
```
http://github.com - automatic!
[GitHub](http://github.com)
```

#### Codeblocks
```
```python3
def iluv (you):
    who = you
    besties = you
    return besties
```.
(start three backticks and language ex -> ```bash)
(end ``` and no mas, without . from 2 lines above)
```



#### GitHub supports emoji!
:+1: :sparkles: :camel: :tada: \
:rocket: :metal: :octocat:
```
:+1: :sparkles: :camel: :tada:
:rocket: :metal: :octocat:
```



Write!