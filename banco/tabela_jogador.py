from sqlalchemy import select
from database import Jogador, db_session

def select_todos_jogadores():
    jogadores_sql = select(Jogador)
    jogadores = db_session.execute(jogadores_sql).scalars().all()
    return jogadores

def salvar_jogadores(nome, numero_camisa, posicao, time_id):
    try:
        jogadores_novos = Jogador(nome=nome, numero_camisa=int(numero_camisa), posicao=posicao, time_id=int(time_id))
        db_session.add(jogadores_novos)
        db_session.commit()
        flash(message='Jogador cadastrado', category="success")
    except SQLAlchemyError as e:
        db_session.rollback()
        flash(message='Ocorreu um erro, tente novamente', category="error")
        print(f"Erro: {e}")
    except Exception as e:
        db_session.rollback()
        flash(message='Ocorreu um erro, tente novamente', category="error")
        print(f"Erro: {e}")
