from flask import Flask
from models import db, User, School, Invoice, InvoiceLine, Payment, ApprovalHistory, SchoolBeneficiary, LoanProduct
from faker import Faker
from app import create_app
import random
import datetime

app = create_app()
fake = Faker()

def generate_users(num_users):
    with app.app_context():
        for _ in range(num_users):
            user = User(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                is_admin=random.choice([True, False])
            )
            db.session.add(user)
        db.session.commit()

def generate_schools(num_schools):
    with app.app_context():
        for _ in range(num_schools):
            school = School(
                name=fake.company(),
                account_number=fake.random_number(digits=10)
            )
            db.session.add(school)
        db.session.commit()

def generate_invoices(num_invoices):
    with app.app_context():
        for _ in range(num_invoices):
            invoice = Invoice(
                user_id=random.randint(1, 10),
                school_id=random.randint(1, 10),
                invoice_number=fake.random_number(digits=5),
                amount=fake.random_number(digits=4),
                date_submitted=fake.date_this_decade()
            )
            db.session.add(invoice)
        db.session.commit()

def generate_invoice_lines(num_lines):
    with app.app_context():
        for _ in range(num_lines):
            line = InvoiceLine(
                invoice_id=random.randint(1, 10),
                description=fake.text(),
                quantity=fake.random_number(digits=1),
                unit_price=fake.random_number(digits=2),
                total_price=fake.random_number(digits=3)
            )
            db.session.add(line)
        db.session.commit()

def generate_payments(num_payments):
    with app.app_context():
        for _ in range(num_payments):
            payment = Payment(
                invoice_id=random.randint(1, 10),
                amount_paid=fake.random_number(digits=3),
                payment_date=fake.date_this_decade()
            )
            db.session.add(payment)
        db.session.commit()

def generate_approval_histories(num_histories):
    with app.app_context():
        for _ in range(num_histories):
            approval = ApprovalHistory(
                invoice_id=random.randint(1, 10),
                approver_id=random.randint(1, 10),
                approval_status=random.choice(['pending', 'approved', 'rejected']),
                approval_date=fake.date_this_decade()
            )
            db.session.add(approval)
        db.session.commit()

def generate_school_beneficiaries(num_beneficiaries):
    with app.app_context():
        for _ in range(num_beneficiaries):
            beneficiary = SchoolBeneficiary(
                school_id=random.randint(1, 10),
                name=fake.name(),
                description=fake.text()
            )
            db.session.add(beneficiary)
        db.session.commit()

def generate_loan_products(num_products):
    with app.app_context():
        for _ in range(num_products):
            product = LoanProduct(
                name=fake.company(),
                interest_rate=fake.random_number(digits=1),
                max_loan_amount=fake.random_number(digits=5)
            )
            db.session.add(product)
        db.session.commit()

if __name__ == '__main__':
    generate_users(10)
    generate_schools(10)
    generate_invoices(10)
    generate_invoice_lines(10)
    generate_payments(10)
    generate_approval_histories(10)
    generate_school_beneficiaries(10)
    generate_loan_products(10)
