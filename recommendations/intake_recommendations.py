def get_intake_advice(glucose_state, trend, user_state):
    # Hipoglucemia (leve a peligrosa)
    if glucose_state in [
        "mild_hypoglycemia",
        "moderate_hypoglycemia",
        "severe_hypoglycemia",
        "dangerous_hypoglycemia"
    ]:
        if user_state == "pre_workout":
            return "Consumir una colación con carbohidratos rápidos antes de entrenar (jugo, banana)."
        elif user_state == "main_meal":
            return "Iniciar la comida con carbohidratos simples para recuperar niveles, luego completar con comida equilibrada."
        else:
            return "Consumir carbohidratos de absorción rápida inmediatamente (jugo, miel, caramelos)."

    # Normoglucemia
    elif glucose_state == "normoglycemia":
        if user_state == "main_meal":
            return "Comer normalmente: combinación de proteínas, carbohidratos complejos y grasas saludables."
        elif user_state == "pre_workout":
            return "Podés consumir una pequeña colación con carbohidratos si la actividad será intensa o larga."
        elif user_state == "prolonged_fasting":
            return "Iniciar ingesta progresiva con alimentos suaves y de bajo índice glucémico."
        else:
            return "Mantener ingesta habitual según tu plan."

    # Hiperglucemia moderada a crítica
    elif glucose_state in [
        "mild_hyperglycemia",
        "moderate_hyperglycemia",
        "severe_hyperglycemia",
        "very_severe_hyperglycemia",
        "dangerous_hyperglycemia"
    ]:
        if trend in ["rising", "rapidly_rising"]:
            return "Evitar carbohidratos simples. Priorizar vegetales, proteínas y grasas saludables."
        elif user_state == "main_meal":
            return "Reducir la carga glucémica total del plato. Usar porciones controladas y evitar pan, arroz, azúcar."
        elif user_state == "after_meal":
            return "No realizar ingesta adicional. Evaluar insulina o actividad para estabilizar niveles."
        else:
            return "Ingesta mínima recomendada. Evitar alimentos con alto índice glucémico."

    # Hiperglucemia crítica
    elif glucose_state == "critical_hyperglycemia":
        return "Evitar cualquier tipo de ingesta hasta estabilizar niveles. Hidratación con agua es prioritaria."

    # Casos especiales por estado del usuario
    elif user_state == "under_stress":
        return "Evitar comidas impulsivas. Optar por snacks livianos y bajos en azúcar."
    elif user_state == "post_workout":
        return "Ingerir proteínas con una porción de carbohidratos complejos para recuperación."
    elif user_state == "just_woke_up":
        return "Iniciar el día con un desayuno balanceado, priorizando carbohidratos complejos y líquidos."

    # Catch-all
    return "Mantener ingesta habitual según tu plan nutricional."
