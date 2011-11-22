%define name kwtools
%define version 0.8.0
%define release 0

Summary: %{name}
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}.tar.gz
BuildRequires: zsh >= 4.2.0, gettext >= 0.14.5
URL: ftp://ftp.berlios.de/pub/netzworkk/scripts/Sources
License: GPL
Packager: kiste@netzworkk.de
Group: Applications
Vendor: Netzworkk

%description
kwtools sind eine Scriptsammlung, um grafische und Konsolenprogramme
zu bedienen.

%package bin
Summary: Includes kwadmin, combines kwtools scripts.
Group: Applications
Requires: kwtools-common = 0.8.0-0

%description bin
Includes kwadmin, a script which combines all kwtools scripts. 
Is divided up into the categories service programmes, graphics, multimedia,
network and system.

%package common
Summary: general functions for kwtools scripts.
Group: Applications
Requires: dialog >= 1.1, file >= 4.10, gettext > 0.14.5, zsh >= 4.2.0, udev, util-linux, sharutils

%description common
These are general functions which are required by every kwtools script.

%package doc
Summary: Documentation.
Group: doc
Requires: kwtools-common = 0.8.0-0

%description doc
Documentation regarding kwtools scripts and their functions which 
are used by almost all scripts.

%package graphic
Summary: Graphics scripts.
Group: Applications
Requires: kwtools-common = 0.8.0-0, gphoto >= 2.1.0, zgv

%description graphic
Graphics scripts to operate digital cameras, etc.

kwcamera: Operation of digital camera

%package multi
Summary: multimedia scripts.
Group: Applications
Requires: kwtools-common = 0.8.0-0, cddb, cd-discid, cdparanoia, cdrdao >= 1.1.9, coreutils >= 5.0, dvd+rw-tools, mjpegtools >= 1.6.0, lame, genisoimage >= 1.1.8, vcdimager

%description multi
Multimedia scripts to create VCD's, audio CD's, rip DVD's etc.

kwrecord: Burns audio, video, data CD's and ISO images, etc., onto CD-R(W) and 
       	DVD-+R(W).
kwrip: Rips a complete CD into a certain directory. Video and audio.
kwsnd2sndfm: Transforms different audio formats into different formats (raw,mp3,ogg,wav).
kwvcdburn: Creates and burns video/photo CD's.

%package net
Summary: network scripts.
Group: Applications
Requires: kwtools-common = 0.8.0-0, rsync, ssh, sudo

%description net
Includes several network scripts.
 
kwnetstat: Displays information regarding your network's current state.
kwproxy: To set the http_ - and ftp_proxy variables. 
        These are saved in /etc/[default|sysconfig]/proxy. To be able to use these 
        variables you must enter the file to read into /etc/profile
        or /etc/(zsh/)zprofile (zsh). 
kwrsync: Synchronises your home directory, directories of choice 
        and can edit the user crontab table for rsync.
kwrsync_backup: Make a snapshot from lokal and remote hosts.

%package net-djbdns
Summary: Network script djbdns.
Group: Applications
Requires: kwtools-common = 0.8.0-0, daemontools, djbdns, ucspi-tcp

%description net-djbdns
kwdjbdns script plus help files and functions.

kwdjbdns: Configures and administrates your DNS server, only  
        D.J.Bernstein's <djb@cr.yp.to>
		

%package net-mutt
Summary: network scripts.
Group: Applications
Requires: kwtools-common = 0.8.0-0, mutt

%description net-mutt
The kwmutt script configures your mail client mutt.
 
kwmutt: Configures your mail client mutt.

%package net-narc
Summary: Netwerk script kwnarc.
Group: Applications
Requires: kwtools-common = 0.8.0-0, ethtool, iptables, lsb >= 3.0-6

%description net-narc
The kwnarcconf script plus help files and functions configures your firewall.

kwnarcconf: Configures your firewall (kwnarc - kwtools Netfilter Automatic
        Rule Configurator) per iptables. It starts, stops, reloads the
        configuration and displaying the single chains rules and the
        current connection tracking infos.

%package net-openmosix
Summary: Netwerk script openmosix.
Group: Applications
Requires: ethtool, kwtools-common = 0.8.0-0, openmosix
%description net-openmosix
Network script openmosix.

openmosix: Configures your openmosix cluster and sets the dfsalinks.
        (DFSA = Direct file system access).	Only works with a 
        Kernel-2.4.*+openmosix-patch.

%package net-postfix
Summary: Network script kwpostfix.
Group: Applications
Requires: kwtools-common = 0.8.0-0, postfix >= 2.3.0

%description net-postfix
Network script kwpostfix.

kwpostfix: Configures and administrates your Postfix Mail Server.
        Is still alpha.

%package sys
Summary: system scripts.
Group: Applications
Requires: kwtools-common = 0.8.0-0, ethtool, grub, logrotate, xntp, openssl, sysvinit >= 2.85 / file-rc >= 0.5

%description sys
Includes several scripts for system administration. 

kwauth: Configures your login. So far only support for local and NIS.
kwclock: Shows the PC's clock and date settings and can set time and date.
        This can be done manually or per ntpdate, if this is installed.
kwgroup: Generates, deletes and changes groups.
kwgrub: Configures and installs the bootloader Grub.
kwnetcardconf: Configures your network cards, either per dhcp or manually.
kwnetconf: Frontend to varous connection tools.
kwlogrotate: An administration script for log files. It uses logrotate for this purpose.
kwrunlevconf: Can configure your runlevel scripts in a very sophisticated manner. 
        It generates and also deletes /usr/sbin/rcinitscriptname links.
        This is intended to save the administrator time and effort typing.
        It supported the systems file-rc and sysv-rc.
kwssl: Generates ssl keys, certifications authority, private keys,
        signs these, checks keys, etc.
kwuser: Can be used to create, change and delete users.
kwwvdialconf: Configures the file wvdial.conf from program wvdial.

%package sys-fuse
Summary: Script to manage FUSE Devices.
Group: Applications
Requires: kwtools-common = 0.8.0-0, fuse-utils

%description sys-fuse
Include a frontend script for filesystem administration (FUSE).

kwfuse: Generates, deletes and changes Entrys in /etc/fstab and
        /etc/fuse.conf. See also Documentation in /usr/share/doc/fuse-utils
        and /usr/share/doc/kwtools-sys-fuse.

%package sys-crypt
Summary: Script to manage encrypted Devices.
Group: Applications
Requires: kwtools-common = 0.8.0-0, gnupg / openssl, ecryptfs-utils / loop-aes-utils / util-linux-crypto >= 2.12

%description sys-crypt
Includes three scripts which enables management of encrypted devices.

kwcrypt: A wrapper for cryptsetup, loop-aes-utils and ecryptfs-utils.
kwecryptfs: A frontend for the ecryptfs-utils (cryptographic filesystem).
kwcryptsetup: A frontend for cryptsetup and dmsetup, with which one can
        encrypted discs and containers (files with file system), respectively.
        It can enlarge and reduce drives with luks extension, create gnupg
        and ssl keys and delete this.
kwlosetup: A frontend for losetup, with which one can generate encrypted
        discs and containers (files with file system), respectively.

%package sys-kwpasswd
Summary: Includes several scripts for general tasks.
Group: Applications
Requires: kwtools-common = 0.8.0-0, expect

%description sys-kwpasswd
Script and files force to change the User password by first login.

kwpasswd: Change the User Password over the programs passwd or yppasswd.
        Only for Bash, Zsh, KDE and Gnome.

%package sys-lvm
Summary: Script to manage LVMs.
Group: Applications
Requires: kwtools-common = 0.8.0-0, lvm / lvm2

%description sys-lvm
Includes a script (kwlvm) to manage LVMs. 

kwlvm: Can display logic volumes, volume groups and physical volumes,
        generate, delete, enlargen, minimise, rename, split,
        join..... It can deal with lvm and lvm2.

%package sys-parted
Summary: system scripts.
Group: Applications
Requires: kwtools-common = 0.8.0-0, parted >= 1.7.1-3

%description sys-parted
Include a frontend script for parted.

kwparted: Uses parted to detect and manipulate devices and partition
        tables while several (optional) filesystem tools provide support for
        filesystems not included in parted.

