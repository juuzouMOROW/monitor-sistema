# 🖥️ Monitor del Sistema - Django + Psutil

## 📘 Descripción del Proyecto

Aplicación web desarrollada en **Django** para monitorear en tiempo real los recursos del sistema utilizando la librería **Psutil**.
Este proyecto fue desarrollado como examen del segundo parcial de la materia **Arquitectura de Computadoras**.

## 👥 Información del Grupo

**Integrantes:**

* Héctor David Bonilla Osorto - 202320110097
* Roberto Carlos Morales Ordoñez - 202310110239
* Hadith Gissell Reyes Sierra - 202310110397

**Clase:** Arquitectura de Computadoras - Segundo Parcial
**Universidad:** UTH - Universidad Tecnológica de Honduras

---

## ⚙️ Características

* Monitoreo en tiempo real de CPU, RAM y Disco.
* Interfaz moderna con modo oscuro y diseño responsive.
* Actualización manual de datos.
* Manejo robusto de errores.
* Información del sistema operativo.
* Barras de progreso visuales.

---

## 🧠 Tecnologías Utilizadas

* **Backend:** Django 5.2.7
* **Frontend:** Bootstrap 5, HTML5, CSS3
* **Librerías:** Psutil, Platform
* **Lenguaje:** Python 3.13
* **Base de datos:** SQLite3

---

## 📁 Estructura del Proyecto

```
monitor-sistema/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── README.md
├── monitor/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── sistema/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── sistema/
            └── index.html
```

---

## 🛠️ Instalación y Configuración

### 🔹 Prerrequisitos

* Python 3.8 o superior.
* pip (gestor de paquetes de Python).

### 🔹 Pasos de Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd monitor-sistema
   ```

2. **Crear entorno virtual:**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones:**

   ```bash
   python manage.py migrate
   ```

5. **Ejecutar el servidor:**

   ```bash
   python manage.py runserver
   ```

6. **Abrir en el navegador:**

   ```
   http://127.0.0.1:8000/
   ```

---

## 📊 Funcionalidades Implementadas

### 🔸 Recolección de Datos del Sistema

* **CPU:** Porcentaje de uso, núcleos físicos y hilos lógicos.
* **Memoria RAM:** Uso en GB, porcentaje y total disponible.
* **Almacenamiento:** Espacio usado, libre y total en GB.
* **Sistema Operativo:** Información detallada del SO y arquitectura.

### 🔸 Interfaz de Usuario

* Diseño moderno con modo oscuro.
* Tarjetas informativas organizadas.
* Barras de progreso visuales.
* Botón de actualización manual.
* Diseño responsive para dispositivos móviles.

---

## 🧩 Características Técnicas

* Manejo de errores con `try/except`.
* Actualización en tiempo real.
* Validación de datos con **Psutil**.
* Estructura **MVC** de Django.

---

## 🚨 Solución de Problemas Comunes

### ❗ Error: `ModuleNotFoundError: No module named 'psutil'`

**Solución:**

```bash
pip install psutil
```

### ❗ Error: `TemplateDoesNotExist`

**Solución:**
Verificar que la estructura de carpetas sea:

```
sistema/templates/sistema/index.html
```

### ❗ Error: Migraciones pendientes

**Solución:**

```bash
python manage.py migrate
```

---

## 🧠 Componentes Principales

### 📂 views.py

Contiene la lógica principal para obtener datos del sistema:

```python
def get_system_info():
    # Obtiene datos de CPU, RAM, Disco y Sistema
    # Maneja errores con try/except
    # Retorna diccionario con toda la información
```

### 📄 index.html

Template principal con:

* Interfaz moderna con Bootstrap.
* Modo oscuro con toques de rosa.
* Visualización de datos en tarjetas.
* Diseño responsive.

### 📜 requirements.txt

Lista de dependencias del proyecto:

```
Django>=5.2
psutil>=5.9
```
