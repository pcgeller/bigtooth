##Set up the RPi as a WAP.

Make sure AP is listed as a a supported interface mode.
```shell
iw list
```
Get access point daemon.

```shell
sudo apt-get install hostapd
```
Edit the /etc/network/interfaces to set static IP.  It should look like:
```shell
iface wlan0 inet static
address 10.0.0.1
netmask 255.255.255.0
```
