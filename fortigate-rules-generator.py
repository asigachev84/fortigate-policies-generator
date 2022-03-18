import csv
from jinja2 import Environment, Template

services_file = 'fgservices.csv'
addr_file = 'fgaddr.csv'
policies_file = 'fgpolicies.csv'
config_template = 'config.j2'
services_list = []
addr_list = []
policies_list = []


with open(services_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        services_list.append(row)

with open(addr_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        addr_list.append(row)

with open(policies_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        policies_list.append(row)

print(policies_list)

with open(config_template) as f:
    template = Template(f.read(), trim_blocks=True)

print(template.render(services_list=services_list, addr_list=addr_list, policies_list=policies_list))



