volumen:
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo Farmacia Johnen</title>
    <link rel="stylesheet" href="{% static 'css/volumen.css' %}">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Catálogo Farmacia Johnen</h1>
            <p>Productos disponibles y no disponibles en stock.</p>
            <a class="back-link" href="/">Volver al inicio</a>
        </div>
        <div class="grid">
            {% for producto in productos %}
                <div class="item {% if producto.stock > 0 %}disponible{% else %}no-disponible{% endif %}">
                    <span class="tag">{{ producto.marca }}</span>
                    <h3>{{ producto.nombre }}</h3>
                    <p>Categoría: {{ producto.categoria }}</p>
                    <p>Precio: {% if producto.precios %}$ {{ producto.precios.precio }}{% else %}Por confirmar{% endif %}</p>
                    <p>Stock: {{ producto.stock }}</p>
                    <p class="estado {% if producto.stock > 0 %}ok{% else %}warning{% endif %}">{{ producto.disponible }}</p>
                </div>
            {% empty %}
                <p>No hay productos registrados.</p>
            {% endfor %}
        </div>
    </div>
</body>
</html>
resumen
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resumen Farmacia Johnen</title>
    <link rel="stylesheet" href="{% static 'css/resumen.css' %}">
</head>
<body>
    <div class="container">
        <div class="card">
            <h1>Resumen de Productos</h1>
            <div class="stat-grid">
                <div class="stat">
                    <strong>{{ total }}</strong>
                    <span>Total de productos</span>
                </div>
                <div class="stat">
                    <strong>{{ disponibles }}</strong>
                    <span>Productos disponibles</span>
                </div>
                <div class="stat alerta">
                    <strong>{{ sin_stock }}</strong>
                    <span>Productos sin stock</span>
                </div>
            </div>
            <a class="back-link" href="/">Volver a la página principal</a>
        </div>
    </div>
</body>
</html>
