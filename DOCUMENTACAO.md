# COMANDOS DO DJANGO

1. ``pip install django`` -> Instala o Django no projeto.
2. ``django-admin startproject nome_do_projeto .`` -> Criando um novo projeto em Django.
3. ``python manage.py runserver`` -> Subindo o servidor.
4. ``python manage.py startapp nome_do_app`` -> Criando um novo app.
5. ``python manage.py migrate`` -> Realiza as migrações(ativa) do projeto. 
6. ``python manage.py createsuperuser`` -> Criar um super usuário.
7. ``python manage.py changepassword nome_usuario`` -> Altera a senha, caso você esqueça
8. ``python manage.py makemigrations`` -> Cria/gera um novo pacote de migração (Útil para novo app e alteração no BD)

# TAGS DO DJANGO HTML
> {% load static %} -> Habilita o static no arquivo. Cada template que usa ``{% static %}`` precisa ser carregado.
> {% block title %} -> Insere o título da aba. As páginas filhas trocam.
> {% block header %} -> O header público (logo + entrar). O ``base_logado.html`` troca por inteiro.
> {% block header_actions %} -> Só o botão "entrar". O ``login.html`` esvazia o bloco. 
> {% include ... %} -> Insere as mensagens e/ou blocos de código.
> {% block content %} -> O miolo da página, cada filha vai ter seu próprio <main>.

## TAGS DE ROTA
> {% url 'sistema:medico-list' %} -> Fica nos templates e se refere a uma lista de médico que está no app sistema.
> {% url 'sistema:medico-update' medico.pk %} -> Utilização no template com parâmetropara update do médico.
> {% url url_voltar %} -> url_voltar é o nome de uma variável que guarda uma lógica de retorno a página anterior.
> redirect('sistema:medico-list') -> Fica numa view e inform que quano uma ação for realizada, o usuário será redirecionado.