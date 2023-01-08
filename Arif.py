#arif.py test
#lê ngọc cương . github :@alexberga757
#              . twitter:@lengoccuong757
#              . carrd  :lengoccuong.carrd.co
#              . yt     :@lengoccuong757


class ArifCreate:
	def __init__(self,content_):
		self.content = content_;

	def getString(self,name):
		token = "";
		content_ = self.content.split("\n");
		for n in range(len(content_)):
			poperties = content_[n].split(":");
			for i in range(len(poperties)):
				if poperties[0] == name:
					if i == 0:
						pass;
					else:
						token += ":" + poperties[i];
				else:
					pass;
		if (len(token) != 0):
			return token[1:]
		else:
			return "";

		return None;

	def getBoolean(self,name):
		v = self.getString(name);
		if (v == "true" or v == "True"):
			return True;
		elif (v == "false" or v == "False"):
			return False;
		return None;

	def getInt(self,name):
		return int(self.getString(name));
	def nonblank(self,name):
		chk = self.getString(name);
		if len(chk) != 0:
			return True;
		elif len(chk) == 0:
			return False;
		return None;
