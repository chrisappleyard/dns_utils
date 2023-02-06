#!/bin/bash

zone="$1"

function get_soa_serial() {
  local nameserver="$1"
  local zone="$2"
  local serial_number

  serial_number=$(dig @"$nameserver" "$zone" SOA +short | awk '{print $3}')
  if [[ -z "$serial_number" ]]; then
    serial_number=$(dig +tcp @"$nameserver" "$zone" SOA +short | awk '{print $3}')
  fi

  if [[ -z "$serial_number" ]]; then
    echo "Failed to get SOA serial for $zone, query timed out" >&2
    return 1
  fi

  echo "$serial_number"
}

serial=$(get_soa_serial "127.0.0.1" "$zone")
echo "$serial"
