from datetime import datetime as dt
from kenkun import generate_all, generate_controller, generate_domain, generate_views, incorporate

import sys

begin = dt.now()

action = sys.argv[1]

if not action:
    print('Usage: python generate.py <action> <domain>')
    sys.exit(1)

domain = sys.argv[2]

if not domain:
    print('Usage: python generate.py <action> <domain>')
    sys.exit(1)

if action == 'all':
    generate_all(domain)

if action == 'controller':
    generate_controller(domain)

if action == 'views':
    generate_views(domain)

if action == 'domain':
    generate_domain(domain)

if action == 'inc':
    print(incorporate(domain))

print(f"Completed in {dt.now() - begin} ms")