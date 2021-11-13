# pymap

## Usage

```
usage: pymap.py [-h] [--basic] [--port] [--service] [--output NORMAL_OUTPUT] IP

Python enhancer for nmap

positional arguments:
  IP                    an integer for the accumulator

optional arguments:
  -h, --help            show this help message and exit
  --basic               Perform a port discovery scan followed by a service scan of the discovered ports
  --port                Perform a port discovery scan. "-p-" option
  --service             Perform a service discovery scan using common scripts. "-sCV" option
  --output NORMAL_OUTPUT
                        Store nmap output into specified file
```
