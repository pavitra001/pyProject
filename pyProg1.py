#counting how often each character appears in text
message = 'If you can control the code, You can control the world'
count = {}

for character in message:
  count.setdefault(character, 0)
  count[character] = count[character] + 1

print(count)  
