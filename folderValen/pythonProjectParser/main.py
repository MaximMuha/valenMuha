import xlsxwriter
from bs4 import BeautifulSoup

table = list()
for i in range(4):
    with open(f"index/index{i}.html", encoding="utf-8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        ans = ""
        for tag in soup.find_all('div', class_='que multichoice deferredfeedback complete'):
            grade = tag.findNext('div', class_='grade')
            q = tag.findNext('div', {'class': 'formulation clearfix'})
            quest = q.find('div', {'class': 'qtext'})
            ans += f"{quest.text}"
            if grade.text == 'Баллов: 1,00 из 1,00':
                answer = q.find('div', {'class': 'answer'})
                for el in answer.find_all('div'):
                    answer_radio = el.find('input', checked='checked')
                    if answer_radio is not None:
                        label = el.find('label', class_='ml-1')
                        uper = label.text
                        ans += f"|{uper.upper()}"
                        table.append(ans)
                        ans = ""
            elif grade.text == 'Баллов: 0,00 из 1,00':
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

workbook = xlsxwriter.Workbook('tab1.xlsx')
worksheet = workbook.add_worksheet()
row = 0
for col, data in enumerate(table):
    worksheet.write_row(col, row, data)

workbook.close()
