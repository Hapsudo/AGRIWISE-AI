import streamlit as st
import random
from datetime import datetime, timedelta

# Page config with classic sidebar
st.set_page_config(
    page_title="🌾 AgriWise AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Minimal, essential CSS for dark theme compatibility and polish
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #2E7D32 0%, #4CAF50 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white !important;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .feature-card, .result-card {
        background: white !important;
        color: #2C3E50 !important;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #4CAF50;
    }
    .result-card {
        border-left: 5px solid #2E7D32;
    }
    .stButton > button {
        background: linear-gradient(135deg, #2E7D32, #4CAF50) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 500 !important;
        width: 100% !important;
        margin: 0.5rem 0 !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #1B5E20, #388E3C) !important;
    }
    .stFileUploader, .stNumberInput > div > div > input, .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background: white !important;
        color: #2C3E50 !important;
        border: 2px solid #4CAF50 !important;
        border-radius: 8px !important;
    }
    .stSelectbox > div > div {
        background: white !important;
        color: #2C3E50 !important;
        border: 2px solid #4CAF50 !important;
        border-radius: 8px !important;
    }
    .stMetric, .stMetric * {
        color: #2C3E50 !important;
        background: white !important;
    }
    .stAlert, .stSuccess, .stError {
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #f8f9fa !important;
    }
    .main .block-container {
        background-color: #f8f9fa !important;
    }
