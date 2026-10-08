# Sistema de Gestión de Carreras Universitarias

Proyecto desarrollado con Django y MariaDB para gestionar carreras universitarias mediante un sistema CRUD.

## Tecnologías utilizadas

- Python 3.13
- Django 5.0.14
- MariaDB 10.4
- XAMPP
- MySQLclient 2.2.8
- Bootstrap 5.3.3
- Git y GitHub

## Funcionalidades

El sistema permite:

- Registrar carreras universitarias.
- Listar carreras registradas.
- Editar carreras.
- Eliminar carreras.
- Validar los datos ingresados.
- Conectarse a una base de datos MariaDB.
- Iniciar sesión en la web mediante usuario y contraseña.
- Generar tokens de autenticación para clientes API.
- Consultar y administrar carreras mediante una API REST protegida.

## API REST

La web y la API se ejecutan juntas con `python manage.py runserver`.
Antes del primer inicio se deben instalar las dependencias y aplicar las
migraciones:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Para obtener un token, enviar las credenciales de un usuario de Django:

```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"tu-clave"}'
```

La respuesta incluye `token` y `usuario`. El token se envía en las siguientes
peticiones usando el encabezado `Authorization: Token <token>`:

```bash
curl http://127.0.0.1:8000/api/carreras/ \
  -H "Authorization: Token <token>"
```

Endpoints disponibles:

- `POST /api/login/`: genera o recupera el token del usuario.
- `GET, POST /api/carreras/`: lista o crea carreras.
- `GET, PUT, PATCH, DELETE /api/carreras/<id>/`: consulta, modifica o elimina
  una carrera.

Para ejecutar las pruebas sin depender de una instancia local de MariaDB:

```bash
python manage.py test --settings=universidad.test_settings
```

En un despliegue real, la API debe publicarse exclusivamente mediante HTTPS
para proteger las credenciales y los tokens durante su transmisión.

## Datos de una carrera

Cada carrera contiene:

- Nombre
- Código
- Facultad
- Duración
- Modalidad
- Jornada
- Arancel
- Cupos
- Correo electrónico

## Estructura del proyecto

```text
universidad_backend/
├── carreras/
│   ├── migrations/
│   ├── templates/
│   │   └── carreras/
│   │       ├── inicio.html
│   │       ├── lista.html
│   │       ├── crear.html
│   │       ├── editar.html
│   │       └── eliminar.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── universidad/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── .gitignore
