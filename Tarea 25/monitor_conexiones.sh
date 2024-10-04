#!/bin/bash

#conexiones de red -established-
netstat -tunapl 2>&1 | grep "ESTABLISHED"