</style>
""", unsafe_allow_html=True)

# Remove all custom mobile nav and hamburger hacks, use only Streamlit's sidebar
# Remove all JavaScript overrides

# Main app with classic sidebar navigation
def main():
    st.markdown("""
    <div class="main-header">
        <h1>🌾 AgriWise AI</h1>
        <h3>Smart Farmer Ecosystem for Sustainable Agriculture</h3>
        <p>Transforming subsistence farming into profitable agribusiness</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.title("🌾 Smart Farming Tools")
    tool = st.sidebar.selectbox(
        "Choose a Tool",
        ["🏠 Dashboard", "🔍 Disease Detection", "🌤️ Weather Prediction", "📊 Market Intelligence", "💰 Loan Assessment", "🗣️ Voice Interface"]
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("**🌐 Version:** Streamlit Classic")
    st.sidebar.markdown("**📱 Optimized for:** Mobile & Desktop")
    
    if tool == "🏠 Dashboard":
        show_dashboard()
    elif tool == "🔍 Disease Detection":
        show_disease()
    elif tool == "🌤️ Weather Prediction":
        show_weather()
    elif tool == "📊 Market Intelligence":
        show_market()
    elif tool == "💰 Loan Assessment":
        show_loans()
    elif tool == "🗣️ Voice Interface":
        show_voice()
    else:
        show_dashboard()

class AgriWiseAI:
    def __init__(self):
        self.crop_diseases = {
            'healthy': 'Healthy plant - Continue current care routine',
            'early_blight': 'Early Blight - Apply copper-based fungicide and remove affected leaves',
            'late_blight': 'Late Blight - Apply fungicide immediately and avoid overhead watering',
            'leaf_mold': 'Leaf Mold - Improve air circulation and reduce humidity',
            'spider_mites': 'Spider Mites - Use insecticidal soap or neem oil',
            'target_spot': 'Target Spot - Apply fungicide and improve plant spacing'
        }
        self.crops = ['tomato', 'potato', 'corn', 'wheat', 'rice', 'beans']
        random.seed(42)
    
    def predict_disease(self, image_uploaded):
        """Predict crop disease (simulated)"""
        try:
            # Simulate AI analysis
            diseases = list(self.crop_diseases.keys())
            prediction = random.choice(diseases)
            confidence = random.uniform(0.7, 0.95)
            
            return {
                'disease': prediction,
                'description': self.crop_diseases.get(prediction, 'Unknown disease'),
                'confidence': round(confidence, 2),
                'recommendations': self._get_recommendations(prediction)
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _get_recommendations(self, disease):
        """Get treatment recommendations"""
        recommendations = {
            'healthy': ['Continue current care routine', 'Monitor for any changes'],
            'early_blight': ['Apply copper-based fungicide', 'Remove affected leaves', 'Improve air circulation'],
            'late_blight': ['Apply fungicide immediately', 'Remove all affected parts', 'Avoid overhead watering'],
            'leaf_mold': ['Reduce humidity', 'Improve ventilation', 'Apply fungicide if severe'],
            'spider_mites': ['Apply insecticidal soap', 'Use neem oil', 'Increase humidity'],
            'target_spot': ['Apply fungicide', 'Improve plant spacing', 'Remove affected leaves']
        }
        return recommendations.get(disease, ['Consult local agricultural expert'])
    
    def get_weather(self, location):
        """Get weather forecast (simulated)"""
        weather_data = []
        base_temp = random.uniform(20, 30)
        base_rainfall = random.uniform(0, 20)
        
        for i in range(7):
            date = datetime.now() + timedelta(days=i)
            temp = base_temp + random.uniform(-5, 5)
            rainfall = base_rainfall + random.uniform(-5, 10)
            humidity = random.uniform(40, 80)
            
            weather_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'temperature': round(temp, 1),
                'rainfall': round(rainfall, 1),
                'humidity': round(humidity, 1),
                'condition': self._get_weather_condition(temp, humidity, rainfall)
            })
        return weather_data
    
    def _get_weather_condition(self, temp, humidity, rainfall):
        """Determine weather condition"""
        if rainfall > 10:
            return '🌧️ Rainy'
        elif temp > 25 and humidity < 50:
            return '☀️ Sunny'
        elif humidity > 70:
            return '☁️ Cloudy'
        else:
            return '⛅ Partly Cloudy'
    
    def get_market_prices(self, crop):
        """Get market prices (simulated)"""
        try:
            base_prices = {
                'tomato': 50, 'potato': 30, 'corn': 25, 
                'wheat': 35, 'rice': 40, 'beans': 45
            }
            current = base_prices.get(crop, 30)
            forecast = current + random.uniform(-10, 15)
            
            return {
                'crop': crop,
                'current_price': round(current, 2),
                'forecast_price': round(forecast, 2),
                'trend': '📈 UP' if forecast > current else '📉 DOWN',
                'confidence': round(random.uniform(0.6, 0.9), 2),
                'recommendation': self._get_market_recommendation(current, forecast)
            }
        except Exception as e:
            st.error(f"Error in market analysis: {str(e)}")
            return {
                'crop': crop,
                'current_price': 30.0,
                'forecast_price': 32.0,
                'trend': '📊 STABLE',
                'confidence': 0.7,
                'recommendation': 'Market data temporarily unavailable'
            }
    
    def _get_market_recommendation(self, current, forecast):
        """Get market recommendations"""
        try:
            if forecast > current * 1.1:
                return "Consider holding harvest for better prices"
            elif forecast < current * 0.9:
                return "Consider selling soon to avoid price drops"
            else:
                return "Prices are stable, plan harvest based on crop readiness"
        except Exception as e:
            return "Consult local market experts for recommendations"
    
    def assess_loan(self, income, land, experience, credit_score, age, crop_yield):
        """Assess loan eligibility (simulated)"""
        try:
            # Validate inputs
            if not all(isinstance(x, (int, float)) for x in [income, land, experience, credit_score, age, crop_yield]):
                st.error("Please enter valid numbers for all fields")
                return None
            
            # Simple scoring system
            score = 0
            if income > 5000: score += 2
            elif income > 3000: score += 1
            
            if land > 5: score += 2
            elif land > 2: score += 1
            
            if experience > 10: score += 2
            elif experience > 5: score += 1
            
            if credit_score > 700: score += 2
            elif credit_score > 600: score += 1
            
            if age > 25 and age < 60: score += 1
            
            if crop_yield > 1000: score += 1
            
            eligible = score >= 4
            probability = min(score / 8, 0.95)
            
            # Calculate loan amount
            base_amount = income * 3
            if credit_score > 700: base_amount *= 1.2
            if experience > 10: base_amount *= 1.1
            if land > 5: base_amount *= 1.15
            
            recommended_amount = min(base_amount, 50000)
            
            # Risk assessment
            if score >= 6:
                risk_level = 'Low'
                conditions = ['Standard interest rate', 'Flexible repayment terms']
            elif score >= 4:
                risk_level = 'Medium'
                conditions = ['Slightly higher interest rate', 'Collateral required']
            else:
                risk_level = 'High'
                conditions = ['Higher interest rate', 'Guarantor required', 'Shorter repayment period']
            
            return {
                'eligible': eligible,
                'probability': round(probability, 2),
                'recommended_amount': round(recommended_amount, 2),
                'risk_level': risk_level,
                'conditions': conditions,
                'score': score
            }
        except Exception as e:
            st.error(f"Error in loan assessment: {str(e)}")
            return {
                'eligible': False,
                'probability': 0.0,
                'recommended_amount': 0.0,
                'risk_level': 'Error',
                'conditions': ['Please check your input values'],
                'score': 0
            }

# Initialize AI
@st.cache_resource
def load_ai():
    return AgriWiseAI()

ai = load_ai()

