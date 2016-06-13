asus-fancontrol
===============

Asus UX32V fan speed regulation

**This fork uses lm-sensors to get the temperature (in a very hackish way) 
and provides a PKGBUILD for Arch Linux**


IMPORTANT NOTE
--------------

**NO WARRANTIES WHATSOEVER. USE AT YOUR OWN RISK.**

**Do not** run this on computers other than Asus UX32V 
unless you know what you are doing.

The wrapper might also work for the UX32VD fanctrl...

Installation
------------

Download the PKGBUILD and run `makepkg`

To use it on a different distro, build it running  `make` and then `make install`.
Copy `asus-fancontrol.service` to `/etc/systemd/system/`. If your distro doesn't use systemd,
you have to use some other tool to make sure that asus-fancontrol is always running.

Usage
-----

    systemctl enable asus-fancontrol.service
    systemctl start asus-fancontrol.service

If the service crashes or you want to stop using it, make sure to run `fanctrl auto` to revert back to the normal fan control.


Authors
-------

Alexander Breckel wrote [`f3jp.c`][1] for Asus F3Jp in 2008.
[Prikolchik][3] wrote [`ux32vd.c`][2] for Asus UX32VD based on Breckel's, and
`ux31a.c` is merely a stripped-down version of Prikolchik's.
Finally, `asus-fancontrol.sh` is an improved version of Breckel's [wrapper][1]. 

The python wrapper script is written by Jakob Schnitzer (https://github.com/yagebu), all the rest is due to the above

I just added back the module for model ux32vd.

[1]: http://www.aneas.org/knowledge/asus_f3jp_fan_control.php  "Asus F3Jp fan control on Linux"
[2]: http://pastebin.com/Hp2pWeyL "fancntrl.c: Asus UX32VD fan control proof of concept"
[3]: http://forum.notebookreview.com/asus/705656-fan-control-asus-prime-ux31-ux31a-ux32a-ux32vd.html "Fan Control on Asus Prime UX31/UX31A/UX32A/UX32VD"
