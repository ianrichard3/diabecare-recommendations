import random
from constants import BASIC_RECOMMENDATIONS


def generate_basic_recommendation(glucose_level):
    if glucose_level < 70:
        return random.choice(BASIC_RECOMMENDATIONS["low"])
    elif 70 <= glucose_level <= 140:
        return random.choice(BASIC_RECOMMENDATIONS["ok"])
    elif 141 <= glucose_level <= 250:
        return random.choice(BASIC_RECOMMENDATIONS["high"])
    else:  # glucose_level > 250
        return random.choice(BASIC_RECOMMENDATIONS["very_high"])


  