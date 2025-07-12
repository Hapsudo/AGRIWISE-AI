from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import os
import json
import numpy as np
import pandas as pd
import cv2
from PIL import Image
import io
import base64
import requests
from datetime import datetime, timedelta
import random
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
import plotly.express as px
from plotly.utils import PlotlyJSONEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from gtts import gTTS
import speech_recognition as sr
import threading
import time

app = Flask(__name__)
CORS(app)

# Global variables for ML models
crop_disease_model = None
weather_model = None
loan_model = None
scaler = StandardScaler()

class AgriWiseAI:
    def __init__(self):
        self.crop_diseases = {
            'healthy': 'Healthy plant',
            'early_blight': 'Early Blight - Use fungicide treatment',
            'late_blight': 'Late Blight - Remove affected leaves and apply copper-based fungicide',
            'leaf_mold': 'Leaf Mold - Improve air circulation and reduce humidity',
            'septoria_leaf_spot': 'Septoria Leaf Spot - Remove infected leaves and apply fungicide',
            'spider_mites': 'Spider Mites - Use insecticidal soap or neem oil',
            'target_spot': 'Target Spot - Apply fungicide and improve plant spacing',
            'yellow_leaf_curl_virus': 'Yellow Leaf Curl Virus - Remove infected plants and control whiteflies',
            'mosaic_virus': 'Mosaic Virus - Remove infected plants and control aphids'
        }
        
        self.crops = ['tomato', 'potato', 'corn', 'wheat', 'rice', 'beans']
        self.weather_data = {}
        self.market_prices = {}
        
    def load_models(self):
        """Load pre-trained ML models"""
        try:
            # Initialize models (in production, these would be pre-trained)
            self.crop_disease_model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.weather_model = RandomForestClassifier(n_estimators=50, random_state=42)
            self.loan_model = RandomForestClassifier(n_estimators=75, random_state=42)
            
            # Generate sample training data and fit models
            self._train_sample_models()
            
        except Exception as e:
            print(f"Error loading models: {e}")
    
    def _train_sample_models(self):
        """Train sample models with synthetic data"""
        # Sample crop disease data
        np.random.seed(42)
        n_samples = 1000
        
        # Generate synthetic image features (RGB values, texture features, etc.)
        image_features = np.random.rand(n_samples, 10)
        disease_labels = np.random.choice(list(self.crop_diseases.keys()), n_samples)
        
        self.crop_disease_model.fit(image_features, disease_labels)
        
        # Sample weather data
        weather_features = np.random.rand(n_samples, 5)  # temp, humidity, pressure, wind, rainfall
        weather_labels = np.random.choice(['sunny', 'rainy', 'cloudy', 'stormy'], n_samples)
        
        self.weather_model.fit(weather_features, weather_labels)
        
        # Sample loan data
        loan_features = np.random.rand(n_samples, 6)  # income, land_size, crop_yield, credit_score, age, experience
        loan_labels = np.random.choice([0, 1], n_samples)  # 0: rejected, 1: approved
        
        self.loan_model.fit(loan_features, loan_labels)
    
    def predict_crop_disease(self, image_data):
        """Predict crop disease from image"""
        try:
            # Convert base64 image to numpy array
            image_bytes = base64.b64decode(image_data.split(',')[1])
            image = Image.open(io.BytesIO(image_bytes))
            image = image.resize((224, 224))
            
            # Extract features (simplified - in production, use CNN features)
            image_array = np.array(image)
            features = self._extract_image_features(image_array)
            
            # Predict disease
            prediction = self.crop_disease_model.predict([features])[0]
            confidence = np.random.uniform(0.7, 0.95)  # Simulated confidence
            
            return {
                'disease': prediction,
                'description': self.crop_diseases.get(prediction, 'Unknown disease'),
                'confidence': round(confidence, 2),
                'recommendations': self._get_treatment_recommendations(prediction)
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _extract_image_features(self, image_array):
        """Extract features from image array"""
        # Simplified feature extraction
        features = []
        
        # Color features
        features.extend([
            np.mean(image_array[:, :, 0]),  # Red channel mean
            np.mean(image_array[:, :, 1]),  # Green channel mean
            np.mean(image_array[:, :, 2]),  # Blue channel mean
            np.std(image_array[:, :, 0]),   # Red channel std
            np.std(image_array[:, :, 1]),   # Green channel std
            np.std(image_array[:, :, 2]),   # Blue channel std
        ])
        
        # Texture features (simplified)
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        features.extend([
            np.mean(gray),
            np.std(gray),
            np.var(gray),
            np.max(gray)
        ])
        
        return features
    
    def _get_treatment_recommendations(self, disease):
        """Get treatment recommendations for detected disease"""
        recommendations = {
            'healthy': ['Continue current care routine', 'Monitor for any changes'],
            'early_blight': ['Apply copper-based fungicide', 'Remove affected leaves', 'Improve air circulation'],
            'late_blight': ['Apply fungicide immediately', 'Remove all affected parts', 'Avoid overhead watering'],
            'leaf_mold': ['Reduce humidity', 'Improve ventilation', 'Apply fungicide if severe'],
            'septoria_leaf_spot': ['Remove infected leaves', 'Apply fungicide', 'Avoid overhead watering'],
            'spider_mites': ['Apply insecticidal soap', 'Use neem oil', 'Increase humidity'],
            'target_spot': ['Apply fungicide', 'Improve plant spacing', 'Remove affected leaves'],
            'yellow_leaf_curl_virus': ['Remove infected plants', 'Control whiteflies', 'Use resistant varieties'],
            'mosaic_virus': ['Remove infected plants', 'Control aphids', 'Disinfect tools']
        }
        return recommendations.get(disease, ['Consult local agricultural expert'])
    
    def predict_weather(self, location):
        """Predict weather for the next 7 days"""
        try:
            # Simulate weather prediction (in production, use real weather API)
            weather_data = []
            base_temp = np.random.uniform(20, 30)
            base_humidity = np.random.uniform(40, 80)
            
            for i in range(7):
                date = datetime.now() + timedelta(days=i)
                temp = base_temp + np.random.uniform(-5, 5)
                humidity = base_humidity + np.random.uniform(-10, 10)
                rainfall = np.random.uniform(0, 20)
                wind_speed = np.random.uniform(0, 15)
                
                weather_data.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'temperature': round(temp, 1),
                    'humidity': round(humidity, 1),
                    'rainfall': round(rainfall, 1),
                    'wind_speed': round(wind_speed, 1),
                    'condition': self._get_weather_condition(temp, humidity, rainfall)
                })
            
            return weather_data
        except Exception as e:
            return {'error': str(e)}
    
    def _get_weather_condition(self, temp, humidity, rainfall):
        """Determine weather condition based on parameters"""
        if rainfall > 10:
            return 'Rainy'
        elif temp > 25 and humidity < 50:
            return 'Sunny'
        elif humidity > 70:
            return 'Cloudy'
        else:
            return 'Partly Cloudy'
    
    def get_market_prices(self, crop_type):
        """Get current market prices and forecasts"""
        try:
            # Simulate market data (in production, use real market APIs)
            base_price = {
                'tomato': 50,
                'potato': 30,
                'corn': 25,
                'wheat': 35,
                'rice': 40,
                'beans': 45
            }
            
            current_price = base_price.get(crop_type, 30)
            price_variation = np.random.uniform(-10, 15)
            forecast_price = current_price + price_variation
            
            return {
                'crop': crop_type,
                'current_price': round(current_price, 2),
                'forecast_price': round(forecast_price, 2),
                'trend': 'up' if forecast_price > current_price else 'down',
                'confidence': round(np.random.uniform(0.6, 0.9), 2),
                'recommendation': self._get_market_recommendation(current_price, forecast_price)
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _get_market_recommendation(self, current, forecast):
        """Get market recommendations based on price trends"""
        if forecast > current * 1.1:
            return "Consider holding harvest for better prices"
        elif forecast < current * 0.9:
            return "Consider selling soon to avoid price drops"
        else:
            return "Prices are stable, plan harvest based on crop readiness"
    
    def assess_loan_eligibility(self, farmer_data):
        """Assess micro-loan eligibility"""
        try:
            # Extract features from farmer data
            features = [
                farmer_data.get('monthly_income', 0),
                farmer_data.get('land_size', 0),
                farmer_data.get('crop_yield', 0),
                farmer_data.get('credit_score', 500),
                farmer_data.get('age', 35),
                farmer_data.get('farming_experience', 5)
            ]
            
            # Predict loan eligibility
            prediction = self.loan_model.predict([features])[0]
            probability = self.loan_model.predict_proba([features])[0]
            
            return {
                'eligible': bool(prediction),
                'probability': round(max(probability), 2),
                'recommended_amount': self._calculate_loan_amount(features),
                'risk_level': self._assess_risk_level(features),
                'conditions': self._get_loan_conditions(features)
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _calculate_loan_amount(self, features):
        """Calculate recommended loan amount"""
        income, land_size, crop_yield, credit_score, age, experience = features
        base_amount = income * 3  # 3 months income
        
        # Adjustments
        if credit_score > 700:
            base_amount *= 1.2
        if experience > 10:
            base_amount *= 1.1
        if land_size > 5:
            base_amount *= 1.15
            
        return round(min(base_amount, 50000), 2)  # Cap at 50,000
    
    def _assess_risk_level(self, features):
        """Assess risk level for loan"""
        income, land_size, crop_yield, credit_score, age, experience = features
        
        risk_score = 0
        if credit_score < 600:
            risk_score += 2
        if income < 1000:
            risk_score += 1
        if experience < 3:
            risk_score += 1
            
        if risk_score <= 1:
            return 'Low'
        elif risk_score <= 3:
            return 'Medium'
        else:
            return 'High'
    
    def _get_loan_conditions(self, features):
        """Get loan conditions based on risk assessment"""
        risk_level = self._assess_risk_level(features)
        
        conditions = {
            'Low': ['Standard interest rate', 'Flexible repayment terms'],
            'Medium': ['Slightly higher interest rate', 'Collateral required'],
            'High': ['Higher interest rate', 'Guarantor required', 'Shorter repayment period']
        }
        
        return conditions.get(risk_level, ['Contact loan officer for details'])

# Initialize AgriWise AI
ai_system = AgriWiseAI()
ai_system.load_models()

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/disease-detection', methods=['POST'])
def detect_disease():
    """API endpoint for crop disease detection"""
    try:
        data = request.get_json()
        image_data = data.get('image')
        
        if not image_data:
            return jsonify({'error': 'No image data provided'}), 400
        
        result = ai_system.predict_crop_disease(image_data)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/weather-prediction', methods=['POST'])
def predict_weather_api():
    """API endpoint for weather prediction"""
    try:
        data = request.get_json()
        location = data.get('location', 'Nairobi')
        
        result = ai_system.predict_weather(location)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/market-prices', methods=['POST'])
def get_market_prices_api():
    """API endpoint for market prices"""
    try:
        data = request.get_json()
        crop_type = data.get('crop_type', 'tomato')
        
        result = ai_system.get_market_prices(crop_type)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/loan-assessment', methods=['POST'])
def assess_loan():
    """API endpoint for loan assessment"""
    try:
        data = request.get_json()
        
        result = ai_system.assess_loan_eligibility(data)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/voice-to-text', methods=['POST'])
def voice_to_text():
    """API endpoint for voice-to-text conversion"""
    try:
        # This would integrate with speech recognition
        # For now, return a sample response
        return jsonify({
            'text': 'Sample voice input converted to text',
            'language': 'Swahili',
            'confidence': 0.85
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    """API endpoint for text-to-speech conversion"""
    try:
        data = request.get_json()
        text = data.get('text', 'Hello from AgriWise AI')
        language = data.get('language', 'en')
        
        # Generate speech (simplified)
        tts = gTTS(text=text, lang=language, slow=False)
        
        # Save to temporary file
        audio_path = f"static/temp_audio_{int(time.time())}.mp3"
        tts.save(audio_path)
        
        return jsonify({
            'audio_url': audio_path,
            'success': True
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create static directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000) 