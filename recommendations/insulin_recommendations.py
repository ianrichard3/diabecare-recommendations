def get_insulin_advice(glucose_state, trend, user_state):
    # Casos especiales donde NO se recomienda aplicar insulina antes del ejercicio
    if user_state in ["pre_workout", "working_out"]:
        if glucose_state in [
            "mild_hyperglycemia",
            "moderate_hyperglycemia",
            "severe_hyperglycemia"
        ]:
            return "Evitar corrección con insulina antes del ejercicio. Riesgo de hipoglucemia durante la actividad."
        elif glucose_state == "critical_hyperglycemia":
            return "Contraindicado hacer ejercicio con hiperglucemia crítica. Corregir primero y consultar al profesional."

    # HIPOGLUCEMIA (leve a severa)
    if glucose_state in [
        "mild_hypoglycemia",
        "moderate_hypoglycemia",
        "severe_hypoglycemia",
        "dangerous_hypoglycemia"
    ]:
        return "No aplicar insulina. Priorizar recuperación glucémica y monitorear evolución."

    # NORMOGLUCEMIA
    elif glucose_state == "normoglycemia":
        if trend in ["rising", "rapidly_rising"]:
            return "Monitorear posible hiperglucemia, aún no aplicar insulina."
        elif trend in ["falling", "rapidly_falling"]:
            return "Evitar correcciones. Riesgo de hipoglucemia si aplica insulina ahora."
        else:
            return "Seguir el plan de insulina habitual."

    # HIPERGLUCEMIA MODERADA A GRAVE (requieren corrección)
    elif glucose_state in [
        "mild_hyperglycemia",
        "moderate_hyperglycemia",
        "severe_hyperglycemia",
        "very_severe_hyperglycemia",
        "dangerous_hyperglycemia"
    ]:
        if trend in ["rising", "rapidly_rising"]:
            return "Aplicar corrección con insulina rápida según protocolo."
        elif trend == "steady":
            return "Aplicar corrección si se mantiene fuera de rango por más de 2 horas."
        elif trend in ["falling", "rapidly_falling"]:
            return "Esperar, la glucosa está descendiendo sola. Evaluar en 30-60 minutos."
        else:
            return "Seguir el protocolo de corrección si aplica."

    # HIPERGLUCEMIA CRÍTICA
    elif glucose_state == "critical_hyperglycemia":
        return "Consultar protocolo de corrección urgente con insulina rápida y contactar al profesional si persiste."

    # Catch-all
    return "Seguir el plan de insulina habitual."
