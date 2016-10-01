import urllib.request
import time
import glob
import random
import string
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
wnl = WordNetLemmatizer()
port = PorterStemmer()
wnl = WordNetLemmatizer()
port = PorterStemmer()


t = time.strftime("%d%m%Y")
prepositions=['a', 'all', 'an', 'aboard', 'about', 'above', 'across', 'after', 'against', 'along', 'amid', 'among', 'and', 'anti', 'around', 'as', 'at', 'away', 'be', 'became', 'become', 'becomes', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'beyond', 'but', 'by', 'come', 'coming', 'came', 'concerning', 'considering', 'create', 'created', 'creates', 'do', 'does', 'dont', 'despite', 'down', 'during', 'except', 'excepting', 'excluding', 'faced', 'faced', 'find', 'following', 'for', 'found', 'from', 'get', 'gets', 'give', 'given', 'gives', 'go', 'goes', 'gone', 'had', 'has', 'have', 'havent', 'he', 'held', 'her', 'here', 'heres', 'his', 'having', 'hold', 'holding', 'holds', 'how', 'in', 'is', 'it', 'its', 'inside', 'into', 'let', 'like', 'liked', 'likely', 'likes', 'made', 'make', 'many', 'may', 'me', 'minus', 'more', 'must', 'nbsp', 'near', 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'only', 'onto', 'opposite', 'or', 'out', 'outside', 'over', 'past', 'per', 'plus', 'regarding', 'round', 'save', 'say', 'says', 'set', 'sets', 'she', 'should', 'shall', 'since', 'so', 'st', 'take', 'takes', 'taking', 'th', 'than', 'that', 'the', 'there', 'theres', 'their', 'this', 'though', 'through', 'to', 'too', 'toward', 'towards', 'under', 'underneath', 'unlike', 'until', 'up', 'upon', 'use', 'used', 'using', 'versus', 'via', 'went', 'with', 'within', 'without', 'what', 'when', 'where', 'who', 'why', 'while', 'would', 'yes', 'yet', 'you', 'your', 'yours', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'jan', 'feb', 'mar', 'apr', 'aug', 'sept', 'oct', 'nov', 'dec', 'monday', 'mon', 'tuesday', 'tue', 'wednesday', 'thursday', 'thu', 'friday', 'fri', 'saturday', 'sunday', 'eight', 'eighteen', 'eighteenth', 'eighth', 'eightieth', 'eighty', 'eleven', 'eleventh', 'fifteen', 'fifteenth', 'fifth', 'fiftieth', 'fifty', 'first', 'five', 'fortieth', 'forty', 'four', 'fourteen', 'fourteenth', 'fourth', 'hundred', 'hundredth', 'nine', 'nineteen', 'nineteenth', 'ninetieth', 'ninety\t', 'ninthten', 'one', 'second', 'three', 'seventeen', 'seventeenth', 'seventh', 'seventieth', 'seventy', 'six', 'sixteen', 'sixteenth', 'sixthseven', 'sixtieth', 'sixty', 'tenth', 'third', 'thirteen', 'thirteenth', 'thirtieth', 'thousand', 'thousandth', 'twelfth', 'twelve', 'twentieth', 'thirty', 'twenty', 'two']


