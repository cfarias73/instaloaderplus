# Instaloader Web Pro

Esta es una bifurcación (fork) mejorada del famoso proyecto `instaloader`. Además de funcionar desde la línea de comandos, esta versión incluye una **Interfaz Gráfica de Usuario (Web UI)** premium, moderna y fácil de utilizar.

## 🌟 Nuevas Funcionalidades (Web UI)
- **Diseño Glassmorphism:** Interfaz limpia, moderna y animada.
- **Descargas con 1 Clic:** Descarga publicaciones específicas o perfiles completos fácilmente.
- **Login Seguro con Chrome:** Importa tu sesión abierta directamente desde Google Chrome sin necesidad de exponer tu contraseña.
- **Gestión de Descargas:** Sistema mejorado con la capacidad de iniciar y **detener forzosamente** la descarga para evitar bloqueos por parte de Instagram.

---

## 🚀 Cómo Instalar

Dado que esta versión usa Python, asegúrate de tener instalado Python 3 y luego ejecuta lo siguiente:

1. **Clonar o descargar** la carpeta del repositorio en tu computadora.
2. Abre tu terminal y colócate dentro de la carpeta:
   ```bash
   cd /Ruta/Hacia/Tu/Carpeta/instaloader
   ```
3. Crea un entorno virtual e instala las dependencias necesarias:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .
   pip install flask browser-cookie3
   ```

---

## 🕹️ Cómo Correr la Interfaz Web

Siempre que quieras utilizar la aplicación, debes levantar el servidor local:

1. Abre la terminal y ve a la carpeta del proyecto.
2. Activa el entorno virtual:
   ```bash
   source venv/bin/activate
   ```
3. Inicia el servidor web:
   ```bash
   python app.py
   ```
4. Abre tu navegador favorito y visita: **[http://localhost:3017](http://localhost:3017)**

---

## 📖 Cómo Operar la Plataforma

1. **Paso 1: Conectar Cuenta**
   - Ve a la primera pestaña de la interfaz.
   - Para evitar bloqueos, Instagram requiere que descargues el contenido como usuario verificado.
   - Coloca tu **nombre de usuario**.
   - Marca la opción **"Extraer sesión abierta de Google Chrome"** (Debes tener tu Instagram abierto en Chrome).
   - Haz clic en Iniciar Sesión.

2. **Paso 2: Descargar Contenido**
   - Ve a la pestaña de descarga.
   - Selecciona si quieres bajar un Perfil Completo o un Post (Reel, Foto).
   - Escribe el @usuario o el Shortcode del Post.
   - Haz clic en iniciar descarga. Podrás ver que los archivos caen mágicamente en tu carpeta `/downloads/`.
   - Si crees que el proceso es muy largo y quieres parar, simplemente haz clic en **"Detener Descarga"**.
