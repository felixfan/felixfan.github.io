---
title: R reading data from Excel, XML and Json
layout: post
categories: [RStudy]
tags: [R]
image: /figure
---

what I have learned from coursera course [Getting and Cleaning Data](https://class.coursera.org/getdata-002).   

### Reading Excel Files

#### read.xlsx {xlsx}


```r
library(xlsx)
mydata = read.xlsx("data.xlsx", sheetIndex = 1, header = TRUE)
```


#### Reading specific rows and columns


```r
mydata = read.xlsx("data.xlsx", sheetIndex = 1, header = TRUE, colIndex = 2:3, 
    rowIndex = 1:4)
```


### Reading XML


```r
library(XML)
fileUrl <- "http://wwww.w3schools.com/xml/simple.xml"
doc <- xmlTreeParse(fileUrl, useInternal = TRUE)
rootNode <- xmlRoot(doc)
xmlName(rootNode)
```

```
[1] "breakfast_menu"
```

```r
names(rootNode)
```

```
  food   food   food   food   food 
"food" "food" "food" "food" "food" 
```


#### Directly access parts of the XML document


```r
rootNode[[1]]
```

```
<food>
  <name>Belgian Waffles</name>
  <price>$5.95</price>
  <description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
  <calories>650</calories>
</food> 
```

```r
rootNode[[1]][[1]]
```

```
<name>Belgian Waffles</name> 
```


#### Programatically extract parts of the file


```r
xmlSApply(rootNode, xmlValue)
```

```
                                                                                                                    food 
                              "Belgian Waffles$5.95Two of our famous Belgian Waffles with plenty of real maple syrup650" 
                                                                                                                    food 
                   "Strawberry Belgian Waffles$7.95Light Belgian waffles covered with strawberries and whipped cream900" 
                                                                                                                    food 
"Berry-Berry Belgian Waffles$8.95Light Belgian waffles covered with an assortment of fresh berries and whipped cream900" 
                                                                                                                    food 
                                               "French Toast$4.50Thick slices made from our homemade sourdough bread600" 
                                                                                                                    food 
                        "Homestyle Breakfast$6.95Two eggs, bacon or sausage, toast, and our ever-popular hash browns950" 
```


#### Get the names and prices on the menu


```r
xpathSApply(rootNode, "//name", xmlValue)
```

```
[1] "Belgian Waffles"             "Strawberry Belgian Waffles" 
[3] "Berry-Berry Belgian Waffles" "French Toast"               
[5] "Homestyle Breakfast"        
```

```r
xpathSApply(rootNode, "//price", xmlValue)
```

```
[1] "$5.95" "$7.95" "$8.95" "$4.50" "$6.95"
```


#### Extract content by attributes

Use htmlTreeParse when the content is known to be (potentially malformed) HTML.   


```r
fileUrl = "http://espn.go.com/nfl/team/_/name/bal/baltimore-ravens"
doc <- htmlTreeParse(fileUrl, useInternal = TRUE)
scores <- xpathSApply(doc, "//li[@class='score']", xmlValue)
scores
```

```
 [1] "49-27"    "14-6"     "30-9"     "23-20"    "26-23"    "19-17"   
 [7] "19-16"    "24-18"    "20-17 OT" "23-20 OT" "19-3"     "22-20"   
[13] "29-26"    "18-16"    "41-7"     "34-17"   
```

```r
teams <- xpathSApply(doc, "//li[@class='team-name']", xmlValue)
teams
```

```
 [1] "Denver"      "Cleveland"   "Houston"     "Buffalo"     "Miami"      
 [6] "Green Bay"   "Pittsburgh"  "Cleveland"   "Cincinnati"  "Chicago"    
[11] "New York"    "Pittsburgh"  "Minnesota"   "Detroit"     "New England"
[16] "Cincinnati" 
```


### Reading Json


```r
library(jsonlite)
jsonData <- fromJSON("https://api.github.com/users/felixfan/repos")
names(jsonData)
```

```
 [1] "id"                "name"              "full_name"        
 [4] "owner"             "private"           "html_url"         
 [7] "description"       "fork"              "url"              
[10] "forks_url"         "keys_url"          "collaborators_url"
[13] "teams_url"         "hooks_url"         "issue_events_url" 
[16] "events_url"        "assignees_url"     "branches_url"     
[19] "tags_url"          "blobs_url"         "git_tags_url"     
[22] "git_refs_url"      "trees_url"         "statuses_url"     
[25] "languages_url"     "stargazers_url"    "contributors_url" 
[28] "subscribers_url"   "subscription_url"  "commits_url"      
[31] "git_commits_url"   "comments_url"      "issue_comment_url"
[34] "contents_url"      "compare_url"       "merges_url"       
[37] "archive_url"       "downloads_url"     "issues_url"       
[40] "pulls_url"         "milestones_url"    "notifications_url"
[43] "labels_url"        "releases_url"      "created_at"       
[46] "updated_at"        "pushed_at"         "git_url"          
[49] "ssh_url"           "clone_url"         "svn_url"          
[52] "homepage"          "size"              "stargazers_count" 
[55] "watchers_count"    "language"          "has_issues"       
[58] "has_downloads"     "has_wiki"          "forks_count"      
[61] "mirror_url"        "open_issues_count" "forks"            
[64] "open_issues"       "watchers"          "default_branch"   
```

```r
names(jsonData$owner)
```

```
 [1] "login"               "id"                  "avatar_url"         
 [4] "gravatar_id"         "url"                 "html_url"           
 [7] "followers_url"       "following_url"       "gists_url"          
[10] "starred_url"         "subscriptions_url"   "organizations_url"  
[13] "repos_url"           "events_url"          "received_events_url"
[16] "type"                "site_admin"         
```

```r
jsonData$owner$login
```

```
 [1] "felixfan" "felixfan" "felixfan" "felixfan" "felixfan" "felixfan"
 [7] "felixfan" "felixfan" "felixfan" "felixfan" "felixfan" "felixfan"
[13] "felixfan" "felixfan" "felixfan" "felixfan" "felixfan" "felixfan"
[19] "felixfan" "felixfan" "felixfan" "felixfan" "felixfan" "felixfan"
[25] "felixfan" "felixfan" "felixfan" "felixfan" "felixfan" "felixfan"
```

```r
jsonData$name
```

```
 [1] "biojava"                "Calculator"            
 [3] "ChiSquareCalculator"    "coursera-android"      
 [5] "CPPLearning"            "datasciencecoursera"   
 [7] "datasharing"            "devtools"              
 [9] "felixfan.github.io"     "FinCal"                
[11] "FunPlots"               "GEO"                   
[13] "IntroRandLaTeXforIR"    "IPGWAS"                
[15] "JavaSwing"              "jekyll"                
[17] "labs"                   "libsvm"                
[19] "markdown-here"          "OG-Platform"           
[21] "oneliners"              "pages"                 
[23] "powerAnalysis"          "ProgrammingAssignment2"
[25] "PubMedWordcloud"        "R-Graphics"            
[27] "random-forest"          "RGenetics"             
[29] "slidify"                "styles"                
```

```r
# create and updated date of project of 'FinCal'
jsonData[jsonData$name == "FinCal", c("created_at", "updated_at")]
```

```
             created_at           updated_at
10 2013-09-24T06:25:02Z 2013-12-23T07:31:54Z
```

```r
# create and updated date of all projects
jsonData[, c("name", "created_at", "updated_at")]
```

```
                     name           created_at           updated_at
1                 biojava 2014-02-25T08:34:06Z 2014-02-25T08:34:07Z
2              Calculator 2014-01-20T06:14:33Z 2014-02-27T09:12:59Z
3     ChiSquareCalculator 2014-02-21T06:52:11Z 2014-02-21T07:32:04Z
4        coursera-android 2014-01-20T14:23:37Z 2014-01-20T14:23:38Z
5             CPPLearning 2013-10-23T06:11:50Z 2013-12-07T15:34:51Z
6     datasciencecoursera 2014-04-08T07:14:57Z 2014-04-08T07:18:50Z
7             datasharing 2014-04-08T07:21:12Z 2014-04-08T07:21:13Z
8                devtools 2013-12-11T05:48:57Z 2013-12-11T05:48:58Z
9      felixfan.github.io 2013-09-18T06:01:49Z 2014-04-15T05:59:25Z
10                 FinCal 2013-09-24T06:25:02Z 2013-12-23T07:31:54Z
11               FunPlots 2013-10-11T05:39:17Z 2013-12-07T15:39:42Z
12                    GEO 2013-11-12T05:52:33Z 2013-12-07T15:37:25Z
13    IntroRandLaTeXforIR 2013-11-14T02:34:24Z 2013-11-14T02:34:24Z
14                 IPGWAS 2014-01-24T03:35:16Z 2014-01-24T03:49:35Z
15              JavaSwing 2014-02-24T07:55:14Z 2014-02-24T08:15:20Z
16                 jekyll 2013-09-17T03:39:15Z 2013-09-17T03:39:16Z
17                   labs 2014-04-14T08:57:57Z 2014-04-14T08:57:58Z
18                 libsvm 2014-03-13T06:33:28Z 2014-03-13T06:33:28Z
19          markdown-here 2014-02-27T09:20:30Z 2014-02-27T09:20:31Z
20            OG-Platform 2013-12-04T03:19:15Z 2013-12-04T03:19:19Z
21              oneliners 2013-10-25T09:03:55Z 2013-10-25T09:03:55Z
22                  pages 2013-11-20T15:39:57Z 2013-11-20T15:39:57Z
23          powerAnalysis 2013-10-02T06:23:16Z 2013-10-02T06:24:13Z
24 ProgrammingAssignment2 2014-04-10T06:34:02Z 2014-04-10T06:34:03Z
25        PubMedWordcloud 2013-09-17T02:51:48Z 2014-01-15T04:00:33Z
26             R-Graphics 2014-02-06T06:15:53Z 2014-02-06T06:15:54Z
27          random-forest 2014-03-11T09:48:53Z 2014-03-11T09:48:54Z
28              RGenetics 2014-01-24T07:06:54Z 2014-01-24T07:07:48Z
29                slidify 2013-12-10T03:32:19Z 2013-12-10T03:32:19Z
30                 styles 2013-11-14T09:50:36Z 2013-11-14T09:50:37Z
```

