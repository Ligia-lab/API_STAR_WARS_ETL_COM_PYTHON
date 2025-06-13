
# 🛠️ API\_STAR\_WARS\_ETL\_COM\_PYTHON

Implementação de um pipeline ETL (Extract, Transform, Load) em Python que consome dados da API de Star Wars (SWAPI), transforma essas informações e as armazena localmente.

## 📚 Conteúdo

* `.gitignore` — lista de arquivos/pastas a serem ignorados pelo Git.
* `request_sw_api.py` — módulo responsável por extrair dados via solicitações HTTP à SWAPI.
* `sw_api.py` — módulo que processa, transforma e armazena os dados coletados.

## 🚀 Funcionalidades

1. **Extração**: coleta dados sobre *personagens*, *filmes*, *planetas*, etc. da SWAPI.
2. **Transformação**: limpa e estrutura os dados (conversões de tipo, normalização de nomes, tratamento de valores nulos e listas).
3. **Load**: salva os resultados em arquivos JSON/CSV no disco local, ou prepara para envio a um banco de dados.

## 📦 Requisitos

* Python ≥ 3.7
* Dependências disponíveis no `requirements.txt` (se houver), como:

  ```text
  requests
  pandas
  ```

## ⚙️ Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Ligia-lab/API_STAR_WARS_ETL_COM_PYTHON.git
   cd API_STAR_WARS_ETL_COM_PYTHON
   ```
2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```
3. Instale os pacotes:

   ```bash
   pip install -r requirements.txt
   ```

## 🧩 Uso

### Executando a extração de dados

```bash
python request_sw_api.py
```

### Processando e salvando os dados

```bash
python sw_api.py
```

Combine ambos em uma execução única com:

```bash
python sw_api.py --run_all
```

*Adapte a parte `--run_all` conforme a implementação real.*

## 📁 Estrutura dos dados gerados

* Pasta `output/`

  * `characters.json` — dados de personagens
  * `films.csv` — dados formatados de filmes
  * `planets.json` — dados de planetas
* Pastas adicionais conforme entidades da SWAPI

## 🧪 Testes

* [ ] Adicionar testes unitários com `pytest` na pasta `tests/`
* [ ] Testar extração, transformação e carga separadamente


## 🌟 Contribuições

1. Fork do projeto
2. Crie uma branch para as alterações (`feat/nova-funcionalidade`, `fix/extrato`)
3. Commit com descrição clara
4. Envie pull request


