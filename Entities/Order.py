class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Employee: {self.employee} Student: {self.student} Books: {str([str(book) for book in self.books])} OrderDate: {self.order_date}'