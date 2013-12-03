import getopt
import re
import sys
import socket


class GuessWho():
	def __init__(self, address, timeout=5):
		address = unicode(address)
		self.address = address
		self.arin_response = None
		self.response = {}
		self.whois()
		self.parse_response()

	def whois(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("whois.arin.net", 43))
		s.send(str(self.address) + "\r\n")
		self.arin_response = ''
		while True:
			d = s.recv(4096)
			self.arin_response += d
			if d == '':
				break
		s.close()

	def parse_response(self):
		delim = '|delim|'
		self.arin_response = re.sub('#.*', '', self.arin_response)
		self.arin_response = re.sub(':\s+', delim, self.arin_response)
		self.arin_response = self.arin_response.split('\n')

		lines = []
		for line in self.arin_response:
			if len(line.strip()):
				lines.append(line)

		for line in lines:
			line = line.split(delim)
			try:
				self.response[line[0].lower()] = line[1]
			except IndexError:
				pass


def main():
	try:
		opts, args = getopt.getopt(sys.argv, "", ["help"])
	except getopt.GetoptError:
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
