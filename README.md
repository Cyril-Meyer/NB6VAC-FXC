# NB6VAC-FXC

:fr: Documentation et outils pour box SFR NB6VAC-FXC et compatibles.

:gb: Documentation and tools for SFR NB6VAC-FXC boxes and compatible.


## My box

|  |   |
|-----------------------|------------------------|
| Modèle                | NB6VAC-FXC-r0          |
| Version principale    | NB6VAC-MAIN-R4.0.45d   |
| Version de secours    | NB6VAC-MAIN-R4.0.44k   |
| Version driver DSL    | NB6VAC-XDSL-A2pv6F039p |

| ![home_sb1](img/home_sb1.png) |
|--|
| NB6VAC-FXC |

## api-client
```
usage: client.py [-h] [--hostname HOSTNAME] [--username USERNAME]
                 [--password PASSWORD] [--warning-level WARNING_LEVEL]
                 [--disable-level DISABLE_LEVEL]
```

| Main Menu | Submenu (wlan) |
|--|--|
| ![](img/capture/menu_1.png) | ![](img/capture/menu_2_wlan.png) |

| auth.getToken () | system.getInfo |
|--|--|
| ![](img/capture/auth_getToken.png) | ![](img/capture/system_getInfo.png) |


## Hidden web page

* http://192.168.1.1/state/lan/extra
* http://192.168.1.1/network/lan
* http://192.168.1.1/rootfs
* http://192.168.1.1/state/device/plug
* http://192.168.1.1/maintenance/dsl/config


## Public Documentations

* [openwrt.org NB6VAC firmware](https://forum.openwrt.org/t/install-openwrt-on-nb6-nb6v-sfr/53153/17)
* [deviwiki.com/wiki/SFR_Neufbox_6](https://deviwiki.com/wiki/SFR_Neufbox_6) ([web.archive.org](https://web.archive.org/web/20230131163452/https://deviwiki.com/wiki/SFR_Neufbox_6))
* [fr.wikipedia.org/wiki/La_box_de_SFR](https://fr.wikipedia.org/wiki/La_box_de_SFR)
* ~~[openbox4.fhocorp.com](http://openbox4.fhocorp.com/doc/)~~ ➡️ [web.archive.org](https://web.archive.org/web/20220309022737/http://openbox4.fhocorp.com/doc/)
* [lafibre.info NB6VAC telnet et autres infos cachées de la box](https://lafibre.info/sfr-la-fibre/nb6vac-telnet-et-autres-infos-cachees-de-la-box/) ([web.archive.org](https://web.archive.org/web/20230131164850/https://lafibre.info/sfr-la-fibre/nb6vac-telnet-et-autres-infos-cachees-de-la-box/))
* [neufbox4.org Flasher une NB6](http://web.archive.org/web/20170816192614/https://www.neufbox4.org/wiki/index.php?title=Flasher_une_NB6)
* [github.com reboot_nb6.sh](https://gist.github.com/notFloran/5788412/revisions)

## Sources

* doc/
  * [api_rest_3.2_2012.pdf](https://lafibre.info/images/altice/201207_sfr_api-rest.pdf)
  * [api_rest_4.0_2016.pdf](https://lafibre.info/sfr-les-news/spec-api-rest-box-de-sfr/)
  * [Compatibilites_Femtocell_Box_Modems_2018.pdf](https://cdn.woopic.com/c10f167280f2414abb346a5347e1ecd9/crc-files/content/download/65352/2687033/version/2/file/box_compatible_femtocell.pdf)
 
