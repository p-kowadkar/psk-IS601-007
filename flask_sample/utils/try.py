import requests

url = "https://anime-db.p.rapidapi.com/anime"

querystring = {"page":"1","size":"10","search":"Fullmetal","genres":"Fantasy,Drama","sortBy":"ranking","sortOrder":"asc"}

headers = {
	"X-RapidAPI-Key": "f13f1b1dfamsha7a40ed62397721p1169fajsn06103cf9eaf0",
	"X-RapidAPI-Host": "anime-db.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())