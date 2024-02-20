from flask import Flask, request, jsonify 
from firebase_admin import credentials, auth
from firebase_admin import initialize_app
from dotenv import load_dotenv
import os

load_dotenv()

private_key = os.getenv("FIREBASE_PRIVATE_KEY")






app = Flask(__name__)

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "bookr-db0e3",
  "private_key_id": "d7c4ce501bcd9a91ba8ba370eaf217836bc6c9eb",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCUDl/9G0okLUUr\nv9Hf5laAOXFpdTShS4+1ygZ+ZlbnVmCtv30EWAFioK+4ENwomSKHiz6pX+FpStT+\n/Z/oLXUTErw6J/BAjRiQ4tQVUfWqv7gfNx4cvAejlRPJvP3Q96JmTjawwgDMK/G8\n6n9UtXnFpPRwwY1s2lkXm1/OQtLlnAhFnRxYL3qBAAq0gYOdjcJmS7MlreGdGJDu\njQXBPoLICOA5kSivHgpL8lzyeBYpEZiVCoItPrA30irAiqY664BhKDRFZtR7Y0tB\nAO22FdPShiDZzuSHM2aj6lq/fk38hStRJg6fhgwAXf95EWQZRRo7mT/te4a69rcm\n/utevk71AgMBAAECggEAF51XWBKDN9P0pW659eFSSK9g1HY6R8O6jz9C2+RM1icj\n0nKpaQj0Z5vDizM9Okh6hm4CN5ewZ0/lOyqO18RwWPNzDD+UhWc71NgpBaGF8o8T\nuf7bka+39DJx7opzXWIyB+lPtc+ruuUDcKNiXct4Obr+tgFZIlSNQ0On+0kTREXp\nvFtKeq59CPeMP6YjaoqptQ22a6OuGK2LBb4nLeF2o4AyWg66JR4g6PW8L83Caa1N\nMOWsZoKUJ/yJKe8RRfhP68cBMbWlq066d5fBAj9UFf/l0I/CCiPbiNLE8Mezfy0W\nqgejaaP0x16Yt0LIzGVN+lU/6qHJPF7JMFRKDiU2vQKBgQDEg9qZwrIY8qJ6COhB\nrSpKoh7X2EMX3eIfGNoB1suoBoZ62kSTIsg9k1QtN5k5VWVa6Ro8nM2qZdFwTf6s\n12N5zvUsTh1MC9VP98zlM7lDlUY/8fkXqCDjRvOO3ruUQzfyIx7qeChtYoyFWPBr\nS3gOo33GyRagdUBKpTXPQ0TN4wKBgQDA32SLNI6OUFELjyfXEeoJlxPp4+KBJekW\nFggfONPGhw3sIz8Pd1DHSDcBCah2twadRynEsLh4TMgaN/WroVsQSqoIEihD9hJV\njOPJkYNS6CUp8yLCapj/talWpxHSwZbxo9H2GssCPHWDSdk2ik1qbjkNPVU0S6OH\nJmAC5VgHRwKBgFF214gmTe5Jp1EvoBiZ0I5f5qlT3XxnXvXFN5rLkGF3Uwhas1LL\neHcOPDcCdWJvJDUrrNSzrA6XZttHeevs3jAAu2JCf6KmxScBcs8RQhviJd0cUkac\nTAXrw8vWSayMsQSPyqEobpnp4Jbm58OS5ZIr9FgTxG2ALcbD9iqVmFBBAoGACTwp\nEklH8iSCXO1T2QZwkFj9iRtyQwDPslEHvob4DO92iTH+2Py7j28zwwb1XAnTdUBt\nDY/wpUH36tl3F+q384W/snc8GlTz98ixN3uSMCwRa3rK1UhJXyURoKaLQe4nDhbr\n/L63rbm7XrfwgJ4KqufwL2QaalCc2eHKgxj8KA0CgYEAwWlXFWRYQ4ZsTwYQmYOM\nDiIjRLU0SqNlamPB9biYOylLh0+qyUhQw6V8zBmpD9cApMYo923Q4nKrVaX1Kn64\novB2lE0yF0CU4etUT/XziuNsTc+WLDYyhOTgGKkgy+OymwUgfMGMUOwAY9enwOxW\nfKuYvhaC0Ng2QYsY53zVxIc=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-j6w9e@bookr-db0e3.iam.gserviceaccount.com",
  "client_id": "106428274030193475253",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-j6w9e%40bookr-db0e3.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"

})
# Initialize Firebase Admin SDK
firebase_admin.initialize_app(cred)

# Protected endpoint that requires authentication
@app.route('/protected-endpoint')
def protected_endpoint():
    # Verify Firebase ID token sent by the client
    id_token = request.headers.get('Authorization').split('Bearer ')[1]
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        # User is authenticated, proceed with protected operation
        return jsonify({'message': 'You are authenticated!'})
    except auth.InvalidIdTokenError:
        # Invalid or expired token
        return jsonify({'error': 'Invalid or expired token'}), 401
    except auth.AuthError:
        # Firebase Admin SDK error
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
