from kenkun import generate_controller

import sys

domain = sys.argv[1]

if not domain:
    print('Usage: python generate_ctrl.py <domain>')
    sys.exit(1)

generate_controller(domain)
