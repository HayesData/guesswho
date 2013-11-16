from subprocess import check_output
import getopt
import ipaddress
import re
import sys


class GuessWho():
	def __init__(self, address, timeout=5):
		address = unicode(address)
		self.address = ipaddress.ip_address(address)

		delim = '|delim|'

		command = 'whois ' + str(self.address)
		cmd_out = check_output([command], shell=True).strip()

		cmd_out = re.sub('#.*', '', cmd_out)
		cmd_out = re.sub(':\s+', delim, cmd_out)

		cmd_out = cmd_out.split('\n')

		lines = []
		for line in cmd_out:
			if len(line.strip()):
				lines.append(line)

		self.response = {}
		for line in lines:
			line = line.split(delim)
			self.response[line[0].lower()] = line[1]


def main():
	try:
		opts, args = getopt.getopt(sys.argv, "", ["help"])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	try:
		address = unicode(args[1])
		ipaddress.ip_address(address)
	except:
		print 'You must provide a valid IP Address.'
		sys.exit(2)

	who = GuessWho(address)

	print who.response


if __name__ == '__main__':
	main()