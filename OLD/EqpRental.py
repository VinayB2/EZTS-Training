class Equipment_Rental_sys:
    def __init__(self):
        pass
    global equipments
    equipments = [{
        "id":1,
        "item":"football",
        "condition":"good",
        "status":"a"
    },{
        "id":2,
        "item":"bat",
        "condition":"better",
        "status":"u"
    }]

    global students
    students = [{
        "USN":"3BR21EC180",
        "name":"Vinay"
    },
    {
        "USN":"3BR21EC000",
        "name":"bot"
    }]

    # format of record
    # record = [{
    #     "id":1,
    #     "USN":"3BR21EC180",
    #     "borrow_time":"time obj need to be inserted here"
    # }]

    global records
    records=[{

    }]

    def test(self):
        print("Class looks good")

    # READ
    def get_equipments(self):
        return equipments
    def get_students(self):
        return students
    


    # CREATE, UPDATE
    def rent_eqp(self, eqp_id, student_id):
        for eqp in equipments:
            if(eqp["id"] == eqp_id):
                pass   
        record = {
            "id": eqp_id,
            "USN":student_id
        }
        self.records.append(record)

sports = Equipment_Rental_sys()
print(sports.get_students())