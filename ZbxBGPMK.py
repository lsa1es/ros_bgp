#!/usr/bin/python
from RosAPI import Core
from sys import argv
import sys
import json
import itertools

OPC = sys.argv[1]
USR = sys.argv[2]
PWS = sys.argv[3]
try:
	a = Core(argv[4])
except:
	print("No connection")

a.login(USR, PWS)
peers = a.response_handler(a.talk(["/routing/bgp/peer/print"]))

if OPC == 'lld':

#	try:
#		a = Core(argv[2])
#	except:
#		print("No connection")
#
#	a.login("luiz", "Layer7@sup")
#	peers = a.response_handler(a.talk(["/routing/bgp/peer/print"]))
	out = {'data': []}
	if len(peers) > 0:
		for peer in peers:
			bgp = {"{#BGPPEER}": peer['remote-address'], "{#BGPNAME}": peer['name'] }
			out['data'].append(bgp)
	print(json.dumps(out, indent=4, sort_keys=True))

if OPC == 'uptime':
	PEER = sys.argv[5]
	for peer in peers:
		if peer['remote-address'] == PEER:
			print peer['uptime']

if OPC == 'state':
	PEER = sys.argv[5]
	for peer in peers:
		if peer['remote-address'] == PEER:
			print peer['state']


if OPC == 'rotas':
	PEER = sys.argv[5]
	for peer in peers:
		if peer['remote-address'] == PEER:
			print peer['prefix-count']

