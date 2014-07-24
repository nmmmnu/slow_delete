#!/usr/bin/python

import os
import sys

DEFAULT_SLEEP       = "0.1"
DEFAULT_SLEEP_COUNT = 2


def process(what, prefix, files, sleep, sleep_count):
	print()
	print("# %s in %s:" % (what, prefix))

	count = 0
	for name in files:
		f = os.path.join(prefix, name)
		print("rm -f %s" % f)

		count = count + 1
		if count >= sleep_count:
			count = 0
			print("sleep %s" % sleep)


def main(path, sleep, sleep_count):
	for root, dirs, files in os.walk(path, topdown = False):

		if files:
			process("files", root, files, sleep, sleep_count)

		if dirs:
			process("directories", root, dirs, sleep, sleep_count)


if len(sys.argv) == 1:
	print("Usage: %s [directory] [sleep | %s] [sleep_count | %d]" % (sys.argv[0], DEFAULT_SLEEP, DEFAULT_SLEEP_COUNT))
	sys.exit(0)


path        = sys.argv[1]
sleep       = DEFAULT_SLEEP
sleep_count = DEFAULT_SLEEP_COUNT

if len(sys.argv) > 2:
	sleep = sys.argv[2]

if len(sys.argv) > 3:
	sleep_count = int(sys.argv[3])

main(path, sleep, sleep_count)


