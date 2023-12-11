# MVP-Sprint-1-BackEnd
## LISTA DE JOGOS 

Lista simples para catalogar jogos visando os mais diferetens tipos de objetivos. 
Aqui você pode encontrar o Repositório do [FrontEnd]() referente ao projeto.

Back end da aplicação (API) utilizando Pyhon e Flask desenvolvida para primeiro projeto de Pós Graduação em Engenharia de Software da PUC-RIO.


Informações sobre como executar:

Será necessário ter todas as libs python listadas no requirements.txt instaladas. Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://docs.python.org/pt-br/3/library/venv.html#creating-virtual-environments).

(venv)$ pip install -r requirements.txt

Este comando instala as dependências/bibliotecas, descritas no arquivo requirements.txt.

Para executar a API basta executar:
'''
(venv)$ flask run --host 0.0.0.0 --port 5000
'''
Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte.

(env)$ flask run --host 0.0.0.0 --port 5000 --reload

Abra o http://localhost:5000/#/ no navegador para verificar o status da API em execução.



Tiago Peniche Barbosa 



