from kenkun import generate_all

import sys

domain = sys.argv[1]

if not domain:
    print('Usage: python generate_all.py <domain>')
    sys.exit(1)

generate_all(domain)
