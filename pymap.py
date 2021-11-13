#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python enhancer for nmap
   Aims the automatization of my nmap scans in Ethical Hacking enviroments
"""

__author__ = "Markel Elorza (0xBeppo)"
__version__ = "0.0.1"
__email__ = "eamarkel@gmail.com"
__status__ = "development"

import argparse
import scanner

def run():
   args, parser = handle_args()
   nmap = scanner.NmapScanner(args.ip[0], args.normal_output)

   if args.port_discovery:
      print('[!] Performing PORT scan')
      print()
      nmap.port_scan()
   elif args.service_discovery:
      print('[!] Method under development!')
   elif args.basic_discovery:
      nmap.port_scan()
      nmap.service_scan()
   else:
      print('[!] ERROR: No scan type found')
      print()
      parser.print_help()




def handle_args():
   parser = argparse.ArgumentParser(description="Python enhancer for nmap")

   parser.add_argument('ip', metavar='IP', type=str, nargs=1,
                     help='The IP of the target machine / network')
   parser.add_argument('-b', '--basic', dest='basic_discovery', action='store_true', default=False,
                     help='Perform a port discovery scan followed by a service scan of the discovered ports')
   parser.add_argument('-p', '--port', dest='port_discovery', action='store_true', default=False,
                     help='Perform a port discovery scan. "-p-" option')
   parser.add_argument('-s', '--service', dest='service_discovery', action='store_true', default=False,
                     help='Perform a service discovery scan using common scripts. "-sCV" option')
   parser.add_argument('-o', '--output', dest='normal_output', default=None,
                     help='Store nmap output into specified file')
   args = parser.parse_args()

   return args, parser


if __name__ == "__main__":
   run()
