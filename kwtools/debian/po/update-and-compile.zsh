#!/bin/zsh
#
# nur fuer den Source-Code.
#
# Datum: 04.02.2008

setopt shwordsplit extendedglob
unsetopt nomatch

# Variablen
DIR=../..
PACKAGES="kwbackup_cron kwcryptsetup kwholiday kwlosetup kwnetcardconf kwrsync_backup_cron kwtex-cal kwrsync_cron kwtermin kwtermin_cron"
PACKAGES_DIR="graphic multi net sys utils"
FUNC_DIR="${DIR}/functions"
SED_FUNC_PATH="${FUNC_DIR}/sys"

set -e

# 1. Level Scripts
for i in $PACKAGES ; {
	if grep gettext ${DIR}/${i} >/dev/null ; then
		if [ -d "${FUNC_DIR}/${i##*/}" ] ; then
			print $i
			xgettext -L Shell -o ${i##*/}/${i##*/}.pot ${DIR}/${i} ${FUNC_DIR}/${i##*/}/*
		else
			print $i
			xgettext -L Shell -o ${i}/${i}.pot ${DIR}/${i}
		fi
		cp ${i}/${i}.pot ${i}/templates.pot
	fi
}

# kwadmin
if grep gettext ${DIR}/kwadmin >/dev/null ; then
	print kwadmin
	xgettext -L Shell -o kwadmin/kwadmin.pot ${DIR}/kwadmin ${FUNC_DIR}/kwadmin/*
	cp kwadmin/kwadmin.pot kwadmin/templates.pot
fi
	
# Allgmeine Funktionen
if [ ! -d kwtools-common ] ; then
	mkdir kwtools-common
fi
#
print kwtools-common
xgettext -L Shell -d kwtools-common -o kwtools-common/kwtools-common.pot ${FUNC_DIR}/sys/*~*check_special_character
cp kwtools-common/kwtools-common.pot kwtools-common/templates.pot

# 2. Level Scripts
for p in $PACKAGES_DIR ; {
	for i in ${DIR}/${p}/* ; {
		if grep gettext $i >/dev/null ; then
			if [ -d "${FUNC_DIR}/${i##*/}" ] ; then
				print ${i##*/}
				xgettext -L Shell -o ${i##*/}/${i##*/}.pot $i ${FUNC_DIR}/${i##*/}/*
			else
				print ${i##*/}
				xgettext -L Shell -o ${i##*/}/${i##*/}.pot $i
			fi
			if [ "${i##*/}" = kwuser ] ; then
			fi
			cp ${i##*/}/${i##*/}.pot ${i##*/}/templates.pot
		fi
	}
}

if [ "$1" == "clean" ] ; then
   echo Removing garbage...
   rm -rf ./**/usr ./**/*.old.*(.) ./**/*~(.) ./**/*.mo(.)
   exit 0
fi

for i in * ; {
	if [ -d $i -a $i != old ] ; then
		pushd $i
		if [ "`ls *.po~*old.po`" ] ; then
			list="$(ls *.po~*old.po)"
			for lang in $list ; {
				x=${lang%.po}
				cp -f $x.po $x.old.po
				echo -n "Updating and compiling $x.po (${i#*/})"
				msgmerge $x.old.po ${i#*/}.pot > $x.po~ && mv $x.po~ $x.po
				msgfmt --statistics $x.po
				mkdir -p usr/share/locale/$x/LC_MESSAGES
				msgfmt -o usr/share/locale/$x/LC_MESSAGES/${i#*/}.mo $x.po
			}
		fi
		popd
	fi
}

exit 0
