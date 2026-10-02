from flask import flash
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import Time, db_session

def select_todos_times():
    times_sql = select(Time)
    times = db_session.execute(times_sql).scalars().all()
    return times

def salvar_times(nome, turma, responsavel):
    try:
        time_novo = Time(nome=nome, turma=turma, responsavel=responsavel)
        db_session.add(time_novo)
        db_session.commit()
        flash(message='Time cadastrado', category="success")
    except SQLAlchemyError as e:
        db_session.rollback()
        flash(message='Ocorreu um erro, tente novamente', category="error")
        print(f"Erro: {e}")
    except Exception as e:
        db_session.rollback()
        flash(message='Ocorreu um erro, tente novamente', category="error")
        print(f"Erro: {e}")