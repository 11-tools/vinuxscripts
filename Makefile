all:
	echo "This Makefile is only used for installation.  Type 'sudo make install'."

install:
	install -d $(DESTDIR)/usr/local/bin $(DESTDIR)/usr/local//share/vinux
	install buildvinux $(DESTDIR)/usr/local/bin
	install local-bin/* $(DESTDIR)/usr/local/bin
	install buildvinuxiso $(DESTDIR)/usr/local/bin
	install gksu/* $(DESTDIR)/usr/local/bin
	install system/11-totd $(DESTDIR)/etc/update-motd.d
	cp -r --preserve=mode vinux_data/* $(DESTDIR)/usr/local/share/vinux
