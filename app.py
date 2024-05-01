from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse
from flask_migrate import Migrate

from models import db, User, School, Invoice, InvoiceLine, Payment, ApprovalHistory, SchoolBeneficiary, LoanProduct



def create_app():
  
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://creadable:B1Y8fNQLYPBxcp8ISl9uTNXZKO5Hbk0E@dpg-cop1n463e1ms73bn17sg-a.oregon-postgres.render.com/hackathon_ssm1'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)
  migrate = Migrate(app, db)
  api = Api(app)

  class UserResource(Resource):
      def get(self, user_id):
          user = User.query.get(user_id)
          if not user:
              return {'message': 'User not found'}, 404
          return user.serialize()

  class SchoolResource(Resource):
      def get(self, school_id):
          school = School.query.get(school_id)
          if not school:
              return {'message': 'School not found'}, 404
          return school.serialize()

  class InvoiceResource(Resource):
      def get(self, invoice_id):
          invoice = Invoice.query.get(invoice_id)
          if not invoice:
              return {'message': 'Invoice not found'}, 404
          return invoice.serialize()

  class InvoiceLineResource(Resource):
      def get(self, line_id):
          line = InvoiceLine.query.get(line_id)
          if not line:
              return {'message': 'Invoice Line not found'}, 404
          return line.serialize()

  class PaymentResource(Resource):
      def get(self, payment_id):
          payment = Payment.query.get(payment_id)
          if not payment:
              return {'message': 'Payment not found'}, 404
          return payment.serialize()

  class ApprovalHistoryResource(Resource):
      def get(self, approval_id):
          approval = ApprovalHistory.query.get(approval_id)
          if not approval:
              return {'message': 'Approval History not found'}, 404
          return approval.serialize()

  class SchoolBeneficiaryResource(Resource):
      def get(self, beneficiary_id):
          beneficiary = SchoolBeneficiary.query.get(beneficiary_id)
          if not beneficiary:
              return {'message': 'School Beneficiary not found'}, 404
          return beneficiary.serialize()

  class LoanProductResource(Resource):
      def get(self, product_id):
          product = LoanProduct.query.get(product_id)
          if not product:
              return {'message': 'Loan Product not found'}, 404
          return product.serialize()

  # Add routes to the API
  api.add_resource(UserResource, '/users/<int:user_id>')
  api.add_resource(SchoolResource, '/schools/<int:school_id>')
  api.add_resource(InvoiceResource, '/invoices/<int:invoice_id>')
  api.add_resource(InvoiceLineResource, '/invoice-lines/<int:line_id>')
  api.add_resource(PaymentResource, '/payments/<int:payment_id>')
  api.add_resource(ApprovalHistoryResource, '/approval-history/<int:approval_id>')
  api.add_resource(SchoolBeneficiaryResource, '/school-beneficiaries/<int:beneficiary_id>')
  api.add_resource(LoanProductResource, '/loan-products/<int:product_id>')

  return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
