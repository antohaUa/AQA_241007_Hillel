import requests

url = "https://swapi-graphql.netlify.app/.netlify/functions/index"

body = """ 
query Query { 
  allFilms { 
    films { 
      title 
    } 
  } 
} 
"""

response = requests.get(url=url, json={"query": body})
print("response status code: ", response.status_code)
if response.status_code == 200:
    print("response : ", response.content)
    print("response : ", response.text)
    print("response : ", response.json())
