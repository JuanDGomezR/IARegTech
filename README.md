# README.md

## IARegTech – Plataforma de Evaluación Ética y Certificación de Sistemas de IA

**IARegTech** es una aplicación web local desarrollada en Python con Flask que permite:

- Subir y analizar archivos de proyectos de inteligencia artificial reales.
- Detectar si contienen componentes de IA (modelos, decisiones, aprendizaje).
- Evaluar aspectos éticos como transparencia, no discriminación, control humano y **autoría IA**.
- Clasificar sistemas por nivel de riesgo (bajo, medio, alto).
- Emitir certificaciones según criterios éticos y sector.
- Generar informes PDF y enviar notificaciones por correo.
- Verificar si el código fue generado por IA (como ChatGPT o Copilot) y considerar este aspecto en la evaluación ética.

---

## 🧠 ¿Qué significa IARegTech?

**IARegTech** es un acrónimo de:

- **IA**: Inteligencia Artificial  
- **RegTech**: Regulatory Technology (Tecnología regulatoria)

Este proyecto representa una herramienta **tecnológica de regulación y control ético aplicada al mundo de la inteligencia artificial**, permitiendo verificar que un sistema o modelo de IA cumpla criterios de transparencia, equidad y control humano.

---
## 🚀 Tecnologías utilizadas

- Python 3.x
- Flask
- Flask-Bootstrap
- Flask-WTF (formularios)
- Flask-Mail (correo)
- Flask-MySQLdb (conexión a MySQL)
- ReportLab (PDF)
- MySQL (XAMPP/MariaDB)

---

## 🛠 Instalación

1. Copea en el escritorio la carpeta del proyecto
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv
# En Windows:
.venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Crea la base de datos en MySQL:
```sql
CREATE DATABASE iaregtech;
USE iaregtech;

-- Ejecuta las sentencias SQL proporcionadas en el proyecto para crear las tablas necesarias (siempre y cuando sea necesario).
```
5. Configura tus credenciales en `config.py`:
```python
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'tu_contraseña'
MAIL_USERNAME = 'tucorreo@gmail.com'
MAIL_PASSWORD = 'tu_contraseña_app'
```

---

## ▶️ Uso

1. Ejecuta el servidor Flask:
```bash
python app.py
```

2. Accede desde el navegador a:
```
http://localhost:5000/registrar         # Para registrar un sistema manual
http://localhost:5000/subir             # Para subir archivo de IA real
```

3. Flujo de trabajo sugerido:
- Registrar un sistema IA manualmente o subir un archivo `.py`, `.ipynb`, `.csv`, `.pkl`.
- El sistema detecta si contiene IA, si automatiza decisiones, si usa datos sensibles y si fue generado por una IA.
- Se realiza una evaluación ética automática basada en:
  - Transparencia
  - No Discriminación
  - Control Humano
  - Autoría IA
- Se clasifica el nivel de riesgo (bajo, medio, alto).
- Se genera certificación (Aprobado, Condicionado, Rechazado).
- Se genera un informe PDF con los resultados.
- (Opcional) Se puede enviar el informe por correo electrónico.

---

## 📁 Estructura del proyecto

```
IARegTech/
├── app.py
├── config.py
├── extensions.py
├── controllers/
│   ├── sistema_controller.py
│   └── carga_controller.py
├── forms/
│   ├── sistema_form.py
│   └── archivo_form.py
├── models/
│   └── sistema.py
├── services/
│   ├── analizador_archivo.py
│   ├── evaluador_automatico.py
│   ├── clasificador.py
│   ├── notificador.py
│   ├── reporte_pdf.py
│   └── estrategias_riesgo/
│       ├── estrategias.py
├── templates/
├── static/
├── uploads/
└── README.md
```

---

## 🧠 Patrones de diseño aplicados

- **Template Method** – Evaluación ética automática
- **Strategy** – Clasificación de riesgo
- **Factory Method** – Certificación personalizada según resultado
- **Observer** – Notificación por correo electrónico (opcional)
- **Builder** – Construcción y evaluación del objeto `SistemaIA`

---

## ⚙️ Actualizaciones recientes

- ✅ Añadido criterio "Autoría IA" para detectar si el código fue generado por herramientas como ChatGPT o Copilot.
- ✅ Informe PDF incluye ahora observaciones éticas por generación automática.
- ✅ Evaluación ética ampliada a 4 criterios.
- ✅ Documentación actualizada con flujos automáticos y manuales.

---

## 📜 Licencia

Este proyecto es de uso educativo y demostrativo. Inspirado en el Proyecto de Ley sobre IA en Colombia (2025).

---

## ✉️ Contacto

Para soporte o consultas: 

---

¡Gracias por usar IARegTech!
