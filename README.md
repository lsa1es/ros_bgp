# Description

One scripts and template for monitoring bgp sessions in zabbix. 

Import template to your zabbix instalation.
* 
Place scripts in zabbix external scripts folder.


# Files

* ZbxBGPMK.py 
  * lld (user) (pass) (ip of RounterOS)
  * uptime (user) (pass) (ip of RouterOS) (ip of bgp peer, get ldd)
  * rotas (user) (pass) (ip of RouterOS) (ip of bgp peer, get ldd)
  * state (user) (pass) (ip of RouterOS) (ip of bgp peer, get ldd)

* bgpdiscovery.py - used for returning peers list to zabbix
* bgpmon.py - get bgp session state and return 0 or 1.
* RosAPI - RouterOS API library for python (thx David Jelić and Luka Blašković)

# Authors

* bsod (t1bur1an)

