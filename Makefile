all:
	echo "This Makefile is only used for installation.  Type 'sudo make install'."

install:
	install -d $(DESTDIR)/usr/local/bin $(DESTDIR)/usr/share/vinux
	install buildvinux $(DESTDIR)/usr/bin
	install local-bin/* $(DESTDIR)/usr/bin
	install buildvinuxiso $(DESTDIR)/usr/bin
	install system/11-totd $(DESTDIR)/etc/update-motd.d
	cp -r --preserve=mode vinux_data/* $(DESTDIR)/usr/share/vinux
