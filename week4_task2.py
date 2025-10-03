import matplotlib.pyplot as plt

amount = [4, 6]
labels = ["Посещающие", "Не посещающие"]
color_ = ["green", "red"]

plt.pie(amount, labels = labels, colors=color_, autopct = '%1.f%%')
plt.title("Посещаемость лекций по информатике")
plt.show()

amount = [1, 54]
labels = ["Поняли", "Не поняли"]
color_ = ["purple", "blue"]

plt.pie(amount, labels = labels, colors = color_, autopct = '%1.f%%')
plt.title("Количество понимающих материал из посещающих")
plt.show()