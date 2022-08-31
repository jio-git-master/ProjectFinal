from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class InvestmentModel(db.Model):

    __tablename__ = 'investment'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DATE)
    passbook = db.Column(db.String(100))
    application_form = db.Column(db.String(100))
    status = db.Column(db.String(100))
    date_approved = db.Column(db.DATE)

    def __init__(self, id, date, passbook, application_form, status):
        self.id = id
        self.date = date
        self.passbook = passbook
        self.application_form = application_form
        self.status = status



class ProductModel(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    unit_price = db.Column(db.DECIMAL)
    unit_quantity = db.Column(db.INTEGER)
    total_cost = db.Column(db.DECIMAL)

    def __init__(self, name, unit_price, unit_quantity, total_cost):
        self.name = name
        self.unit_price = unit_price
        self.unit_quantity = unit_quantity
        self.total_cost = total_cost

        def __repr__(self):
            return f"{self.name}"
class ClientModel(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    address = db.Column(db.String(200))
    p_number = db.Column(db.String(200))
    email = db.Column(db.String(200))
    birthday = db.Column(db.DATE)
    earnings = db.Column(db.FLOAT)
    password = db.Column(db.String(20))

    def __init__(self, name, address, p_number, email, birthday, earnings, password):
        self.name = name
        self.address = address
        self.p_number = p_number
        self.email = email
        self.birthday = birthday
        self.earnings = earnings
        self.password = password

        def __repr__(self):
            return f"{self.id}"



class LoanModel(db.Model):
    __tablename__ = "loan"

    id = db.Column(db.Integer, primary_key=True)
    employer_name = db.Column(db.String(200))
    occupation = db.Column(db.String(200))
    gross_income = db.Column(db.DECIMAL)
    date = db.Column(db.DATE)
    amount = db.Column(db.FLOAT(100), default=0)
    loan_plan = db.Column(db.String(100), default=None)
    purpose = db.Column(db.String(100))
    total_payable = db.Column(db.FLOAT(100), default=0)
    monthly_payable = db.Column(db.FLOAT(100), default=0)
    penalty_payable = db.Column(db.FLOAT(100), default=0)
    approved = db.Column(db.String(50))
    date_approved = db.Column(db.DATE)

    def __init__(self, id, employer_name, occupation, gross_income, date, amount, loan_plan, purpose, total_payable, monthly_payable, penalty_payable, approved):
        self.id = id
        self.employer_name = employer_name
        self.occupation = occupation
        self.gross_income = gross_income
        self.date = date
        self.amount = amount
        self.loan_plan = loan_plan
        self.purpose = purpose
        self.total_payable = total_payable
        self.monthly_payable = monthly_payable
        self.penalty_payable = penalty_payable
        self.approved = approved


        def __repr__(self):
            return f"{self.client_id}"


class AdminModel(db.Model):

    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))


    def __init__(self, email, password):
        self.email = email
        self.password = password



        def __repr__(self):
            return f"{self.username}:{self.password}"