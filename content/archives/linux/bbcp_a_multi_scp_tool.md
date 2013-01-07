Date:2013-01-07
Title:bbcp,替代scp的多线程传输工具
Tags:bbcp, scp, p2p
Slug:bbcp-a-muliti-scp-tool

###选用bbcp替代scp的原因
这两天用scp往服务器上传数据，scp传输速度太慢。特别是网络不太稳定的时候，速度非常慢。惨不忍睹。
所以想找个替代工具。

###使用中遇到的问题
如何好用， 比scp 快多少就不测试了。这里说说遇到问题。

1. 需要目标服务器上同样放置bbcp程序。如果有admin权限，比较好办。
2. 防火墙。由于采用了多个端口同时传输数据， 所以需要开发至少8个端口用于传输数据。
    - 目标服务器在公网，并且开放端口，直接传输；
    - 目标服务器在内网，
        - 防火墙映射端口，直接传输。
        - 目标服务器无法映射端口，本地开放端口或者可以映射端口， 可以使用-Z(同--port 此为12.08.17版本中加入，如果无法使用， 请使用 --help 查看版本) 传输。
        - 本地也无法映射端口。那就没辙了。
3. 连接目标服务器ssh的端口貌似没法修改, 默认22。 但是好多服务器都修改了这个端口。（提供了-S， 但是不会设置）

###bbcp的相关网页
- [官方文档 http://www.slac.stanford.edu/~abh/bbcp/](http://www.slac.stanford.edu/~abh/bbcp/), 主要介绍bbcp 的使用方法，并提供源码地址和二进制文件下载。
    - [源码](http://www.slac.stanford.edu/~abh/bbcp/bbcp.git)

            git clone http://www.slac.stanford.edu/~abh/bbcp/bbcp.git

    - [可执行文件官方下载 http://www.slac.stanford.edu/~abh/bbcp/bin/](http://www.slac.stanford.edu/~abh/bbcp/bin/), 目前仅提供一下平台

            amd64_darwin_100/       17-Aug-2012 19:49
            amd64_linux26/          24-Apr-2012 14:43
            amd64_rhel50/           17-Aug-2012 19:49
            amd64_rhel60/           17-Aug-2012 19:01
            i386_linux26/           19-May-2012 08:56
            i386_rhel50/            17-Aug-2012 19:48
            i386_rhel60/            17-Aug-2012 19:49
            sun4x_510/              30-Jan-2012 23:12
            sunx86_510/             12-Jan-2012 18:19
            x86_darwin_100/         17-Aug-2012 19:49

- [HOWTO move data](http://moo.nac.uci.edu/~hjm/HOWTO_move_data.html), 介绍如何移动数据， 其中介绍到bbcp，以及与rsync的区别， 以下引用的文章目录
    1. Executive Summary
    2. Compression & Encryption
    3. Avoiding data transfer
        1. kdirstat
        2. rsync
        3. Unison
    4. Streaming Data Transfer
        1. bbcp
        2. bbftp
        3. Fast Data Transfer (fdt)
        4. GridFTP
        5. Globus Online
        6. netcat

- [Using BBCP](http://pcbunn.cithep.caltech.edu/bbcp/using_bbcp.htm)， 比较详细的介绍
- [用 bbcp 取代 scp](http://imysql.cn/2008_12_08_using_bbcp_instead_scp)，上篇 “Using BBCP” 的中文译文(非全文翻译)
- [Using bbcp At NERSC](http://www.nersc.gov/users/data-and-networking/transferring-data/bbcp/), 简单介绍
- [bbcp测试](http://hutong236.i.sohu.com/blog/view/212355791.htm)， 国人简单的测试


