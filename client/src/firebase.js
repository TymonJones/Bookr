// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import firebase from "firebase/compat/app";
import "firebase/compat/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCmst7pW5ChZvm2wIyO3UQVqz0XsJWBFN4",
  authDomain: "bookr-db0e3.firebaseapp.com",
  projectId: "bookr-db0e3",
  storageBucket: "bookr-db0e3.appspot.com",
  messagingSenderId: "531696080544",
  appId: "1:531696080544:web:ce4b4f7fcbcfa87a28dbc5"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export default firebase;
