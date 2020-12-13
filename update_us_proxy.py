with open('proxy-list.txt') as f:
    proxy_list = f.readlines()


us_proxy = []

for i in proxy_list:
    p = i.split(" ")
    address = p[0]
    if len(p) > 1:
        c = p[1].split("-")[0]
        if c == "US":
            print(address)
            us_proxy.append(address)


with open("us_proxy.txt", "w") as f:
    for i in us_proxy:
        f.write(i)
        f.write("\n")
    f.close()
