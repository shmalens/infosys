SELECT Patient.surname, History.diagnose_in, History.diagnose_out, datediff(History.date_descharge, History.date_receipt)
FROM Patient
LEFT JOIN Doctors ON Patient.therapist = Doctors.doc_id
LEFT JOIN History ON Patient.pat_id = History.patient
WHERE History.hist_id IS NOT NULL AND Doctors.surname = '$doctor_name'
;