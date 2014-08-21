#!/usr/bin/env bash

DIR="/opt/karaage-test"

set -e
set -x
export DEBCONF_DEBUG=developer
export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install --yes python-pip
pip install schroot
# apt-get install python-schroot python3-schroot

cd "$DIR"
./dotest --distribution=wheezy  --ldap=openldap --localhost --keep
