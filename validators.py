from constants import USER_STATES, GLUCOSE_STATES, GLUCOSE_TRENDS

# Validate float number
def validate_float(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
   
def get_body_data(request):
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
    return data
  
  
def validate_user_state(user_state):
  if not isinstance(user_state, str):
    return False
  return user_state.lower() in USER_STATES
  
def validate_glucose_state(glucose_state):
  if not isinstance(glucose_state, str):
    return False
  return glucose_state.lower() in GLUCOSE_STATES
  
def validate_glucose_trend(glucose_trend):
  if not isinstance(glucose_trend, str):
    return False
  return glucose_trend.lower() in GLUCOSE_TRENDS
