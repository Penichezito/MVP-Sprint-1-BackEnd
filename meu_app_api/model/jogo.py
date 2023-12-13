from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Game(Base):
    __tablename__ = 'jogo'

    id = Column("pk_jogo", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    genero = Column(String(50))
    plataforma = Column(String(50))
    ano = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o jogo e o comentário.
    # Essa relação é implicita, não está salva na tabela 'jogo',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, nome:str, genero:str, plataforma:str, ano:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Jogo na lista
        Argumentos:
            nome: nome do jogo
            gênero:diz a qual genero pertece aquele jogo. ex: Rpg, Açaõ, Aventura etc
            plataforma: quais "locais"(plataformas) o jogo pode ser jogado. ex: PC, Nintendo 64, Playstation 5 etc
            ano: ano de lançamento do jogo 
            data_insercao: data de quando o jogo foi inserido à base
        """
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano

                # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao


    def adiciona_comentario(self, comentario:Comentario):
        """Adiciona um novo comentário ao Jogo
        """
        self.comentarios.append(comentario)