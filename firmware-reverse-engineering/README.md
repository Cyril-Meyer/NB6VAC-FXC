# Firmware Reverse Engineering

Disclaimer: I do not know what I am doing !

### Get the dump

Search the web or dump it yourself, I found one here :
[NB6VAC DUMP.bin]([openwrt.org NB6VAC firmware](https://forum.openwrt.org/t/install-openwrt-on-nb6-nb6v-sfr/53153/17))
(CRC32 : `BD3752EA`).

Looking at the file in a text editor, I found strings about `R4.0.40` so this is
probably `NB6VAC-MAIN-R4.0.40`.

### Analysis : text editor

Looking at the bin file in notepad++, I searched for the documented `getInfo`.
I found `wlan.getInfo.xml` and searching in the area with `.xml`,
I found `api.routes.xml` which help a lot for api-client development.

I also found password hashes, but I cannot tell if they are from the user or the ISP.
* `ff85a28634619b414f1c6e8d14c4c545a822720884536a7032e57debfbebb904`
* `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8`


### Analysis : binwalk

```
> binwalk DMP.bin

ECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
32868         0x8064          SHA256 hash constants, big endian
135168        0x21000         JFFS2 filesystem, big endian
345660        0x5463C         JFFS2 filesystem, big endian
476436        0x74514         JFFS2 filesystem, big endian
2703360       0x294000        UBI erase count header, version: 1, EC: 0x1, VID header offset: 0x800, data offset: 0x1000
35143680      0x2184000       JFFS2 filesystem, big endian
35354172      0x21B763C       JFFS2 filesystem, big endian
35484948      0x21D7514       JFFS2 filesystem, big endian
35932872      0x2244AC8       JFFS2 filesystem, big endian
```


### Extract JFFS2 filesystem

```
> jefferson DMP.bin
```

```
> dd bs=1 skip=35932872 if=DMP.bin of=DATA_35932872.jffs2
> dd bs=1 skip=35484948 count=447924 if=DMP.bin of=DATA_35484948.jffs2
> dd bs=1 skip=35354172 count=130776 if=DMP.bin of=DATA_35354172.jffs2
> dd bs=1 skip=35143680 count=210492 if=DMP.bin of=DATA_35143680.jffs2
> dd bs=1 skip=476436 count=2226924 if=DMP.bin of=DATA_476436.jffs2
> dd bs=1 skip=345660 count=130776 if=DMP.bin of=DATA_345660.jffs2
> dd bs=1 skip=135168 count=210492 if=DMP.bin of=DATA_135168.jffs2
```


**No more information at the moment...**
