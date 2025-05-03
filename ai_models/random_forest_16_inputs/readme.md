# Uso de modelo

### Ejemplo de input (puede ser cualquier combinación válida)
```
nuevo_paciente = pd.DataFrame([{
    "glucosa_actual": 82,
    "ejercicio_reciente": 1,
    "carbohidratos_recientes": 0,
    "tiempo_ultima_comida": 150,
    "va_a_hacer_ejercicio": 0,
    "va_a_dormir": 1,
    "glucosa_bajando": 1,
    "historial_hipo_nocturnas": 1,
    "tiempo_ultima_insulina": 90,
    "dosis_insulina_reciente": 3,
    "tipo_insulina": "acción lenta",
    "comida_ultima_fue_alta_en_grasas": 1,
    "sintomas_hipoglucemia": 0,
    "enfermedad_actual": 0,
    "estrés": 3,
    "actividad_fisica_hoy_total": 60
}])

# Asegurarse de que las columnas categóricas estén bien codificadas
nuevo_paciente_encoded = pd.get_dummies(nuevo_paciente)
nuevo_paciente_encoded = nuevo_paciente_encoded.reindex(columns=X.columns, fill_value=0)

```


### Predecir
```
prediccion = model.predict(nuevo_paciente_encoded)[0]
recomendacion = le.inverse_transform([prediccion])[0]
```