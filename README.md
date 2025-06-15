# Guia Passo a Passo: Como Rodar uma Aplicação Django

Abaixo estão os passos necessários para iniciar ou rodar um projeto Django, com todos os comandos detalhados.

---

## **1. Preparar o Ambiente**

### **a. Criar a pasta do projeto**
Se você está iniciando um projeto Django:

```bash
mkdir nome_do_projeto
cd nome_do_projeto
```

Se o projeto já existe, apenas navegue até o diretório onde o código está localizado:

```bash
cd caminho_para_o_projeto_existente
```

---

### **b. Criar e ativar um ambiente virtual**
É importante isolar as dependências do projeto em um ambiente virtual.

#### Criar o ambiente virtual:

```bash
python -m venv venv
```

#### Ativar o ambiente virtual:
- **Windows**:

```powershell
venv\Scripts\activate
```

Caso dê problema ao executar no Windows, fazer Bypass nas políticas de execução:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate
```

- **Linux/Mac**:

```bash
source venv/bin/activate
```

Você verá o nome do ambiente (`venv`) no início do terminal, indicando que ele foi ativado.

---

## **2. Instalar Django e outras dependências**
Se você está criando um projeto do zero:

```bash
pip install django
```

Se o projeto já existe e possui um arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

> **Nota**: O arquivo `requirements.txt` geralmente contém todas as dependências necessárias para o projeto.

---

### **a. Verificar Versão do Django instalada**
Para verificar a versão do Django instalada, execute o comando:

```bash
django-admin --version
```

ou

```bash
python -m django --version
```

---

## **3. Criar ou configurar o projeto Django**

### **a. Criar um novo projeto**
Se você está começando um projeto do zero, rode:

```bash
django-admin startproject nome_do_projeto .
```

> O ponto (`.`) no final garante que o projeto seja criado no diretório atual, em vez de criar uma subpasta adicional.

---

### **b. Rodar um projeto existente**
Se o projeto já existe, basta garantir que as dependências estejam instaladas (veja a etapa 2) e continuar para as próximas etapas.

---

## **4. Criar um aplicativo (app)**

Use o comando abaixo dentro da pasta do projeto:

```bash
django-admin startapp <nome_do_app>
```

---

## **5. Configurar o banco de dados**
Antes de rodar o projeto, configure o banco de dados no arquivo `settings.py`. Para começar, geralmente é utilizado o SQLite (configuração padrão).

---

## **6. Rodar as migrações**

Crie as tabelas no banco de dados com os comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **7. Criar um superusuário (opcional)**
Se você quiser acessar o Django Admin:

```bash
python manage.py createsuperuser
```

Preencha o nome de usuário, e-mail (opcional) e senha.

---

## **8. Rodar o servidor**

Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

O terminal exibirá algo como:

```
Starting development server at http://127.0.0.1:8000/
```

Acesse a aplicação no navegador no endereço [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## **9. Geração de nova `SECRET_KEY` para Django**

Para gerar uma nova `SECRET_KEY` no Django, utilize um dos métodos abaixo:

### ✅ Método 1: Via shell interativo do Python

```bash
# Ative seu ambiente virtual (se aplicável)
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Acesse o interpretador Python
python
```

Dentro do interpretador Python:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())  # Copie esta chave
exit()  # Para sair
```

### ✅ Método 2: Comando único (recomendado)

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### ✅ Método 3: Usando `manage.py`

```bash
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 🔐 Onde configurar a chave?

Abra o arquivo `settings.py` do seu projeto Django e adicione a chave gerada:

```python
# settings.py
SECRET_KEY = 'sua-chave-gerada-aqui'  # Substitua pela chave copiada
```

---

## **10. Outras Configurações Úteis**

### **a. Instalar novas dependências**

Se precisar adicionar mais bibliotecas, use o `pip`:

```bash
pip install nome_da_biblioteca
```

Para salvar a biblioteca no `requirements.txt`:

```bash
pip freeze > requirements.txt
```

### **b. Desativar o ambiente virtual**

Quando terminar, desative o ambiente virtual:

```bash
deactivate
```

### **c. Alterar temporariamente a política de execução**

Para habilitar a execução de scripts apenas enquanto o terminal atual estiver aberto:

Abra o PowerShell como administrador. Clique com o botão direito no ícone do PowerShell e selecione "Executar como Administrador".

Rode o seguinte comando para permitir a execução temporária de scripts:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Tente ativar o ambiente virtual novamente:

```powershell
.\venv\Scripts\Activate
```

Os comandos juntos em uma única linha ficam:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\venv\Scripts\Activate
```

---

## **Resumo dos Comandos**

### 1. Criar pasta e ambiente virtual:

```bash
mkdir nome_do_projeto
cd nome_do_projeto
python -m venv venv
source venv/bin/activate
```

### 2. Instalar Django:

```bash
pip install django
```

### 3. Criar projeto:

```bash
django-admin startproject nome_do_projeto .
```

### 4. Rodar migrações e servidor:

```bash
python manage.py migrate
python manage.py runserver
```

Agora você está pronto para trabalhar no seu projeto Django! 🚀
