---
title: python编程注意事项
layout: post
categories: [Python]
tags: [Python]
image: /figure2016
---

{% include JB/setup %}


# 1. 不要使用可变对象作为函数默认值

字典,集合,列表等等对象是不适合作为函数默认值的. 因为这个默认值实在函数建立的时候就生成了, 每次调用都是用了这个对象的”缓存”。

# 2. 在循环中修改列表项

```
b = [2, 4, 5, 6]

for i in b:
  if not i % 2:
    b.remove(i)

In: b
Out: [4, 5] # 本来我想要的结果应该是去除偶数的列表
# 是因为你对列表的remove,影响了它的index
# 因为2被删除后的列表是[4, 5, 6], 所以索引list[1]直接去找5, 忽略了4
```

# 3. IndexError – 列表取值超出了他的索引数

```
my_list = [1, 2, 3, 4, 5]

In: my_list[5] # 根本没有这个元素, IndexError

In: my_list[5:] # 但是可以这样,一定要注意, 用好了是trick,用错了就是坑啊
Out: []
```

# 4. 列表的+和+=, append和extend

```
>>> myList = [1,2,3,4]
>>> print myList
[1, 2, 3, 4]

>>> myList + [1]
[1, 2, 3, 4, 1]
>>> print myList
[1, 2, 3, 4]
### 不改变原列表

>>> myList += [1]
>>> print myList
[1, 2, 3, 4, 1]
### 在原有列表添加

>>> myList.append(2)
>>> print myList
[1, 2, 3, 4, 1, 2]
### 在原有列表添加

>>> myList.extend([9])
>>> print myList
[1, 2, 3, 4, 1, 2, 9]
### 在原有列表添加
```

# 5. '==' 和 is 的区别

'is'是判断2个对象的身份, '=='是判断2个对象的值.

```
# But, 有个特例
In: a = float('nan')

In: print('a is a,', a is a)
Out:('a is a,', True)

In: print('a == a,', a == a)
Out: ('a == a,', False) # 亮瞎我眼睛了
```

# 6. 浅拷贝和深拷贝

对于dict和list等数据结构的对象，直接赋值使用的是引用的方式。我们在实际开发中都可以向对某列表的对象做修改,但是可能不希望改动原来的列表。浅拷贝只拷贝父对象，深拷贝还会拷贝对象的内部的子对象。

```
In [65]: list1 = [1, 2]
In [66]: list2 = list1 # 就是个引用, 你操作list2,其实list1的结果也会变

In [67]: list3 = list1[:] # 浅拷贝

In [69]: import copy
In [70]: list4 = copy.copy(list1) # 浅拷贝, 对list3和list4操作都不会对list1有影响

In [71]: id(list1), id(list2), id(list3), id(list4)
Out[71]: (4480620232, 4480620232, 4479667880, 4494894720)


# 再看看深拷贝和浅拷贝的区别

In [88]: from copy import copy, deepcopy

In [89]: list1 = [[1], [2]]

In [90]: list2 = copy(list1) # 还是浅拷贝

In [91]: list3 = deepcopy(list1) # 深拷贝

In [92]: id(list1), id(list2), id(list3)
Out[92]: (4494896592, 4495349160, 4494896088)

In [93]: list2[0][0] = 3

In [94]: print('list1:', list1)
('list1:', [[3], [2]]) # 看到了吧 假如你操作其子对象 还是和引用一样 影响了源

In [95]: list3[0][0] = 5

In [96]: print('list1:', list1)
('list1:', [[3], [2]]) # 深拷贝就不会影响
```

# 7. bool其实是int的子类

```
In [97]: isinstance(True, int)
Out[97]: True

In [98]: True + True
Out[98]: 2

In [99]: 3 * True + True
Out[99]: 4

In [100]: 3 * True - False
Out[100]: 3
```

# 8. 元组是不是真的不可变?

