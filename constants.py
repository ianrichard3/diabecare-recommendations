# 📌 Diccionario con recomendaciones según el nivel de glucosa
BASIC_RECOMMENDATIONS = {
    # 🟡 "low": Hipoglucemia leve (50-80 mg/dL)
    "low": [
        "Consumir de inmediato carbohidratos de absorción rápida (ej: jugo o caramelos) para corregir la hipoglucemia.",
        "Complementar con carbohidratos de absorción lenta para mantener los niveles estables después de la corrección.",
        "Evitar insulina adicional hasta que la glucemia se normalice.",
        "Si ocurrió después de actividad física, considerar ajustar dosis futuras.",
        "Repetir medición en 15 minutos para verificar recuperación."
    ],

    # 🔴 "very_low": Hipoglucemia severa (<50 mg/dL)
    "very_low": [
        "Consumir inmediatamente carbohidratos de absorción rápida (ej: alimento rico en azúcares).",
        "Después de la recuperación, ingerir una fuente de carbohidratos de absorción lenta para evitar que la glucosa vuelva a bajar.",
        "Avisar a un contacto de confianza y evitar estar solo/a hasta que los niveles se estabilicen.",
        "Monitorear cada 15 minutos hasta alcanzar un nivel seguro.",
        "Si los síntomas empeoran, buscar atención médica urgente."
    ],

    # 🟢 "ok": Glucemia dentro del rango (80-180 mg/dL)
    "ok": [
        "Mantener monitoreo regular, especialmente antes de comidas o actividad física.",
        "Continuar con alimentación y rutina normal.",
        "Beber agua regularmente para mantener hidratación óptima.",
        "Registrar el nivel en la app para seguimiento de patrones.",
        "Si hubo cambios recientes en insulina o comida, evaluar estabilidad del control."
    ],

    # 🟠 "high": Hiperglucemia leve/moderada (180-240 mg/dL)
    "high": [
        "Evaluar actividad física leve si es seguro.",
        "Revisar el consumo de alimentos recientes y ajustar próximos cálculos de insulina.",
        "Tomar agua para ayudar a reducir la glucosa.",
        "Si la glucemia persiste alta realizar la corrección necesaria."
    ],
    
    # 🔴 "very_high": Hiperglucemia grave (>240 mg/dL)
    "very_high": [
        "Aplicar corrección con insulina según pautas médicas.",
        "Aumentar frecuencia de monitoreo, especialmente si persiste la hiperglucemia.",
        "Beber agua en cantidad suficiente para prevenir deshidratación.",
        "Evitar actividad física intensa, es riesgoso con medidas altas.",
        "Si se presentan síntomas como náuseas o dificultad para respirar, buscar atención médica."
    ],

    # ⚠️ "critical": Hiperglucemia peligrosa (>450 mg/dL, posible cetoacidosis)
    "critical": [
        "Buscar asistencia médica urgente para evaluación y posible tratamiento hospitalario.",
        "Verificar presencia de cetonas si hay malestar, vómitos o respiración acelerada.",
        "Evitar correcciones excesivas sin supervisión médica.",
        "Tomar líquidos con electrolitos si hay signos de deshidratación grave.",
        "Reducir actividad hasta que los niveles de glucosa bajen."
    ]
}
