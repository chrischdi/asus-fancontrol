asus-fancontrol
===============

Asus UX31A and UX32VD fan speed regulation

**This fork uses lm-sensors to get the temperature (in a very hackish way) 
and provides a PKGBUILD for Arch Linux **

IMPORTANT NOTE
--------------

**NO WARRANTIES WHATSOEVER. USE AT YOUR OWN RISK.**

**Do not** run this on computers other than Asus UX31A and UX32VD 
unless you know what you are doing.

Installation
------------

Asus UX31A:


    make MODEL=ux31a
    make install


Asus UX32VD:


    make MODEL=ux32vd
    make install



Usage
-----

    asus-fancontrol
    asus-fancontrol --help
    asus-fancontrol --verbose



Example
-------

Set up a `cron` job to run `asus-fancontrol` at boot-time. Run:

    sudo crontab -e
    
And add this line to the system's `crontab`:

    @reboot /usr/local/bin/asus-fancontrol

Save, and quit.

Create an executable script to restart `asus-fancontrol` upon resume from suspend.

`/etc/pm/sleep.d/98asus-fancontrol`

    #!/bin/bash
    case "$1" in
    hibernate|suspend) true;;
    resume|thaw) echo path/to/asus-fancontrol | /usr/bin/at now;;
    esac
    
Finally, you may either reboot, or suspend and resume, to get it going on the background.


Authors
-------

Alexander Breckel wrote [`f3jp.c`][1] for Asus F3Jp in 2008.
[Prikolchik][3] wrote [`ux32vd.c`][2] for Asus UX32VD based on Breckel's, and
`ux31a.c` is merely a stripped-down version of Prikolchik's.
Finally, `asus-fancontrol.sh` is an improved version of Breckel's [wrapper][1]. 

[1]: http://www.aneas.org/knowledge/asus_f3jp_fan_control.php  "Asus F3Jp fan control on Linux"
[2]: http://pastebin.com/Hp2pWeyL "fancntrl.c: Asus UX32VD fan control proof of concept"
[3]: http://forum.notebookreview.com/asus/705656-fan-control-asus-prime-ux31-ux31a-ux32a-ux32vd.html "Fan Control on Asus Prime UX31/UX31A/UX32A/UX32VD"
