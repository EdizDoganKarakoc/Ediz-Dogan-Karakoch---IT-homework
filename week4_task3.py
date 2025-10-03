import matplotlib.pyplot as plt

x = ['Лекции', 'Семинары']
y = [99, 0.1]

plt.bar(x, y, label = 'Данные с календаря', color = "purple", alpha = 0.6)


plt.xlabel('Месяц года')
plt.ylabel('Кол-во дней')
plt.title('Столбчатая диаграмма')
plt.legend(loc='center')
plt.show()