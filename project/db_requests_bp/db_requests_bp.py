from datetime import date

from flask import Blueprint, render_template, request, url_for
from project.launch import sql_provider, DB_CONFIG
from project.db_processing.db_access import DBConnector

service = Blueprint('requests', __name__, template_folder='templates')


@service.route('/')
def blueprint_interface_menu():
    return render_template('requests_main.html')


@service.route('/youngest_patient')
def blueprint_youngets_patient():
    sql_req = tuple()
    with DBConnector(DB_CONFIG) as cursor:
        if cursor is None:
            raise ValueError('cursor')
        cursor.execute(sql_provider.get('youngest_patient.sql'))
        sql_req = cursor.fetchall()
        sql_req = {
            'pat_id': sql_req[0][0],
            'surname': sql_req[0][1],
            'name': sql_req[0][2],
            'second_name': sql_req[0][3],
            'pasport': sql_req[0][4],
            'address': sql_req[0][5],
            'therapist': sql_req[0][6],
            'birthday': str(sql_req[0][7])
        }

    return render_template('youngest_patient.html', **sql_req)


@service.route('/last_receipt')
def blueprint_last_receipt():
    sql_req = tuple()
    with DBConnector(DB_CONFIG) as cursor:
        if cursor is None:
            raise ValueError('cursor')
        cursor.execute(sql_provider.get('most_late_receipt_doctor.sql'))
        sql_req = cursor.fetchall()
        sql_req = {
            'doc_id': sql_req[0][0],
            'surname': sql_req[0][1],
            'name': sql_req[0][2],
            'second_name': sql_req[0][3],
            'specialty': sql_req[0][4],
            'corpus_no': sql_req[0][5],
            'date_receipt': str(sql_req[0][6]),
            'date_dismissal': str(sql_req[0][7]),
        }

    return render_template('last_receipt_doctor.html', **sql_req)


@service.route('/report_doctor')
def blueprint_report_doctor():
    report_doctor = request.args.get('doctor_select', None)

    with DBConnector(DB_CONFIG) as cursor:
        if cursor is None:
            raise ValueError('cursor')
        _SQL = 'SELECT surname FROM Doctors;'
        cursor.execute(_SQL)
        notes = cursor.fetchall()
    notes = {note[0] for note in notes}

    with DBConnector(DB_CONFIG) as cursor:
        if cursor is None:
            raise ValueError('cursor')
        if report_doctor is None:
            sql_req = {'doctor': None, 'notes': tuple()}
        else:
            cursor.execute(sql_provider.get('report_doctor_xxx.sql', doctor_name=report_doctor))
            sql_req = {'doctor': report_doctor, 'notes': cursor.fetchall()}

    return render_template('report_doctor.html', doctors=tuple(notes), report=sql_req)


months = [
    {'month': 'Январь', 'num': 1},
    {'month': 'Февраль', 'num': 2},
    {'month': 'Март', 'num': 3},
    {'month': 'Апрель', 'num': 4},
    {'month': 'Май', 'num': 5},
    {'month': 'Июнь', 'num': 6},
    {'month': 'Июль', 'num': 7},
    {'month': 'Август', 'num': 8},
    {'month': 'Сентябрь', 'num': 9},
    {'month': 'Октябрь', 'num': 10},
    {'month': 'Ноябрь', 'num': 11},
    {'month': 'Декабрь', 'num': 12},
]

years = range(1970, 2022)


@service.route('/notes_changed')
def blueprint_notes_changed():
    report_doctor = request.args.get('doctor', None)
    year = request.args.get('year', None)
    month = request.args.get('month', None)

    with DBConnector(DB_CONFIG) as cursor:
        if cursor is None:
            raise ValueError('cursor')
        _SQL = 'SELECT surname FROM Doctors;'
        cursor.execute(_SQL)
        notes = cursor.fetchall()
    notes = {note[0] for note in notes}

    with DBConnector(DB_CONFIG) as cursor:
        if cursor is None:
            raise ValueError('cursor')
        if report_doctor is None:
            sql_req = None
        else:
            cursor.execute(sql_provider.get('notes_in_xxx_year_by_xxx_doc.sql', doctor_name=report_doctor, year=year, month=month))
            sql_req = cursor.fetchall()
        print(sql_req)

    return render_template('changed_notes.html', doctors=tuple(notes), months=months, years=years, changed_notes=sql_req)
