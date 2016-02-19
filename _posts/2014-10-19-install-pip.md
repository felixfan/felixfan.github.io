---
title: using pip on windows 7
layout: post
categories: [Python]
tags: [Python]
image: /figure
---
{% include JB/setup %}

Starting from version Python 3.4, pip is already included in the regular install, it is under the **Scripts** directory. so what you need to do is just add it (e.g., C:\\Python34\\Scripts) your system's PATH environment variable.

If pip is not installed, you can add the **Scripts** directory to your system's PATH environment variable. Then use the **easy_install** to install pip.

```
easy_install pip
```

Just type **pip** to see the help information.

```
pip
```

Install package using the following command:

```
pip install pkgName
```

e.g.,

```
pip install matplotlib
```

