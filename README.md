# fortigate-policies-generator
Generate Firewall Policies from CSV

How to use:

1. Fill the following spreadsheets:
   fgaddr.csv - addresses
   fgservces.csv - services
   fgpolicies.csv - policies
2. Put them at the same folder with config.j2 (JINJA2-template) and fortigate-rules-generator.py
3. Run the script

As a result generated_config.txt file will be created with config and rollback ready to be pasted into device.