places = ['Ambaji', 'Abids', 'Agra', 'Ahmedabad', 'Ahmednagar', 'Alappuzha', 'Allahabad', 'Alwar', 'Akola', 'Alibag', 'Almora', 'Amlapuram', 'Amravati', 'Amritsar', 'Anand', 'AnandpurSahib', 'Angul', 'AnnaSalai', 'Arambagh', 'Asansol', 'Ajmermap', 'Amreli', 'Aizawl', 'Agartala', 'Aligarhmap', 'Auli', 'Aurangabad', 'Azamgarh', 'Aurangabad', 'Baran', 'Bettiah', 'Badaun', 'Badrinath', 'Balasore', 'Banaswara', 'Bankura', 'Ballia', 'Bardhaman', 'Baripada', 'Barrackpore', 'Barnala', 'Barwani', 'Beed', 'Beawar', 'Bellary', 'Bhadohi', 'Bhadrak', 'Bharuch', 'Bhilai', 'Bhilwara', 'Bhiwani', 'Bidar', 'Bilaspur', 'Bangalore', 'Bhind', 'Bhagalpur', 'Bharatpur', 'Bhavnagar', 'Bhopal', 'Bhubaneshwar', 'Bhuj', 'Bilimora', 'Bijapur', 'Bikaner', 'BodhGaya', 'Bokaro', 'Bundi', 'Barasat', 'Bareilly', 'Basti', 'Bijnor', 'Burhanpur', 'Buxur', 'Calangute', 'Chandigarh', 'Chamba', 'Chandausi', 'Chandauli', 'Chandrapur', 'Chhapra', 'Chidambaram', 'Chiplun', 'Chhindwara', 'Chitradurga', 'Chittoor', 'CoochBehar', 'Chennai', 'Chittaurgarh', 'Churu', 'Coimbatore', 'Cuddapah', 'Cuttack', 'Dahod', 'Dalhousie', 'Davangere', 'Dehri', 'Dewas', 'Dwarka', 'Dehradun', 'Delhi', 'Deoria', 'Dhanbad', 'Dharamshala', 'Dispur', 'Dholpur', 'DiuIsland', 'Durgapur', 'Didwana', 'Ernakulam', 'Etah', 'Etawah', 'Erode', 'Faridabad', 'Ferozpur', 'Faizabad', 'Gandhinagar', 'Gangapur', 'Garia', 'Gaya', 'Ghaziabad', 'Godhra', 'Gokul', 'Gonda', 'Gorakhpur', 'GreaterMumbai', 'Gulbarga', 'Guna', 'Guntur', 'Gurgaon', 'GreaterNoida', 'Gulmarg', 'Hanumangarh', 'Haflong', 'Haldia', 'Haridwar', 'Hajipur', 'Haldwani', 'Hampi', 'Hapur', 'Hubli', 'Hardoi', 'Hyderabad', 'Guwahati', 'Gangtok', 'Gwalior', 'Imphal', 'Indore', 'Itanagar', 'Itarsi', 'Jabalpur', 'Jagadhri', 'Jalna', 'Jamalpur', 'Jhajjar', 'Jhalawar', 'Jaipur', 'Jaisalmer', 'Jalandhar', 'Jammu', 'Jamshedpur', 'Jhansi', 'Jaunpur', 'Jodhpur', 'Junagadh', 'Jalore', 'Kishanganj', 'Katihar', 'Kanpur', 'Kangra', 'Kasauli', 'Kapurthala', 'Kanchipuram', 'Karnal', 'Karaikudi', 'Kanyakumari', 'Katni', 'Khajuraho', 'Khandala', 'Khandwa', 'khargone', 'Kishangarh', 'Kochi', 'Kodaikanal', 'Kohima', 'Kolhapur', 'Kolkata', 'Kollam', 'Kota', 'Kottayam', 'Kovalam', 'Kozhikode', 'Kumbakonam', 'Kumarakom', 'Kurukshetra', 'Lalitpur', 'Latur', 'Lucknow', 'Ludhiana', 'Lavasa', 'Leh', 'Laxmangarh', 'Madikeri', 'Madurai', 'Mahabaleshwar', 'Mahabalipuram', 'Mahbubnagar', 'Manali', 'ManduFort', 'Mangalore', 'Malegaon', 'Manipal', 'Margoa', 'Mathura', 'Meerut', 'Mirzapur', 'Mohali', 'Morena', 'Motihari', 'Moradabad', 'MountAbu', 'Mumbai', 'Munger', 'Munnar', 'Mussoorie', 'Mysore', 'Muzaffarnagar', 'Mokokchung', 'Muktsar', 'Nagpur', 'Nagaon', 'Nagercoil', 'Naharlagun', 'Naihati', 'Nainital', 'Nalgonda', 'Namakkal', 'Nanded', 'Narnaul', 'Nasik', 'Nathdwara', 'Navsari', 'Neemuch', 'Noida', 'Ooty', 'Orchha', 'Palakkad', 'Palanpur', 'Pali', 'Palwal', 'Panaji', 'Panipat', 'Panvel', 'Pathanamthitta', 'Pandharpur', 'PatnaSahib', 'Panchkula', 'Patna', 'Periyar', 'Phagwara', 'Pilibhit', 'Pinjaur', 'Pollachi', 'Pondicherry', 'Ponnani', 'Porbandar', 'PortBlair', 'Porur', 'Pudukkottai', 'Punalur', 'Pune', 'Puri', 'Purnia', 'Pushkar', 'Patiala', 'Raxual', 'Rajkot', 'Rameswaram', 'Rajahmundry', 'Ranchi', 'Ratlam', 'Raipur', 'Rewa', 'Rewari', 'Rishikesh', 'Rourkela', 'Sitamrahi', 'Sagar', 'Sangareddy', 'Saharanpur', 'Salem', 'SaltLake', 'Samastipur', 'Sambalpur', 'Sambhal', 'Sanchi', 'Sangli', 'Sarnath', 'Sasaram', 'Satara', 'Satna', 'Secunderabad', 'Sehore', 'Serampore', 'Sangrur', 'Sirhind', 'Shillong', 'Shimla', 'Shirdi', 'ShivaGanga', 'Shivpuri', 'Silvassa', 'Singrauli', 'Sirsa', 'Sikar', 'Siwan', 'Somnath', 'Sonipat', 'Sopore', 'Srikakulam', 'Srirangapattna', 'Srinagar', 'Sultanpur', 'Surat', 'Surendranagar', 'Suri', 'Tawang', 'Tezpur', 'Thrippunithura', 'Thrissur', 'Tiruchchirappalli', 'Tirumala', 'Tirunelveli', 'Thiruvannamalai', 'Tirur', 'Thalassery', 'Thanjavur', 'Thekkady', 'Theni', 'Thiruvananthpuram', 'Thiruvannamalai', 'Tirupati', 'Trichy', 'Trippur', 'Tumkur', 'Tuni', 'Udaipur', 'Udhampur', 'Udupi', 'Ujjain', 'Unnao', 'UjjainFort', 'Vidisha', 'Vadodra', 'Valsad', 'Vapi', 'Varanasi', 'Varkala', 'VascodaGama', 'Vellore', 'Vishakhapatnam', 'Vijayawada', 'Vizianagaram', 'Vrindavan', 'Warangal', 'Washim', 'Yamunanagar', 'Yelahanka', 'bangladesh', 'bdesh', 'china', 'chinese', 'deshindia', 'indian', 'ind', 'pak', 'pakistan', 'us', 'uk', 'usa', 'ahmedabad', 'allahabad', 'aurangabad', 'bangalore', 'bengaluru', 'bangaloreans', 'bluru', 'bhopal', 'bhubaneswar', 'chandigarh', 'chennaicgarh', 'coimbatore', 'delhi', 'delhites', 'garhgoa', 'gurgaon', 'guwahati', 'hyderabad', 'indore', 'jaipur', 'kanpur', 'kochi', 'kolhapur', 'kolkata', 'kozhikode', 'ludhiana', 'luru', 'madurai', 'mumbai', 'mumbaikars', 'nagpur', 'nashik', 'nashikites', 'navi', 'mumbai', 'noida', 'patna', 'patnaites', 'puducherry', 'pune', 'raipur', 'rajkot', 'ranchi', 'surat', 'thane', 'thiruvananthapuram', 'trichy', 'vadodara', 'varanasi', 'yelagiri', 'rajasthan', 'karnataka', 'raj', 'ktaka', 'ap', 'hp', 'andhra', 'pradesh', 'arunachal', 'assam', 'bihar', 'chhattisgarh', 'goa', 'gujarat', 'haryana', 'himachal', 'jammu', 'kashmir', 'jharkhand', 'kerala', 'maharashtra', 'manipur', 'meghalaya', 'agaland', 'orissa', 'odisha', 'punjab', 'rajasthan', 'rajasthan', 'sikkim', 'tamil', 'nadu', 'tripura', 'uttarakhand', 'uttar', 'bengal', 'andaman', 'lakshadweep', 'pondicherry', 'pondi', 'pondy']

