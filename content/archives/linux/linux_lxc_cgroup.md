Date:2013-01-09
Title:认识cgroup和 lxc
Tags:Lxc, cgroup, linux containers, control groups
Slug:cgroup-lxc

###引子
[CPyUG] 对于python的sandbox,有什么好的方案吗？
由python的沙箱引出虚拟化中的两个名词lxc和cgroup。

##cgroup(control groups)
- [cgroup](http://en.wikipedia.org/wiki/cgroup), wikipedia 中的定义
- [http://www.kernel.org/doc/Documentation/cgroups/](http://www.kernel.org/doc/Documentation/cgroups/), cgroups 官方文档
- [http://www.cnblogs.com/lisperl/tag/虚拟化技术](http://www.cnblogs.com/lisperl/tag/%E8%99%9A%E6%8B%9F%E5%8C%96%E6%8A%80%E6%9C%AF/), 这里对官方文档做了翻译

##Lxc(LinuX Containers)
- [lxc](http://en.wikipedia.org/wiki/Lxc), wikipedia 中的定义
- [Linux Containers - ArchWiki](http://wiki.archlinux.org/index.php/Linux_Containers)
- [LXC - Community Ubuntu Documentation](https://help.ubuntu.com/community/LXC), See also
- [How to LXC - this is one of the best documents available](http://lxc.teegra.net/), 比较详细的lxc 的介绍手册
- [LXC - Gentoo Wiki](wiki.gentoo.org/wiki/LXC)
- [LXC - Debian Wiki](http://wiki.debian.org/LXC)
- [LXC - openSUSE](http://en.opensuse.org/LXC)
- [https://www.stgraber.org/category/lxc/](https://www.stgraber.org/category/lxc/), ubutnu的软件工程 Stéphane Grabers的blog。
- [lxc-in-ubuntu-12-04-lts](https://www.stgraber.org/2012/05/04/lxc-in-ubuntu-12-04-lts/), Stéphane Grabers lxc tutorial
- [LXC: Linux container tools](http://www.ibm.com/developerworks/linux/library/l-lxc-containers/), IBM linux 技术中心软件工程师的一篇介绍
- [Secure Linux containers cookbook](http://www.ibm.com/developerworks/linux/library/l-lxc-security/index.html), 和上篇是姐妹篇, 通过 LSM([Linux Security Modules](http://en.wikipedia.org/wiki/Linux_Security_Modules)), SELinux([Security-Enhanced Linux](http://en.wikipedia.org/wiki/SELinux)), Smack()
- [LXC – Linux Containers on Steroids](http://www.janoszen.com/2012/06/04/lxc-linux-containers-on-steroids/), lxc 简单使用心得
- [LXC（Linux Containers）的不足和改进](http://www.cnblogs.com/lisperl/archive/2012/06/15/2551067.html), 提出以下观点

    缺少对磁盘配额（disk quota）的支持
    缺少对写时复制（copy on write）的支持
    进程和容器之间的动态关联还不够完善
    不支持checkpoint

由于与OpenVZ同为OS级别的虚拟化技术,免不了对比两者之前的差异。

##OpenVZ vs LXC
- [Future of OpenVZ?](http://lwn.net/Articles/507997/)
- [openvz-vz-lxc](https://ask.fedoraproject.org/question/929/openvz-vz-lxc), lxc 再次被吐嘈不支持checkpoint。
- [Lightweight-virtualization-LXC-vs-OpenVZ.pdf](http://www.thomas-krenn.com/de/wikiDE/images/3/35/20110511-Lightweight-virtualization-LXC-vs-OpenVZ.pdf), 德文写的。

通过上面的文章可以看到目前lxc 还不适合是用在生产环境。Lxc 依赖的cgroup 早已加入linux kernel mainline中。我比较认同Lxc 最终会替代 OpenVZ。

##see also
- [http://ubuntuforums.org/showthread.php?t=1382823](http://ubuntuforums.org/showthread.php?t=1382823), Lucid and OpenVZ and/or LXC ?
- [http://manpages.ubuntu.com/manpages/karmic/man5/lxc.conf.5.html](http://manpages.ubuntu.com/manpages/karmic/man5/lxc.conf.5.html), lxc.conf 配置帮助
- [https://access.redhat.com/knowledge/docs/zh-CN/Red_Hat_Enterprise_Linux/6/html/Resource_Management_Guide/](https://access.redhat.com/knowledge/docs/zh-CN/Red_Hat_Enterprise_Linux/6/html/Resource_Management_Guide/), 'RHEL6的资源管理指南'。 其中主要介绍cgrous, 由于是针对rhel 系统的。对于非red hat用户建议主要看看概念和机制。
- [http://agiletesting.blogspot.com/2011/08/anybody-using-lxc-or-openvz-in.html](http://agiletesting.blogspot.com/2011/08/anybody-using-lxc-or-openvz-in.html), twitter 上lxc 杂谈

