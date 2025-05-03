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