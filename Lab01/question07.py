import re

f=open("weather.txt", mode="r", encoding="utf8")
content=f.read()
f.close()

pattern=re.compile("([A-ω]*[άέίόύήώϊΆΈΊΌΎΉΏ][A-ω]*)")
result=pattern.findall(content)

print(result)
print(len(result))

