# main project structure
# smart_health_advisor/
#   ├── main.py
#   ├── symptom_analyzer.py
#   ├── health_recommendations.py
#   ├── data/
#   │   └── symptoms_database.json
#   └── requirements.txt

# main.py
import json
from symptom_analyzer import SymptomAnalyzer
from health_recommendations import HealthRecommendationEngine

class SmartHealthAdvisor:
    def __init__(self):
        self.symptom_analyzer = SymptomAnalyzer()
        self.recommendation_engine = HealthRecommendationEngine()
    
    def run(self):
        print("Welcome to Smart Health Advisor")
        
        # Collect user symptoms
        symptoms = self._collect_symptoms()
        
        # Analyze symptoms
        symptom_analysis = self.symptom_analyzer.analyze_symptoms(symptoms)
        
        # Generate recommendations
        recommendations = self.recommendation_engine.generate_recommendations(symptom_analysis)
        
        # Display results
        self._display_results(symptom_analysis, recommendations)
    
    def _collect_symptoms(self):
        symptoms = {}
        print("\nPlease input your health parameters:")
        
        # Basic health parameters
        symptoms['temperature'] = float(input("Body Temperature (°C): "))
        symptoms['heart_rate'] = int(input("Heart Rate (bpm): "))
        symptoms['blood_pressure'] = input("Blood Pressure (e.g., 120/80): ")
        
        # Symptom checklist
        print("\nSelect your current symptoms (yes/no):")
        symptom_list = [
            'fever', 'headache', 'fatigue', 'cough', 
            'sore_throat', 'body_aches', 'shortness_of_breath'
        ]
        
        for symptom in symptom_list:
            response = input(f"{symptom.replace('_', ' ').title()}: ").lower()
            symptoms[symptom] = response == 'yes'
        
        return symptoms
    
    def _display_results(self, analysis, recommendations):
        print("\n--- Health Analysis Results ---")
        print("Symptom Analysis:")
        for key, value in analysis.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("\nRecommendations:")
        for rec in recommendations:
            print(f"- {rec}")
        
        print("\nDisclaimer: This is preliminary advice. Please consult a healthcare professional.")

# symptom_analyzer.py
class SymptomAnalyzer:
    def __init__(self):
        # Simplified symptom analysis logic
        self.risk_thresholds = {
            'temperature': {
                'normal_range': (36.5, 37.5),
                'fever_threshold': 38.0
            },
            'heart_rate': {
                'normal_range': (60, 100)
            }
        }
    
    def analyze_symptoms(self, symptoms):
        analysis = {}
        
        # Temperature analysis
        temp = symptoms.get('temperature')
        if temp:
            if temp < self.risk_thresholds['temperature']['normal_range'][0]:
                analysis['temperature_status'] = 'Low'
            elif temp > self.risk_thresholds['temperature']['fever_threshold']:
                analysis['temperature_status'] = 'Fever'
            else:
                analysis['temperature_status'] = 'Normal'
        
        # Heart rate analysis
        heart_rate = symptoms.get('heart_rate')
        if heart_rate:
            if heart_rate < self.risk_thresholds['heart_rate']['normal_range'][0]:
                analysis['heart_rate_status'] = 'Below Normal'
            elif heart_rate > self.risk_thresholds['heart_rate']['normal_range'][1]:
                analysis['heart_rate_status'] = 'Above Normal'
            else:
                analysis['heart_rate_status'] = 'Normal'
        
        # Symptom presence analysis
        symptom_count = sum(1 for sym in ['fever', 'headache', 'fatigue', 'cough', 
                                           'sore_throat', 'body_aches', 'shortness_of_breath'] 
                             if symptoms.get(sym, False))
        
        if symptom_count == 0:
            analysis['overall_symptom_severity'] = 'No Significant Symptoms'
        elif symptom_count <= 2:
            analysis['overall_symptom_severity'] = 'Mild'
        elif symptom_count <= 4:
            analysis['overall_symptom_severity'] = 'Moderate'
        else:
            analysis['overall_symptom_severity'] = 'Severe'
        
        return analysis

# health_recommendations.py
class HealthRecommendationEngine:
    def generate_recommendations(self, analysis):
        recommendations = []
        
        # Temperature-based recommendations
        if analysis.get('temperature_status') == 'Fever':
            recommendations.extend([
                "Rest and stay hydrated",
                "Take fever-reducing medication if needed",
                "Monitor temperature regularly"
            ])
        
        # Heart rate recommendations
        if analysis.get('heart_rate_status') != 'Normal':
            recommendations.append("Consult a healthcare professional about your heart rate")
        
        # Symptom severity recommendations
        severity = analysis.get('overall_symptom_severity')
        if severity == 'Moderate':
            recommendations.extend([
                "Consider seeing a healthcare provider",
                "Get plenty of rest",
                "Stay hydrated"
            ])
        elif severity == 'Severe':
            recommendations.extend([
                "Seek immediate medical attention",
                "Avoid physical exertion",
                "Rest completely"
            ])
        
        # Default recommendations
        if not recommendations:
            recommendations = [
                "You appear to be in good health",
                "Maintain your current health routine",
                "Continue regular exercise and balanced diet"
            ]
        
        return recommendations

# requirements.txt content
# No external libraries required for this basic version

if __name__ == "__main__":
    health_advisor = SmartHealthAdvisor()
    health_advisor.run()