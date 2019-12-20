(这里忽略了hexo和next的安装过程)

一.对主题的配置

1.使用next主题，并将语言改为中文

进入博客的根文件，打	开_config.yml	文件，找到Site里的language属性，在后面加上zh-Hans(简体中文)这里要注意langeuage：后面要有一个空格。接着一直滑到底部，看到Extensions属性里有一个theme，将后面的landscape更改为next，着用用Git Bash点击自己的博客文件，输入`hexo g`(这里的g为generate生成之意)，再输入`hexo s`(这里的s为service启动服务之意)进入网页即可观看效果。

![1使用next主题并将语言改为中文的网页截图](C:\Users\zhao_\Pictures\hexo\1使用next主题并将语言改为中文的网页截图.png)

2.增加并配置标签页与分类页

首先在博客的根目录里边进入theme/next，找到_config.yml,打开后找到menu这里会发现tags跟categories被注释了，将注释删去后运行，我们会得到这样的页面

![2搜索menu并启用分类页与标签页](C:\Users\zhao_\Pictures\hexo\2搜索menu并启用分类页与标签页.png)

![3启用分类页与标签页后的网页](C:\Users\zhao_\Pictures\hexo\3启用分类页与标签页后的网页.png)

随后点击标签，发现页面错误，我们接下来配置这个页面。

![4点击tags后的网页](C:\Users\zhao_\Pictures\hexo\4点击tags后的网页.png)

我们先进入source文件夹里，只有一个_posts,接着我们在Git Bash里输入`hexo n page tags`会发source这个文件夹里会多一个tags文件夹，进入里边的index修改如下

![5tags里的index](C:\Users\zhao_\Pictures\hexo\5tags里的index.png)

这里多加入了一个type ，加于不加效果如下(先是加的，后是不加)

![6加type](C:\Users\zhao_\Pictures\hexo\6加type.png)

![7不加type](C:\Users\zhao_\Pictures\hexo\7不加type.png)

当然如果我加入tpye但是后边的值是categories效果如下

![8tpye的值为categories](C:\Users\zhao_\Pictures\hexo\8tpye的值为categories.png)

接下来分类页面也是如此。

3.更改主题

在theme/next下找到_config.yml找到scheme，这里有提供四个主题，可以根据喜欢来更改。这里我选的是最后一个。效果如下：

![9更换主题](C:\Users\zhao_\Pictures\hexo\9更换主题.png)

4.配置个人信息(更改自己的头像，姓名与title)

打开博客下的配置文件_config.yml,分别修改title与author，再搜索avatar，可以使用图片的url，或者是图片的路径(图片要在source里)

![10配置个人信息](C:\Users\zhao_\Pictures\hexo\10配置个人信息.png)



5.配置交友链接

打开next里的配置文件，找到social，分别启用Github，E-mail，也可以自己加上微博或者其他的，配置与效果如下。

![11配置social](C:\Users\zhao_\Pictures\hexo\11配置social.png)

![12配置万交由由连接的页面](C:\Users\zhao_\Pictures\hexo\12配置万交由由连接的页面.png)

6.让自己的头像变为圆形，添加旋转功能

进入themes\next\source\css\_common\components\sidebar/sidebar-author.styl修改如下

![13让头像变为圆形可转](C:\Users\zhao_\Pictures\hexo\13让头像变为圆形可转.png)

第一个是让头像变为圆形，注释的是让头像旋转。

7.设置阅读全文

这里有两种方法一种是修改主题里的配置文件

![14设置阅读全文](C:\Users\zhao_\Pictures\hexo\14设置阅读全文.png)

另一个是在文章里加入`<!-- more -->`代码

8.添加动态背景

同样也是在主题的配置文件里搜索canvas，会有四个动态背景供选择

![15背景动画](C:\Users\zhao_\Pictures\hexo\15背景动画.png)

9.添加建站时间

在主题的配置文件里加入since字段eg:`since:2010-2011`这个时间会在页面最下面显示。

![16建站时间显示](C:\Users\zhao_\Pictures\hexo\16建站时间显示.png)

10.设置链接颜色

在\themes\next\source\css\_common\components\post\post.styl里设置如下

![17链接样式](C:\Users\zhao_\Pictures\hexo\17链接样式.png)

11.增加搜索服务

按照官方文档的配置即可(这里用的是local search)

![18搜索服务](C:\Users\zhao_\Pictures\hexo\18搜索服务.png)

12.增加统计服务

在主题文件配置如下(这里用的是不蒜子统计)

![19统统服务](C:\Users\zhao_\Pictures\hexo\19统统服务.png)

13.增加分享功能

同样，按照官方文档做即可

![20分享服务](C:\Users\zhao_\Pictures\hexo\20分享服务.png)

14.设置加载效果

在主题的配置文件搜索pace字段配置如下

![21设置加载效果](C:\Users\zhao_\Pictures\hexo\21设置加载效果.png)

有多种选择可以尝试。

15.字数统计与阅读时长

在博客根目录输入如下命令`$ npm install hexo-wordcount --save`然后在主题的配置文件搜索post_wordcount关键字，修改如下

![22字数同体积与阅读时长](C:\Users\zhao_\Pictures\hexo\22字数同体积与阅读时长.png)

16.部署到github