```
In [111]: tup = ([],)
In [112]: tup[0] += [1]
---------------------------------------------------------------------------
TypeError Traceback (most recent call last)
<ipython-input-112-d4f292cf35de> in <module>()
----> 1 tup[0] += [1]

TypeError: 'tuple' object does not support item assignment

In [113]: tup
Out[113]: ([1],) # 明明抛了异常 还能修改?

In [114]: tup = ([],)
In [115]: tup[0].extend([1])
In [116]: tup[0]
Out[116]: [1] # 好吧,我有点看明白了, 虽然我不能直接操作元组，但是不能阻止我操作元组中可变的子对象(list)

In [117]: my_tup = (1,)
In [118]: my_tup += (4,)
In [119]: my_tup = my_tup + (5,)
In [120]: my_tup
Out[120]: (1, 4, 5) # ? 嗯 不是不能操作元组嘛?
```

# 9. 枚举

```
>>> myList=['a','b','c']
>>> for i, item in enumerate(myList):
...  print i, item
... 
0 a
1 b
2 c
```

```
>>> list(enumerate('abc')) 
[(0, 'a'), (1, 'b'), (2, 'c')]
>>> list(enumerate('abc', 1)) 
[(1, 'a'), (2, 'b'), (3, 'c')]
```

# 10. 列表/字典/集合 解析

```
>>> my_list = [i for i in xrange(3)]
>>> print my_list
[0, 1, 2]
```

```
>>> my_dict = {i: i * i for i in xrange(3)} 
>>> print my_dict
{0: 0, 1: 1, 2: 4}
```

```
my_set = {i * 15 for i in xrange(3)}
>>> print my_set
set([0, 30, 15])
```

# 11. 强制浮点除法

```
a = 3
b = 4
result = 1.0 * a / b
```

# 12. 简单服务器

快速方便的共享某个目录下的文件.

```
# Python2
python -m SimpleHTTPServer

# Python 3
python3 -m http.server
```

假设你的ip是147.8.103.234， 所有人可以通过`http://147.8.103.234:8000/` 访问你共享的文件夹。

# 13. if 结构简化

如果你需要检查几个数值你可以用以下方法：

```
if n in [1,4,5,6]:
```

来替代下面这个方式:

```
if n==1 or n==4 or n==5 or n==6:
```

# 14. 字符串/数列 逆序

```
>>> a = [1,2,3,4]
>>> a[::-1]
[4, 3, 2, 1]

# This creates a new reversed list. 
# If you want to reverse a list in place you can do:

a.reverse()
```

```
>>> a = 'hello world'
>>> a[::-1]
'dlrow olleh'
```

# 15. 三元运算

三元运算是if-else 语句的快捷操作，也被称为条件运算。

```
>>> x, y = 1, 2
>>> min = x if x < y else y
>>> max = x if x > y else y
>>> print min, max
1 2
```

# 16. 优化循环

循环之外能做的事不要放在循环内.

# 17. 优化包含多个判断表达式的顺序

对于and，应该把满足条件少的放在前面，对于or，把满足条件多的放在前面。

# 18. 使用join合并迭代器中的字符串

# 19. 不借助中间变量交换两个变量的值

```
a, b = b, a
```

# 20. 使用if is

使用 if is True 比 if == True 将近快一倍。

# 21. 使用级联比较x < y < z

x < y < z效率略高，而且可读性更好。

# 22. while 1 比 while True 更快

# 23. 使用**而不是pow

```
**就是快10倍以上！
```

# 24. 使用计数器对象计数

```
>>> from collections import Counter
>>> c = Counter("hello world")
>>> c
Counter({"l": 3, "o": 2, " ": 1, "e": 1, "d": 1, "h": 1, "r": 1, "w": 1})
>>> c.most_common(2)
[("l", 3), ("o", 2)]
```

# 25. 在Python 2中使用Python 3式的输出/除法

```
from __future__ import print_function
from __future__ import division
```



