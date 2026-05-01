# Despliegue Automático en Azure - Flask App

## Información del Estudiante

- **Nombre:** José Andrés
- **Curso:** Despliegue Automático de Aplicaciones
- **Fecha:** Mayo 2026

---

## Descripción del Proyecto

Esta es una aplicación web simple desarrollada con **Flask** (Python) diseñada para ser desplegada en **Azure App Service**. La aplicación incluye:

- Página de bienvenida con diseño atractivo (gradientes, efectos visuales)
- Contador interactivo con JavaScript
- Endpoint de verificación de salud (`/health`)
- Configuración optimizada para Azure App Service

---

## Estructura del Proyecto

```
despliegue_automatico/
├── app.py              # Aplicación Flask principal
├── requirements.txt    # Dependencias del proyecto
├── templates/
│   └── index.html      # Template HTML con CSS inline
├── .gitignore          # Archivos ignorados por Git
└── README.md           # Este archivo
```

---

## Instrucciones de Ejecución Local

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clonar o descargar el repositorio:**
   ```bash
   cd despliegue_automatico
   ```

2. **Crear un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

6. **Abrir en el navegador:**
   - Local: http://127.0.0.1:5000
   - O el puerto que aparezca en la consola

---

## Instrucciones de Despliegue en Azure App Service

### Método 1: Despliegue Local (Azure CLI)

1. **Instalar Azure CLI** (si no lo tienes):
   ```bash
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   ```

2. **Iniciar sesión en Azure:**
   ```bash
   az login
   ```

3. **Crear el App Service:**
   ```bash
   az webapp up --name mi-app-flask-azure --resource-group mi-grupo-recursos --runtime "PYTHON:3.11" --sku B1 --location eastus
   ```

### Método 2: Despliegue con GitHub Actions (Automático)

1. **Subir el código a GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
   git push -u origin main
   ```

2. **En Azure Portal:**
   - Ir a tu App Service
   - Sección **Deployment Center**
   - Elegir **GitHub** como fuente
   - Seleccionar tu repositorio y rama
   - Azure generará automáticamente el workflow de GitHub Actions

3. **El workflow incluirá:**
   - Build de la aplicación
   - Instalación de dependencias
   - Despliegue automático en cada push a `main`

### Variables de Entorno en Azure

Configurar en **Azure Portal > Configuración > Configuración de la aplicación**:

| Variable | Valor | Descripción |
|----------|-------|-------------|
| `SCM_DO_BUILD_DURING_DEPLOYMENT` | `true` | Construir durante el despliegue |
| `PYTHON_VERSION` | `3.11` | Versión de Python |

---

## Endpoints de la Aplicación

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal con mensaje de bienvenida |
| `/health` | Verificación de salud (JSON) |

---

## Notas Importantes

- La app usa el puerto definido por la variable de entorno `PORT` (Azure lo configura automáticamente)
- En local, por defecto usa el puerto 8000
- Gunicorn está incluido en `requirements.txt` para producción
- Azure App Service detecta automáticamente aplicaciones Flask

---

## Licencia

Proyecto educativo para curso de despliegue automático.
