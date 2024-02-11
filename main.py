import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class CoffeeBase(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect('coffee.sqlite')
        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)
        # выведем содержимое базы данных в файл без всяких лишних действий
        self.show_data()

        self.add_edit_btn.clicked.connect(self.open_add_edit_form)

    def show_data(self):
        query = "SELECT * FROM Coffee"
        cur = self.connection.cursor()
        # cur.description = ["id", "variety_name", "degree_of_roasting", "ground_or_beans", "description_of_taste", \
        #                    "price", "packaging_volume_gram"]
        res = cur.execute(query).fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()

    def open_add_edit_form(self):
        self.add_edit_form = AddEditCoffeeForm()
        self.add_edit_form.show()


class AddEditCoffeeForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect('coffee.sqlite')
        self.initUI()

    def initUI(self):
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.add_btn.clicked.connect(self.add_data)
        self.edit_btn.clicked.connect(self.edit_data)

    def get_data(self, param):
        flag = all([self.id.text(), self.variety_name.text(), self.degree_of_roasting.text(),
                    self.ground_or_beans.text(), self.description_of_taste.text(),
                    self.price.text(), self.packaging_volume_gram.text()])
        if flag:
            variety_name = self.variety_name.text()
            degree_of_roasting = self.degree_of_roasting.text()
            ground_or_beans = self.ground_or_beans.text()
            description_of_taste = self.description_of_taste.text()
            if self.id.text().isdigit() and self.packaging_volume_gram.text().isdigit():
                id = int(self.id.text())
                is_id = self.connection.cursor().execute(f"SELECT id FROM Coffee WHERE id={id}").fetchall()
                if param == "add":
                    # print(is_id)
                    if is_id:
                        return False
                elif param == "edit":
                    if not is_id:
                        return False
                packaging_volume_gram = int(self.packaging_volume_gram.text())
                float_number = self.price.text().split('.')
                if len(float_number) <= 2 and ''.join(float_number).isdigit():
                    price = float(self.price.text())
                    return [id, variety_name, degree_of_roasting, ground_or_beans, description_of_taste,
                            price, packaging_volume_gram]
        return False

    def add_data(self):
        cur = self.connection.cursor()
        line = self.get_data("add")
        # print(line)
        if line:
            query = f"""INSERT INTO Coffee (
            id, variety_name, degree_of_roasting, 
            ground_or_beans, description_of_taste, 
            price, packaging_volume_gram) 
            VALUES {tuple(line)}"""
            # print(query)
            cur.execute(query)
            self.connection.commit()
        else:
            QMessageBox().warning(self, "Ошибка заполнения", "Заполните поля корректно!")

    def edit_data(self):
        cur = self.connection.cursor()
        line = self.get_data("edit")
        # print(line)
        if line:
            query = f"""UPDATE Coffee 
                    SET 
                    id = ?,
                    variety_name = ?,
                    degree_of_roasting = ?, 
                    ground_or_beans = ?,
                    description_of_taste = ?, 
                    price = ?,
                    packaging_volume_gram = ? 
                    WHERE id = {line[0]}"""
            # print(query)
            cur.execute(query, tuple(line))
            self.connection.commit()
        else:
            QMessageBox().warning(self, "Ошибка заполнения", "Заполните поля корректно!\nВозможно нет такой записи")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee_db = CoffeeBase()
    coffee_db.show()
    sys.exit(app.exec())
