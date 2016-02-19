---
title: linux comm command
layout: post
categories: [Bioinformatics]
tags: [Linux]
image: /figure2016
---
{% include JB/setup %}


```sh
echo -e "a\nb\nc\n" > 1.txt
```

```sh
echo -e "a\nc\nd\n" > 2.txt
```

Compare **sorted** files FILE1 and FILE2 line-by-line. With no options, comm produces three-column output. Column one contains lines unique to FILE1, column two contains lines unique to FILE2, and column three contains lines common to both files. Each of these columns can be suppressed individually with options.

```
-1     suppress column 1 (lines unique to FILE1)
-2     suppress column 2 (lines unique to FILE2)
-3     suppress column 3 (lines that appear in both files)
```

输出3列，第一列是1.txt特有的，第二列是2.txt特有的，第三列是共有的。   

```sh
comm 1.txt 2.txt
```

```
		a
b
		c

	d
```

只输出第三列，即两个文件的共同行。   

```sh
comm -12 1.txt 2.txt
```

```
a
c
```

只输出第二列，即第二个文件特有的行。   

```sh
comm -13 1.txt 2.txt
```

```
d
```

只输出第一列，即第一个文件特有的行。   

```sh
comm -23 1.txt 2.txt
```

```
b
```

只输出第二，三列    

```sh
comm -1 1.txt 2.txt
```

```
	a
	c
d
```

只输出第一，三列    

```sh
comm -2 1.txt 2.txt
```

```
	a
b
	c
```

只输出第一，二列    

```sh
comm -3 1.txt 2.txt
```

```
b

	d
```

