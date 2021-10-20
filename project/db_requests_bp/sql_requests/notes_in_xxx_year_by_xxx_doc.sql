SELECT  History.hist_id, Patient.surname FROM History
LEFT JOIN Note ON Note.history = History.hist_id
LEFT JOIN Doctors ON Note.edited_by = Doctors.doc_id
LEFT JOIN Patient ON Patient.pat_id = patient
WHERE note_id IS NOT NULL AND Doctors.surname = '$doctor_name' AND year(Note.note_date) = '$year' AND month(Note.note_date) = '$month'
;