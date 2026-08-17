Date:2013-01-11
Title:cefpython - python bindings for CEF(Chromium Embedded Framework)
Tags:cefpython, python
Slug:cefpython-python-bindings-for-CEF

手头有个pyQT的项目里面使用QtWebKit, 用于在客户端中展示网页内容。虽然使用QtWebkit实现了基本功能。但是存在不少问题。
QtWebKit打开页面速度慢，一些js代码无法正常运行，需要自己去实现的东西太多。由于时间有点紧，所以就准备找第三方实现的库来做。

最后采用 [Chromium Embedded Framework](https://chromiumembedded.github.io/cef/)（CEF）。
这个项目稳定（2008 开始），源码托管在 [chromiumembedded/cef](https://github.com/chromiumembedded/cef)，并有 Python 实现 cefpython。

[cefpython](https://github.com/cztomczak/cefpython) 使用 Cython 实现与 libcef 的交互。项目 2012-05-08 提交 0.11，到 2012-12-27 提交 0.51 版本的 cef1。

使用New BSD License 开源协议。目前只有czarek.tomczak一人维护。
cefpython项目分为cef1, cef3 。cef1的完成度比较高，cef3可用的api太少。
由于项目中对webkit的要求比较少。 所以直接拿来使用。

###问题和不足
- 项目完成度还不高，存在一些问题。好在作者开发热情很高，问题能很快解决。
- 目前只支持windows和mac。
- 编译需要安装windows SDK和vs2008。

###更多链接
- [CEF 中文文档部分翻译 ”cef site:www.cnblogs.com/think“的google 链接](https://www.google.com.hk/search?q=cef+site%3Awww.cnblogs.com%2Fthink)
- [CEF vs. QtWebkit](http://www.magpcss.org/ceforum/viewtopic.php?f=6&t=395)

