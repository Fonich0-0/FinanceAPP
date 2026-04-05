from PySide6.QtWidgets import (QApplication, QWidget, QComboBox, 
                               QLabel, QLineEdit, QPushButton, 
                               QCheckBox, QFrame, 
                               QPlainTextEdit, QMessageBox, QGridLayout,
                               QSpacerItem)

from PySide6.QtGui import Qt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import database as db
from datetime import datetime


# Виджеты
class StatWidgets(QWidget):
    def __init__(self, tab1, tab2):
        super().__init__()
        # Сохраняем ссылки на вкладки, которые пришли извне
        self.tab1w = tab1
        self.tab2w = tab2
        
        # Переменные
        self.combo_diagram = None
        self.input_date = None
        self.combo_categories = None
        self.input_amount = None
        self.combo_currency = None
        self.text_zone = None
        self.ready_bttn = None
        self.create_widgets()


    def add_operation(self):
        operation_is = "income"
        date = self.input_date.text() if self.input_date.text() else datetime.now().strftime('%Y-%m-%d')
        category = self.combo_categories.currentText()
        amount = int(self.input_amount.text())
        currency = self.combo_currency.currentText()
        description = self.text_zone.toPlainText() if self.text_zone else None

        database = db.DataBase()

        if database.connection_database():
            database.add_operation_to_db(operation_is, date, category, amount, currency, description)

            msg = QMessageBox(None)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Сообщение")
            msg.setText("Данные добавлены успешно!")
            msg.exec()
        
        else:
            msg = QMessageBox(None)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Сообщение")
            msg.setText("Произошла ошибка, данные не добавлены.")
            msg.exec()





    def create_widgets(self):
        self.grid = QGridLayout(self.tab1w)
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop) 
        # 1 вкладка -------------------------------------------------------------------------------------------------
        # Тип диаграммы
        self.label_diagram = QLabel("Тип диаграммы:", self.tab1w)
        self.grid.addWidget(self.label_diagram, 0, 0)


        diagrams = ["Круговая", "Линейная", "Столбчатая"]
        self.combo_diagram = QComboBox(self.tab1w)
        self.combo_diagram.setFixedSize(220, 30)
        self.combo_diagram.addItems(diagrams)
        self.grid.addWidget(self.combo_diagram, 1, 0)
        
        # Период времени
        label_period = QLabel("Выберите период времени:", self.tab1w)
        self.grid.addWidget(label_period, 2, 0)

        period_times = ["За всё время", "За год", "За месяц", "За неделю", "За день"]
        self.combo_period = QComboBox(self.tab1w)
        self.combo_period.setFixedSize(220, 30)
        self.combo_period.addItems(period_times)
        self.grid.addWidget(self.combo_period, 3, 0)
        # За какую-то дату
        self.text_area = QLineEdit(self.tab1w)
        self.text_area.setPlaceholderText(f"Или например за: {datetime.now().strftime("%Y-%m-%d")}") 
        self.text_area.setFixedSize(220, 20)
        self.grid.addWidget(self.text_area, 4, 0)

        # Операции
        self.label_operation = QLabel("Выберите тип операций:", self.tab1w)
        self.grid.addWidget(self.label_operation, 5, 0)

        operations = ["Расход", "Доход"]
        self.combo_operation = QComboBox(self.tab1w)
        self.combo_operation.setFixedSize(220, 30)
        self.combo_operation.addItems(operations)
        self.grid.addWidget(self.combo_operation, 6, 0)

        # Валюта
        self.label_currency = QLabel("Выберите валюту:", self.tab1w)
        self.grid.addWidget(self.label_currency, 7, 0)

        currencies = ["RUB", "USD", "EUR"]
        self.combo_currency = QComboBox(self.tab1w)
        self.combo_currency.setFixedSize(220, 30)
        self.combo_currency.addItems(currencies)
        self.grid.addWidget(self.combo_currency, 8, 0)

        # Кнопка для подтверждения
        self.ready_bttn = QPushButton("Подтвердить выбор", self.tab1w)
        self.ready_bttn.setStyleSheet(
            "padding: 9px;"
            "font-weight: bold;"
        )
        self.grid.addWidget(self.ready_bttn, 9, 0)

        

        # 2 Вкладка ------------------------------------------------------------------------------------
        # ЛЕВО
        # Чекбокс Расход/Доход
        # check_type_op = QCheckBox(Qt.Orientation.Vertical, self.tab2w)
        # check_type_op.setGeometry(12, 20, 150, 20)

        self.label_info = QLabel("Заполните данные для учета операции", self.tab2w)
        self.label_info.setGeometry(12, 55, 250, 30)

        categories_list = ["Продукты", "Развлечения", "Транспорт", "Кафе/Рестораны", "Здоровье", "Образование", "Другое"]
        self.combo_categories = QComboBox(self.tab2w)
        self.combo_categories.addItems(categories_list)
        self.combo_categories.setGeometry(12, 90, 250, 30)

        # Поле ввода даты
        self.input_date = QLineEdit(self.tab2w)
        current_date_str = datetime.now().strftime("%Y-%m-%d")
        self.input_date.setPlaceholderText(f"Например за: {current_date_str}") 
        self.input_date.setGeometry(12, 130, 250, 25)

        # Поле ввода суммы
        self.input_amount = QLineEdit(self.tab2w)
        self.input_amount.setPlaceholderText("Сумма, например: 1000") 
        self.input_amount.setGeometry(12, 165, 150, 30)

        # Выбор валюты 
        currency_list = ["Рубль", "Доллар", "Евро", "Юань", "..."]
        self.combo_currency = QComboBox(self.tab2w)
        self.combo_currency.addItems(currency_list)
        self.combo_currency.setGeometry(162, 165, 100, 30) 

        # Комментарий
        self.text_zone = QPlainTextEdit(self.tab2w)
        self.text_zone.setGeometry(12, 198, 250, 80)

        

        # Кнопка для подтверждения
        self.btn_confirm = QPushButton("Подтвердить выбор", self.tab2w)
        self.btn_confirm.clicked.connect(self.add_operation)
        self.btn_confirm.setGeometry(12, 280, 250, 30)

        # ПРАВО (подсказки и информация)

        hint_type = QLabel("--> Выберите тип операции: расход либо доход", self.tab2w)
        hint_type.setGeometry(280, 20, 350, 20)

        # Подсказка к категории
        hint_category = QLabel("--> Укажите, к какой статье бюджета относится операция", self.tab2w)
        hint_category.setGeometry(280, 90, 350, 30)

        # Подсказка к дате
        hint_date = QLabel("--> Дата, когда была совершена операция (ГГГГ-ММ-ДД)", self.tab2w)
        hint_date.setGeometry(280, 130, 350, 25)

        # Подсказка к сумме и валюте
        hint_amount_currency = QLabel("--> Введите сумму и выберите валюту операции", self.tab2w)
        hint_amount_currency.setGeometry(280, 165, 350, 30)
        
        # Подсказка к комментарию
        hint_comment = QLabel("--> Небольшое описание для памяти и таблицы", self.tab2w)
        hint_comment.setGeometry(280, 210, 350, 25)









