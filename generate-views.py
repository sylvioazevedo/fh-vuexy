from kenkun import generate_views

import sys

domain = sys.argv[1]

if not domain:
    print('Usage: python generate_views.py <domain>')
    sys.exit(1)

generate_views(domain)

