---
title: shell script one-liners
layout: post
categories: [Bioinformatics]
tags: [Bioinformatics,Linux]
image: /figure
---

### 1 awk

#### 1.1 Sum/average column 1 of file.txt

```   
awk '{sum+=$1} END {print sum}' file.txt
awk '{sum+=$1} END {print sum/NR}' file.txt
```

#### 1.2 Number each line in file.txt

```
sed = file.txt | sed 'N;s/\n/ /'
```

#### 1.3 Get unique entries in file based on column 2 (takes only the first instance)

```
awk '!arr[$2]++' file.txt
awk '!($2 in arr){print}{arr[$2]++}' file.txt
```

#### 1.4 Print each line where the 5th field is equal/not equal to abc123

```
awk '$5 == "abc123"' file.txt
awk '$5 != "abc123"' file.txt
```

#### 1.5 Print each line where the 1st field is between 1 and 22

```
awk '$1 >0 && $1 <23' file.txt
```

#### 1.6 Print first two lines where the 1st field is "yes" or the 2nd field is "yes"

```
awk '$1=="yes" || $2=="yes"{print $1,$2}' file.txt
```

#### 1.7 Print each line whose 7th field matches/does not match the regular expression

```
awk '$7  ~ /[a-f]/' file.txt
awk '$7  ~ /[1-4]/' file.txt
awk '$7  ~ /^[a-f]/' file.txt
awk '$7  !~ /[1-4]/' file.txt
awk '$7 ~/rs/' file.txt
awk '$7 !~/rs/' file.txt
```

### 2 sed

#### 2.1 Trim leading and/or trailing whitespace in file.txt

```
sed 's/^[ \t]*//' file.txt
sed 's/[ \t]*$//' file.txt
sed 's/^[ \t]*//;s/[ \t]*$//' file.txt
```

#### 2.2 Delete blank lines in file.txt

```
sed '/^$/d' file.txt
```

#### 2.3 Replace all occurances of "foo" with "bar" in file.txt

```
sed 's/foo/bar/g' file.txt

# only replace the first instance in each line
sed 's/foo/bar/' file.txt     
```

#### 2.4 Extract every 4th line starting at the second line 

```
## line 2, 6, 10, ...
sed -n '2~4p' file.txt
```

### 3 sort, uniq

#### 3.1 Count the number of unique lines in file.txt

```
sort file.txt | uniq | wc -l   
```

#### 3.2 Find number of lines shared by 2 files:

A $\cap$ B
```
sort file1 file2 | uniq -d
```

#### 3.3 Find number of unique lines in 2 files:

A $\cup$ B
```
sort file1 file2 | uniq
```

#### 3.4 Sort file by column

file: 1.txt   

```
1       2       3
2       2       4
1       1       1
3       4       1
3       1       2
10      2       9
```

**sort -k1,1 1.txt**   # sort by first column
```
1       1       1
1       2       3
10      2       9
2       2       4
3       1       2
3       4       1
```

**sort -k1,1 -n 1.txt**  # sort by first column, numeric sort
```
1       1       1
1       2       3
2       2       4
3       1       2
3       4       1
10      2       9
```

**sort -k1,1 -k3,3 -n 1.txt**  # then use the third column as a tie breaker
```
1       1       1
1       2       3
2       2       4
3       4       1
3       1       2
10      2       9
```

**sort -k1,1 -k3,3 -n -r 1.txt** # reverse the order
```
10      2       9
3       1       2
3       4       1
2       2       4
1       2       3
1       1       1
```

### 4 cut

#### 4.1 Find the most common strings in column 2

```
cut -f2 file.txt | sort | uniq -c | sort -k1nr | head
```

### 5 split

#### 5.1 Customize Split File Size using -b option

```
split -b2000000 test.txt        # 2Mb perl file
```

#### 5.2 Customize the Number of Split Chunks using -n option

```
split -n20 test.txt             # create 20 chunks of split files
```

#### 5.3 Customize Number of Lines using -l option

```
split -l5000 test.txt             # split files are created with 5000 lines
```

#### 5.4 Do not generate empty output files with -e option

```
split -n20 -e test.txt            
```

### 6 join

#### 6.1 Join two files by matching the first fields

```
join FILE1 FILE2
```

#### 6.2 Join two files by matching the first fields, ignore case using -i option

```
join -i FILE1 FILE2
```

#### 6.3  Also print unpairable lines from file FILENUM using -a option

where FILENUM is 1 or 2, corresponding to FILE1 or FILE2     
```
join -a1 FILE1 FILE2           ## also print unpairable lines from FILE1
```

#### 6.4 Print only unpaired lines using -v option

```
join -v FILE1 FILE2           ## only print unpaired lines
```

#### 6.5 Join based on different columns from both biles using -1 and -2 option

```
join -1 2 -2 1 FILE1 FILE2  
##join based on the second column of FILE1 and the first column of FILE2         
```

### 7 paste
paste is used to create columns of data with a user-specified delimiter.   

a.txt    
```
a
b
c
```

b.txt    
```
1
2
3
```

**paste a.txt b.txt**   
```
a       1
b       2
c       3
```

**paste b.txt a.txt**   
```
1       a
2       b
3       c
```

**paste -d ',' a.txt b.txt**   
```
a,1
b,2
c,3
```

### 8 cat

**cat a.txt b.txt**   
```
a
b
c
1
2
3
```

**cat b.txt a.txt**    
```
1
2
3
a
b
c
```

### 9 Conditionals

```
if [expression]
then
        code if 'expression' is true.
fi
```

```
if [expression]
then
        code if 'expression' is true.
else
       code if 'expression' is false.   
fi
```

```
x=1
if [ $x -le 5 ] # a space after "[" and before "]", respectively
then
        echo "x is less or equal to 5"
else
        echo "x is larger than 5"
fi
```
### 10 Loops

```
for i in {1..22} # bash version 3.0+
do
   echo "chromosome $i"
done
```

```
for i in {1..10..2}      #{START..END..INCREMENT} # bash v4.0+
do
   echo "chromosome $i"
done
```

```
for((c=1; c<=5; c++ )) # you need (()) but not ()
do
   echo "Welcome $c times"
done
```

```
x=1
while [ $x -le 5 ] # a space after "[" and before "]", respectively
do
  echo "Welcome $x times"
  x=$(( $x + 1 ))
done
```

### 11 shuf

#### 11.1 Pick 10 random lines from a file:

```
shuf file.txt | head -n 10
```

### 12 echo

#### 12.1 Print all possible 3mer DNA sequence combinations:

```
echo {A,C,T,G}{A,C,T,G}{A,C,T,G}
```

### References:

* <http://sed.sourceforge.net/sed1line.txt>
* <https://github.com/lh3/seqtk>
* <http://lh3lh3.users.sourceforge.net/biounix.shtml>
* <http://genomespot.blogspot.com/2013/08/a-selection-of-useful-bash-one-liners.html>
* <http://biowize.wordpress.com/2012/06/15/command-line-magic-for-your-gene-annotations/>
* <http://genomics-array.blogspot.com/2010/11/some-unixperl-oneliners-for.html>
* <http://gettinggeneticsdone.blogspot.com/2013/10/useful-linux-oneliners-for-bioinformatics.html#comments>
* <http://github.com/stephenturner/oneliners>
