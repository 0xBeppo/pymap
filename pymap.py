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


if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Python enhancer for nmap")

   parser.add_argument('ip', metavar='IP', type=str, nargs=1,
                     help='an integer for the accumulator')
   parser.add_argument('--port', dest='port_discovery', action='store_true', default=False,
                     help='Perform a port discovery scan. "-p-" option')
   parser.add_argument('--service', dest='service_discovery', action='store_true', default=False,
                     help='Perform a service discovery scan using common scripts. "-sCV" option')
   parser.add_argument('--output', dest='normal_output', default=False,
                     help='Store nmap output into specified file')
   
   args = parser.parse_args()
   print(args)
