from datetime import datetime as dt

import dataclasses
import importlib.util
import os
import jinja2 as jj2

target_path = "./kenkun/dist/views/"

tl = jj2.FileSystemLoader(searchpath="./kenkun/templates")
te = jj2.Environment(loader=tl)

def load_module_from_file(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def generate_views(domain: str):

    domain_file_path = f"./domain/{domain}.py"
    module_name = os.path.splitext(os.path.basename(domain_file_path))[0]
    
    # Load the module
    domain_module = load_module_from_file(domain_file_path, module_name)
    
    # Access an object from the module (e.g., a class or function)
    # Replace 'ObjectName' with the actual name of the object you want to access
    _c = getattr(domain_module, domain.title(), None)     

    if not _c:        
        raise Exception(f"Object 'ObjectName' not found in {domain_file_path}")        

    fields = dataclasses.fields(_c)  
    
    template = te.get_template("__init__.py")

    outputText = template.render(domain=domain, fields=fields)

    if not os.path.exists(f"{target_path}{domain}"):
        os.makedirs(f"{target_path}{domain}")

    with open(f"{target_path}{domain}/__init__.py", "w") as f:
        f.write(outputText)

    print(f"Generated {domain} views")

    