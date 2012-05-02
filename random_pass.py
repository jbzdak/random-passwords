#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'jb'

import argparse
import passgen
parser = argparse.ArgumentParser()

parser.add_argument("--count", required=False, default=3)

args = parser.parse_args()



print passgen.random_pass(args.count)
 