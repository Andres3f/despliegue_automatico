"""
Aplicación Flask para despliegue en Azure App Service.
Desarrollado como parte del proyecto de despliegue automático.
"""

import os
from flask import Flask, render_template

# Crear instancia de Flask
app = Flask(__name__)


@app.route("/")
def home():
    """
    Ruta principal que muestra la página de bienvenida.
    """
    return render_template("index.html")


@app.route("/health")
def health_check():
    """
    Endpoint de verificación de salud para Azure.
    """
    return {"status": "healthy", "message": "La aplicación está funcionando correctamente"}, 200


if __name__ == "__main__":
    # Obtener el puerto de las variables de entorno de Azure
    # Azure App Service usa el puerto 8000 por defecto para Python
    port = int(os.environ.get("PORT", 8000))
    
    # Ejecutar la aplicación
    # host="0.0.0.0" es necesario para que Azure pueda acceder a la app
    app.run(host="0.0.0.0", port=port, debug=False)
