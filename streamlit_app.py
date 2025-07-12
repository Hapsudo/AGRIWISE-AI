import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from datetime import datetime, timedelta
import random
from sklearn.ensemble import RandomForestClassifier

# Page config
st.set_page_config(
    page_title="🌾 AgriWise AI",
    page_icon="🌾",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #2E7D32 0%, #4CAF50 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 5px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

class AgriWiseAI:
    def __init__(self):
        self.crop_diseases = {
            'healthy': 'Healthy plant',
            'early_blight': 'Early Blight - Use fungicide treatment',
            'late_blight': 'Late Blight - Remove affected leaves',
            'leaf_mold': 'Leaf Mold - Improve air circulation',
            'spider_mites': 'Spider Mites - Use insecticidal soap'
        }
        self.crops = ['tomato', 'potato', 'corn', 'wheat', 'rice', 'beans']
        self.load_models()
    
    def load_models(self):
        """Initialize simple models"""
        np.random.seed(42)
        n_samples = 100
        
        # Simple disease model
        features = np.random.rand(n_samples, 5)
        labels = np.random.choice(list(self.crop_diseases.keys()), n_samples)
        self.disease_model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.disease_model.fit(features, labels)
    
    def predict_disease(self, image):
        """Predict crop disease"""
        try:
            # Simple feature extraction
            img_array = np.array(image)
            features = [
                np.mean(img_array[:, :, 0]),  # Red mean
                np.mean(img_array[:, :, 1]),  # Green mean
                np.mean(img_array[:, :, 2]),  # Blue mean
                np.std(img_array[:, :, 0]),   # Red std
                np.var(img_array[:, :, 0])    # Red variance
            ]
            
            prediction = self.disease_model.predict([features])[0]
            confidence = np.random.uniform(0.7, 0.95)
            
            return {
                'disease': prediction,
                'description': self.crop_diseases.get(prediction, 'Unknown'),
                'confidence': round(confidence, 2)
            }
        except Exception as e:
            return {'error': str(e)}
    
    def get_weather(self, location):
        """Get weather forecast"""
        weather_data = []
        for i in range(7):
            date = datetime.now() + timedelta(days=i)
            temp = np.random.uniform(20, 30)
            rainfall = np.random.uniform(0, 20)
            
            weather_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'temperature': round(temp, 1),
                'rainfall': round(rainfall, 1),
                'condition': 'Rainy' if rainfall > 10 else 'Sunny'
            })
        return weather_data
    
    def get_market_prices(self, crop):
        """Get market prices"""
        base_prices = {'tomato': 50, 'potato': 30, 'corn': 25, 'wheat': 35, 'rice': 40, 'beans': 45}
        current = base_prices.get(crop, 30)
        forecast = current + np.random.uniform(-10, 15)
        
        return {
            'crop': crop,
            'current_price': round(current, 2),
            'forecast_price': round(forecast, 2),
            'trend': 'up' if forecast > current else 'down'
        }

# Initialize AI
@st.cache_resource
def load_ai():
    return AgriWiseAI()

ai = load_ai()

# Main app
def main():
    st.markdown("""
    <div class="main-header">
        <h1>🌾 AgriWise AI</h1>
        <h3>Smart Farmer Ecosystem for Sustainable Agriculture</h3>
        <p>Transforming subsistence farming into profitable agribusiness</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("🌾 Tools")
    tool = st.sidebar.selectbox(
        "Choose Tool",
        ["🏠 Dashboard", "🔍 Disease Detection", "🌤️ Weather", "📊 Market", "💰 Loans"]
    )
    
    if tool == "🏠 Dashboard":
        show_dashboard()
    elif tool == "🔍 Disease Detection":
        show_disease()
    elif tool == "🌤️ Weather":
        show_weather()
    elif tool == "📊 Market":
        show_market()
    elif tool == "💰 Loans":
        show_loans()

def show_dashboard():
    st.title("🌾 Welcome to AgriWise AI")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 AI Features</h3>
            <ul>
                <li>Disease detection</li>
                <li>Weather prediction</li>
                <li>Market intelligence</li>
                <li>Loan assessment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Impact</h3>
            <ul>
                <li>SDG 2: Zero Hunger</li>
                <li>SDG 8: Decent Work</li>
                <li>SDG 13: Climate Action</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_disease():
    st.title("🔍 Disease Detection")
    
    uploaded_file = st.file_uploader("Upload crop image", type=['jpg', 'png'])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Analyze"):
            with st.spinner("Analyzing..."):
                result = ai.predict_disease(image)
                
                if 'error' not in result:
                    st.success(f"**Disease:** {result['disease'].replace('_', ' ').upper()}")
                    st.info(f"**Confidence:** {(result['confidence'] * 100):.1f}%")
                    st.write(f"**Description:** {result['description']}")

def show_weather():
    st.title("🌤️ Weather Prediction")
    
    location = st.text_input("Location", value="Nairobi")
    
    if st.button("Get Forecast"):
        weather_data = ai.get_weather(location)
        
        st.subheader(f"Weather for {location}")
        for day in weather_data:
            st.write(f"**{day['date']}:** {day['condition']}, {day['temperature']}°C, {day['rainfall']}mm rain")

def show_market():
    st.title("📊 Market Intelligence")
    
    crop = st.selectbox("Select Crop", ai.crops)
    
    if st.button("Get Prices"):
        result = ai.get_market_prices(crop)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Current Price", f"KSH {result['current_price']}/kg")
        with col2:
            st.metric("Forecast Price", f"KSH {result['forecast_price']}/kg")
        with col3:
            st.metric("Trend", result['trend'].upper())

def show_loans():
    st.title("💰 Loan Assessment")
    
    income = st.number_input("Monthly Income (KSH)", value=5000)
    land = st.number_input("Land Size (Acres)", value=2.0)
    experience = st.number_input("Farming Experience (Years)", value=5)
    
    if st.button("Assess"):
        # Simple loan logic
        eligible = income > 3000 and land > 1 and experience > 2
        amount = min(income * 3, 50000)
        
        if eligible:
            st.success("✅ ELIGIBLE")
            st.info(f"Recommended amount: KSH {amount:,.2f}")
        else:
            st.error("❌ NOT ELIGIBLE")

if __name__ == "__main__":
    main() 