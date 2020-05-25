# Information Retrieval

### Directorios:
- Carpeta **template**: Propio de la interfaz de usuario
- Carpeta **Data**: Contiene el Corpus de Google. 
    _procesamiento.py_: Contiene la lematización, factorización y la eliminación de _stopWords_
    ```plain
         python procesamiento.py
     ```
     _boolean_model.py_: Funciones para hallar la similitud de las palabras basándose en modelo booleano y la métrica de Jaccard. 
     _modelo_binario.py_: Primera alternativa para obtener similitud, fue descartada.
     _func.py_: Funciones adicionales que será usadas.

### Ejecución general en desktop:
```plain
export FLASK_APP="routes.py"
flask run
```