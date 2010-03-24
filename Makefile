all:
	echo "This Makefile is only used for installation.  Type 'sudo make install'."

install:
	install buildvinux /usr/bin
	install restorespeech /usr/bin
	install set_vinux_globals /usr/bin
	install buildvinuxiso /usr/bin
	install -d /usr/share/vinux
	rsync -a vinux_data/ /usr/share/vinux
	chown -R root.root /usr/share/vinux
