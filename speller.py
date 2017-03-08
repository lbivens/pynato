#!/usr/bin/env python
import sys

from pynato import Pynato

input = Pynato("")

for line in sys.stdin:
    input.message = line
    input.print_nato()
