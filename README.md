# Guia Passo a Passo: Como Rodar uma Aplicação Django

Abaixo estão os passos necessários para iniciar ou rodar um projeto Django, com todos os comandos detalhados.

---

## **1. Preparar o Ambiente**

### **a. Criar a pasta do projeto**
Se você está iniciando um projeto Django:
```
mkdir nome_do_projeto
cd nome_do_projeto
```

Se o projeto já existe, apenas navegue até o diretório onde o código está localizado:
```
cd caminho_para_o_projeto_existente
```

---

### **b. Criar e ativar um ambiente virtual**
É importante isolar as dependências do projeto em um ambiente virtual.

#### Criar o ambiente virtual:
```
python -m venv venv
```

#### Ativar o ambiente virtual:
- **Windows**:
```
venv\Scripts\activate
```
- **Linux/Mac**:
```
source venv/bin/activate
```

Você verá o nome do ambiente (`venv`) no início do terminal, indicando que ele foi ativado.

---

## **2. Instalar Django e outras dependências**
Se você está criando um projeto do zero:
```
pip install django
```

Se o projeto já existe e possui um arquivo `requirements.txt`:
```
pip install -r requirements.txt
```

> **Nota**: O arquivo `requirements.txt` geralmente contém todas as dependências necessárias para o projeto.

---

## **3. Criar ou configurar o projeto Django**

### **a. Criar um novo projeto**
Se você está começando um projeto do zero, rode:
```
django-admin startproject nome_do_projeto .
```
> O ponto (`.`) no final garante que o projeto seja criado no diretório atual, em vez de criar uma subpasta adicional.

---

### **b. Rodar um projeto existente**
Se o projeto já existe, basta garantir que as dependências estejam instaladas (veja a etapa 2) e continuar para as próximas etapas.

---

## **4. Configurar o banco de dados**
Antes de rodar o projeto, configure o banco de dados no arquivo `settings.py`. Para começar, geralmente é utilizado o SQLite (configuração padrão).

---

## **5. Rodar as migrações**
Crie as tabelas no banco de dados com o comando:
```
python manage.py migrate
```

---

## **6. Criar um superusuário (opcional)**
Se você quiser acessar o Django Admin:
```
python manage.py createsuperuser
```
Preencha o nome de usuário, e-mail (opcional) e senha.

---

## **7. Rodar o servidor**
Inicie o servidor de desenvolvimento do Django:
```
python manage.py runserver
```

- O terminal exibirá algo como:
Starting development server at http://127.0.0.1:8000/

yaml
Copiar
Editar
- Acesse a aplicação no navegador no endereço [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## **8. Outras Configurações Úteis**

### **a. Instalar novas dependências**
Se precisar adicionar mais bibliotecas, use o `pip`:
```
pip install nome_da_biblioteca
```
Para salvar a biblioteca no `requirements.txt`:
```
pip freeze > requirements.txt
```

### **b. Desativar o ambiente virtual**
Quando terminar, desative o ambiente virtual:
```
deactivate
```

---

## **Resumo dos Comandos**

1. **Criar pasta e ambiente virtual**:
```
mkdir nome_do_projeto
cd nome_do_projeto
python -m venv venv
source venv/bin/activate
```

2. **Instalar Django**:
```
pip install django
```

3. **Criar projeto**:
```
django-admin startproject nome_do_projeto .
```

4. **Rodar migrações e servidor**:
```
python manage.py migrate
python manage.py runserver
```

Agora você está pronto para trabalhar no seu projeto Django! 🚀
