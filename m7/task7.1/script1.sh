#!/bin/bash

function show_subnet {
    echo "Hosts in subnet: "
    ip -o -f inet addr show | awk '/scope global / {print $4}'
    arp -a
}

function show_open_ports {
    echo "All open ports in system: "
    sudo netstat -tulpn | grep tcp
}


# check parameters that were sent
if [[ $1 = "--all" ]]
then
    show_subnet
elif [[ $1 = "--target" ]]
then
    show_open_ports
elif [[ $# -eq 0 ]]
then
    echo "Usage of script:"
    echo "--all - displays the IP addresse and symbolic names of all hosts in the current subnet"
    echo "--target - displays a list of open system TCP ports"
fi