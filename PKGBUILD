# Maintainer: Jakob Schnitzer <mail[at]jakobschnitzer[dot]de>
pkgname=asus-fancontrol
pkgver=0.1
pkgrel=1
pkgdesc="Fan control for ASUS UX31A"
arch=('x86_64')
depends=('lm_sensors' 'python')
source=('git://github.com/yagebu/asus-fancontrol.git')
md5sums=('SKIP')

build() {
    cd ${srcdir}/asus-fancontrol
    make
}

package() {
    cd ${srcdir}/asus-fancontrol
    make BINDIR="$pkgdir/usr/bin" install

    install -Dm644 asus-fancontrol.service "${pkgdir}/usr/lib/systemd/system/asus-fancontrol.service"
}
