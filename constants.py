USER_STATES = [
    "just_woke_up",
    "main_meal",
    "after_meal",
    "pre_workout",
    "working_out",
    "post_workout",
    "studying",
    "working",
    "under_stress",
    "resting",
    "pre_sleep",
    "sleeping",
    "prolonged_fasting"
]

GLUCOSE_STATES = [
  "normoglycemia",
  "mild_hypoglycemia",       # misma recomendacion
  "moderate_hypoglycemia",   # misma recomendacion
  "severe_hypoglycemia",     # misma recomendacion
  "dangerous_hypoglycemia",
  "mild_hyperglycemia",             # metete insulina
  "moderate_hyperglycemia",         # metete insulina
  "severe_hyperglycemia",           # metete insulina
  "very_severe_hyperglycemia",      # metete insulina
  "dangerous_hyperglycemia",        # metete insulina
  "critical_hyperglycemia"
]

GLUCOSE_TRENDS = [
    "rapidly_falling", 
    "falling",          
    "steady",           
    "rising",           
    "rapidly_rising"   
]