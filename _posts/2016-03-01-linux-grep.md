---
title: linux grep 例子
layout: post
categories: [Bioinformatics]
tags: [Linux]
image: /figure2016
---
{% include JB/setup %}


```bash
echo "Hello World" > test.txt
echo "hello python" >> test.txt
echo "big apple" >> test.txt
echo "key1" >> test.txt 
echo "code99" >> test.txt 
```

### 区分大小写

```bash
grep "Hello" test.txt
```

```
Hello World
```

### 不区分大小写

```bash
grep -i "Hello" test.txt
```

```
Hello World
hello python
```

### 只显示以'h'开头的文本行

```bash
grep "^h" test.txt
```

```
hello python
```

### 检索以'e'结尾的文本格式

```bash
grep -i "e$" test.txt 
```

```
big apple
```

### 搜索空白行

```bash
grep '^$' test.txt
```

### 匹配 'Hello' 或 'hello'

```bash
grep "[Hh]ello" test.txt 
```

```
Hello World
hello python
```

### 匹配数字

```bash
grep "y[0-9]" test.txt 
```

```
key1
```

### 以匹配两位数

```bash
grep "e[0-9][0-9]" test.txt 
```

```
code99
```

### 匹配字母

```bash
grep '[A-Za-z]' test.txt
```

```
Hello World
hello python
big apple
key1
code99
```

### 显示所有包含 “p” 或 “y” 字母的文本行

```bash
grep '[py]'' test.txt
```

```
hello python
big apple
key1
```

### 匹配包含两个字母'p'的字符串结果

```bash
egrep "p{2}" test.txt 
```

```
big apple
```

### 检索文件内包含'p'和'pp'的字符串结果

```bash
egrep "p{1,2}" test.txt 
```

```
hello python
big apple
```

### 匹配至少含有3个字母'p'的结果

```bash
egrep "p{3,}" test.txt 
```

### 从文件读入多个匹配模式

```bash
echo "y1" > p.txt
echo "d$" >> p.txt
grep -f p.txt test.txt
```

```
Hello World
key1
```

![](/figure2016/grep_re.png)