%package sys-quota
Summary: Script to manage quota.
Group: Applications
Requires: kwtools-common = 0.8.0-0, quota >= 3.15

%description sys-quota
Includes a script (kwquota) to manage quota. 

kwquota: Can display actual quota and manage quota on disk. It
        supported for ext2/3, and reiserfs user- and group-quota.
        At the xfs filesystem also supported project-quota.

%package sys-raid
Summary: script for software RAID administration.
Group: Applications
Requires: kwtools-common = 0.8.0-0, mdadm >= 2.6.0
Conflicts: mdctl < 0.7.2, raidtools2 < 1.00.3

%description sys-raid
Includes a script to manage software RAID Arrays. 

kwraid: Shows the status of arrays and one can create RAID arrays
        (linear,0,1,4,5,6,10), add and delete partitions
        to or from an array, while system is running. RAID levels 6 and 10
        are only available from Kernel >=2.5 onwards.

NOTE: may not work with several spare discs. I am afraid I couldn't check this.

%package utils
Summary: Includes several scripts for general tasks.
Group: Applications
Requires: kwtools-common = 0.8.0-0, bzip2, expect, gnupg, muttprint, pwsafe, tar

%description utils
Includes several scripts for general tasks.

kwbackup: Simple backup script for the system and directories of your choice. Also
        possible per crontab entry.
kwgpgcrypt: De- , encodes and signs whole directories or single files. 
        Management of keys and configuration of gnupg.
kwmuttprintcf: Configures the program muttprint.
kwpwsafe: A frontend for pwsafe. pwsafe is a unix commandline program that
        manages encrypted password databases.
kwvmstat: Displays the current processor load.

%package utils-pim
Summary: Scripts for the Personal Information Management (PIM)
Group: Applications
Requires: kwtools-common = 0.8.0-0, bsdmainutils, gcal, tetex

%description utils-pim
Includes several scripts for the Personal Information Management (PIM).

kwholiday: Displays public holidays per date.
kwplaner: A script which communicates with create.cal.pl, gcal and calendar.
        kwholiday, kwtex-cal and kwtermin can be operated with kwplaner.
kwtermin: A schedule planner.
kwtex-cal: Generates a calendar with images and public holidays.

%prep
# entpacke die kwtools
%setup -q -n kwtools-%{version}

# install
%install
./install --prefix=/usr
 
%files bin
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools
%attr(0755,root,root) /usr/lib/kwtools/kwadmin
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwadmin
%attr(0644,root,root) /usr/share/kwtools/functions/kwadmin/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/lang_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/kw_conf_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/graphic_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/multi_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/utils_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-bin
%attr(0644,root,root) /usr/share/doc/kwtools-bin/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-bin/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-bin/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/kwadmin.1.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwadmin.mo

