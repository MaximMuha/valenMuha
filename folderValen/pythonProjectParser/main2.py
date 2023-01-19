from bs4 import BeautifulSoup

table = list()
for i in range(7):
    with open(f"index{i}.html", encoding="utf-8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        ans = ""

        for tag in soup.find_all('div', {'class': 'formulation clearfix'}):
            quest = tag.find('div', {'class': 'qtext'})
            table.append(quest.text)

table.sort()
time_list = list(set(table))


for i in range(len(time_list)):
    print(f"{i+1}\t{time_list[i]}")

