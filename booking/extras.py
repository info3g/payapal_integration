from django.conf import settings
import braintree


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        environment='sandbox',
        merchant_id='r5kz2v8yvb7wvxqk',
        public_key='d9s8mg2qxpq6gnsm',
        private_key='df64ca446a9a445f43f7424dbe366922'
    )
)

def generate_client_token():
    return gateway.client_token.generate()

def transact(options):
    return gateway.transaction.sale(options)

def find_transaction(id):
    return gateway.transaction.find(id)
