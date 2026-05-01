# Guía de Instalación Paso a Paso (InstaloaderPlus)

Esta guía te ayudará a instalar y usar el programa en tu computadora (Windows o Mac). He preparado una versión "rápida" que no requiere instalar nada técnico.

---

## Opción A: El Método Rápido (Recomendado) 🚀
Este método es el más sencillo: solo descargas un archivo y lo usas. No requiere instalar nada técnico.

1. **Descarga el programa** para tu computadora:
   - 💻 [Descargar para **Windows** (PC)](https://github.com/cfarias73/instaloaderplus/raw/master/InstaloaderPlus-windows-latest.zip)
   - 🍎 [Descargar para **Mac**](https://github.com/cfarias73/instaloaderplus/raw/master/InstaloaderPlus-Mac.zip)

2. **Cómo abrirlo:**
   - **En Windows:** Descomprime el archivo y haz doble clic en `InstaloaderPlus.exe`.
   - **En Mac:** Descomprime el archivo, haz **clic derecho** sobre `InstaloaderPlus` y elige **"Abrir"**.

3. **¡Listo!** Se abrirá una ventana y luego tu navegador con el programa. No cierres la ventana negra mientras lo uses.

---

## Opción B: Instalación Manual (Para desarrolladores)
Si prefieres correr el código fuente directamente, sigue estos pasos:

### 1. Descargar el programa

1. Ve a la página del proyecto en GitHub: [https://github.com/cfarias73/instaloaderplus](https://github.com/cfarias73/instaloaderplus)
2. Haz clic en el botón verde que dice **"<> Code"**.
3. Elige la opción **"Download ZIP"**.
4. Una vez descargado, busca el archivo en tu carpeta de Descargas y **descomprímelo** (clic derecho -> Extraer todo).

---

## 2. Instalar Python (El motor que hace que esto funcione)

Si ya tienes Python, puedes saltar este paso. Si no estás seguro, instálalo:

### En Windows:
1. Ve a [python.org/downloads](https://www.python.org/downloads/windows/).
2. Descarga el instalador más reciente (ej. "Windows installer 64-bit").
3. **MUY IMPORTANTE:** Al abrir el instalador, marca la casilla que dice **"Add Python to PATH"** antes de darle a "Install Now".
4. Sigue las instrucciones hasta que termine.

### En Mac:
1. Ve a [python.org/downloads](https://www.python.org/downloads/macos/).
2. Descarga e instala el archivo .pkg más reciente.
3. Sigue los pasos de instalación normales.

---

## 3. Preparar el programa (Instalar dependencias)

Ahora vamos a decirle a la computadora qué librerías necesita el programa.

### En Windows:
1. Abre la carpeta que descomprimiste en el Paso 1.
2. Haz clic en la barra de direcciones de la carpeta (donde aparece la ruta arriba) y escribe la palabra `cmd`, luego presiona **Enter**. Se abrirá una ventana negra (Terminal).
3. Escribe el siguiente comando y presiona **Enter**:
   ```bash
   pip install -r requirements.txt .
   ```
   *(Espera a que terminen de cargar todas las barritas).*

### En Mac:
1. Abre la aplicación **Terminal** (búscala en el Spotlight con `Cmd + Espacio`).
2. Escribe `cd ` (con un espacio al final), y luego **arrastra la carpeta** del proyecto directamente dentro de la ventana de la Terminal. Presiona **Enter**.
3. Escribe el siguiente comando y presiona **Enter**:
   ```bash
   pip3 install -r requirements.txt .
   ```
   *(Si te pide contraseña, es la de tu Mac).*

---

## 4. Iniciar el programa

Cada vez que quieras usar el programa, haz lo siguiente:

1. Abre la carpeta del proyecto y abre la terminal (como hiciste en el paso anterior).
2. Escribe el comando:
   - **En Windows:** `python app.py`
   - **En Mac:** `python3 app.py`
3. Verás un mensaje que dice algo como `Running on http://127.0.0.1:3017`.
4. **No cierres esa ventana negra.**

---

## 5. Usar el programa

1. Abre tu navegador favorito (Chrome, Edge, etc.).
2. En la barra de direcciones, escribe: `http://127.0.0.1:3017` y presiona **Enter**.
3. ¡Listo! Ya puedes empezar a descargar contenido de Instagram.

---

### Notas importantes:
- **Carpeta de descargas:** Todo lo que descargues se guardará automáticamente en una carpeta llamada `downloads` dentro de la carpeta del proyecto.
- **Cerrar el programa:** Para apagarlo, simplemente cierra la ventana negra (Terminal) o presiona `Ctrl + C` dentro de ella.
