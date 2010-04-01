all:
	echo "This Makefile is only used for installation.  Type 'sudo make install'."

install:
	install -d $(DESTDIR)/usr/bin $(DESTDIR)/usr/share/vinux
	install buildvinux $(DESTDIR)/usr/bin
	install restorespeech $(DESTDIR)/usr/bin
	install set_vinux_globals $(DESTDIR)/usr/bin
	install buildvinuxiso $(DESTDIR)/usr/bin
	install gksu/gksu $(DESTDIR)/usr/bin
	install gksu/askpass $(DESTDIR)/usr/bin
	cp -r --preserve=mode vinux_data/* $(DESTDIR)/usr/share/vinux
