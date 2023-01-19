from bs4 import BeautifulSoup

table = list()
for i in range(7):
    with open(f"index{i}.html", encoding="utf-8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        ans = ""
        for tag in soup.find_all('div', {'class': 'que multichoice deferredfeedback correct'}):
            q = tag.findNext('div', {'class': 'formulation clearfix'})
            quest = q.find('div', {'class': 'qtext'})
            ans += f"{quest.text}"
            answer = q.find('div', {'class': 'answer'})
            for el in answer.find_all('div'):
                answer_radio = el.find('input', checked='checked')
                if answer_radio is not None:
                    label = el.find('label', class_='ml-1')
                    uper = label.text
                    ans += f"|{uper.upper()}"
                    table.append(ans)
                    ans = ""

        for tag in soup.find_all('div', {'class': 'que multichoice deferredfeedback incorrect'}):
            q = tag.findNext('div', {'class': 'formulation clearfix'})
            quest = q.find('div', {'class': 'qtext'})
            ans += f"{quest.text}"
            answer = q.find('div', {'class': 'answer'})
            for el in answer.find_all('div'):
                answer_radio = el.find('input', checked='checked')
                if answer_radio is not None:
                    label = el.find('label', class_='ml-1')
                    ans += f"||{label.text}"
                    table.append(ans)
                    ans = ""

time_list = list(set(table))
time_list.sort()

table = []

for el in time_list:
    table.append(el.split('|'))

for el in table:
    print(el)
    print('_'*200)
