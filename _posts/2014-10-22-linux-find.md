---
title: "find: search for files or directories hierarchy"
layout: post
categories: [Bioinformatics]
tags: [Linux]
image: /figure
---
{% include JB/setup %}

### Usage

```
find -path pattern -type [d|f]
```

### Find directories

Find all directories whose name start with "2" under current location.

```
find -path './2*' -type d
```

Find all directories whose name start with "2" under all directories that in current directories.

```
find -path './*/2*' -type d
```

### Find files

Change the '-type d' to '-type f'.


