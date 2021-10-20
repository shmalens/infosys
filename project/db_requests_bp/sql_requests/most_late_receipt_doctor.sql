SELECT * from Doctors WHERE date_receipt = (SELECT max(date_receipt) from Doctors);
