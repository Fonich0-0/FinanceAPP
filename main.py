import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout
from ui.classes import stat_widgets as w
from ui.classes import data_charts as d

app = QApplication(sys.argv)

# 1. Создаем главное окно и вкладки
window = QWidget()
window.setWindowTitle("FinanceAPP")
window.resize(800, 600)

tabs = QTabWidget(window)
tabs.resize(800, 600)

tab1 = QWidget()
tab2 = QWidget()

# 2. Инициализируем виджеты (кнопки, поля ввода)
widgets = w.StatWidgets(tab1, tab2)

# 3. Инициализируем график
# ВАЖНО: Создаем Layout на tab1 справа от настроек для графика
chart_layout = QVBoxLayout()
# Добавляем отступ, чтобы график не перекрывал кнопки (или добавьте в grid)
widgets.grid.addLayout(chart_layout, 0, 1, 10, 1) 

diagram = d.DataCharts()
diagram.chart_container = chart_layout # Передаем контейнер в класс графика
diagram.set_ui(chart_layout, widgets) 

# 4. Логика кнопок
tabs.addTab(tab1, "Главное меню")
tabs.addTab(tab2, "Настройка")

# Связываем кнопку с обновлением
widgets.ready_bttn.clicked.connect(diagram.update_diagram)

window.show()
sys.exit(app.exec())

