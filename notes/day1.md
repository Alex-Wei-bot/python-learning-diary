在和VS做了长达一个月的艰苦斗争之后，我终于决定把编译器换成VScode。在下载和安装的时候意外发现需要挂梯子，否则基本教学视频没有办法观看，上次想去coursera上课也遇到了同样的问题，深深地感觉到GFW在某些方面并不是那么合理。等到尝试在VScode上运行代码时发现引用pandas这样的第三方库会报错，于是开始了面向csdn编程(bushi)，搜了大概一个小时终于找到了问题所在，是VScode在运行第三方库时候的引用路径和pip安装的路径不一致，所以无法运行。于是通过：

	‘文件-设置-首选项-拓展-python-Auto Complete: Extra Paths-进入setting.json’

的方式添加了一个额外的引用路径：

	"python.autoComplete.extraPath": ["C:\\Users\\韦思弢\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages"]

之后再次import就不再继续报错了。这和最开始配置VS环境出现的问题如出一辙，但是VS的配置方法和这里还是有很大的区别，我也忘了究竟怎么解决的了，反正暂时也用不上它。
