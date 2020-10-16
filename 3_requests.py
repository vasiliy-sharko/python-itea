import requests

r = requests.get("https://google.com")
print(f"URL - {r.url}, status code - {r.status_code}, response time - .{r.elapsed.microseconds % 1000} ms")

r = requests.post("https://httpbin.org/post", data={'key': 'value'})
print(r.json())

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("https://httpbin.org/get", params=payload)
print(f"URL - {r.url}")

requests.get("https://api.github.com", auth=("user", "pass"))
