from flask import Blueprint, render_template, request

from db_processing.db_access import db_get_data
from launch import sql_provider

service = Blueprint('requests', __name__, template_folder='templates')


@service.route('/')
def blueprint_interface_menu():
    return render_template('requests_main.html')


@service.route('/youngest_patient', methods=['GET', 'POST'])
def blueprint_youngets_patient():
    if request.method == 'POST':
        year = request.form.get('year')
        sql_req = db_get_data(sql_provider.get('youngest_patient.sql', year=year))
        print(sql_req)
    else:
        sql_req = db_get_data(sql_provider.get('get_all_patients.sql'))
        print(sql_req)

    return render_template('youngest_patient.html', patients=sql_req)


@service.route('/last_receipt', methods=['GET', 'POST'])
def blueprint_last_receipt():
    if request.method == 'POST':
        year = request.form.get('year')
        sql_req = db_get_data(sql_provider.get('most_late_receipt_doctor.sql', year=year))
    else:
        sql_req = db_get_data(sql_provider.get('get_all_doctors.sql'))

    print(sql_req)
    return render_template('last_receipt_doctor.html', doctors=sql_req)


@service.route('/report_doctor', methods=['GET', 'POST'])
def blueprint_report_doctor():
    if request.method == 'POST':
        report_doctor = request.form.get('doctor_select')
        sql_req = {'doctor': report_doctor,
                   'notes': db_get_data(sql_provider.get('report_doctor_xxx.sql', doctor_name=report_doctor))}
    else:
        sql_req = {'doctor': None, 'notes': tuple()}
    notes = {note[0] for note in db_get_data(sql_provider.get('get_all_doctors_surname.sql'))}
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


@service.route('/notes_changed', methods=['GET', 'POST'])
def blueprint_notes_changed():
    notes = {note[0] for note in db_get_data(sql_provider.get('get_all_doctors_surname.sql'))}
    if request.method == 'POST':
        report_doctor = request.form.get('doctor')
        year = request.form.get('year')
        month = request.form.get('month')
        sql_req = db_get_data(
            sql_provider.get('notes_in_xxx_year_by_xxx_doc.sql', doctor_name=report_doctor, year=year, month=month))
    else:
        sql_req = None

    return render_template('changed_notes.html', doctors=tuple(notes), months=months, years=years,
                           changed_notes=sql_req)
