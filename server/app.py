from flask import Flask, request, jsonify
from firebase_admin import credentials, auth, firestore
from firebase_admin import initialize_app
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

private_key = os.getenv("FIREBASE_PRIVATE_KEY")

# Initialize Firebase Admin SDK
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": private_key,
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-j6w9e%40bookr-db0e3.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})
initialize_app(cred)


# Initialize Firestore client
db = firestore.client()

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

# Create a new user
@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.json
    uid = data['uid']
    email = data['email']
    display_name = data['display_name']
    
    user_ref = db.collection('Users').document(uid)
    user_ref.set({
        'email': email,
        'display_name': display_name
    })

    return jsonify({'message': 'User created successfully'})

if __name__ == '__main__':
    app.run(debug=True)
