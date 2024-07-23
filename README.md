# Aula básica sobre rotas, views e links no Django

### 1. Rotas (URLs)

Em Django, as rotas são configuradas no arquivo `urls.py`. Elas mapeiam URLs específicas para views específicas.

Vamos criar um projeto simples com um app chamado `myapp`.

**Estrutura do projeto:**

```
rotas_django/
    manage.py
    core/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    myapp/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        urls.py
        templates/
            myapp/
                index.html
                about.html
```

**core/urls.py:**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Inclui as URLs do app "myapp"
]
```

**myapp/urls.py:**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a página inicial
    path('about/', views.about, name='about'),  # Rota para a página "About"
]
```

### 2. Views

As views são funções ou classes que processam requisições HTTP e retornam respostas HTTP.

**myapp/views.py:**

```python
from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')  # Renderiza o template "index.html"

def about(request):
    return render(request, 'myapp/about.html')  # Renderiza o template "about.html"
```

### 3. Templates

Os templates são arquivos HTML que definem como o conteúdo será exibido.

**myapp/templates/myapp/index.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h1>Welcome to the Home Page</h1>
    <p>This is the home page.</p>
    <a href="{% url 'about' %}">About</a>  <!-- Link para a página "About" -->
</body>
</html>
```

**myapp/templates/myapp/about.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>About Page</title>
</head>
<body>
    <h1>About Us</h1>
    <p>This is the about page.</p>
    <a href="{% url 'index' %}">Home</a>  <!-- Link para a página inicial -->
</body>
</html>
```

### Explicação

1. **Rotas (URLs)**:
   - No arquivo `myproject/urls.py`, estamos incluindo as URLs definidas no app `myapp` usando `include('myapp.urls')`.
   - No arquivo `myapp/urls.py`, definimos duas rotas: uma para a página inicial (`path('', views.index, name='index')`) e outra para a página "About" (`path('about/', views.about, name='about')`).

2. **Views**:
   - No arquivo `myapp/views.py`, criamos duas funções de view: `index` e `about`. Cada uma renderiza um template HTML correspondente (`index.html` e `about.html`).

3. **Templates**:
   - No diretório `myapp/templates/myapp/`, criamos dois arquivos HTML: `index.html` e `about.html`.
   - Em `index.html`, incluímos um link para a página "About" usando `{% url 'about' %}`.
   - Em `about.html`, incluímos um link para a página inicial usando `{% url 'index' %}`.

### Configurações Adicionais

Para garantir que tudo funcione corretamente, verifique se `myapp` está incluído no `INSTALLED_APPS` em `myproject/settings.py`:

```python
INSTALLED_APPS = [
    # Outros apps...
    'myapp',
]
```

### Executando o Projeto

1. Acesse o diretório do seu projeto:
   ```bash
   cd myproject
   ```

2. Crie e aplique as migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Crie um superusuário para acessar a interface administrativa (opcional):
   ```bash
   python manage.py createsuperuser
   ```

4. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

Agora, acesse `http://127.0.0.1:8000/` no seu navegador para ver a página inicial, e clique no link "About" para navegar para a página "About".

Essa é uma introdução básica sobre rotas, views e links em Django.
