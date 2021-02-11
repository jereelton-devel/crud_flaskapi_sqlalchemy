
# Projeto CRUD Python

> API criada em Python para executar as seguintes operações SQL: 

<br />
* Create
<br />
* Read
<br />
* Update
<br />
* Delete
<hr />

# Informações

* Para criar uma tabela, use o endpoint:

<pre>
[POST] http://127.0.0.1:5000/create/full
</pre>

* Para criar um usuario, use o endpoint:

<pre>
[POST] http://127.0.0.1:5000/create/user
Body:
    {
        "name": "Nome Sobrenome",
        "email": "email@email.com"
    }
</pre>

* Para ler varios usuarios, use o endpoint:

<pre>
[GET] http://127.0.0.1:5000/read/users/{option}
option = all, full, para listar todas os usuários
option = 1, Nome, Email, para listar todos os usuarios com base no filtro {option}, exemplo: 
    ...WHERE id LIKE '1%' OR name LIKE 'Nome%' OR email LIKE 'Email%' 
</pre>

* Para atualizar um usuario, use o endpoint:

<pre>
[GET] http://127.0.0.1:5000/read/user/{option}
option = 1, Nome, Email, para listar todos os usuarios com base no filtro {option}, exemplo: 
    ...WHERE id LIKE '1%' OR name LIKE 'Nome%' OR email LIKE 'Email%' 
</pre>

* Para ler um usuario, use o endpoint:

<pre>
[PUT] http://127.0.0.1:5000/update/user/{option}
option = id referente ao registro a ser atualizado 
</pre>

* Para deletar um usuario, use o endpoint:

<pre>
[DELETE] http://127.0.0.1:5000/delete/user/{option}
option = id referente ao registro a ser atualizado 
</pre>

* Para apagar uma tabela, use o endpoint:

<pre>
[DELETE] http://127.0.0.1:5000/delete/full
</pre>

<hr />
