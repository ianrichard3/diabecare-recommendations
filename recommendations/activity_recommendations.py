def get_activity_advice(glucose_state, trend, user_state):
    # Si ya está en actividad física, y hay una complicación
    if user_state == "working_out":
        if glucose_state in ["dangerous_hypoglycemia", "severe_hypoglycemia"]:
            return "Detener el ejercicio inmediatamente. Recuperar glucosa y monitorear."
        elif trend == "rapidly_falling":
            return "Reducir intensidad y monitorear frecuentemente. Considerar ingerir carbohidratos."
        elif glucose_state == "critical_hyperglycemia":
            return "Suspender la actividad. Riesgo elevado de cetoacidosis."

    # Pre-entrenamiento
    if user_state == "pre_workout":
        if glucose_state in ["mild_hypoglycemia", "moderate_hypoglycemia"]:
            return "Ingerir una colación antes del ejercicio para prevenir bajones."
        elif glucose_state == "dangerous_hypoglycemia":
            return "Contraindicado iniciar ejercicio. Corregir glucosa primero."
        elif glucose_state == "critical_hyperglycemia":
            return "Evitar ejercicio. Corregir niveles antes de cualquier actividad física."
        elif trend in ["falling", "rapidly_falling"]:
            return "Precaución: tendencia a la baja. Ingerir algo antes de entrenar."

    # Post-entrenamiento
    if user_state == "post_workout":
        if glucose_state == "normoglycemia":
            return "Buen momento para recuperación. Actividad finalizada correctamente."
        elif trend == "rapidly_falling":
            return "Monitorear después del ejercicio. Riesgo de hipoglucemia tardía."

    # Hipoglucemia en general
    if glucose_state in [
        "mild_hypoglycemia",
        "moderate_hypoglycemia",
        "severe_hypoglycemia",
        "dangerous_hypoglycemia"
    ]:
        return "Evitar cualquier actividad física hasta recuperar niveles normales."

    # Hiperglucemia crítica
    if glucose_state == "critical_hyperglycemia":
        return "Evitar ejercicio. Riesgo elevado de cetoacidosis. Corregir primero."

    # Hiperglucemia moderada
    if glucose_state in [
        "mild_hyperglycemia",
        "moderate_hyperglycemia",
        "severe_hyperglycemia",
        "very_severe_hyperglycemia"
    ]:
        if trend == "rising":
            return "Evitar ejercicio hasta estabilizar niveles. Requiere monitoreo."
        elif trend == "steady":
            return "Actividad leve puede ayudar, como caminar post comida."
        elif trend in ["falling", "rapidly_falling"]:
            return "Puede iniciar actividad leve, pero monitorear por posible bajón."

    # Normoglucemia
    if glucose_state == "normoglycemia":
        return "Actividad física permitida según rutina. Monitorear si es prolongada."

    # Por defecto
    return "Evaluar actividad física en función de tu rutina y niveles. Monitoreo recomendado."
