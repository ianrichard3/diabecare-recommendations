import random
from constants import BASIC_RECOMMENDATIONS


def generate_basic_recommendation(glucose_level):
    if glucose_level < 50:
        return random.choice(BASIC_RECOMMENDATIONS["very_low"])
    
    elif glucose_level >= 50 and glucose_level < 80:
        return random.choice(BASIC_RECOMMENDATIONS["low"])
    
    elif glucose_level >= 80 and glucose_level < 180:
        return random.choice(BASIC_RECOMMENDATIONS["ok"])
    
    elif glucose_level >= 180 and glucose_level < 240:
        return random.choice(BASIC_RECOMMENDATIONS["high"])
    elif glucose_level >= 240:
        return random.choice(BASIC_RECOMMENDATIONS["very_high"])
    elif glucose_level >= 450:
        return random.choice(BASIC_RECOMMENDATIONS["critical"])
    else:
        return "No hay recomendaciones disponibles."
    


  