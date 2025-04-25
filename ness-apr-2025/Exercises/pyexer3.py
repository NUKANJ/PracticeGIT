import re

log = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)'

pattern = r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<date>.*?)\] "GET (?P<pics_url>/pics/.*?) HTTP.*?" \d+ \d+ "(?P<refer>http[s]?://[^"]+)"'
#\d{1,3} Matches 1 to 3 digits — like 123
#\. A literal period "."
#{3} Repeats 3 times
#?P<date> named group"date"
#.*? matches the characters/match of any character
#HTTP.*?" matches the rest of HTTP method string, ending on the closing quote
match = re.search(pattern,log)

if match:
    ip = match.group("ip")
    date = match.group("date")
    pics_url = match.group("pics_url")
    referer = match.group("refer")

    print("IP:",ip)
    print("Date:", date)
    print("Pics URL:", pics_url)
    print("Referer URL:", referer)
else:
    print("No match found.")