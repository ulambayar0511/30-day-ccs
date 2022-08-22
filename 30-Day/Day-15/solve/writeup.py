import requests

url = "http://localhost:8000/"
response = requests.get(url)
text = response.text
regex = text[430:500]
regex = regex.split('+')
a = regex[0]
b = regex[1][0:regex[1].index('=')]


num1 = requests.get("http://md5decrypt.net/Api/api.php?hash=" + a +
                    "&hash_type=md5&email=ulmaaulambayar4@gmail.com&code=7c3164ebc151124b").text
num2 = requests.get("http://md5decrypt.net/Api/api.php?hash=" + b +
                    "&hash_type=md5&email=ulmaaulambayar4@gmail.com&code=7c3164ebc151124b").text
niilber = int(num1)+int(num2)
print(niilber)
result = requests.post(url+"/sum", data={'sum': niilber})
print(result.text)
