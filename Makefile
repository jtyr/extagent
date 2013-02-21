####
## Author: Jiri Tyr (c) 2012-2013
####

NAME = extagent
DNAME = $(NAME)d
DESTDIR =
VERSION = $(shell grep 'Version' rpm/$(NAME).spec | awk '{print $$2}')
DISTVNAME = $(NAME)-$(VERSION)

BINDIR = $(DESTDIR)/usr/bin
ETCDIR = $(DESTDIR)/etc
CONFDIR = $(ETCDIR)/$(NAME)
DEFCONFDIR = $(ETCDIR)/$(NAME)/default
INITDDIR = $(ETCDIR)/init.d
SYSCONFIGDIR = $(ETCDIR)/sysconfig
LOGROTDIR = $(ETCDIR)/logrotate.d
VARDIR = $(DESTDIR)/var
LOGDIR = $(VARDIR)/log/$(NAME)

PERLRUN = perl
DIST_CP = best
TAR = tar
TARFLAGS = cvf
COMPRESS = gzip --best --force
RM_RF = rm -rf
TEST = test
ECHO = echo
CP = cp
MKDIR_P = mkdir -p
CD = cd
SVN = svn
P4 = p4
TOUCH = touch


.PHONY: install uninstall manifest dist clean svn perforce


all : install


install :
	$(MKDIR_P) $(BINDIR) \
		$(CONFDIR) \
		$(DEFCONFDIR) \
		$(LOGDIR) \
		$(LOGROTDIR) \
		$(INITDDIR) \
		$(SYSCONFIGDIR)
	$(CP) bin/* $(BINDIR)
	$(CP) conf/$(NAME).conf $(CONFDIR)
	$(CP) conf/default/*.conf $(DEFCONFDIR)
	$(CP) logrotate/$(NAME) $(LOGROTDIR)
	$(CP) init.d/$(DNAME) $(INITDDIR)
	$(CP) sysconfig/$(DNAME) $(SYSCONFIGDIR)
	$(TOUCH) $(LOGDIR)/$(DNAME).log


manifest :
	$(PERLRUN) "-MExtUtils::Manifest=mkmanifest" -e mkmanifest
	echo 'Makefile' >> ./MANIFEST
	rm -f ./MANIFEST.bak


svn :
	@if [ `whereis -b $(SVN) | sed -e 's/.*:\s*//' -e '/^\s*$$/d' | wc -l` == 1 ]; then \
		echo "I: SVN exists..."; \
		sed -r 's/^(Release:\s*)[0-9]*/\1'`$(SVN) update | grep 'At revision' | sed -e 's/.* //' -e 's/\.//'`'/' rpm/$(NAME).spec > ./$(NAME).spec; \
	else \
		echo "I: SVN doesn't exist!"; \
	fi


perforce :
	@if [ `whereis -b $(P4) | sed -e 's/.*:\s*//' -e '/^\s*$$/d' | wc -l` == 1 ]; then \
		echo "I: Perforce exists..."; \
		sed -r 's/^(Release:\s*)[0-9]*/\1'`$(P4) changes -m 1 ...@$(P4CLIENT) | cut -d ' ' -f 2`'/' rpm/$(NAME).spec > ./$(NAME).spec; \
	else \
		echo "I: Perforce doesn't exist!"; \
	fi


dist : create_distdir
	$(TEST) -e MANIFEST
	$(TAR) $(TARFLAGS) $(DISTVNAME).tar $(DISTVNAME)
	$(RM_RF) $(DISTVNAME)
	$(COMPRESS) $(DISTVNAME).tar

create_distdir :
	$(RM_RF) $(DISTVNAME)
	$(PERLRUN) "-MExtUtils::Manifest=manicopy,maniread" \
		-e "manicopy(maniread(),'$(DISTVNAME)', '$(DIST_CP)');"


clean :
	$(RM_RF) $(NAME)*

clear : clean
	$(RM_RF) ./MANIFEST
