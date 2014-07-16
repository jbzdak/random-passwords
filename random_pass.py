#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import passgen
parser = argparse.ArgumentParser()

parser.add_argument("--count", required=False, default=5, type=int)
parser.add_argument("--lines", required=False, default=1, type=int)

args = parser.parse_args()

for __ in range(args.lines):
    print(passgen.random_pass(args.count))
