from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QLineEdit, QPushButton
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QLineSeries
from PySide6.QtGui import QPainter
from datetime import datetime
import sys

app = QApplication(sys.argv)  # Создание приложения

window = QWidget()  
window.setWindowTitle("FinancialAPP")
window.setGeometry(444, 215, 700, 500)  # (x, y, width, height)
#window.setStyleSheet('''background: #ebf2fc''')

# Диаграмма
chart = QChart()
chart.setTitle("Расходы по категориям")

chart_view = QChartView(chart, window)
chart_view.setRenderHint(QPainter.Antialiasing)  # Сглаживание
chart_view.setGeometry(225, 13, 480, 300)

def diagram():
    global chart_view, chart
    if combo_diagram.currentText() == "Круговая":
        series = QPieSeries()
        series.append("Продукты", 15000).setLabelVisible(True)
        series.append("Развлечения", 8000).setLabelVisible(True)
        series.append("Транспорт", 5000).setLabelVisible(True)
        series.append("Кафе/Рестораны", 12000).setLabelVisible(True)
        series.append("Другое", 1260).setLabelVisible(True)
        series.append("Здоровье", 10000).setLabelVisible(True)
        series.append("Образование", 8000).setLabelVisible(True)
        #.setExploded(True)

        chart.removeAllSeries()
        chart.addSeries(series)
        

    elif combo_diagram.currentText() == "Линейная":
        series = QLineSeries()
        days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
        values = [2000, 3500, 1500, 4000, 3000, 5000, 1000]
        series.append(0, 2)
        series.append(1, 5)

        chart.removeAllSeries()
        chart.addSeries(series)

    elif combo_diagram.currentText() == "Столбчатая":
        pass





# Тип диаграммы
label_diagram = QLabel("Тип диаграммы:", window)
label_diagram.setGeometry(12, 7, 220, 30)

diagrams = ["Круговая", "Линейная", "Столбчатая"]
combo_diagram = QComboBox(window)
combo_diagram.setFixedSize(220, 30)
combo_diagram.addItems(diagrams)
combo_diagram.setGeometry(12, 35, 220, 30)

# label_category = QLabel("Выберите категорию:", window)
# label_category.setGeometry(12, 7, 220, 30)

# categories = ["Продукты", "Развлечения", "Транспорт", "Кафе/Рестораны", "Здоровье", "Образование", "Другое"]
# combo_categories = QComboBox(window)
# combo_categories.setFixedSize(220, 30)
# combo_categories.addItems(categories)
# combo_categories.setGeometry(12, 35, 220, 30)

# Период времени
label_period = QLabel("Выберите период времени:", window)
label_period.setGeometry(12, 70, 220, 30)

period_times = ["За всё время", "За год", "За месяц", "За неделю", "За день"]
combo_period = QComboBox(window)
combo_period.setFixedSize(220, 30)
combo_period.addItems(period_times)
combo_period.setGeometry(12, 98, 220, 30)

# За какую-то дату
text_area = QLineEdit(window)
text_area.setPlaceholderText(f"Или например за: {datetime.now().strftime("%Y-%m-%d")}") 
text_area.setFixedSize(220, 20)
text_area.setGeometry(12, 135, 270, 15)


# Операции
label_operation = QLabel("Выберите тип операций:", window)
label_operation.setGeometry(12, 155, 220, 30)

operations = ["Расход", "Доход"]
combo_operation = QComboBox(window)
combo_operation.setFixedSize(220, 30)
combo_operation.addItems(operations)
combo_operation.setGeometry(12, 183, 220, 30)

# Валюта
label_currency = QLabel("Выберите валюту:", window)
label_currency.setGeometry(12, 218, 220, 30)

currencies = ["RUB", "USD", "EUR"]
combo_currency = QComboBox(window)
combo_currency.setFixedSize(220, 30)
combo_currency.addItems(currencies)
combo_currency.setGeometry(12, 246, 220, 30)

# Кнопка для подтверждения
ready_bttn = QPushButton("Подтвердить выбор", window)
ready_bttn.setGeometry(12, 280, 220, 30)
ready_bttn.clicked.connect(diagram)




window.show()
sys.exit(app.exec())