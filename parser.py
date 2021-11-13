#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python functions to handle nmap output parsing"""

__author__ = "Markel Elorza (0xBeppo)"
__version__ = "0.0.1"
__email__ = "eamarkel@gmail.com"
__status__ = "development"

import xml.etree.ElementTree as ET
import pyperclip

class NmapXMLOutputParser:
    def __init__(self, file="nmap/portScan.xml") -> None:
        self.file = file
        self.up_machines = self.get_machines()
        self.ports = ""

    def get_machineIP(self):
        up_machines = []
        xmltree = ET.parse(self.file)
        xmlroot = xmltree.getroot()
        for host in xmlroot.findall('host'):
            status = host.find('status').get('state')
            if status == "up":
                up_machines.append(host.find('address').get('addr'))

        return up_machines

    def get_machines(self):
        machines = {}
        up_machines = self.get_machineIP()
        xmltree = ET.parse(self.file)
        xmlroot = xmltree.getroot()
        for host in xmlroot.findall('host'):
            host_ip = host.find('address').get('addr')  
            if host_ip in up_machines:
                ports = []
                for found_port in host.find('ports').findall('port'):
                    port = {
                        "port_number" : found_port.get('portid'),
                        "protocol": found_port.get('protocol'),
                        "state": found_port.find('state').get('state'),
                    }
                    ports.append(port)
                machines[host_ip] = ports

        return machines

    def beautify_results(self):
        machines = self.up_machines
        for ip in machines:
            print(f'[+] Machine IP: {ip}')
            for port in machines[ip]:
                port_number = port['port_number']
                print(f'\t[*] Open Port: {port_number}')
            print()
    
    def copyPortsToClipboard(self):
        ports = ""
        machines = self.up_machines
        for ip in machines:
            for port in machines[ip]:
                port_number = port['port_number']
                ports += port_number +","
        self.ports = ports[:-1]
        pyperclip.copy(self.ports)
        print()
        print('[*] Ports copyed to clipboard!')
        print()

    def get_ports(self):
        return self.ports

