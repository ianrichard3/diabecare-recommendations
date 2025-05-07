BASIC_RECOMMENDATIONS = {
  "low": [
    "Comer inmediatamente algo con azúcar rápida (ej: jugo o caramelos)",
    "Revisar insulina aplicada, posible exceso",
    "Avisar a alguien de confianza y monitorear la glucosa"
  ],
  "ok": [
    "Todo en orden, seguir monitoreando regularmente",
    "Beber agua y mantener actividad normal",
    "Aprovechar para registrar en la app el buen momento glucémico"
  ],
  "high": [
    "Hacer ejercicio suave si es seguro",
    "Evaluar corrección con insulina (según indicación médica)",
    "Revisar alimentos recientes y planificar la próxima comida"
  ],
  "very_high": [
    "Aplicar corrección urgente si está indicado",
    "Consultar a un profesional si los valores persisten altos",
    "Monitorear con mayor frecuencia, riesgo de cetoacidosis"
  ]
}




# Recomendaciones
from datetime import datetime, timedelta

SCHEDULE = {
        "BREAKFAST_SCHEDULE": (datetime.now().replace(hour=6, minute=0, second=0), datetime.now().replace(hour=10, minute=0, second=0)),
        "EXERCISE_SCHEDULE": (datetime.now().replace(hour=17, minute=0, second=0), datetime.now().replace(hour=19, minute=0, second=0)),
        "LUNCH_SCHEDULE": (datetime.now().replace(hour=12, minute=0, second=0), datetime.now().replace(hour=15, minute=0, second=0))
          }

