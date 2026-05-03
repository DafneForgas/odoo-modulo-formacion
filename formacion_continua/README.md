# Módulo Formación Continua - Odoo 18

## Descripción del Proyecto

Este proyecto contiene un módulo personalizado para **Odoo 18** desarrollado para **Juguetes Reunidos SL**. El módulo está diseñado para gestionar y controlar la **formación continua de los trabajadores** de la empresa.

### Contexto
La empresa Juguetes Reunidos SL lleva varios años trabajando con Odoo y ha migrado recientemente a la versión 18. Los módulos principales en uso son:
- Ventas
- Recursos Humanos (HR)
- Facturación

### Objetivo del Módulo
El módulo **formacion_continua** permite:

1. **Crear acciones formativas** con información sobre:
   - Nombre del curso
   - Formador responsable
   - Participantes (empleados inscritos)
   - Horas totales del curso
   - Horas por sesión
   - Cálculo automático del número de sesiones

2. **Gestionar especialidades formativas** para clasificar tipos de formación

3. **Extender la ficha del empleado** para visualizar las acciones formativas en las que participa

4. **Vistas especializadas**:
   - Vista de lista (lista de acciones formativas)
   - Vista de formulario (detalle de cada acción)
   - Vista de calendario (cronograma de acciones)
   - Vista de búsqueda (filtros y búsquedas avanzadas)

---

## Instalación y Configuración

### Requisitos Previos

- Python 3.12+
- PostgreSQL (base de datos Odoo)
- Entorno virtual (venv)
- Odoo 18 instalado

### Pasos de Instalación

#### 1. Navegar a la carpeta del proyecto

```powershell
cd C:\Digitech\SistemasGestionEmpresarial\OdooProyectos\Entregable4
```

#### 2. Activar el Entorno Virtual

```powershell
.\venv\Scripts\Activate.ps1
```

Verifica que el entorno está activado (deberías ver `(venv)` al inicio del prompt):
```
(venv) PS C:\Digitech\SistemasGestionEmpresarial\OdooProyectos\Entregable4>
```

#### 3. Verificar la Configuración de Odoo

Navega a la carpeta `odoo18dev` y verifica que el archivo `config/odoo.conf` está configurado correctamente:

```powershell
cd odoo18dev
cat config\odoo.conf
```

**Configuración importante en `odoo.conf`:**
```ini
[options]
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
addons_path = C:\Digitech\SistemasGestionEmpresarial\OdooProyectos\Entregable4\odoo18dev\odoo\addons, C:\Digitech\SistemasGestionEmpresarial\OdooProyectos\Entregable4\odoo18dev\odoo\custom_addons
admin_passwd = admin
http_port = 8069
```

---

## Cómo Ejecutar Odoo

### Opción 1: Iniciar Odoo en Modo Normal

```powershell
cd C:\Digitech\SistemasGestionEmpresarial\OdooProyectos\Entregable4\odoo18dev
python .\odoo\odoo-bin -c config\odoo.conf
```

Odoo estará disponible en: `http://localhost:8069`

### Opción 2: Instalar el Módulo por Primera Vez

```powershell
python .\odoo\odoo-bin -c config\odoo.conf -i formacion_continua -d EmpresaEntrega4
```

- `-i formacion_continua`: Instala el módulo
- `-d EmpresaEntrega4`: Especifica la base de datos

### Opción 3: Actualizar el Módulo (después de cambios)

```powershell
python .\odoo\odoo-bin -c config\odoo.conf -u formacion_continua -d EmpresaEntrega4
```

- `-u formacion_continua`: Actualiza el módulo
- `-d EmpresaEntrega4`: Especifica la base de datos

---

## Detener Odoo

Para detener la ejecución, presiona **`Ctrl + C`** en el terminal donde está corriendo Odoo.

---

## Estructura del Módulo

```
formacion_continua/
├── __init__.py                          # Inicializador del módulo
├── __manifest__.py                      # Configuración del módulo
├── models/
│   ├── __init__.py                      # Inicializador de modelos
│   ├── accion_formativa_model.py        # Modelo: Acción Formativa
│   ├── especialidad.py                  # Modelo: Especialidad
│   ├── res_partner.py                   # Herencia: res.partner (formadores)
│   └── hr_employee.py                   # Herencia: hr.employee (participantes)
├── views/
│   ├── accion_formativa_views.xml       # Vistas de acciones formativas
│   ├── res_partner_views.xml            # Herencia de vistas de partner
│   ├── hr_employee_views.xml            # Herencia de vistas de empleado
│   └── menu.xml                         # Menú principal del módulo
├── security/
│   ├── formacion_security.xml           # Grupos de seguridad
│   └── ir.model.access.csv              # Control de acceso
├── demo/
│   └── demo.xml                         # Datos de demostración
└── controllers/
    └── controllers.py                   # Controladores (si aplica)
```

