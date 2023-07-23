# M5 - Pet Kare
## Desccrição
Configuração básica do projeto:

Crie um novo projeto Python e configure um ambiente virtual (venv) para isolar as dependências do projeto.
Defina um arquivo .gitignore para evitar que arquivos necessários sejam versionados pelo Git.
Crie um arquivo requirements.txt para listar todas as dependências do projeto.
Diagrama de Entidade e Relacionamento (DER):

Crie um diagrama de entidade e relacionamento para modelar a estrutura de dados da aplicação.
Identifique como entidades envolvidas, como animais de estimação, grupos e características, e estabeleça os relacionamentos entre elas.
Modelagem do Banco de Dados:

Com base no DER, crie os modelos de banco de dados usando um framework de ORM (Object-Relational Mapping) como o Django ORM ou SQLAlchemy (no caso de usar Flask).
Serializadores:

Crie serializadores para validar a entrada e saída de dados para as entidades animais de estimação, grupos e características. Isso garante que os dados enviados e recebidos pela API estejam em um formato correto.
Visualizações (Rotas):

Implemente as views (rotas) para realizar as operações solicitadas:
Rota de criação de pet (POST): Para cadastrar novos pets no sistema.
Rota de listagem de pets (GET): Para listar todos os pets cadastrados.
Rota de filtragem de pet (GET): Para buscar informações de um pet específico com base no seu pet_id.
Rota de atualização de pet (PATCH): Para atualizar informações de um pet específico.
Rota de exclusão de animal de estimação (DELETE): Para excluir um animal de estimação do sistema.
Relacionamentos e filtros:

Implemente os relacionamentos entre as mesas de animais de estimação, grupos e recursos, permitindo que você obtenha informações de três mesas ao mesmo tempo, quando necessário.
Implemente a funcionalidade de filtragem para a listagem de animais de estimação, permitindo que o usuário aplique filtros específicos para encontrar animais de estimação com base em determinadas características.
Tratamento de excluídos:

Implemente tratamento de recompensa para as rotas de criação, atualização, filtragem e exclusão, garantindo que a API responda de forma adequada e amigável em caso de erros ou situações inesperadas.
Testes:

O projeto teve 22 testes e consegui passar em todos

Documente uma API para que outros desenvolvedores possam entender como utilizá-la corretamente.
## Como rodar os testes localmente

- Verifique se os pacotes pytest e/ou pytest-testdox estão instalados globalmente em seu sistema:

```shell
pip list
```

- Caso seja listado o pytest e/ou pytest-testdox e/ou pytest-django em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest pytest-testdox -y
```

<hr>

## Próximos passos:

### 1 Crie seu ambiente virtual:

```shell
python -m venv venv
```

### 2 Ative seu venv:

```shell
# linux:
source venv/bin/activate

# windows (powershell):
.\venv\Scripts\activate

# windows (git bash):
source venv/Scripts/activate
```

### 3 Instalar o pacote <strong>pytest-testdox</strong>:

```shell
pip install pytest-testdox pytest-django
```

### 4 Rodar os testes referentes a cada tarefa isoladamente:

Exemplo:

- Tarefa 1

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/
```

- Tarefa 2

```shell
pytest --testdox -vvs tests/tarefas/tarefa_2/
```

- Tarefa 3

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/
```

Você também pode rodar cada método de teste isoladamente seguindo uma substring, adicionando a flag `-k` seguido da substring a ser encontrada
(atenção, se o pytest achar multiplos métodos que contenham a mesma substring em seu nome, ele executará todos):

```shell
pytest --testdox -vvsk test_can_not_create_pet_when_missing_keys
```

<hr>

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

Exemplo: executar somente "test_can_get_product_by_id".

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/test_get_product_by_id.py::TestGetProductById::test_can_get_product_by_id
```
