from .activity_recommendations import get_activity_advice
from .intake_recommendations import get_intake_advice
from .insulin_recommendations import get_insulin_advice



def generate_full_recommendation(user_state, glucose_state, glucose_trend):
    return {
        "intake": get_intake_advice(glucose_state, glucose_trend, user_state),
        "insulin": get_insulin_advice(glucose_state, glucose_trend, user_state),
        "activity": get_activity_advice(glucose_state, glucose_trend, user_state)
    }