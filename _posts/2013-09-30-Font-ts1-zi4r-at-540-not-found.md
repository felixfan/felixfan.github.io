---
title: Font ts1-zi4r at 540 not found
layout: post
categories: [RStudy]
tags: [R, MiKTeX, LaTeX]
---
{% include JB/setup %}

When I use {devtools} to builds and checks a source package, I got the Error: Font ts1-zi4r at 540 not found.

OS: Win7
R: 3.0.2
RStudio: 0.98.309
MikTeX: 2.9

I solved this peoblem using the following method:

* Open a Command Prompt window. [How?](http://windows.microsoft.com/en-hk/windows-vista/open-a-command-prompt-window)

* type "initexmf --update-fndb" in the command window, this step may take several seconds

```
initexmf --update-fndb
```

* type "initexmf --edit-config-file updmap" in the command window, this command will open updmap.cfg in your default editor. Since I use notepad++, it was opened in notepad++.

```
initexmf --edit-config-file updmap
```

* add "Map zi4.map" to updmap.cfg (the opened file)

```
Map zi4.map
```

* save and close updmap.cfg

* type "initexmf --mkmaps" in the command window.

```
initexmf --mkmaps
```

It works now.       
Have fun!        

**Note**: You need to update R to **3.0.2** first. Or check this [post](http://r.789695.n4.nabble.com/inconsolata-sty-is-liable-to-disappear-texinfo-5-1-td4669976.html) to fix **"inconsolata.sty is not available"** problem first.            

[Reference](http://tex.stackexchange.com/questions/125274/error-font-ts1-zi4r-at-540-not-found)           