def scraper():
	city ="bangalore"		#city name

	src=urllib.request.urlopen("http://timesofindia.indiatimes.com/city/"+city)
	src = str(src.read())
	print(city+" done")
	#print(src[:10])
	return src

def cleaner(text):
	head=[]
	curpos=0
	while curpos<len(text):
		start=curpos
		if(text[curpos:curpos+4]=='<div'):
			while text[curpos:curpos+6]!= '</div>': curpos+=1
			if 'fsts' in text[start:curpos] : head.append(text[start:curpos])
		curpos+=1


	for i in range(len(head)):
		s = head[i].index('<span class="bln">')
		head[i] = head[i][:s-9]
		s = head[i].rfind('>')
		head[i] = head[i][s+1:]
	#print(head)
	return head


def predictor(hd):
	cnames=['politics','crime','civic','science','academic','environment', 'health','business','art' ,'other']
	catcount=[0]*len(cnames)

	wordlist=[]

	for cat in cnames : exec(cat+'={}')

	def classify(hd):
		hd=hd.lower()
		hd=cleaned(hd)
		hd=rooted(hd)
		categorypredicted = predict(hd)
		return categorypredicted

	def cleaned(hd):
		for punc in ['&rsquo;','&lsquo;','&rsquo','&lsquo',';',':',',','.','!','@','#','$','%','&','*','-','(',')','+','/','?',"'",'1','2','3','4','5','6','7','8','9','9','0',"\\",'1st','2nd','3rd']:
			if punc=="'" or punc=='&rsquo' or punc =='&lsquo'or punc=='&rsquo;' or punc =='&lsquo;':
				hd=hd.replace(punc,'')
			else:
				hd=hd.replace(punc,' ')
		hd=hd.split(" ")
		hd = [word for word in hd if word != '']
		hd = [value for value in hd if value not in prepositions]
		hd = [value for value in hd if value not in places]
		return hd

	def rooted(hd):
		roots=[]
		partOfSp = pos_tag(word_tokenize(' '.join(hd)),tagset='universal')
		for word in partOfSp:
			if word[1]=='VERB':
				roots.append(wnl.lemmatize(word[0],'v'))
			elif word[1]=='ADJ':
				roots.append(wnl.lemmatize(word[0],pos='a'))
			else:roots.append(wnl.lemmatize(word[0]))
		hd = roots
		return hd


	def predict(headline):
		catprob = [0]*len(cnames)
		for word in headline:
			total=0
			for cat in cnames:
				if word in wordlist[cnames.index(cat)]: total+= wordlist[cnames.index(cat)][word]
			if total==0: total=1
			for cat in cnames:
				if word in wordlist[cnames.index(cat)]:
					catprob[cnames.index(cat)] += 2.7183**(wordlist[cnames.index(cat)][word]/total)
		catcount[catprob.index(max(catprob))] = catcount[catprob.index(max(catprob))]+1
		return cnames[catprob.index(max(catprob))]	


	for cat in cnames:
			print('getting words from '+cat)
			cfile = open('catcount/'+cat+'.ccn',encoding='utf-8' , mode='r')
			w = cfile.readlines()
			cfile.close()
			while '\n' in w: w.remove('\n')
			while ' ' in w:  w.remove(' ')
			w=[w[i].split(' ') for i in range(len(w))]
			words = [x[0] for x in w if x!=['\n'] or x!=[' ']]
			freq =[int(x[1]) for x in w if x!=['\n'] or x!=[' ']]
			d = dict(list(zip(words,freq)))
			d.pop(' ',None)
			d.pop('',None)
			d.pop('\n',None)

			wordlist.append(d)
	#hd=[headline[:-1]*(headline[-1]=='\n')+headline*(headline[-1]!='\n') for headline in hd]
	hdno=1
	for headline in hd : 
		print(str(hdno)+':'+headline +' -- '+classify(headline))
		hdno=hdno+1


src = scraper()
headlines = cleaner(src)
predictor(headlines)


