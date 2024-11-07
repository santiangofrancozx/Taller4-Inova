
# Dashboard de Educación en Colombia

Este proyecto es un dashboard interactivo desarrollado con **Streamlit** que permite explorar y visualizar datos educativos de los años 2020 a 2022. Los datos contienen información sobre los admitidos en diferentes programas académicos y permiten realizar análisis detallados según varios filtros.

## Características

- Visualización interactiva de los datos de admitidos por **año**, **sexo**, **institución** y **programa académico**.
- Filtros dinámicos para personalizar las visualizaciones.
- Gráficos y métricas clave sobre los datos generales y filtrados.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalados los siguientes requisitos:

- Python 3.7 o superior

## Instalación

### 1. Crear un entorno virtual (opcional pero recomendado)

Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto. Puedes crear uno con el siguiente comando:

```bash
python -m venv venv
```

### 2. Activar el entorno virtual

En **Windows**, utiliza:

```bash
venv\Scriptsctivate
```

En **macOS/Linux**, utiliza:

```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

Instala las dependencias necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

Para ejecutar la aplicación, usa el siguiente comando:

```bash
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador predeterminado.

## Estructura del proyecto

```bash
dashboard-educacion-colombia/
├── app.py                   # Archivo principal de la aplicación Streamlit
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
```

## Descripción de la aplicación

La aplicación permite realizar las siguientes acciones:

- **Filtros Interactivos:** Puedes seleccionar los años (2020, 2021, 2022) y la institución educativa de interés.
- **Visualización de Datos Filtrados:** Una vez seleccionados los filtros, se muestran los datos relevantes y se generan gráficos interactivos que muestran el total de admitidos por año, sexo, y programa académico.
- **Consulta y Análisis Detallado:** Los usuarios pueden elegir columnas para crear consultas personalizadas y visualizar la distribución de los datos seleccionados.
- **Datos Generales:** También se pueden visualizar los datos generales sin filtros, con gráficos que muestran el total de admitidos por año, sexo y programa académico, y métricas clave como el año con más admitidos o el programa con más admitidos.

## Dependencias

Las dependencias necesarias para ejecutar esta aplicación están listadas en el archivo `requirements.txt`, que incluye:

- **streamlit**: Para crear la interfaz de usuario interactiva.
- **pandas**: Para el manejo y análisis de datos.
- **seaborn**: Para la creación de gráficos estadísticos.
- **matplotlib**: Para la creación de gráficos personalizados.

## Contribución

Si deseas contribuir al desarrollo de esta aplicación, sigue estos pasos:

1. Haz un **fork** del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza los cambios necesarios.
4. Haz **commit** de tus cambios (`git commit -am 'Añadida nueva característica'`).
5. Haz **push** de tus cambios a tu repositorio (`git push origin feature/nueva-caracteristica`).
6. Abre un **Pull Request**.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
