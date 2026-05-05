import sqlite3
from pathlib import Path
from typing import Optional

DB=Path(__file__).resolve().parent.joinpath('database.db')

def connect():
    conn=sqlite3.connect(DB)
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        create table if not exists loan_application(
        application_id text primary key,
        customer_id text not null,
        property_value real not null,
        existing_mortgage real not null,
        loan_amount REAL NOT NULL,
        total_debt_after_loan REAL NOT NULL,
        available_equity REAL NOT NULL,
        ltv REAL NOT NULL,
        risk_level TEXT NOT NULL,
        decision TEXT NOT NULL,
        status TEXT NOT NULL,
        created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

def save_application(application_info:dict)->None:
    conn=connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        insert into loan_application(
        application_id,
        customer_id,
        property_value,
        existing_mortgage,
        loan_amount,
        total_debt_after_loan,
        available_equity,
        ltv,
        risk_level,
        decision,
        status,
        created_at
    )
    values(?,?,?,?,?,?,?,?,?,?,?,?)  
        """,(
            application_info['application_id'],
            application_info['customer_id'],
            application_info['property_value'],
            application_info['existing_mortgage'],
            application_info['loan_amount'],
            application_info['total_debt_after_loan'],
            application_info['available_equity'],
            application_info['ltv'],
            application_info['risk_level'],
            application_info['decision'],
            application_info['status'],
            application_info['created_at'],
        )
    )
    conn.commit()
    conn.close()

def get_application(application_id:str)-> Optional[dict]:
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    select * from 
    loan_application
    where application_id=?
    """,(application_id,))
    row=cursor.fetchone()
    conn.close()

    if row is None:
        return None
    return dict(row)

def list_application(limit:int)->list:
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    select * 
    from loan_application
    limit ?""",(limit,))
    rows=cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]

def update_application(
        application_id:str,
        status:str,
        decision:Optional[str]=None)->int:

    conn = connect()
    cursor = conn.cursor()

    if decision is None:
        cursor.execute("""
        update loan_application
        set status=?,
        where application_id=?,
        """,(status,application_id))
    else:
        cursor.execute("""
        update loan_application
        set status=?,decision=?
        where application_id=?
        """,(status,decision,application_id))

    conn.commit()
    update_row=cursor.rowcount()
    conn.close()
    return update_row

def delete_application(application_id:str)->None:
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    delete from loan_application
    where application_id=?
    """,(application_id,))

    delete_row=cursor.rowcount
    conn.commit()
    conn.close()
    return delete_row




