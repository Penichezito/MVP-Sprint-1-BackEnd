from pydantic import BaseModel
from typing import Optional, List
from model.jogo import Game

from schemas import ComentarioSchema


class GameSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Zelda: Ocarina of Time"
    genero: str = "RPG"
    plataforma: str = "Nintendo 64"
    ano: int = 1998


class GameBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Zelda Ocarina of Time" 


class ListagemGamesSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    jogos:List[GameSchema]

def apresenta_jogos(jogos: List[Game]):
    """REtorna uma apresentação do jogos seguindo schema em 
    GameViewSchema
    """  
    result=[]
    for jogo in jogos:
        result.append({
            "nome": jogo.nome,      
            "genero": jogo.genero,
            "plataforma": jogo.plataforma,  
            "ano": jogo.ano,
        })

    return {"jogos": result} 


class GameViewSchema(BaseModel):
    """Define como um jogo será retornado: jogo + comentários.
    """
    id: int = 1
    nome: str = "Zelda Ocarina of Time"
    genero: str = "RPG"
    plataforma: str = "Nintendo 64"
    ano: Optional[int] = 1998
    total_comentarios: int = 1
    comentarios: List[ComentarioSchema]


class GameDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_jogo(jogo: Game):
    """Retorna uma representação do jogo seguindo schema definido em 
    GameViewSchema
    """
    return {
      "id": jogo.id,
      "nome": jogo.nome,
      "genero": jogo.genero,
      "plataforma": jogo.plataforma,
      "ano": jogo.ano,
      "total_comentarios": len(jogo.comentarios), 
      "comentarios": [{"texto": c.texto} for c in jogo.comentarios]
    }       






