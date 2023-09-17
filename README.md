# Flask_Api_Tarea

Se tiene una empresa en la cual se maneja a las áreas (Marketing, Sistemas, Contabilidad, etc) y a sus empleados, los empleados pertenecen a un área en específica (no pueden pertenecer a mas de una).

Cada area tiene la siguiente data: 

id
nombre
piso
Cada empleado tiene la siguiente data:

id
nombre
apellido
email
area_id
Crear la API con documentación en la cual se considera los siguientes endpoints:

GET /areas: devolver todas las áreas
POST /area: crear una área
GET /area/:id: devolver una área con el ID y si no existe indicar
POST /empleado: crear un empleado
GET /empleados: devolver a los empleados y opcionalmente pasarle sus "query params" que podrían ser:
email: filtrar por sus email
nombre: filtrar por sus nombres
PISTA: para validar si existe o no el query param usar condicionales (if - elif - else)

#Resulado del método get a /areas
![flask1](https://github.com/StefanoZevallos/Rest-Api-Basica-hecha-en-Flask/assets/107054283/42fe5064-268a-467f-a500-18affb030a0b)

#Resulado del método Post a /area
![flask2](https://github.com/StefanoZevallos/Rest-Api-Basica-hecha-en-Flask/assets/107054283/a90c9ffd-6c80-4e25-b61d-eb1a31aa0dd4)

