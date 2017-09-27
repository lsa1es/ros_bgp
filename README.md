# Description

Two scripts and template for monitoring bgp sessions in zabbix. 

Import template to your zabbix instalation.

Place scripts in zabbix external scripts folder.


# Files

* ZbxBGPMK.py 
  * lld <usuario> <senha> <ip do mk>
  * uptime <usuario> <senha> <ip do mk> <ip do bgp peer(pegar no lld)>
  * rotas <usuario> <senha> <ip do mk> <ip do bgp peer(pegar no lld)>
  * state <usuario> <senha> <ip do mk> <ip do bgp peer(pegar no lld)>

* bgpdiscovery.py - used for returning peers list to zabbix
* bgpmon.py - get bgp session state and return 0 or 1.
* RosAPI - RouterOS API library for python (thx David Jelić and Luka Blašković)

# Authors

* bsod (t1bur1an)

