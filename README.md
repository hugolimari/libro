# LectuVault - Web Estática de Libros Digitales

Sitio web estático optimizado para desplegar en **GitHub Pages** o **Netlify**.

---

## 📁 Dónde y con qué nombre guardar el libro cuando lo generes

Guarda tu libro generado en la siguiente ruta exacta:

```plaintext
d:\pirata\downloads\Make_More_Money_Gavin_Ross.pdf
```

> **Nombre exacto del archivo:**
> `Make_More_Money_Gavin_Ross.pdf`

*(Ya hemos incluido un archivo PDF de prueba con ese nombre exacto para que el enlace y la descarga ya funcionen desde el primer momento).*

---

## 🚀 Pasos para subir a GitHub (`https://github.com/hugolimari/libro`)

Abre tu terminal en esta carpeta (`d:\pirata`) y ejecuta los siguientes comandos:

```bash
# 1. Inicializar git si no lo has hecho
git init

# 2. Agregar todos los archivos
git add .

# 3. Crear el commit inicial
git commit -m "feat: sitio web LectuVault con libro Make More Money"

# 4. Asignar la rama principal
git branch -M main

# 5. Conectar con tu repositorio de GitHub
git remote add origin https://github.com/hugolimari/libro.git

# 6. Subir los cambios a GitHub
git push -u origin main
```

*(Si ya tenías el repositorio inicializado o te pide autenticación, ingresa con tu usuario o Personal Access Token de GitHub).*

---

## 🌐 Cómo publicar en Netlify (Gratis en 1 minuto)

### Método 1: Conectar con GitHub (Recomendado)
1. Ve a [Netlify.com](https://app.netlify.com/) e inicia sesión con tu cuenta de GitHub.
2. Haz clic en **"Add new site"** > **"Import an existing project"**.
3. Selecciona **GitHub** y busca tu repositorio: `hugolimari/libro`.
4. En la configuración de despliegue:
   - **Branch:** `main`
   - **Build command:** *(dejar en blanco)*
   - **Publish directory:** `.` *(el punto o déjalo en blanco)*
5. Haz clic en **"Deploy site"** ¡y listo! Te dará una URL pública activa de inmediato (ej: `https://lectuvault.netlify.app`).

### Método 2: Arrastrar y Soltar (Aún más rápido sin configurar nada)
1. En Netlify, entra en **Sites** y busca la zona que dice: **"Want to deploy without connecting to Git? Drag and drop your site output folder here"**.
2. Arrastra la carpeta `d:\pirata` completa directamente a esa ventana de tu navegador.
3. En 5 segundos tendrás tu página web en línea.

---

## 🎭 Características para la trampa / broma
- **Diseño underground profesional:** Modo oscuro tipo Z-Library / Anna's Archive.
- **Portada realista:** Portada generada en alta resolución para *"Make More Money"* de Gavin Ross con sello de Bestseller.
- **Libros cebo:** Títulos famosos (*Padre Rico*, *Hábitos Atómicos*, *Clean Code*); al hacer clic, muestran una alerta creíble de *"Enlace bloqueado por reclamo DMCA"*, dejando como **único libro activo y descargable** el de Gavin Ross.
- **Falso selector de servidores:** Cuenta regresiva de 4 segundos con verificación de firma digital antes de disparar la descarga directa del PDF.
