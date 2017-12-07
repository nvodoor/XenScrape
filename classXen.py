from bs4 import BeautifulSoup as bs
import requests as req


class Xen:
	#Xf Attributes
	def __init__(self, url):
		self.url = url;
		self.soup = 'blank'

	def retrieve(self):
		try:
			pyforum = req.get(self.url);
		except:
			return 'pyforum did not make request'
		soup = bs(pyforum.text, 'html.parser')

		self.soup = soup;

		return soup.title;

	def messageCount(self, obj, name):
		message = self.soup.find('dl', {'class': 'messageCount'})
		children = message.findChildren();
		count = 0
		for child in children:
		#the contents of each tag is an array.
			content = str(child.contents[0])
			if count > 0:
				num = list(content)
				truenum = []
				for x in num:
					if x != ',':
						truenum.append(x)
				strnumber = ''.join(truenum)
				number = int(strnumber);
				obname = name + 'message'
				obj[obname] = number
			count += 1

		return obj;

	def discussionCount(self, obj, name):
		discussion = self.soup.find('dl', {'class': 'discussionCount'})
		children = discussion.findChildren();
		count = 0
		for child in children:
			content = str(child.contents[0])
			if count > 0:
				num = list(content)
				truenum = []
				for x in num: 
					if x != ',':
						truenum.append(x)
				strnumber = ''.join(truenum)
				number = int(strnumber);
				obname = name + 'discussions'
				obj[obname] = number
			count += 1

		return obj;

	def memberCount(self, obj, name):
		member = self.soup.find('dl', {'class': 'memberCount'})
		children = member.findChildren();
		count = 0
		for child in children:
			content = str(child.contents[0])
			if count > 0:
				num = list(content)
				truenum = []
				for x in num: 
					if x != ',':
						truenum.append(x)
				strnumber = ''.join(truenum)
				number = int(strnumber);
				obname = name + 'members'
				obj[obname] = number
			count += 1

		return obj;



