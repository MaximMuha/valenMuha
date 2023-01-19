from bs4 import BeautifulSoup

table = list()
for i in range(7):
    with open(f"index{i}.html", encoding="utf-8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        ans = ""

        for tag in soup.find_all('div', {'class': 'formulation clearfix'}):
            quest = tag.find('div', {'class': 'qtext'})
            answer = tag.find('div', {'class': 'answer'})
            ans += quest.text
            for el in answer.find_all('div'):
                answer_radio = el.find('input', checked='checked')
                if answer_radio is not None:
                    label = el.find('label', class_='ml-1')
                    if el.find('div', class_='r0 r1 correct') is not None:
                        uper = label.text
                        ans += f"|{uper.upper()}"
                    elif el.find('div', class_='r0 r1 incorrect') is not None:
                        ans += f"|{label.text}"
                table.append(ans)
                ans = ""

table.sort()
time_list = list(set(table))

table = []

for el in time_list:
    table.append(el.split('|'))

for i in range(len(table)):
    print(f"{i + 1}\t{table[i]}")
