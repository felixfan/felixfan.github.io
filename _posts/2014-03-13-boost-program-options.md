---
title: Manage C++ command line options using Boost Program Options
layout: post
categories: [CPlusPlus]
tags: [C++]
image: /figure
---

{% include JB/setup %}

OS: Windows 7
C++ IDE: [Microsoft Visual Studio Express 2013 for Windows Desktop](http://www.microsoft.com/en-hk/download/details.aspx?id=40787)

#### Install Boost

Download [boost_1_55_0.zip](http://www.boost.org/users/history/version_1_55_0.html) and unpack it to a directory (e.g. D:\myprograms\boost_1_55_0). This directory is called the **Boost root directory**.

Open the command prompt and change your current directory to the **Boost root directory**.

Then, type the following command:

```
bootstrap.bat
```

and then, type the following command:

```
b2.exe
```

The first command prepares the Boost.Build system for use. The second command invokes Boost.Build to build the separately-compiled Boost libraries. The second command may take a very long time (e.g. ~1hr).

After the second command finished, you will find a new directory **stage** was generated under the **Boost root directory**. There is a subdiretory **lib** under directory **stage** (e.g. D:\myprograms\boost_1_55_0\stage\lib).

#### Link Your Program to a Boost Library

1. Right-click project titile in the **Solution Explorer** pane of Visual Studio IDE and select **Properties** from the resulting pop-up menu.

2. In **Configuration Properties** select **C/C++**,then select **General**, then select **Additional Include Directories**, enter the path to the Boost root directory (e.g. D:\myprograms\boost_1_55_0)

3. In **Configuration Properties** select **Linker**, then select **Additional Library Directories**, enter the path to the Boost binaries (e.g. D:\myprograms\boost_1_55_0\stage\lib).

4. From the Build menu, select Build Solution.

#### Example code

```{cpp}
#include "stdafx.h"
#include <iostream>
#include <boost/program_options.hpp>

using namespace std;


int main(int argc, char *argv[])
{
namespace po = boost::program_options;

po::options_description description("Usage:");

description.add_options()
("help,h", "Display this help message")
("version,v", "Display the version number")
("compression,c", po::value<int>(), "Compression level")
("score,s", po::value<int>()->default_value(60), "Final score");

po::variables_map vm;
po::store(po::command_line_parser(argc, argv).options(description).run(), vm);
po::notify(vm);

if (vm.count("help")){
cout << description;
}

if (vm.count("compression")){
cout << "Compression level " << vm["compression"].as<int>() << endl;
}

return 0;
}

```


#### References
* [Boost Getting Started on Windows](http://www.boost.org/doc/libs/1_55_0/more/getting_started/windows.html)
* [Manage command-line options with Boost Program Options](http://www.baptiste-wicht.com/2012/07/manage-command-line-boost-program-options/)
* [How To Use Boost.Program_options](http://www.radmangames.com/programming/how-to-use-boost-program_options)
* [Boost Command Line Argument Processing](http://chuckaknight.wordpress.com/2013/03/24/boost-command-line-argument-processing/)


