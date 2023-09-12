from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age:{self.age}'


# Процессы
class Process(models.Model):
    name = models.CharField(max_length=5)

# Процессы
# prs = sqlalchemy.Table(
#     "prs",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer,  primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String(128))


# Операции
class Operation(models.Model):
    name = models.CharField(max_length=100)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)


# # Операции
# operation = sqlalchemy.Table(
#     "operation",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String(128)),
#     sqlalchemy.Column("process_id", sqlalchemy.ForeignKey('process.id'), nullable=False),
#
# )

# долженность работника
class Employ_position (models.Model):
    mane = models.CharField(max_length=100)

# # должность работника
# employ_position = sqlalchemy.Table(
#     "employ_position",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String(128)),
#
#)


# работник
class Worker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    employ_position = models.ForeignKey(Employ_position, on_delete=models.CASCADE)

# # работник
# worker = sqlalchemy.Table(
#     "worker",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String(128)),
#     sqlalchemy.Column("surname", sqlalchemy.String(128)),
#     sqlalchemy.Column("employ_position", sqlalchemy.ForeignKey('employ_position.id'), nullable=False),
# )
#
# Контрольные дествия


class Control_action(models.Model):
    name = models.CharField(max_length=100)


# # конрольное действие
# control_action = sqlalchemy.Table(
#     "control_action",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String(128)),
#
# )

#    Метод контроля
class Method(models.Model):
    name = models.CharField(max_length=100)


# # метод котроля
# method = sqlalchemy.Table(
#     "method",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("name", sqlalchemy.String(128)),
#
# )


# Справка о нарушкении
class Certificate_of_violations(models.Model):
    date = models.DateField(auto_now_add=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)


# # Справка о нарушении
# certificate_of_violations = sqlalchemy.Table(
#     "certificate_of_violations",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("date", sqlalchemy.Date, default=datetime.utcnow),
#     sqlalchemy.Column("worker", sqlalchemy.ForeignKey('worker.id'), nullable=False),
#
# )
#

#Реестр
class Reestr(models.Model):
    code = models.CharField(max_length=5)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    control_action = models.ForeignKey(Control_action, on_delete=models.CASCADE)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)

# Реестр
# reestr = sqlalchemy.Table(
#     "reestr",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("code", sqlalchemy.String(5)),
#     sqlalchemy.Column("operation_id", sqlalchemy.ForeignKey('operation.id'), nullable=False),
#     sqlalchemy.Column("worker", sqlalchemy.ForeignKey('worker.id'), nullable=False),
#     sqlalchemy.Column("control_action", sqlalchemy.ForeignKey('control_action.id'), nullable=False),
#     sqlalchemy.Column("method", sqlalchemy.ForeignKey('method.id'), nullable=False),


 # Строка в справке о нарушениях
class Violation(models.Model):
     certificate_of_violations = models.ForeignKey(Certificate_of_violations, on_delete=models.CASCADE)
     reestr = models.ForeignKey(Reestr, on_delete=models.CASCADE)
     title= models.TextField(max_length=256)
     employ_position = models.ForeignKey(Employ_position, on_delete=models.CASCADE)
     worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
     amount = models.FloatField(max_length=256)

#
# # Строка в справке о нарушениях
# violation = sqlalchemy.Table(
#     "violation",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("certificate_of_violations", sqlalchemy.ForeignKey('certificate_of_violations.id'), nullable=False),
#     sqlalchemy.Column("core_reestr", sqlalchemy.ForeignKey('reestr.id'), nullable=False),
#     sqlalchemy.Column("title", sqlalchemy.String(128)),
#     sqlalchemy.Column("employ_position", sqlalchemy.ForeignKey('employ_position.id'), nullable=False),
#     sqlalchemy.Column("worker", sqlalchemy.ForeignKey('worker.id'), nullable=False),
#     sqlalchemy.Column("amount", sqlalchemy.Float),
#
# )


# Журнал
class Journal(models.Model):
    date = models.DateField(auto_now_add=True)
    violation = models.ForeignKey(Violation, on_delete=models.CASCADE)
    measures = models.TextField(max_length=256)

# # Журнал
# journal = sqlalchemy.Table(
#     "journal",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("date", sqlalchemy.Date, default=datetime.utcnow),
#     sqlalchemy.Column("violation", sqlalchemy.ForeignKey('violation.id'), nullable=False),
#     sqlalchemy.Column("measures", sqlalchemy.String(128)),
#
# )
#


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'