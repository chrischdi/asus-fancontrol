MODEL=ux32v
BINDIR=/usr/bin

bin:
	gcc $(MODEL).c -o fanctrl

clean:
	rm -f fanctrl

install:
	install -Dm755 fanctrl            $(BINDIR)/fanctrl
	install -Dm755 asus-fancontrol.py $(BINDIR)/asus-fancontrol

uninstall:
	rm -f $(BINDIR)/fanctrl
	rm -f $(BINDIR)/asus-fancontrol
