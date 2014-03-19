#!/usr/bin/env bash

DIR="/opt/karaage-test"

set -e
set -x
export DEBCONF_DEBUG=developer
export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install --yes python-pip git
if false
then
    # current version of schroot is missing commit
    # https://github.com/paultag/python-schroot/commit/c6537b7a8443702447b8ec2347a662e12e2b1d2c
    # and won't work as a result
    pip install schroot
else
    if ! test -d /opt/python-schroot
    then
        git clone https://github.com/paultag/python-schroot.git /opt/python-schroot
        pip install -e /opt/python-schroot
    fi
fi

cd "$DIR"
./dotest --distribution=wheezy  --source=github --ldap=openldap --localhost --keep
