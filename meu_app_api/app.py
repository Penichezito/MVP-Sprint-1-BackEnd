from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Game, Comentario
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API Lista de Jogos", version="1.0.0")
app = OpenAPI(__name__, info=info)

#Definição das tags para documentação
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou Rapidoc")
jogo_tag = Tag(name= "Jogo",description="Adição, visualização e remoção de itend a base")
comentario_tag= Tag(name="Comentario", description="Adição de um comentario aos itens cadastrados na base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para openapi para escolha do tipo de documentação
    """
    return redirect('/openapi')



@app.post('/jogo', tags=[jogo_tag], 
          responses={"200": GameViewSchema, "409": ErrorSchema, "400": ErrorSchema})

def add_jogo(form: GameSchema):
    """Adiciona um novo item a base de dados
    
    Retorna uma representação dos jogos e comentarios associados
    """
    jogo = Game(
        nome = form.nome,
        genero = form.genero,
        plataforma = form.plataforma,
        ano = form.ano)
    logger.debug(f"Adicionando nome do jogo: '{jogo.nome}'")
    
    try:
        # criando conexão com a base
        session = Session()
        # adicionando jogo
        session.add(jogo)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado jogo de nome: '{jogo.nome}'")
        return apresenta_jogo(jogo), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Jogo de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar jogo '{jogo.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar jogo '{jogo.nome}', {error_msg}")
        return {"mesage": error_msg}, 400
    
@app.get('/jogos', tags=[jogo_tag], 
         responses={"200": ListagemGamesSchema, "404": ErrorSchema})
def get_jogos():
    """Faz a busca po todos os jogos cadastrados

    Retorna uma representação da listagem de jogos.
    """
    logger.debug(f"Coletando jogos")
    #criando conexão com a base
    session = Session()
    #fazendo a busca
    jogos = session.query(Game).all()

    if not jogos:
        #se não houver jogos cadastrados
        return{"jogos": []}, 200
    else:
        logger.debug(f"%d Jogos encontrados" % len(jogos))
        #retorna representação de jogos
        print(jogos)
        return apresenta_jogos(jogos), 200
    


@app.get('/jogo', tags=[jogo_tag], 
         responses={"200": GameViewSchema, "404": ErrorSchema})

def get_jogo(query: GameBuscaSchema):
    """Faz a busca por um Jogo a partir do id do jogo

    Retorna a representação dos jogos e comentarios associados
    """
    jogo_id = query.id
    logger.debug(f"Coletando dados sobre o jogo #{jogo_id}")
      # criando conexão com a base
    session = Session()
    # fazendo a busca
    jogo = session.query(Game).filter(Game.id == jogo_id).first()

    if not jogo:
        # se o jogo não foi encontrado
        error_msg = "Jogo não encontrado na base :/"
        logger.warning(f"Erro ao buscar jogo '{jogo_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Jogo econtrado: '{jogo.nome}'")
        # retorna a representação de jogo
        return apresenta_jogo(jogo), 200
    


@app.delete('/jogo', tags=[jogo_tag],
            responses={"200": GameDelSchema, "404": ErrorSchema})
def del_jogo(query: GameBuscaSchema):
    """Deleta um Jogo a partir do nome de jogo informado

    Retorna uma mensagem de confirmação da remoção.
    """
    jogo_nome = unquote(unquote(query.nome))
    print(jogo_nome)
    logger.debug(f"Deletando dados sobre jogo #{jogo_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Game).filter(Game.nome == jogo_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado jogo #{jogo_nome}")
        return {"mesage": "Jogo removido", "id": jogo_nome}
    else:
        # se o jogo não foi encontrado
        error_msg = "Jogo não encontrado na base :/"
        logger.warning(f"Erro ao deletar jogo #'{jogo_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.post('/cometario', tags=[comentario_tag],
          responses={"200": GameViewSchema, "404": ErrorSchema})
def add_comentario(form: ComentarioSchema):
    """Adiciona de um novo comentário à um jogo cadastrado na base identificado pelo id

    Retorna uma representação dos jogos e comentários associados.
    """
    jogo_id  = form.jogo_id
    logger.debug(f"Adicionando comentários ao jogo #{jogo_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo jogo
    jogo = session.query(Game).filter(Game.id == jogo_id).first()

    if not jogo:
        # se jogo não encontrado
        error_msg = "jogo não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao jogo '{jogo_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    # criando o comentário
    texto = form.texto
    comentario = Comentario(texto)

    # adicionando o comentário ao jogo
    jogo.adiciona_comentario(comentario)
    session.commit()

    logger.debug(f"Adicionado comentário ao jogo #{jogo_id}")

    # retorna a representação de jogo
    return apresenta_jogo(jogo), 200


    








      




     


