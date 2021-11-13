#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python functions to handle nmap scanning"""

__author__ = "Markel Elorza (0xBeppo)"
__version__ = "0.0.1"
__email__ = "eamarkel@gmail.com"
__status__ = "development"

import sys
import subprocess
import shlex
import parser


class NmapScanner:

    def __init__(self, target, output=None) -> None:
        self.target = target
        self.output = output
        self.nmap_path = self.locate_nmap()

    def locate_nmap(self):
        query = ["which", "nmap"]
        process = subprocess.Popen(query, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        stdout = stdout.decode("utf-8")
        print(stdout)
        
        error_code = process.wait()
        if error_code:
            print(f"[!] ERROR: {stderr}")
            print()
            print("[!] ERROR: Could not find nmap binary, to fix this issue add nmap to your $PATH")
            sys.exit(error_code)
        if stdout.endswith("\n'"):
            stdout = stdout[:-2]
        print(f"[*] Nmap found at: {stdout}")
        return stdout
            
    def port_scan (self):
        print(self.output)
        if self.output == None:
            nmap_query=(f'{self.nmap_path} -sS -p- --open --min-rate 2000 --min-parallelism 100 -Pn -n -vv {self.target} -oX nmap/portScan.xml')
        else:
            nmap_query=(f'{self.nmap_path} -sS -p- --open --min-rate 2000 --min-parallelism 100 -Pn -n -vv {self.target} -oX nmap/portScan.xml -oN nmap/{self.output}')
        query = shlex.split(nmap_query)
        print(f"[+] Executing: {nmap_query}")
        print()
        try:
            subprocess.check_call(query,stdout=sys.stdout, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            print()
            print(f"[!] ERROR! Read above and try again")
            sys.exit(error.returncode)
        my_parser = parser.NmapXMLOutputParser()
        my_parser.copyPortsToClipboard()


    def service_scan ():
        pass
