import json

s = [{"website_name": "r", "mail_id": "t", "pass_str": "Pe6:l"}, {"website_name": "r", "mail_id": "t", "pass_str": "Pe6:l"}]

with open('temp1.json', 'r+') as f:
    if f.read() != "":
        f.seek(0)
        j = json.load(f)
        print(j)

with open('temp1.json', 'w+') as f:
    json.dump(s, f, indent=4)
