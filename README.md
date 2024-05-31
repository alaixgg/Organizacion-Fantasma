Requiere un celery 

Para instalar 
<pip install celery django-celery-beat>

# Organizacion-Fantasma

PROYECTO TERCER CORTE

Proyecto de programación avanzada

## ENDPOINTS para usar API CRUD

## User endpoints:

# Crear un nuevo usuario.

POST /api/users/ 

# Obtener la lista de usuarios.

GET /api/users/  

# Obtener un usuario específico.

GET /api/users/<int:pk>/

# Actualizar un usuario existente.

PUT /api/users/<int:pk>/  


# Eliminar un usuario.
DELETE /api/users/<int:pk>/ 


## Department endpoints:

# Crear un nuevo departamento.
POST /api/departments/

# Obtener la lista de departamentos.
GET /api/departments/list/ 

# Obtener un departamento específico.
GET /api/departments/<int:pk>/ 

# Actualizar un departamento existente.
PUT /api/departments/<int:pk>/ 

# Eliminar un departamento.

DELETE /api/departments/<int:pk>/ 

Introducción:
En el mundo empresarial, la gestión eficiente de la nómina y los recursos humanos
representa un aspecto crítico para el éxito organizacional. Con el objetivo de optimizar
este proceso, se plantea el desarrollo de una API REST para un sistema de nómina, que
no solo automatice las tareas administrativas asociadas, sino que también garantice la
transparencia y la puntualidad en el pago de salarios, así como la comunicación efectiva
con los empleados.


El problema:
En muchos entornos empresariales, la gestión de la nómina y los recursos humanos
sigue siendo un desafío considerable. Los procesos manuales, la falta de integración
entre sistemas y la ausencia de notificaciones automáticas pueden generar
ineficiencias, retrasos en los pagos y, en última instancia, insatisfacción entre los
empleados. Además, la falta de un acceso fácil y claro a la información relacionada con
los pagos puede dificultar la comprensión de los detalles salariales por parte de los
trabajadores.


Requerimientos del cliente:


Con el fin de abordar estas problemáticas, el cliente requiere el desarrollo de una API
REST con los siguientes componentes:


• Módulo de empleados (CRUD): Este módulo permitirá gestionar de manera
integral la información de los empleados, incluyendo la creación, lectura,
actualización, eliminación de registros e inicio de sesión. Se establece que los
empleados, incluidos aquellos del departamento de gestión humana, tendrán
permiso para actualizar ciertos campos específicos de su perfil, como datos de
contacto o información personal. Los cambios relacionados con el salario y el
cargo se reservarán solo a usuarios con privilegios adicionales, designados
específicamente para la gestión de recursos humanos.

• Módulo de gestión humana: Este módulo estará disponible para los empleados
designados en el área de recursos humanos, quienes tendrán acceso privilegiado
para realizar acciones administrativas relacionadas con la contratación, la
gestión y la administración de empleados. Esto incluirá la capacidad de crear,
actualizar y eliminar registros de empleados, así como gestionar otros aspectos
relevantes del personal de la empresa, como permisos, roles y asignaciones.

• Pago de nóminas diario: Se establece la necesidad de realizar el pago de las
nóminas todos los días a las 6 pm hora colombiana, garantizando así la
puntualidad en los pagos y la estabilidad financiera de los empleados.


• Notificación automática por correo electrónico: Tras efectuar el pago de la
nómina, el sistema deberá enviar notificaciones automáticas a los empleados a
través de correo electrónico, informándoles sobre la realización del pago y
adjuntando el desprendible de pago correspondiente.


• Generación de desprendible de pago: Se deberá generar un desprendible de pago
que contenga los detalles pertinentes del salario de cada empleado. Este
desprendible estará disponible para consulta en la plataforma y se adjuntará en
el correo electrónico de notificación.


Se recomienda utilizar twilio, ya que su capa gratuita permite 100 correos al día,
independientemente por la solución que opten deben leer la documentación para
entender como enviar mensajes con archivos adjuntos.
https://www.twilio.com/en-us


Para el almacenamiento de archivos pueden valerse de dos opciones, manejarlas
localmente, es decir los archivos se generan y guardan en el servidor de la aplicación
con los problemas que esto puede presentar, o pueden almacenar los archivos en algún
servicio cloud preferiblemente gratuito, para esto recomiendo S3 de Amazon, google
cloud storage o azure blob storage.


La API puede ser desarrollada en cualquier lenguaje de alto nivel fuertemente tipado
(java, C, C#, F#, go, etc) además se va a poder realizar en Python.


La entrega se debe hacer por medio de un repositorio preferiblemente en GitHub en un
repositorio público, en el archivo readme deben colocar los nombres de los integrantes
(tres personas máximo) y la documentación de la API.



Para la documentación recomiendo utilizar postman o swagger.


Los proyectos convalidados serán validos siempre y cuando tengan o usen sistema de mailing y generación de archivos.


