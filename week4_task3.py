import matplotlib.pyplot as plt

x = ['Лекции', 'Семинары']
y = [99, 0.1]

plt.bar(x, y, label = 'Информатика', color = "purple", alpha = 0.6)


plt.xlabel('Процент материала который я понимаю')
plt.ylabel('%')
plt.title('Столбчатая диаграмма')
plt.legend(loc='center')
plt.show()