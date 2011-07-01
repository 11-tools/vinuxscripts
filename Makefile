all:
	echo "This Makefile is only used for installation.  Type 'sudo make install'."

install:
	install -d $(DESTDIR)/usr/bin $(DESTDIR)/usr/share/vinux
	install buildvinux $(DESTDIR)/usr/bin
	install bin/configurespeech $(DESTDIR)/usr/bin
	install bin/pulseuser $(DESTDIR)/usr/bin
	install bin/pulsesystem $(DESTDIR)/usr/bin
	install bin/set_vinux_globals $(DESTDIR)/usr/bin
	install bin/cdburn $(DESTDIR)/usr/bin
	install bin/usbinstall $(DESTDIR)/usr/bin
	install buildvinuxiso $(DESTDIR)/usr/bin
	install bin/volume_keys $(DESTDIR)/usr/bin
	install bin/update_manual $(DESTDIR)/usr/bin
	install bin/fix $(DESTDIR)/usr/bin
	install bin/restore_sound $(DESTDIR)/usr/bin
	install gksu/gksu $(DESTDIR)/usr/bin
	install gksu/askpass $(DESTDIR)/usr/bin
	cp -r --preserve=mode vinux_data/* $(DESTDIR)/usr/share/vinux