%files common
%attr(0755,root,root) %dir /etc/kwtools
%attr(0644,root,root) /etc/kwtools/main.cf
%attr(0755,root,root) %dir /usr/lib/kwtools
%attr(0755,root,root) /usr/lib/kwtools/skeleton-dialog.zsh
%attr(0755,root,root) %dir /usr/share/kwtools/help/share
%attr(0644,root,root) /usr/share/kwtools/help/share/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/sys
%attr(0644,root,root) /usr/share/kwtools/functions/sys/*
%attr(0755,root,root) %dir /usr/share/doc/kwtools-common
%attr(0644,root,root) /usr/share/doc/kwtools-common/README.*
%attr(0644,root,root) /usr/share/doc/kwtools-common/Release
%attr(0644,root,root) /usr/share/doc/kwtools-common/copyright
%attr(0644,root,root) /usr/share/doc/kwtools-common/changelog*
%attr(0644,root,root) /usr/share/doc/kwtools-common/BUGS
%attr(0644,root,root) /usr/share/doc/kwtools-common/TODO
%attr(0755,root,root) /usr/share/doc/kwtools-common/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-common/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man5
%attr(0644,root,root) /usr/share/man/de/man5/main.cf.5.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwtools-common.mo

%files doc
%attr(0755,root,root) %dir /usr/share/doc/kwtools-doc
%attr(0644,root,root) /usr/share/doc/kwtools-doc/*

%files graphic
%attr(0755,root,root) %dir /usr/bin
%attr(0755,root,root) %dir /usr/lib/kwtools/graphic/
%attr(0755,root,root) /usr/lib/kwtools/graphic/kwcamera
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwcamera
%attr(0644,root,root) /usr/share/kwtools/functions/kwcamera/kwcamera_config
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwcamera
%attr(0644,root,root) /usr/share/kwtools/help/kwcamera/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/graphic_*_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-graphic
%attr(0644,root,root) /usr/share/doc/kwtools-graphic/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-graphic/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-graphic/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/kwcamera.1.gz
%attr(0755,root,root) %dir /usr/share/man/de/man5
%attr(0644,root,root) /usr/share/man/de/man5/kwcamerarc.5.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwcamera.mo

%files multi
%attr(0755,root,root) %dir /usr/bin
%attr(0755,root,root) %dir /usr/lib/kwtools/multi
%attr(0755,root,root) /usr/lib/kwtools/multi/kwrecord
%attr(0755,root,root) /usr/lib/kwtools/multi/kwrip
%attr(0755,root,root) /usr/lib/kwtools/multi/kwsnd2sndfm
%attr(0755,root,root) /usr/lib/kwtools/multi/kwvcdburn
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwrecord
%attr(0644,root,root) /usr/share/kwtools/functions/kwrecord/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwrip
%attr(0644,root,root) /usr/share/kwtools/functions/kwrip/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwsnd2sndfm
%attr(0644,root,root) /usr/share/kwtools/functions/kwsnd2sndfm/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwvcdburn
%attr(0644,root,root) /usr/share/kwtools/functions/kwvcdburn/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwrip
%attr(0644,root,root) /usr/share/kwtools/help/kwrip/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwrecord
%attr(0644,root,root) /usr/share/kwtools/help/kwrecord/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwsnd2sndfm
%attr(0644,root,root) /usr/share/kwtools/help/kwsnd2sndfm/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwvcdburn
%attr(0644,root,root) /usr/share/kwtools/help/kwvcdburn/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/en/kwadmin/multi_*_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-multi
%attr(0644,root,root) /usr/share/doc/kwtools-multi/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-multi/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-multi/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/kwrecord.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwrip.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwsnd2sndfm.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwvcdburn.1.gz
%attr(0755,root,root) %dir /usr/share/man/de/man5
%attr(0644,root,root) /usr/share/man/de/man5/cd_dvdrc.5.gz
%attr(0644,root,root) /usr/share/man/de/man5/kwriprc.5.gz
%attr(0644,root,root) /usr/share/man/de/man5/kwsnd2sndfmrc.5.gz
%attr(0644,root,root) /usr/share/man/de/man5/kwvcdburnrc.5.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwrecord.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwrip.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwsnd2sndfm.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwvcdburn.mo

%files net
%attr(0755,root,root) %dir /usr/bin
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /etc/kwtools
%attr(0644,root,root) %dir /etc/kwtools/kwrsync_backup.cf
%attr(0644,root,root) %dir /etc/kwtools/kwrsync_backup-excludes
%attr(0755,root,root) %dir /usr/lib/kwtools
%attr(0755,root,root) /usr/lib/kwtools/kwrsync_cron
%attr(0700,root,root) /usr/lib/kwtools/kwrsync_backup_cron
%attr(0755,root,root) %dir /usr/lib/kwtools/net
%attr(0755,root,root) /usr/lib/kwtools/net/kwnetstat
%attr(0755,root,root) /usr/lib/kwtools/net/kwproxy
%attr(0755,root,root) /usr/lib/kwtools/net/kwrsync_backup
%attr(0755,root,root) /usr/lib/kwtools/net/kwrsync
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwrsync_backup
%attr(0644,root,root) /usr/share/kwtools/functions/kwrsync_backup/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwrsync
%attr(0644,root,root) /usr/share/kwtools/functions/kwrsync/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwproxy
%attr(0644,root,root) /usr/share/kwtools/help/kwproxy/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwnetstat
%attr(0644,root,root) /usr/share/kwtools/help/kwnetstat/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwrsync
%attr(0644,root,root) /usr/share/kwtools/help/kwrsync/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_kwnetstat_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_kwproxy_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_kwrsync_backup_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_kwrsync_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-net
%attr(0644,root,root) /usr/share/doc/kwtools-net/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-net/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-net/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/kwnetstat.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwrsync.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwrsync_cron.1.gz
%attr(0755,root,root) %dir /usr/share/man/de/man5
%attr(0644,root,root) /usr/share/man/de/man5/kwrsyncrc.5.gz
%attr(0644,root,root) /usr/share/man/de/man5/kwrsync_backup.cf.5.gz
%attr(0755,root,root) %dir /usr/share/man/de/man8
%attr(0644,root,root) /usr/share/man/de/man8/kwrsync_backup.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwrsync_backup_cron.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwproxy.8.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwnetstat.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwrsync.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwrsync_cron.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwrsync_backup.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwrsync_backup_cron.mo

%files net-djbdns
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools/net
%attr(0755,root,root) /usr/lib/kwtools/net/kwdjbdns
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwdjbdns
%attr(0644,root,root) /usr/share/kwtools/functions/kwdjbdns/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwdjbdns
%attr(0644,root,root) /usr/share/kwtools/help/kwdjbdns/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_kwdjbdns_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-net-djbdns
%attr(0644,root,root) /usr/share/doc/kwtools-net-djbdns/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-net-djbdns/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-net-djbdns/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/kwdjbdns.1.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwdjbdns.mo

%files net-mutt
%attr(0755,root,root) %dir /usr/bin
%attr(0755,root,root) /usr/bin/check-smtp-auth
%attr(0755,root,root) /usr/bin/mutt.vcard.filter
%attr(0755,root,root) /usr/bin/mutt.octet.filter
%attr(0755,root,root) %dir /usr/lib/kwtools/net
%attr(0755,root,root) /usr/lib/kwtools/net/kwmutt
%attr(0755,root,root) %dir /usr/share/kwtools/data/kwmutt
%attr(0644,root,root) /usr/share/kwtools/data/kwmutt/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwmutt
%attr(0644,root,root) /usr/share/kwtools/help/kwmutt/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_kwmutt_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-net
%attr(0644,root,root) /usr/share/doc/kwtools-net-mutt/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-net-mutt/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-net-mutt/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/kwmutt.1.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwmutt.mo

%files net-narc
%attr(0755,root,root) %dir /usr/sbin
%attr(0700,root,root) /usr/sbin/kwnarc
%attr(0755,root,root) %dir /etc/init.d
%attr(0755,root,root) /etc/init.d/kwnarc
%attr(0755,root,root) %dir /etc/kwtools
%attr(0600,root,root) /etc/kwtools/kwnarc.conf
%attr(0755,root,root) %dir /etc/ppp/ip-up.d
%attr(0600,root,root) /etc/ppp/ip-up.d/1kwnarc
%attr(0755,root,root) %dir /etc/ppp/ip-down.d
%attr(0600,root,root) /etc/ppp/ip-down.d/kwnarc
%attr(0755,root,root) %dir /usr/lib/kwtools/net
%attr(0755,root,root) /usr/lib/kwtools/net/kwnarcconf
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwnarcconf
%attr(0644,root,root) /usr/share/kwtools/functions/kwnarcconf/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwnarcconf
%attr(0644,root,root) /usr/share/kwtools/help/kwnarcconf/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_kwnarcconf_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-net-narc
%attr(0644,root,root) /usr/share/doc/kwtools-net-narc/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-net-narc/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-net-narc/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man5
%attr(0644,root,root) /usr/share/man/de/man5/kwnarc.conf.5.gz
%attr(0755,root,root) %dir /usr/share/man/de/man8
%attr(0644,root,root) /usr/share/man/de/man8/kwnarc.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwnarcconf.8.gz
%attr(0755,root,root) %dir /usr/share/man/en/man5
%attr(0644,root,root) /usr/share/man/en/man5/kwnarc.conf.5.gz
%attr(0755,root,root) %dir /usr/share/man/en/man8
%attr(0644,root,root) /usr/share/man/en/man8/kwnarc.8.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwnarcconf.mo

%files net-openmosix
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools/net
%attr(0755,root,root) /usr/lib/kwtools/net/openmosix
%attr(0755,root,root) %dir /usr/share/kwtools/functions/openmosix
%attr(0644,root,root) /usr/share/kwtools/functions/openmosix/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/openmosix
%attr(0644,root,root) /usr/share/kwtools/help/openmosix/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_openmosix_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-net-openmosix
%attr(0644,root,root) /usr/share/doc/kwtools-net-openmosix/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-net-openmosix/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-net-openmosix/prerm.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-net-openmosix/openmosix.kwtools
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/openmosix.1.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/openmosix.mo

%files net-postfix
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools/net
%attr(0755,root,root) /usr/lib/kwtools/net/kwpostfix
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwpostfix
%attr(0644,root,root) /usr/share/kwtools/functions/kwpostfix/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwpostfix
%attr(0644,root,root) /usr/share/kwtools/help/kwpostfix/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/net_kwpostfix_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-net-postfix
%attr(0644,root,root) /usr/share/doc/kwtools-net-postfix/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-net-postfix/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-net-postfix/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/kwpostfix.1.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwpostfix.mo

%files sys
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools/sys
%attr(0755,root,root) /usr/lib/kwtools/kwnetcardconf
%attr(0755,root,root) /usr/lib/kwtools/sys/kwauth
%attr(0755,root,root) /usr/lib/kwtools/sys/kwclock
%attr(0755,root,root) /usr/lib/kwtools/sys/kwgroup
%attr(0755,root,root) /usr/lib/kwtools/sys/kwgrub
%attr(0755,root,root) /usr/lib/kwtools/sys/kwnetconf
%attr(0755,root,root) /usr/lib/kwtools/sys/kwlogrotate
%attr(0755,root,root) /usr/lib/kwtools/sys/kwssl
%attr(0755,root,root) /usr/lib/kwtools/sys/kwuser
%attr(0755,root,root) /usr/lib/kwtools/sys/kwwvdialconf
%attr(0755,root,root) /usr/lib/kwtools/sys/kwrunlevconf
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwauth
%attr(0644,root,root) /usr/share/kwtools/functions/kwauth/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwgrub
%attr(0644,root,root) /usr/share/kwtools/functions/kwgrub/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwnetcardconf
%attr(0644,root,root) /usr/share/kwtools/functions/kwnetcardconf/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwlogrotate
%attr(0644,root,root) /usr/share/kwtools/functions/kwlogrotate/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwssl
%attr(0644,root,root) /usr/share/kwtools/functions/kwssl/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwwvdialconf
%attr(0644,root,root) /usr/share/kwtools/functions/kwwvdialconf/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwrunlevconf
%attr(0644,root,root) /usr/share/kwtools/functions/kwrunlevconf/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwauth
%attr(0644,root,root) /usr/share/kwtools/help/kwauth/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwclock
%attr(0644,root,root) /usr/share/kwtools/help/kwclock/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwnetcardconf
%attr(0644,root,root) /usr/share/kwtools/help/kwnetcardconf/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwnetconf
%attr(0644,root,root) /usr/share/kwtools/help/kwnetconf/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwlogrotate
%attr(0644,root,root) /usr/share/kwtools/help/kwlogrotate/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwssl
%attr(0644,root,root) /usr/share/kwtools/help/kwssl/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwgroup
%attr(0644,root,root) /usr/share/kwtools/help/kwgroup/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwgrub
%attr(0644,root,root) /usr/share/kwtools/help/kwgrub/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwuser
%attr(0644,root,root) /usr/share/kwtools/help/kwuser/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwwvdialconf
%attr(0644,root,root) /usr/share/kwtools/help/kwwvdialconf/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwrunlevconf
%attr(0644,root,root) /usr/share/kwtools/help/kwrunlevconf/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwauth_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwclock_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwgroup_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwgrub_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwlogrotate_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwnetconf_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwssl_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwuser_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwwvdialconf_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwrunlevconf_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-sys
%attr(0644,root,root) /usr/share/doc/kwtools-sys/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-sys/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-sys/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man5
%attr(0644,root,root) /usr/share/man/de/man5/kwsslrc.5.gz
%attr(0644,root,root) /usr/share/man/de/man5/kwuserrc.5.gz
%attr(0755,root,root) %dir /usr/share/man/de/man8
%attr(0644,root,root) /usr/share/man/de/man8/kwauth.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwclock.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwgrub.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwgroup.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwlogrotate.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwnetcardconf.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwnetconf.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwssl.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwuser.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwwvdialconf.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwrunlevconf.8.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwauth.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwclock.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwgrub.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwgroup.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwlogrotate.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwnetcardconf.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwnetconf.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwssl.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwuser.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwwvdialconf.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwrunlevconf.mo

%files sys-fuse
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools
%attr(0755,root,root) %dir /usr/lib/kwtools/sys
%attr(0755,root,root) /usr/lib/kwtools/sys/kwfuse
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwfuse
%attr(0644,root,root) /usr/share/kwtools/functions/kwfuse/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwfuse
%attr(0644,root,root) /usr/share/kwtools/help/kwfuse/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwfuse_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-sys-fuse
%attr(0644,root,root) /usr/share/doc/kwtools-sys-fuse/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-sys-fuse/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-sys-fuse/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man8
%attr(0644,root,root) /usr/share/man/de/man8/kwfuse.8.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwfuse.mo

%files sys-crypt
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/bin
%attr(0755,root,root) %dir /usr/lib/kwtools/sys
%attr(0755,root,root) /usr/lib/kwtools/sys/kwcrypt
%attr(0755,root,root) /usr/lib/kwtools/kwecryptfs
%attr(0755,root,root) /usr/lib/kwtools/kwcryptsetup
%attr(0755,root,root) /usr/lib/kwtools/kwlosetup
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwecryptfs
%attr(0644,root,root) /usr/share/kwtools/functions/kwecryptfs/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwcryptsetup
%attr(0644,root,root) /usr/share/kwtools/functions/kwcryptsetup/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwlosetup
%attr(0644,root,root) /usr/share/kwtools/functions/kwlosetup/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwcrypt
%attr(0644,root,root) /usr/share/kwtools/help/kwcrypt/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwecryptfs
%attr(0644,root,root) /usr/share/kwtools/help/kwecryptfs/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwcryptsetup
%attr(0644,root,root) /usr/share/kwtools/help/kwcryptsetup/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwlosetup
%attr(0644,root,root) /usr/share/kwtools/help/kwlosetup/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwcrypt_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-sys-crypt
%attr(0644,root,root) /usr/share/doc/kwtools-sys-crypt/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-sys-crypt/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-sys-crypt/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man5
%attr(0644,root,root) /usr/share/man/de/man5/kwecryptfsrc.5.gz
%attr(0644,root,root) /usr/share/man/de/man5/kwcryptsetuprc.5.gz
%attr(0644,root,root) /usr/share/man/de/man5/kwlosetuprc.5.gz
%attr(0755,root,root) %dir /usr/share/man/de/man8
%attr(0644,root,root) /usr/share/man/de/man8/kwcrypt.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwecryptfs.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwcryptsetup.8.gz
%attr(0644,root,root) /usr/share/man/de/man8/kwlosetup.8.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwlosetup.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwecryptfs.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwcryptsetup.mo

%files sys-kwpasswd
%attr(0755,root,root) %dir /usr/bin
%attr(0755,root,root) /usr/bin/firstlogin
%attr(0755,root,root) %dir /etc/skel/.kde/Autostart
%attr(0644,root,root) /etc/skel/.kde/Autostart/firstlogin.desktop
%attr(0755,root,root) %dir /etc/skel/.config/autostart
%attr(0644,root,root) /etc/skel/.config/autostart/firstlogin.desktop
%attr(0644,root,root) /etc/skel/.firstlogin
%attr(0644,root,root) /etc/skel/.bash_login
%attr(0755,root,root) %dir /usr/lib/kwtools/sys
%attr(0755,root,root) /usr/lib/kwtools/sys/kwpasswd
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwpasswd
%attr(0644,root,root) /usr/share/kwtools/help/kwpasswd/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwpasswd_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-sys-kwpasswd
%attr(0644,root,root) /usr/share/doc/kwtools-sys-kwpasswd/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-sys-kwpasswd/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-sys-kwpasswd/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/kwpasswd.1.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwpasswd.mo

%files sys-lvm
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools
%attr(0755,root,root) %dir /usr/lib/kwtools/sys
%attr(0755,root,root) /usr/lib/kwtools/sys/kwlvm
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwlvm
%attr(0644,root,root) /usr/share/kwtools/functions/kwlvm/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwlvm
%attr(0644,root,root) /usr/share/kwtools/help/kwlvm/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwlvm_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-sys-lvm
%attr(0644,root,root) /usr/share/doc/kwtools-sys-lvm/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-sys-lvm/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-sys-lvm/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man8
%attr(0644,root,root) /usr/share/man/de/man8/kwlvm.8.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwlvm.mo

%files sys-parted
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools/sys
%attr(0755,root,root) /usr/lib/kwtools/sys/kwparted
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwparted
%attr(0644,root,root) /usr/share/kwtools/functions/kwparted/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwparted
%attr(0644,root,root) /usr/share/kwtools/help/kwparted/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwparted_help
%attr(0755,root,root) %dir /usr/share/man/de/man8
%attr(0644,root,root) /usr/share/man/de/man8/kwparted.8.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwparted.mo

%files sys-quota
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools
%attr(0755,root,root) %dir /usr/lib/kwtools/sys
%attr(0755,root,root) /usr/lib/kwtools/sys/kwquota
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwquota
%attr(0644,root,root) /usr/share/kwtools/functions/kwquota/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwquota
%attr(0644,root,root) /usr/share/kwtools/help/kwquota/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwquota_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-sys-quota
%attr(0644,root,root) /usr/share/doc/kwtools-sys-quota/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-sys-quota/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-sys-quota/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man8
%attr(0644,root,root) /usr/share/man/de/man8/kwquota.8.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwquota.mo

%files sys-raid
%attr(0755,root,root) %dir /usr/sbin
%attr(0755,root,root) %dir /usr/lib/kwtools
%attr(0755,root,root) %dir /usr/lib/kwtools/sys
%attr(0755,root,root) /usr/lib/kwtools/sys/kwraid
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwraid
%attr(0644,root,root) /usr/share/kwtools/help/kwraid/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/sys_kwraid_help
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwraid
%attr(0644,root,root) /usr/share/kwtools/functions/kwraid/*
%attr(0755,root,root) %dir /usr/share/doc/kwtools-sys-raid
%attr(0644,root,root) /usr/share/doc/kwtools-sys-raid/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-sys-raid/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-sys-raid/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man8
%attr(0644,root,root) /usr/share/man/de/man8/kwraid.8.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwraid.mo

%files utils
%attr(0755,root,root) %dir /usr/bin
%attr(0755,root,root) %dir /usr/lib/kwtools
%attr(0755,root,root) /usr/lib/kwtools/kwbackup_cron
%attr(0755,root,root) %dir /usr/lib/kwtools/utils
%attr(0755,root,root) /usr/lib/kwtools/utils/kwbackup
%attr(0755,root,root) /usr/lib/kwtools/utils/kwgpgcrypt
%attr(0755,root,root) /usr/lib/kwtools/utils/kwmuttprintcf
%attr(0755,root,root) /usr/lib/kwtools/utils/kwpwsafe
%attr(0755,root,root) /usr/lib/kwtools/utils/kwvmstat
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwbackup
%attr(0644,root,root) /usr/share/kwtools/functions/kwbackup/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwgpgcrypt
%attr(0644,root,root) /usr/share/kwtools/functions/kwgpgcrypt/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwmuttprintcf
%attr(0644,root,root) /usr/share/kwtools/functions/kwmuttprintcf/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwpwsafe
%attr(0644,root,root) /usr/share/kwtools/functions/kwpwsafe/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwvmstat
%attr(0644,root,root) /usr/share/kwtools/functions/kwvmstat/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwbackup
%attr(0644,root,root) /usr/share/kwtools/help/kwbackup/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwgpgcrypt
%attr(0644,root,root) /usr/share/kwtools/help/kwgpgcrypt/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwmuttprintcf
%attr(0644,root,root) /usr/share/kwtools/help/kwmuttprintcf/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwpwsafe
%attr(0644,root,root) /usr/share/kwtools/help/kwpwsafe/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwvmstat
%attr(0644,root,root) /usr/share/kwtools/help/kwvmstat/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/utils_kwbackup_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/utils_kwgpgcrypt_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/utils_kwmuttprintcf_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/utils_kwpwsafe_help
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/utils_kwvmstat_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-utils
%attr(0644,root,root) /usr/share/doc/kwtools-utils/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-utils/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-utils/prerm.rpm
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/kwbackup.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwgpgcrypt.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwmuttprintcf.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwpwsafe.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwbackup_cron.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwvmstat.1.gz
%attr(0755,root,root) %dir /usr/share/man/de/man5
%attr(0644,root,root) /usr/share/man/de/man5/kwbackuprc.5.gz
%attr(0644,root,root) /usr/share/man/de/man5/kwvmstatrc.5.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwbackup.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwgpgcrypt.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwmuttprintcf.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwpwsafe.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwbackup_cron.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwvmstat.mo

%files utils-pim
%attr(0755,root,root) %dir /usr/lib/kwtools
%attr(0755,root,root) /usr/lib/kwtools/create.cal.pl
%attr(0755,root,root) /usr/lib/kwtools/kwholiday
%attr(0755,root,root) /usr/lib/kwtools/kwtex-cal
%attr(0755,root,root) /usr/lib/kwtools/kwtermin
%attr(0755,root,root) /usr/lib/kwtools/kwtermin_cron
%attr(0755,root,root) %dir /usr/lib/kwtools/utils
%attr(0755,root,root) /usr/lib/kwtools/utils/kwplaner
%attr(0755,root,root) %dir /usr/share/kwtools/data/calendar
%attr(0644,root,root) /usr/share/kwtools/data/calendar/calendar.tex
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwplaner
%attr(0644,root,root) /usr/share/kwtools/functions/kwplaner/*
%attr(0755,root,root) %dir /usr/share/kwtools/functions/kwtermin
%attr(0644,root,root) /usr/share/kwtools/functions/kwtermin/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwplaner
%attr(0644,root,root) /usr/share/kwtools/help/kwplaner/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwtermin
%attr(0644,root,root) /usr/share/kwtools/help/kwtermin/*
%attr(0755,root,root) %dir /usr/share/kwtools/help/kwadmin
%attr(0644,root,root) /usr/share/kwtools/help/kwadmin/utils_kwplaner_help
%attr(0755,root,root) %dir /usr/share/doc/kwtools-utils-pim
%attr(0644,root,root) /usr/share/doc/kwtools-utils-pim/copyright
%attr(0755,root,root) /usr/share/doc/kwtools-utils-pim/postinst.rpm
%attr(0755,root,root) /usr/share/doc/kwtools-utils-pim/prerm.rpm
%attr(0755,root,root) %dir /usr/share/doc/kwtools-utils-pim/examples
%attr(0755,root,root) /usr/share/doc/kwtools-utils-pim/examples/call-jpeg2ps.zsh
%attr(0755,root,root) %dir /usr/share/man/de/man1
%attr(0644,root,root) /usr/share/man/de/man1/create.cal.pl.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwholiday.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwtex-cal.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwplaner.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwtermin.1.gz
%attr(0644,root,root) /usr/share/man/de/man1/kwtermin_cron.1.gz
%attr(0755,root,root) %dir /usr/share/man/de/man5
%attr(0644,root,root) /usr/share/man/de/man5/kwplanerrc.5.gz
%attr(0755,root,root) %dir /usr/share/locale/en/LC_MESSAGES
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwholiday.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwtex-cal.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwplaner.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwtermin.mo
%attr(0644,root,root) /usr/share/locale/en/LC_MESSAGES/kwtermin_cron.mo

# postinstall Scripts
%post bin
/usr/share/doc/kwtools-bin/postinst.rpm

%post common
/usr/share/doc/kwtools-common/postinst.rpm

%post graphic
/usr/share/doc/kwtools-graphic/postinst.rpm

%post multi
/usr/share/doc/kwtools-multi/postinst.rpm

%post net
/usr/share/doc/kwtools-net/postinst.rpm

%post net-djbdns
/usr/share/doc/kwtools-net-djbdns/postinst.rpm

%post net-mutt
/usr/share/doc/kwtools-net-narc/postinst.rpm

%post net-narc
/usr/share/doc/kwtools-net-narc/postinst.rpm

%post net-openmosix
/usr/share/doc/kwtools-net-openmosix/postinst.rpm

%post net-postfix
/usr/share/doc/kwtools-net-postfix/postinst.rpm

%post sys
/usr/share/doc/kwtools-sys/postinst.rpm

%post sys-crypt
/usr/share/doc/kwtools-sys-crypt/postinst.rpm

%post sys-fuse
/usr/share/doc/kwtools-sys-fuse/postinst.rpm

%post sys-kwpasswd
/usr/share/doc/kwtools-sys-kwpasswd/postinst.rpm

%post sys-lvm
/usr/share/doc/kwtools-sys-lvm/postinst.rpm

%post sys-parted
/usr/share/doc/kwtools-sys-parted/postinst.rpm

%post sys-quota
/usr/share/doc/kwtools-sys-quota/postinst.rpm

%post sys-raid
/usr/share/doc/kwtools-sys-raid/postinst.rpm

%post utils
/usr/share/doc/kwtools-utils/postinst.rpm

%post utils-pim
/usr/share/doc/kwtools-utils-pim/postinst.rpm

# preuninstall Scripts
%preun bin
/usr/share/doc/kwtools-bin/prerm.rpm

%preun common
/usr/share/doc/kwtools-common/prerm.rpm

%preun graphic
/usr/share/doc/kwtools-graphic/prerm.rpm

%preun multi
/usr/share/doc/kwtools-multi/prerm.rpm

%preun net
/usr/share/doc/kwtools-net/prerm.rpm

%preun net-djbdns
/usr/share/doc/kwtools-net-djbdns/prerm.rpm

%preun net-mutt
/usr/share/doc/kwtools-net-narc/prerm.rpm

%preun net-narc
/usr/share/doc/kwtools-net-narc/prerm.rpm

%preun net-openmosix
/usr/share/doc/kwtools-net-openmosix/prerm.rpm

%preun net-postfix
/usr/share/doc/kwtools-net-postfix/prerm.rpm

%preun sys
/usr/share/doc/kwtools-sys/prerm.rpm

%preun sys-crypt
/usr/share/doc/kwtools-sys-crypt/prerm.rpm

%preun sys-fuse
/usr/share/doc/kwtools-sys-fuse/prerm.rpm

%preun sys-kwpasswd
/usr/share/doc/kwtools-sys-kwpasswd/prerm.rpm

%preun sys-lvm
/usr/share/doc/kwtools-sys-lvm/prerm.rpm

%preun sys-parted
/usr/share/doc/kwtools-sys-parted/prerm.rpm

%preun sys-quota
/usr/share/doc/kwtools-sys-quota/prerm.rpm

%preun sys-raid
/usr/share/doc/kwtools-sys-raid/prerm.rpm

%preun utils
/usr/share/doc/kwtools-utils/prerm.rpm

%preun utils-pim
/usr/share/doc/kwtools-utils-pim/prerm.rpm

%changelog
* Fri Jan 08 2010 Kai Wilke <kiste@netzworkk.de>
- new Scripts kwecryptfs, kwmutt, kwmuttprintcf, kwpwsafe, firstlogin
  and kwpasswd.
- Scripts/functions: all back, save, delete, exit menupoints
  change to variables $gv_Back, $gv_....
- new option in mount_check function: -c - check mount or no mount.
- new option in count_display_line function: -f - check lines for
  dialogbox mixedform.
- kwnarcconf: ALLOW_* input messages fixed.
- kwtermin: sort terminfile.
- kwcal-tex: choice menu for holidays/birthdays to create calendar.
- new functions set_filetype, filetype and mixedform.
- kwquota: choice Bug fixed.
- kwtools zsh options are to reconfigure and smaller.
- updates from (un)install scripts.
- kwpostfix: update to kwtools funktions.
- kwrsync: used rsync daemon too.
- Function rsh_ssh renamed to remote_sh.
- delete functions fhost, no_group_msg, no_user_msg.
- manpages: customized
- kwraid: configuration (mdadm.conf) created.
- kwlvm: can with encrypt devices (cryptsetup) and has support
  for UUID and LABEL.
- kwcryptsetup: has support for UUID and LABEL.
- kwuser: has configuration and support for QUOTA.
- kwauth: is new and has support for local and NIS-authenticication.
- kwrunlevconf: Support for openrc (gentoo) removed.

* Sun Oct 12 2008 Kai Wilke <kiste@netzworkk.de>
- kwparted: Status display/Help bug fixed. The calculation of
  partition size to changed (KByte -> Byte).
- kwquota: Support for "JFS" filesystem. Support for warnquota
  to configure.
- only support udev (filesystems).
- kwwvdialconf: Support for tel-nr (*99# - Handy data).
- to calculate the drive size was bettered.
- kwnetcardconf: Support for WLAN Configuration.
- Function convert_drive_size: calculation of *Byte bettered.
- Function os_check update (Fedora -> fedora, cat /proc/version)
- Scripts update to os_check.
- new function check_part_fs (filesystemtyp) and convert_si_size
  (1MByte = 1000.000 Byte).
- kwvmstat: new - no part to display - Info message.
- kwgrub: delete Bug fixed.
- main.cf and functions kwadmin_config - support for color update.
- kwrunlevconf: Support for openrc (gentoo).
- kwpostfix: *delimiter* to exist are earmarked for dialogbox.
- kwuser: more then one user to create.

* Fri Jul 11 2008 Kai Wilke <kiste@netzworkk.de>
- kwparted: Status display bug fixed.
- kwquota: Support for "JFS" filesystem.
- only support udev (filesystems).

* Mon Jul 07 2008 Kai Wilke <kiste@netzworkk.de>
- manpages (1) updatet: docbook-{xml,xslt}.
- kwquota: support for usr- and grpquota simultan.
  prjquota (xfs) is only seperat support (man 8 xfs_quota).

* Thu Jun 26 2008 Kai Wilke <kiste@netzworkk.de>
- manpages (5,8) updatet; docbook-{xml,xslt}.
- kwgroup/kwuser: add new options and display.
- kwquota: create.
- function read_fstab: simplified.
- function search_packages: new variables NO_PACKAGES(_E).
- new function no_package_inst_msg.

* Sun May 11 2008 Kai Wilke <kiste@netzworkk.de>
- kwrip: Bug mit mount Verzeichnissen gefixt.
- help files in "locale system" to integrated.
- kwadmin; add new colors.
- kwfirewall and narc to merged.
- kwnarc to renamed -> kwnarcconf.
- upgrade uninstall script.
- kwvmstat: add new Options.
- kwcryptsetup: add display /etc/crypttab.
- kwproxy: Bug in to read the proxy file fixed.
- kwnetstat: add new options.

* Fri Mar 21 2008 Kai Wilke <kiste@netzworkk.de>
- many new functions
- all system functions merged to script_init, sys_conf, fs_conf,
  hw_conf, multi_conf, net_conf and check_spacial_character.
- multi_conf functions updated (KB->YB).
- new Script kwxen-tools (Alpha).
- po file from kwtools-common extended.
- Script raid renamed to kwraid and have gauge for create and
  raidhot_add_remove. Support for raidtools(2) to removed.
- Script kwrsync - new help.
- Script runlevconf renamed to kwrunlevconf.
- Script gpgcrypt renamed to kwgpgcrypt.
- Script planer renamed to kwplaner.
- Scripts termin* renamed to kwtermin*.
- Script kwtermin_cron - Bug fixed in display from mail.
- kwgrub has support for module, savedefault and lock.
- kwrecord/cd_dvd_burn has support for mkisofs options and
  correctly conversion from medium size to KBytesize.
- kwcamera has gauge, choice and preview support. display Bug fixed.
- function gauge has support for variable display size.
- new functions count_msg_char, count_char_to_line.
- new devel dokumentation (html).
- kwadmin support for PAGER/EDITOR Variable (Configuration)
  and update mapages (main.cf.5, kwadmin.1).
- new screenshots.
- kwproxy and kwfirewall (help) updated.
- kwrip has support to gauge and encode (mp3,ogg).
- kwvcdburn has support to create photo-cd.
- kwfilm2film used "mplex" instead "tcmplex".
- new functions editbox, dselect and dselect_check.
- old fselect* functions renamed to dselect* (directory choice/check).
- new fselect* functions (file choice/check).
- many functions menubox/check-/radiolist/... have variable columns
  size to display.
- new functions check_size (Directory size) and check_home_conf_dir.
- new functions convert_over_size, check_cd_state and check_dvd_state.
- new functions check_number - once check_integer.
- check_integer is now only.
- Script kwcryptsetup have support for option "luksKillSlot".
  up to Release >=1.0.6
- kwparted to verify the partitions table before create a backup from disk.
- kwtools has supported KByte up to ZB -
  ZettaByte=1.180.591.620.717.411.303.424 Byte
- kwrecord can CD/DVD copy with 1 drive.

* Sat Jun 23 2007 Kai Wilke <kiste@netzworkk.de>
- the functions resize_fs and mount_check for Debian/sid updated.
- Script termin_cron Bug fixed, not removed the directory in ~/tmp
- update kwrsync_backup (help, config, man5, html)
- rename djbdns and proxy to kwdjbdns and kwproxy (manpage too).
- update kwdjbdns (Attention display, help, html)

* Sun May 13 2007 Kai Wilke <kiste@netzworkk.de>
- functions lvm_version and os_check updated.

* Thu Apr 19 2007 Kai Wilke <kiste@netzworkk.de>
- function cd_driver updated.
- Script kwrip updated (full CD rip).
- Scripts vcdburn, vdvdburn, snd2sndfm rename to kw${Old_Name}
- function for update from configurations files from scripts to rename.

* Sun Apr 08 2007 Kai Wilke <kiste@netzworkk.de>
- Script cdrip rename to kwrip and add gauge.
  Support to configure the rip, CDDB and CDDB server options for Audio.
- Script camera rename to kwcamera.
- Script kwlogrotate updated.

* Tue Apr 03 2007 Kai Wilke <kiste@netzworkk.de>
- function kwrsync_backup_exec - display for mails (cron - subject) updated.
- function script_backtitle - year updated.
- functions if_conf_file, kwgrub_conf for grub extended.
  (hiddenmenu and splashimage).
- manpages from kwgrub.8, kwrecord.1, snd2sndfmrc.5, snd2sndfm.1
  and cd_dvdrc.5 updated.
- function cd_dvd_burn add CDDB Support (only Option --cdcopy),
  on-the-fly and tmp directory.
- function cd_driver supported flags for cdrdao driver.
- function kwrecord_conf supported configuration from a tmp directory,
  CDDB and the Option on-the-fly.
- snd2sndfm can configure the decode and encode options.
- functions mount_check and resize_fs added readlink for devices.
- docs, help updated.
- function file_filter for MP3 updated.
- Bugs fixed and BUGS file updated (cd_dvd_burn+mkisofs).

* Fri Mar 09 2007 Kai Wilke <kiste@netzworkk.de>
- add autoload function cd_dvd_conf in cd_dvd_burn.
- function cd_dvd_burn support for iso-dvd.
- Script vdvdburn - composite bug for ppmtoy4m fixed.

* Sat Feb 23 2007 Kai Wilke <kiste@netzworkk.de>
- changeover to the gettext finished.
- first insert from function sys_logger.
- function if_conf_file for runlevconf upgraded.
- kwclock for opensuse upgraded.
- remotesync rename to kwrsync and upgraded.
- kwrecord - no check setuid of program cdrdao >=1.2.2.
- Support for Fedora6 in different functions and scripts.
- Script kwnetcardconf upgraded.
- more locale C support (export LC_ALL=C ; command), simplification of
  evaluation from variablen

* Mon Dec 18 2006 Kai Wilke <kiste@netzworkk.de>
- The function crontbconf can accurate the cronjob configuration for
  select script.
- Bugfixing in /etc/init.d/kwfirewall and kwuser.
- kwpostfix function smtp_conf finished.

* Fri Dec 15 2006 Kai Wilke <kiste@netzworkk.de>
- po files update and upgrade.
- Many files adapted to po files (Language en).
- kwrsync_backup_cron mailt the logfile.
- kwrecord - new item DVD-copy.

* Mon Nov 27 2006 Kai Wilke <kiste@netzworkk.de>
- Bug in kwtools-sys-crypt.postinst fixed.
- Doku/help from kwrsync_backup upgradet.
- kwrsync_backup's Konfiguration and function
  kwrsync_backup_exec upgradet.

* Sun Nov 22 2006 Kai Wilke <kiste@netzworkk.de>
- Display Bug - in function cd_dvd_burn fixed.
- kwcryptsetup help extended.
- Functions no_fs_type_msg, number_input, convert_drive_size,
  resize_fs, no_prog_exec_msg and prog_check changed.
- New function copy_fs (fs cloning).
- kwparted can clone fs now.
- kwparted manpage updated.
- Function convert_drive_size extended.
- Scripts kwlvm, kwpostfix, raid and gpgcrypt to use function
  view_file for display.

* Mon Oct 30 2006 Kai Wilke <kiste@netzworkk.de>
- new script kwcrypt - a wrapper for cryptsetup and loop-aes-utils.
- new script kwcryptsetup.
- new function lo_setup - for kwcryptsetup and kwlosetup.
- script kwlosetup upgrade.
- Script snd2sndfm upgrade (burn).
- Bug in function vg_group deleted.
- in function fhost upgrade, then in /proc is icmp_echo_ignore_broadcasts=1.
- Outsourcing from functions of kwlvm (lv_free_size, ...).
- Help from kwlosetup/kwcryptsetup to extend kernel parameter - max_loop=Count
- New function convert_drive_size (in KiloByte) and mount_path.
- html Dokumetation extended.
- functions format (reiser*), mount_check (-fs) upgrade.

* Fri Sep 19 2006 Kai Wilke <kiste@netzworkk.de>
- function read_file read in /root, when used programm "sudo", su-to-root,...
- all Scripts with function root_check read the configuration file in
  /root/.kwtools/.
- Bug in function vg_groups from script kwlvm fixed.

* Tue Sep 05 2006 Kai Wilke <kiste@netzworkk.de>
- function lvm_version - Bug for RPM rested distributions fixed.
- function if_conf_prog - support for CentOS and RedHat by mail
  and raid.
- upgrade help for script raid.
- upgrade scripts gpgcrypt, kwholiday and kwssl.
- function search_packages - Bug for rpm fixed

* Tue Aug 29 2006 Kai Wilke <kiste@netzworkk.de>
- Script runlevconf - upgrade for sysv-rc.
 
* Thu Aug 24 2006 Kai Wilke <kiste@netzworkk.de>
  * Init Script kwfirewall upgrade
  * Function default_menu_lst (kwgrub) evacuated.
  * Script kwclock - new input "Option" for ntpdate (only Debian).
  * In functions and Scripts Bugs fixed (gettext, display).

* Sat Aug 11 2006 Kai Wilke <kiste@netzworkk.de>
- html Dokumentation of devel is actual.
- delete functions ssh, cd_convert, u_mask and form2 and to adapt
  to some functions.

* Fri Aug 04 2006 Kai Wilke <kiste@netzworkk.de>
- add function no_dezimal_msg.
- duplicate help directory kwlogrotate delete.
- small Bug in kwtools-common fixed (gettext).
- function termin_change is themen sorted.

* Sat Jul 29 2006 Kai Wilke <kiste@netzworkk.de>
- function no_perm_prog_msg - message display fixed.
- functions para_conf and net_config false char.

* Wed Jul 26 2006 Kai Wilke <kiste@netzworkk.de>
- kwgrub - Bug (gettext+menubox) in function kwgrub_boot_conf fixed.
- kwparted - multi Flags selectable, font problem (utf-8) solved.
- in kwlogrotate/kwwvdialconf small Bugs fixed.
- runlevconf - no break when no found package sysv-rc or file-rc
  (SuSE has package aaa_base).
- function net_config for centos upgraded.
- script camera - modell choice for CentOS fixed.
- Support for CentOS >=4.0, SuSE >=8.0, Debian >=3.0, tested  on
  CentOS-4.{0,3}, SuSE-{8,10.0} und Dabian Sarge/sid.

* Sat Jul 22 2006 Kai Wilke <kiste@netzworkk.de>
- function lock - miscall positions parameter fixed.
- kwuser/kwgroup - upgrade.
- kwparted support for parted version >=1.7.0.
- function number_input extented (-z = dezimal).
- Initscript kwfirewall is LSB konform.
- planer - configuration upgrade.
- paket kwtools-utils - internationalisation failed.

* Wed Jul 19 2006 Kai Wilke <kiste@netzworkk.de>
- djbdns - functions tinydns_management, a break failed.
- function fhost Bug fixed.
- kwrsync_backup - display delete the last directory,
  (snapshot.7).

* Wed Jul 05 2006 Kai Wilke <kiste@netzworkk.de>
- function kwrecord_conf failed in kwtools-multi*.deb.
- kwpostfix - smtpd configuration extended.

* Sat Jul 01 2006 Kai Wilke <kiste@netzworkk.de>
- many functions renamed and new (see README.kwtools).
- many functions/scripts bugs gefixt and change to code.
- install and uninstall are better (Support Locale and create program
  links).

* Sat Jun 24 2006 Kai Wilke <kiste@netzworkk.de>
- kwpostfix - upgrade from pgsql/mysql and ldap.
- kwpostfix - upgrade from sql/ldap help files.
- kwpostfix - upgrade from *_table functions.
- kwpostfix - support for cdb format.

* Sat Jun 03 2006 Kai Wilke <kiste@netzworkk.de>
- raid - spelling mistake fixt (help).
- function fusetab_input (kwfuse) - menupoint uid and gid upgrade.
- function fusetab_input (kwfuse) - support for network filesystems.
- kwfuse - support for different location from fuse.conf.
- function lv_volumes (kwlvm) - error messages handling upgrade.
- kwnetconf - configuration from /etc/wvdial.conf with $EDITOR.

* Tue May 30 2006 Kai Wilke <kiste@netzworkk.de>
- error messages entry for kwnetcardconf lacked.
- kwgrub Bugs fixt.
- kwlosetup Bugs fixt - same title and messages lacked.
- kwtools.spec to refitted.

* Sat May 27 2006 Kai Wilke <kiste@netzworkk.de>
- kwlogrotate - 1 Bug fixt (DATEI -> LOGDATEI).
- runlevconf - is better, configuration for runlevel S and
  Support for file-rc
- add overrides files for lintian
- change kwnetconf to kwnetcardconf
- add porting from grml-network to kwnetconf
- function gauge is the first time in action (kwnetconf).
- function netcard to use new format for Variable DEVICE_LIST
  "interface_card_Macaddress_driver" and to use the tool ethtool.

* Mon May 21 2006 Kai Wilke <kiste@netzworkk.de>
- snd2sndfm - delete progessbox.
- kwnetconf - delete echo in line 33 and Bugfixing (manual_netconf).
- function route_check is better
- install Script is better

* Mon May 20 2006 Kai Wilke <kiste@netzworkk.de>
- kwnarc - Bugs gefixt.
- Bugs for english, in files, fixt - zurueck|break) -> $gv_Back)

 -- Kai Wilke <kiste@netzworkk.de>  Sat, 20 May 2006 00:23:24 +0100

* Mon May 01 2006 Kai Wilke <kiste@netzworkk.de>
- openmosix - in para_conf, a title lacked.
- djbdns - Bugs gefixt.
- Bug in message file title gefixt.
- film2film bugs gefixt (display).
- kwlvm - ntfs support.
- kwadmin - configuration is better.
- Bug in kwrsync_backup_rotate gefixt.
- Bug in cd_dvd_burn (PREGAP * -> SILENCE 00:02:00 // pre-gap) gefixt.

* Tue Apr 11 2006 Kai Wilke <kiste@netzworkk.de>
- root_check - to use sudo or su-to-root, or su.
- bugfixing - *(Hh)ilfe*|*(Hh)elp*) -> HELP*)

* Fri Apr 07 2006 Kai Wilke <kiste@netzworkk.de>
- kwuser to use the functions is_value and generate_ist_file.
- kwuser - user to change to need no password.
- new function is_value.
- new script kwfuse, a frontend for fuse.

* Tue Mar 28 2006 Kai Wilke <kiste@netzworkk.de>
- Bug fixed in function kwrsync_backup_exec.
- kwparted created swap signature.
- kwnarc - dialog rested Port Forwarding Configuration.
- all dialogboxes to own locale support.
- new functions infobox, progressbox, route_check and dialog_version.
- kwrecord/cd_dvd_burn - check for CD/DVD in drive and empty CD/DVD. 
- kwnetconf, configuration from gateway is better (route_check). 
- many scripts to use the function progressbox.
- install script compile the functions directorys
- kwbackup, backup from files to change/create the last 7 days is better.
- kwlvm xfs_growfs Bug gefixt.
  
* Thu Mar 16 2006 Kai Wilke <kiste@netzworkk.de>
- lv_volumes - Size Bug gefixt.
- function disk exported the Variablen.
  
* Wed Mar 15 2006 Kai Wilke <kiste@netzworkk.de>
- firewall Frontend kwnarc for the Script "narc" kam hinzu.

* Sat Feb 25 2006 Kai Wilke <kiste@netzworkk.de>
- almost to conform to lintian
- manpages (de) for all Scripts
- new termin Scripts (termin, termin_cron).
- Bugs gefixt.
- name for the function calendar changed to calendarbox.
- raid management for kwlvm and raid (raidhotadd_remove) is better.
- all scripts have english names.
- feiertage -> kwholiday, jahrprint -> kwtex-cal, uhr -> kwclock.

* Sat Jan 21 2006 Kai Wilke <kiste@netzworkk.de>
- new functions timebox & calendar
- Script uhr to use the functions timebox & calendar
- Bugs gefixt
- manpage kwfirewall (man 8 kwfirewall)

* Mon Jan 16 2006 Kai Wilke <kiste@netzworkk.de>
- Generation of packets was improved. changelog, changelog.de, 
  changelog.Debian and README.Debian are now handled by
  dh_installchangelogs and dh_installdocs.
- The administration of Debian by kwtools-net-firewall was improved.

* Mon Nov 07 2005 Kai Wilke <kiste@netzworkk.de>
- Proxy still had a bug in the ftp proxys configuration.
- kwlvm can now convert VG's metadata in case lvm2 is installed.
- When deleting CD-R/W's it is checked whether cdrdao has suid rights.
- kwpostfix, kwgrub, kwuser and pgpcrypt were adapted to the changed 
  password function.
- One now has to assign a minimum length of key to password function.
- The script kwlosetup was added. This script can encrypt drives and
  generate encrypted containers.
- File system reiser4 was added to formatprogs_check.
- The function format can now deal with mkfs.reiser4.
- The function search_packages was added and checks whether the delivered
  packet names are installed.
- The script kwlosetup was added and can generate encrypted containers
  (files with file system), partitions and logical volumes.
- The scripts kwparted and kwssl now use the new function search_packages.
- mail_conf (kwpostfix): If nothing is entered for packet management in main.cf, or
- only tar, the default value for mail_version is used (postconf -dh mail_version).
- cdrip, vcdburn, kwlosetup are asked when closed down if the mounted
  directory/device is to be unmounted.
- The function part_auswahl can offer partitions for choice with the option -s Swap.
- The function partdb has received a better handling of swap partions,
  e.g. a description is added to the end of the partition (linux swap)
- All bugs are fixed in the script termin and its functions.
- Feature text_box can now display the window size variably,
  depending on how many lines the file has.
- kwadmin no longer uses any functions to show the individual categories.

* Thu Oct 15 2005 Kai Wilke <kiste@netzworkk.de>
- kwparted can now enlargen and minimise partitions.
  Message and Help files were extended.
- Packets now have an English description.
- kwfirewall's debconf is in English and German.
- The function cd_dvd_burn still had bugs when calculating 
  and dealing with files/directories with spaces.
- The function datei_filter can now also offer directories with spaces
  to dialog.
  
%changelog
* Wed Oct 05 2005 Kai Wilke <kiste@netzworkk.de>
- kwuser had a bug when copying the /etc/skel files. 
  and one curly brace was wrong in one variable.
- Programme "dialog" only exists once under "Depends" in the packet 
  generating files in kwtols-common.
- all functions in ./functions/ were checked and extended.
  At the same time the devel-documentation was amended.
- kwnetstat had a bug when repeatedly displaying with different options.
- kwlogrotate no longer delivers a "compress" to the funktion compress_auswahl.
- Documentation now is/has a directory/packet of its own.
- kwssl now generates the missing directory structure (/etc/ssl/{certs,private}).
- The function cd_dvd_burn had wrongly repeatedly written the cdrdao.toc.
- Function read_conf can now als read pure data from files without the command source.
- Function os_check was extended by CentOS.
- All scripts were completed for Debian/SuSE/Redhat and CentOS.
- The function dhcp had a missing variable which was to be delivered.
- The function if_conf_file is completed for all supported distributions.

* Sun Sep 18 2005 Kai Wilke <kiste@netzworkk.de>
- The script kwpostfix had a bug displaying tables e.g. when the values 
  are seperated by a comma.
- The kwpostfix function regexp_table had the variable STRING1 which no
  longer existed.
- The configuration of mydestination was missing in the function 
  haupt_conf (kwpostfix).
- All lines which will begin with space are now recognised in main,cf and
  master.cf (kwpostfix).
- kwuser only copies the files from /etc/skel if the home directory has not
  yet been generated.
- The function z_host had a mistake searching for ping6 and therefore
  could not find the PC's/networks.
- The function script_init now generates the directory $HOME/tmp if not 
  available
- help was adapted in djbdns.
- The function datei_filter had a bug in the Function ist_file.
- Script kwfirewall was added and configures netfilter (firewall).
- The packet kwtools-utils was divided up into kwtools-utils and 
  kwtools-utils-pim.
- The script remotesync was moved to ./net.
- The script kwssl had a bug checking the size of newcert.pem. Apart from
  that the keys, when copying, are assigned the service names (e.g. 
  newcert.pem -> postfix_cert.pem) and saved in /etc/ssl/certs respectively 
  in /etc/ssl/private. 
  Copying works with courier*, cyrus*, postfix, sendmail and stunnel.
  kwssl can now also copy the Certificate to Courier.
- kwtools.spec still had some /usr/local paths and scsitools was swapped with
  scsi (SuSE packet name).

* Fri Jul 22 2005 Kai Wilke <kiste@netzworkk.de>
- The construct usr/*(.) was removed again from the function kwbackup_sys.
- kwpostfix now supports ldap and cidr. All table configurations were 
  revised. The main table configurations are now supportes (approx. 25). 
  Some tables only require certain types, which can only then be displayed.
  I could not test LDAP support as I do not have a LDAP server.
- 18 new restrictions have been added but can not yet all be selected.
- kwpostfix can now remove left over temporary files and repair the 
  queue structure if necessary.
- Functions h_ip_zerlegung and z_host are being prepared for IPv6.
  "ping -c 1 -b" (-b=Broadcast) is now executed for IPv6 when
  hosts, IPs, IP networks or domains are to be checked.
- NOTE: IPv6 does not yet work!
- kwpostfix has deactivated *_bind_address6 configurations because 
  I can not check these.
- openmosix's main menue was changed (display --> state). So far there
  2 selectable/interactive state displays of the cluster.
- setterm -inversescreen is now switched on by the function script_init
  no longer by functions prog_exec*.
- kwnetconf/uhr/runlevconf now use yast under OS, SuSE to accomplish 
  configuration. 