---

## Modelos Definidos

### 1. **formacion.accion** (Acción Formativa)

Campos principales:
- `name` (Char): Nombre del curso
- `formador_id` (Many2one): Referencia al formador (res.partner)
- `participante_ids` (Many2many): Empleados participantes (hr.employee)
- `horas_totales` (Float): Duración total en horas
- `horas_sesion` (Float): Duración de cada sesión
- `num_sesiones` (Integer, computed): Número de sesiones (cálculo automático)
- `fecha_inicio` (Datetime): Fecha de inicio

### 2. **formacion.especialidad** (Especialidad)

Campos principales:
- `name` (Char): Nombre de la especialidad

### 3. **res.partner** (Extensión - Formadores)

Campos adicionales:
- `es_formador` (Boolean): Indica si es formador
- `especialidad_id` (Many2one): Especialidad del formador

### 4. **hr.employee** (Extensión - Participantes)

Campos adicionales:
- `formacion_ids` (Many2many): Acciones formativas en las que participa

---

## Vistas Disponibles

### Acciones Formativas (formacion.accion)

1. **Vista de Lista (List View)**
   - Muestra nombre del curso, formador, horas totales y número de sesiones

2. **Vista de Formulario (Form View)**
   - Formulario completo con todos los campos
   - Campo `num_sesiones` en modo lectura (calculado automáticamente)
   - Selector de participantes con etiquetas (many2many_tags)

3. **Vista de Búsqueda (Search View)**
   - Búsqueda por nombre y formador
   - Filtro: "Con formador"

4. **Vista de Calendario (Calendar View)**
   - Calendario que muestra las acciones por fecha de inicio

---

## Seguridad y Permisos

### Grupo de Usuarios
- **Nombre**: Usuario Formación
- **Categoría**: Recursos Humanos

### Control de Acceso (ACL)

| Modelo | Permiso | Lectura | Escritura | Creación | Eliminación |
|--------|---------|---------|-----------|----------|-------------|
| formacion.accion | Completo | ✓ | ✓ | ✓ | ✓ |

Por defecto, todos los usuarios pueden acceder al módulo sin necesidad de grupo específico.

---

## Acceso al Módulo en Odoo

### Menú Principal
Una vez instalado y actualizado, el módulo aparece en el menú con:

- **Menú raíz**: Formación
  - **Submenú**: Acciones Formativas

### En Recursos Humanos

Si accedes a la ficha de un empleado:
1. Ve a **Recursos Humanos > Empleados**
2. Abre un empleado
3. En la pestaña **Formación**, verás las acciones formativas en las que participa

---

## Reiniciar/Actualizar el Módulo

Cada vez que hagas cambios en el módulo (modelos, vistas, campos), debes actualizar:

```powershell
python .\odoo\odoo-bin -c config\odoo.conf -u formacion_continua -d EmpresaEntrega4
```

Luego recarga el navegador con **F5** o **Ctrl + Shift + R**.

---

## Solución de Problemas

### El menú no aparece
- Verifica que el comando de instalación/actualización se ejecutó sin errores
- Recarga el navegador (Ctrl + Shift + R)
- Comprueba los permisos en **Configuración > Usuarios y Empresas > Usuarios**

### Error al instalar el módulo
- Revisa el archivo `odoo.log` en la carpeta `odoo18dev/`
- Verifica que todos los archivos XML estén bien formados
- Asegúrate de que las dependencias (`base`, `hr`) están instaladas

### Vistas no se cargan correctamente
- Verifica que los nombres de modelo coinciden en `accion_formativa_views.xml` y `accion_formativa_model.py`
- Confirma que el id de la acción (`action_formacion`) se referencia correctamente en el menú

---

## Notas Importantes

- El módulo requiere el módulo **HR** (Recursos Humanos) de Odoo
- Los campos de fecha usan formato `Datetime` (incluyen hora)
- El cálculo de sesiones es automático: `num_sesiones = ceil(horas_totales / horas_sesion)`
- La vista de calendario usa `fecha_inicio` como fecha de inicio

---

## Autor
Dafne Forgas

**Versión del Módulo**: 0.1  
**Versión de Odoo**: 18.0  
**Categoría**: Human Resources
