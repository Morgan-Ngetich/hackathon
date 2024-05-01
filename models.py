from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    invoices = relationship('Invoice', backref='user', lazy=True)
    
    def serialize(self):
      return {
          'id': self.id,
          'username': self.username,
          'email': self.email,
          'is_admin': self.is_admin
      }

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    account_number = db.Column(db.String(50), nullable=False)

    beneficiaries = relationship('SchoolBeneficiary', backref='school', lazy=True)
    
    def serialize(self):
      return {
          'id': self.id,
          'name': self.name,
          'account_number': self.account_number
      }

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    invoice_number = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date_submitted = db.Column(db.Date, nullable=False)
    extracted_text = db.Column(db.Text)  # New column to store extracted text
    
    invoice_lines = relationship('InvoiceLine', backref='invoice', lazy=True)
    payments = relationship('Payment', backref='invoice', lazy=True)
    approval_history = relationship('ApprovalHistory', backref='invoice', lazy=True)
    
    def serialize(self):
      return {
          'id': self.id,
          'user_id': self.user_id,
          'school_id': self.school_id,
          'invoice_number': self.invoice_number,
          'amount': self.amount,
          'date_submitted': self.date_submitted,
          'extracted_text': self.extracted_text  # Include extracted text in serialization
      }

class InvoiceLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    
    def serialize(self):
      return {
          'id': self.id,
          'invoice_id': self.invoice_id,
          'description': self.description,
          'quantity': self.quantity,
          'unit_price': self.unit_price,
          'total_price': self.total_price
      }
      
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    amount_paid = db.Column(db.Integer, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    
    def serialize(self):
      return {
          'id': self.id,
          'invoice_id': self.invoice_id,
          'amount_paid': self.amount_paid,
          'payment_date': self.payment_date
      }

class ApprovalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    approver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    approval_status = db.Column(db.String(50), nullable=False)
    approval_date = db.Column(db.Date, nullable=False)
    
    def serialize(self):
      return {
          'id': self.id,
          'invoice_id': self.invoice_id,
          'approver_id': self.approver_id,
          'approval_status': self.approval_status,
          'approval_date': self.approval_date
      }

class SchoolBeneficiary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    
    
    def serialize(self):
      return {
          'id': self.id,
          'school_id': self.school_id,
          'name': self.name,
          'description': self.description
      }

class LoanProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    interest_rate = db.Column(db.Integer, nullable=False)
    max_loan_amount = db.Column(db.Integer, nullable=False)    

    def serialize(self):
      return {
          'id': self.id,
          'name': self.name,
          'interest_rate': self.interest_rate,
          'max_loan_amount': self.max_loan_amount
      }
