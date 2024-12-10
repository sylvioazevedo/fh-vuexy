from datetime import datetime as dt

import dataclasses
import importlib.util
import jinja2 as jj2
import os

# constants
template_path = "./kenkun/templates"

def load_module_from_file(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def render_template(domain, fields, template, type: str='view'):

    tl = jj2.FileSystemLoader(searchpath=f'{template_path}/{type}')
    te = jj2.Environment(loader=tl)

    tpl = te.get_template(f'{template}.tpl')

    outputText = tpl.render(domain=domain, fields=fields)    
    
    if type == 'view':
        target_path = f"./{type}/{domain}"
        
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        target_file = f"{target_path}/{template}.py"

    else:
        target_path = f"./{type}"
        
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        target_file = f"{target_path}/{domain}_{type}.py"

    with open(target_file, "w") as f:
        f.write(outputText) 
        f.flush()

    print(f"Generated {type} for domain {domain}: {target_file}")

def load_fields(domain: str):

    domain_file_path = f"./domain/{domain}.py"
    module_name = os.path.splitext(os.path.basename(domain_file_path))[0]
    
    # Load the module
    domain_module = load_module_from_file(domain_file_path, module_name)
    
    # Access an object from the module (e.g., a class or function
    _c = getattr(domain_module, domain.title(), None)

    if not _c:
        raise Exception(f"Object 'ObjectName' not found in {domain_file_path}")
    
    fields = dataclasses.fields(_c)

    return fields
    
def generate_views(domain: str):

    fields = load_fields(domain)

    # generate crud views
    print(f'Creating views for domain: {domain}')
    render_template(domain, fields, '__init__')
    render_template(domain, fields, 'create')
    render_template(domain, fields, 'show')
    render_template(domain, fields, 'edit')

    print(f"Generated {domain} views")

def generate_controller(domain: str):

    fields = load_fields(domain)

    # generate crud views
    print(f'Creating controller for domain: {domain}')
    render_template(domain, fields, 'controller', 'controller')
    print(f"Generated {domain} controller")

def generate_all(domain: str):
    
    generate_views(domain)
    generate_controller(domain)
