---
title: how to delete a tag of GitHub
layout: post
categories: [Bioinformatics]
tags: [GitHub]
image: /figure2016
---

{% include JB/setup %}

open up a terminal window and navigate to your local GitHub repository.

```
git tag -d tagName
git push origin :tagName
```

If your tag has the same name as one of your branches, use this instead:

```
git tag -d tagName
git push origin :refs/tags/tagName
```

You need to replace **tagName** with the tag name that you want to delete.
