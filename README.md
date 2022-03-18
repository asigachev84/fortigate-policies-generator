# fortigate-policies-generator
Generate Firewall Policies from CSV

How to use:

1. Fill the following spreadsheets:
   fgaddr.csv - addresses
   fgservces.csv - services
   fgpolicies.csv - policies
2. Put them at the same folder with config.j2 (JINJA2-template) and fortigate-rules-generator.py
3. Run the script

As a result generated_config.txt file will be created with config and rollback:

config firewall service custom
    edit "Myservice1"
        set tcp-portrange 332
    next
    edit "Myservice2"
        set udp-portrange 252
    next
    edit "Myservice3"
        set tcp-portrange 123
        set udp-portrange 456
    next
end

config firewall address
    edit "Server1"
        set subnet 192.168.1.1 255.255.255.0
    next
    edit "Server2"
        set subnet 172.16.12.10 255.255.255.0
    next
    edit "Host2"
        set subnet 10.23.14.51 255.255.255.0
    next
end

config firewall policy
    edit "1"
        set name
        set srcintf Port1
        set dstintf Wan1
        set action accept
        set srcaddr Server1
        set dstaddr Server2
        set service Myservice1
        set logtraffic all
    next
    edit "2"
        set name
        set srcintf Port2
        set dstintf Wan2
        set action accept
        set srcaddr Server1
        set dstaddr Server2
        set service Myservice1
        set logtraffic all
    next
    edit "3"
        set name
        set srcintf Wan1
        set dstintf PortA
        set action accept
        set srcaddr Server1
        set dstaddr Server2
        set service Myservice3
        set logtraffic utm
    next
    edit "4"
        set name
        set srcintf Wan2
        set dstintf Port1
        set action accept
        set srcaddr Host2
        set dstaddr Server1
        set service Myservice3
        set logtraffic disable
    next
    edit "5"
        set name
        set srcintf PortA
        set dstintf Port2
        set action accept
        set srcaddr Host2
        set dstaddr Server1
        set service Myservice3
        set logtraffic disable
    next
end

##################
##   ROLLBACK   ##
##################

config firewall service custom
    delete "Myservice1"
    delete "Myservice2"
    delete "Myservice3"
end

config firewall address
    delete "Server1"
    delete "Server2"
    delete "Host2"
end

config firewall policy
    delete "1"
    delete "2"
    delete "3"
    delete "4"
    delete "5"
end
