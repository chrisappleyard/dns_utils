#!/usr/bin/env python3

import argparse
import dns.resolver

def get_soa_serial(nameserver, zone):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [nameserver]
    try:
        answer = resolver.resolve(zone, 'SOA')
        serial_number = answer.rrset[0].serial
        return str(serial_number)
    except dns.resolver.Timeout:
        try:
            resolver.use_tcp = True
            answer = resolver.resolve(zone, 'SOA')
            serial_number = answer.rrset[0].serial
            return str(serial_number)
        except dns.resolver.Timeout:
            print("Failed to get SOA serial for " + zone + " , query timed out")

parser = argparse.ArgumentParser()
parser.add_argument("zone")
args = parser.parse_args()
zone = args.zone

serial = get_soa_serial('127.0.0.1', zone)
print(serial)