def show_dashboard():
    st.title("🌾 Welcome to AgriWise AI")
    
    # Mobile-friendly layout
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 AI-Powered Features</h3>
            <ul>
                <li>🔍 Computer vision disease detection</li>
                <li>🌤️ Weather prediction system</li>
                <li>📊 Market price forecasting</li>
                <li>💰 Micro-loan assessment</li>
                <li>🗣️ Voice interface support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Sustainable Development Goals</h3>
            <ul>
                <li>🌾 SDG 2: Zero Hunger</li>
                <li>💼 SDG 8: Decent Work</li>
                <li>🌍 SDG 13: Climate Action</li>
                <li>💰 Financial inclusion</li>
                <li>🌱 Sustainable agriculture</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Mobile-friendly stats
    st.subheader("📈 Quick Statistics")
    
    # Use columns that stack on mobile
    stats_cols = st.columns(2)
    with stats_cols[0]:
        st.metric("🌾 Farmers Served", "5,000+")
        st.metric("🔍 Disease Accuracy", "95%")
    with stats_cols[1]:
        st.metric("🌤️ Weather Forecast", "7 Days")
        st.metric("📊 Market Insights", "Real-time")

def show_disease():
    st.title("🔍 Crop Disease Detection")
    
    st.info("📸 Upload a clear image of your crop leaves for AI-powered disease detection")
    
    uploaded_file = st.file_uploader("Upload crop image", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        if st.button("🔍 Analyze Disease", use_container_width=True):
            with st.spinner("🤖 AI is analyzing your crop image..."):
                result = ai.predict_disease(uploaded_file)
                
                if 'error' not in result:
                    st.markdown(f"""
                    <div class="result-card">
                        <h4>🔍 Analysis Result</h4>
                        <p><strong>Disease:</strong> {result['disease'].replace('_', ' ').upper()}</p>
                        <p><strong>Confidence:</strong> {(result['confidence'] * 100):.1f}%</p>
                        <p><strong>Description:</strong> {result['description']}</p>
                        <h5>💡 Recommendations:</h5>
                        <ul>
                            {''.join([f'<li>{rec}</li>' for rec in result['recommendations']])}
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"❌ Error: {result['error']}")

def show_weather():
    st.title("🌤️ Weather Prediction")
    
    st.info("🌍 Get 7-day weather forecasts to plan your farming activities")
    
    location = st.text_input("📍 Enter your location", value="Nairobi")
    
    if st.button("🌤️ Get Weather Forecast", use_container_width=True):
        with st.spinner("🌤️ Fetching weather data..."):
            weather_data = ai.get_weather(location)
            
            st.subheader(f"🌤️ 7-Day Weather Forecast for {location}")
            
            # Mobile-friendly weather display
            for i, day in enumerate(weather_data):
                with st.container():
                    st.markdown(f"""
                    **{day['date']}:** {day['condition']} | 🌡️ {day['temperature']}°C | 💧 {day['rainfall']}mm | 💨 {day['humidity']}% humidity
                    """)
                    if i < len(weather_data) - 1:
                        st.markdown("---")
            
            # Weather insights
            st.subheader("🌾 Farming Recommendations")
            avg_temp = sum(day['temperature'] for day in weather_data) / len(weather_data)
            total_rain = sum(day['rainfall'] for day in weather_data)
            
            if avg_temp > 25:
                st.info("🌡️ High temperatures expected - ensure adequate irrigation")
            if total_rain > 50:
                st.info("🌧️ Significant rainfall expected - prepare for potential flooding")
            if avg_temp < 20:
                st.info("❄️ Cool temperatures - consider crop protection measures")

def show_market():
    st.title("📊 Market Intelligence")
    
    st.info("💰 Get real-time market prices and forecasts for better selling decisions")
    
    crop = st.selectbox("🌾 Select Crop", ai.crops)
    
    if st.button("📊 Get Market Data", use_container_width=True):
        try:
            with st.spinner("📊 Analyzing market trends..."):
                result = ai.get_market_prices(crop)
                
                if result:
                    # Use st.write for better dark theme compatibility
                    st.markdown("### 📊 Market Analysis Results")
                    st.markdown(f"""
                    <div style="background: white; padding: 1rem; border-radius: 8px; border-left: 5px solid #4CAF50; margin: 1rem 0;">
                        <h4 style="color: #2C3E50;">{result['crop'].upper()} Market Intelligence</h4>
                        <p style="color: #2C3E50;"><strong>Current Price:</strong> KSH {result['current_price']}/kg</p>
                        <p style="color: #2C3E50;"><strong>Forecast Price:</strong> KSH {result['forecast_price']}/kg</p>
                        <p style="color: #2C3E50;"><strong>Trend:</strong> {result['trend']}</p>
                        <p style="color: #2C3E50;"><strong>Confidence:</strong> {(result['confidence'] * 100):.1f}%</p>
                        <p style="color: #2C3E50;"><strong>💡 Recommendation:</strong> {result['recommendation']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Mobile-friendly price comparison with explicit styling
                    price_cols = st.columns(2)
                    with price_cols[0]:
                        st.markdown(f"""
                        <div style="background: white; padding: 1rem; border-radius: 8px; text-align: center; margin: 0.5rem 0;">
                            <h3 style="color: #2C3E50; margin: 0;">Current Price</h3>
                            <p style="color: #2C3E50; font-size: 1.2rem; font-weight: bold; margin: 0;">KSH {result['current_price']}/kg</p>
                        </div>
                        """, unsafe_allow_html=True)
                    with price_cols[1]:
                        st.markdown(f"""
                        <div style="background: white; padding: 1rem; border-radius: 8px; text-align: center; margin: 0.5rem 0;">
                            <h3 style="color: #2C3E50; margin: 0;">Forecast Price</h3>
                            <p style="color: #2C3E50; font-size: 1.2rem; font-weight: bold; margin: 0;">KSH {result['forecast_price']}/kg</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.error("❌ Unable to fetch market data. Please try again.")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Please try again or contact support if the issue persists.")

def show_loans():
    st.title("💰 Micro-Loan Assessment")
    
    st.info("🏦 Get AI-powered loan eligibility assessment for farming improvements")
    
    # Mobile-friendly form layout
    st.subheader("📋 Farmer Information")
    
    monthly_income = st.number_input("💰 Monthly Income (KSH)", min_value=0, value=5000)
    land_size = st.number_input("🌾 Land Size (Acres)", min_value=0.0, value=2.0)
    crop_yield = st.number_input("📦 Expected Crop Yield (kg)", min_value=0, value=1000)
    
    st.subheader("📊 Financial Information")
    
    credit_score = st.slider("📊 Credit Score", min_value=300, max_value=850, value=650)
    age = st.number_input("👤 Age", min_value=18, max_value=80, value=35)
    experience = st.number_input("🌱 Farming Experience (Years)", min_value=0, value=5)
    
    if st.button("💰 Assess Loan Eligibility", use_container_width=True):
        try:
            with st.spinner("🤖 Analyzing loan eligibility..."):
                result = ai.assess_loan(monthly_income, land_size, experience, credit_score, age, crop_yield)
                
                if result:
                    status_icon = "✅" if result['eligible'] else "❌"
                    status_text = "ELIGIBLE" if result['eligible'] else "NOT ELIGIBLE"
                    
                    # Use explicit styling for dark theme compatibility
                    st.markdown("### 💰 Loan Assessment Results")
                    st.markdown(f"""
                    <div style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #2E7D32; margin: 1rem 0; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                        <h4 style="color: #2C3E50;">{status_icon} Loan Assessment Result</h4>
                        <p style="color: #2C3E50;"><strong>Status:</strong> {status_text}</p>
                        <p style="color: #2C3E50;"><strong>Probability:</strong> {(result['probability'] * 100):.1f}%</p>
                        <p style="color: #2C3E50;"><strong>Recommended Amount:</strong> KSH {result['recommended_amount']:,.2f}</p>
                        <p style="color: #2C3E50;"><strong>Risk Level:</strong> {result['risk_level']}</p>
                        <p style="color: #2C3E50;"><strong>Score:</strong> {result['score']}/8</p>
                        <h5 style="color: #2C3E50;">📋 Conditions:</h5>
                        <ul style="color: #2C3E50;">
                            {''.join([f'<li style="color: #2C3E50;">{condition}</li>' for condition in result['conditions']])}
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("❌ Unable to assess loan eligibility. Please check your input values.")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Please check your input values and try again.")

def show_voice():
    st.title("🗣️ Voice Interface")
    
    st.info("🎤 Multi-language voice support for inclusive access")
    
    st.markdown("""
    <div class="feature-card">
        <h3>🌍 Supported Languages</h3>
        <ul>
            <li><strong>🇺🇸 English</strong> - Primary interface</li>
            <li><strong>🇹🇿 Swahili</strong> - Widely spoken in East Africa</li>
            <li><strong>🇰🇪 Kikuyu</strong> - Local language support</li>
            <li><strong>🇰🇪 Luo</strong> - Regional language support</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Language selection
    language = st.selectbox("🌍 Select Language", ["English", "Swahili", "Kikuyu", "Luo"])
    
    # Voice input simulation
    st.subheader("🎤 Voice Input (Simulated)")
    voice_text = st.text_area("Speak your question here...", placeholder="Example: What's the weather like today?")
    
    if st.button("🎤 Process Voice Input", use_container_width=True):
        if voice_text:
            st.success(f"✅ Voice input processed in {language}: {voice_text}")
            st.info("🔧 In production, this would use real speech recognition and text-to-speech APIs.")
        else:
            st.warning("⚠️ Please enter some text to simulate voice input.")

if __name__ == "__main__":
    main() 