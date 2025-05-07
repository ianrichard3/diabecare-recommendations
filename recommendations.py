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


# ========================================================================    
# ========================================================================    
# ========================================================================    
# ========================================================================    



# ========================================================================
# ========================================================================
# Multi criteria recommendation
# ========================================================================
# ========================================================================

from datetime import datetime, timedelta
from constants import SCHEDULE



def generate_breakfast_recommendation(glucose_level):
    recommendations = {}
    # if it's morning
        
    if glucose_level < 70:
        # LOW
        recommendations["intake"] = "Consumir una fuente mínima de carbohidratos (jugo de frutas, miel) seguida de una fuente de carbohidratos complejos (pan integral, avena)."
        recommendations["insulin"] = "Ajustar la dosis de insulina para evitar hipoglucemia posterior al desayuno (no inyectar si no es necesario, depende de cuánto se ingiera)."
        recommendations["activity"] = "No hacer ejercicio."

    elif 70 <= glucose_level <= 140:
        # OK
        recommendations["intake"] = "Mantener un desayuno balanceado con proteínas, grasas saludables y carbohidratos complejos."
        recommendations["insulin"] = "Recordar ajustar la dosis de insulina según el plan de tratamiento y el contenido del desayuno."
        recommendations["activity"] = "No hacer ejercicio inmediatamente después."

    elif 141 <= glucose_level <= 250:
        # HIGH
        recommendations["intake"] = "Evitar carbohidratos de absorción rápida y priorizar alimentos con baja carga glucémica."
        recommendations["insulin"] = "Sugerir una caminata breve post desayuno para ayudar a reducir los niveles de glucosa."
        recommendations["activity"] = "Postergar ejercicio intenso."

    else:  # glucose_level > 250
        # VERY HIGH
        recommendations["intake"] = "Limitar al máximo los carbohidratos y priorizar líquidos sin azúcar."
        recommendations["insulin"] = "Consultar al profesional y aplicar corrección si está indicado antes de ingerir alimentos."
        recommendations["activity"] = "Evitar cualquier ejercicio, riesgo elevado de cetoacidosis."

    return recommendations




def generate_prev_exercise_recommendation(glucose_level):
    # if it's before doing exercise
    recommendations = {}
        
        
    if glucose_level < 70:
        # LOW GLUCOSE
        recommendations["intake"] = "Consumir una pequeña cantidad de carbohidratos antes del ejercicio (ejemplo: banana o barra energética)."
        recommendations["insulin"] = "Alertar sobre el riesgo de hipoglucemia y recordar llevar fuentes de carbohidratos rápidos."
        recommendations["activity"] = "No hacer ejercicio."

    elif 70 <= glucose_level <= 140:
        # OK GLUCOSE
        recommendations["intake"] = "Continuar con el plan de ejercicio sin necesidad de ajuste."
        recommendations["insulin"] = "Recordar la importancia de monitorear los niveles de glucosa a lo largo del entrenamiento."
        recommendations["activity"] = "Ejercicio permitido."

    elif 141 <= glucose_level <= 250:
        # HIGH GLUCOSE
        recommendations["intake"] = "Evaluar si el ejercicio es conveniente en ese momento, ya que niveles elevados pueden indicar resistencia a la insulina."
        recommendations["insulin"] = "Sugerir una breve espera, hidratación adecuada y monitoreo antes de iniciar la actividad."
        recommendations["activity"] = "Postergar ejercicio momentáneamente."
        
    else:  # glucose_level > 250
        # VERY HIGH GLUCOSE
        recommendations["intake"] = "Evitar ejercicio. Niveles muy elevados pueden ser indicio de cetoacidosis."
        recommendations["insulin"] = "Consultar al profesional y aplicar corrección si está indicado."
        recommendations["activity"] = "Contraindicado realizar actividad física."
    
    return recommendations


def generate_lunch_recommendation(glucose_level):
    recommendations = {}

    if glucose_level < 70:
        # LOW
        recommendations["intake"] = "Asegurar la ingesta de suficientes carbohidratos en el almuerzo (combinar simples y complejos)."
        recommendations["insulin"] = "Evaluar la necesidad de reducir la dosis de insulina si hay actividad intensa planificada."
        recommendations["activity"] = "Evitar ejercicio hasta estabilizar niveles."

    elif 70 <= glucose_level <= 140:
        # OK
        recommendations["intake"] = "Almuerzo equilibrado con proteínas, carbohidratos complejos y grasas saludables."
        recommendations["insulin"] = "Mantener la rutina sin ajustes mayores, salvo indicación específica."
        recommendations["activity"] = "Ejercicio permitido según planificación habitual."

    elif 141 <= glucose_level <= 250:
        # HIGH
        recommendations["intake"] = "Reducir el consumo de carbohidratos y priorizar alimentos con bajo índice glucémico."
        recommendations["insulin"] = "Sugerir una caminata breve post almuerzo para ayudar a estabilizar los niveles."
        recommendations["activity"] = "Actividad física leve post comida puede ser beneficiosa."

    else:  # >250
        # VERY HIGH
        recommendations["intake"] = "Evitar ingesta de carbohidratos. Priorizar líquidos e hidratación controlada."
        recommendations["insulin"] = "Consultar protocolo de corrección con insulina rápida antes de almorzar."
        recommendations["activity"] = "Evitar cualquier actividad física, riesgo de cetoacidosis."

    return recommendations


def generate_recommendations(glucose_level):
    now = datetime.now()
    if now < SCHEDULE.get("BREAKFAST_SCHEDULE")[0]:
        # if it's before breakfast
        recommendations = generate_breakfast_recommendation(glucose_level)
        
    elif SCHEDULE.get("EXERCISE_SCHEDULE")[0] - timedelta(hours=1) <= now < SCHEDULE.get("EXERCISE_SCHEDULE")[0]:
        # Before doing exercise
        recommendations = generate_prev_exercise_recommendation(glucose_level)
        
    elif SCHEDULE.get("LUNCH_SCHEDULE")[0] <= now < SCHEDULE.get("LUNCH_SCHEDULE")[1]:
        # Before lunch
        recommendations = generate_lunch_recommendation(glucose_level)

    else:
        recommendations = {}

    return recommendations