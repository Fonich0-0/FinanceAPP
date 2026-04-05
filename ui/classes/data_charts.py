from PySide6.QtCharts import (QChart, QChartView, QPieSeries, 
                              QLineSeries, QBarSeries, QBarSet, 
                              QBarCategoryAxis, QValueAxis, QPieSlice)
from PySide6.QtGui import QPainter, QFont, Qt, QBrush, QColor

# Диаграмма
class DataCharts:
    COLORS = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD"]
    
    def __init__(self):
        self.chart = QChart()
        self.chart_view = QChartView(self.chart)
        self.chart_container = None # Будет задано позже
        self.widgets = None         # Будет задано позже
        
        # Базовая настройка
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setBackgroundVisible(False)
        
        # Инициализируем оси (но не добавляем их пока нет данных)
        self.axis_x = QBarCategoryAxis()
        self.axis_y = QValueAxis()

    def set_ui(self, container_layout, widgets_instance):
        """Связываем логику графиков с интерфейсом"""
        self.chart_container = container_layout
        self.widgets = widgets_instance
        
        # Добавляем виджет графика в макет
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setStyleSheet("background-color: white; border-radius: 10px;")
        self.chart_container.addWidget(self.chart_view)

    def clear_diagram(self):
        """Очистка перед перерисовкой"""
        self.chart.removeAllSeries()
        # Удаляем старые оси, чтобы они не дублировались
        for axis in self.chart.axes():
            self.chart.removeAxis(axis)

    def update_diagram(self):
        if not self.widgets: return
        
        self.clear_diagram()
        diagram_type = self.widgets.combo_diagram.currentText()
        data = {"Еда": 500, "Игры": 1000, "Кино": 300} # Заглушка
        
        if diagram_type == "Круговая":
            self.create_pie_chart(data)
        elif diagram_type == "Линейная":
            self.create_line_chart()
        elif diagram_type == "Столбчатая":
            self.create_bar_chart(data)

    def create_pie_chart(self, data):
        self.chart.setTitle("Распределение по категориям")
        series = QPieSeries()
        for label, val in data.items():
            series.append(label, val)
        self.chart.addSeries(series)

    def create_line_chart(self):
        self.chart.setTitle("Динамика операций")
        series = QLineSeries()
        days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
        values = [2000, 3500, 1500, 2800, 4200, 1900, 2300]
        
        for i, v in enumerate(values):
            series.append(i, v)
        
        self.chart.addSeries(series)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)
        self.axis_x.setCategories(days)
        self.axis_y.setRange(0, max(values) * 1.1)

    def create_bar_chart(self, data):
        self.chart.setTitle("Сравнение категорий")
        series = QBarSeries()
        bar_set = QBarSet("Сумма")
        for val in data.values():
            bar_set.append(val)
        series.append(bar_set)
        
        self.chart.addSeries(series)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)
        self.axis_x.setCategories(list(data.keys()))
        self.axis_y.setRange(0, max(data.values()) * 1.1)
