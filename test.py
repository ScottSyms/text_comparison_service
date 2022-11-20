import requests

url_prefix = 'http://localhost:8000'

text1 = "Environment Canada has issued a winter storm warning for parts of Cape Breton, noting as much as 35 centimetres of snow could fall. The warning applies to Victoria County and Inverness County-Mabou and north. The weather agency says the snowfall will start Sunday evening over northern Cape Breton, with the largest snowfall expected over the Cape Breton Highlands. The snow is expected to continue falling until Monday afternoon. Westerly winds of 90 km/h will develop after midnight and continue until almost noon on Monday. 'Consider postponing non-essential travel until conditions improve,' said Environment Canada. 'Rapidly accumulating snow could make travel difficult over some locations. Prepare for quickly changing and deteriorating travel conditions.' It said above-freezing temperatures in areas near sea level will reduce the amount of snowfall to somewhere between 10 and 15 centimetres."
text2 = "Environment Canada has released a winter storm advisory for sections of Cape Breton, indicating as much as 35 centimetres of snow could fall. The warning covers Victoria County and Inverness County-Mabou and north. The weather agency says the snowfall will begin Sunday evening over northern Cape Breton, with the greatest snowfall expected over the Cape Breton Highlands. The snow is expected fall into Monday afternoon. Westerly winds of 90 km/h will develop after midnight and continue until almost noon on Monday. 'Consider postponing non-essential travel until conditions improve,' said Environment Canada. 'Rapidly accumulating snow could make travel difficult over some locations. Prepare for quickly changing and deteriorating travel conditions.' It said above-freezing temperatures in areas near sea level will reduce the amount of snowfall to somewhere between 10 and 15 centimetres."

# Test bert
print("Testing Google Bleu")
url_suffix = "/googlebleu"
myobj = {'text1': text1, 'text2': text2, 'lang': 'en'}
x = requests.post(url_prefix + url_suffix, json=myobj)
print(x.text)

# Test meteor
print("Testing Meteor")
url_suffix = "/meteor"
myobj = {'text1': text1, 'text2': text2, 'lang': 'en'}
x = requests.post(url_prefix + url_suffix, json=myobj)
print(x.text)

# Test BERT
print("Testing Bert")
url_suffix = "/bertscore"
myobj = {'text1': text1, 'text2': text2, 'lang': 'en'}
x = requests.post(url_prefix + url_suffix, json=myobj)
print(x.text)


# Test WER
print("Testing WER")
url_suffix = "/wer"
myobj = {'text1': text1, 'text2': text2, 'lang': 'en'}
x = requests.post(url_prefix + url_suffix, json=myobj)
print(x.text)


# Test BLEU
print("Testing BLEU")
url_suffix = "/bleu"
myobj = {'text1': text1, 'text2': text2, 'lang': 'en'}
x = requests.post(url_prefix + url_suffix, json=myobj)
print(x.text)

# Test ROUGE
print("Testing ROUGE")
url_suffix = "/rouge"
myobj = {'text1': text1, 'text2': text2, 'lang': 'en'}
x = requests.post(url_prefix + url_suffix, json=myobj)
print(x.text)


# Test SacreBLEU
print("Testing SacreBleu")
url_suffix = "/sacrebleu"
myobj = {'text1': text1, 'text2': text2, 'lang': 'en'}
x = requests.post(url_prefix + url_suffix, json=myobj)
print(x.text)
