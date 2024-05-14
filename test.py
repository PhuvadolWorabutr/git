import datetime

class DrivingLicenseSystem:
    def __init__(self):
        self.exam_records = []

    # A
    def record_exam_result(self, first_name, last_name, physical_exam, theory_exam, practical_exam):
        timestamp = datetime.datetime.now()
        self.exam_records.append({'first_name': first_name, 'last_name': last_name, 'physical_exam': physical_exam, 'theory_exam': theory_exam, 'practical_exam': practical_exam, 'timestamp': timestamp})

    # B
    def update_exam_result(self, index, physical_exam=None, theory_exam=None, practical_exam=None):
        if physical_exam is not None:
            self.exam_records[index]['physical_exam'] = physical_exam
        if theory_exam is not None:
            self.exam_records[index]['theory_exam'] = theory_exam
        if practical_exam is not None:
            self.exam_records[index]['practical_exam'] = practical_exam

    def delete_exam_record(self, index):
        del self.exam_records[index]

    # C
    def get_exam_processes(self):
        return ['physical', 'theory', 'practical']
    

    # D
    def evaluate_physical_exam(self, results):
        passed_steps = sum(1 for result in results.values() if result == 'pass')
        if passed_steps >= 3:
            return 'pass'
        else:
            return 'fail'

    # E
    def evaluate_theory_exam(self, results):
        total_score = sum(results.values())
        if total_score > 80:
            return 'pass'
        else:
            return 'fail'

    # F
    def record_practical_exam_result(self, result):
        if result == 'pass':
            return 'pass'
        else:
            return 'fail'

    # G
    def evaluate_driving_license_test(self, results):
        if 'fail' in results.values():
            return 'ไม่ผ่านการทดสอบ'
        elif len(results) < 3:
            return 'รอพิจารณา'
        else:
            return 'ผ่านการทดสอบ'

    def generate_report(self):
        pass_names = []
        fail_names = []
        pass_count = 0
        fail_count = 0
        for record in self.exam_records:
            test_results = {'physical': record['physical_exam'], 'theory': record['theory_exam'], 'practical': record['practical_exam']}
            if self.evaluate_driving_license_test(test_results) == 'ผ่านการทดสอบ':
                pass_names.append(f"{record['first_name']} {record['last_name']}")
                pass_count += 1
            else:
                fail_names.append(f"{record['first_name']} {record['last_name']}")
                fail_count += 1

        print("รายงานการทดสอบใบอนุญาตขับขี่:")
        print("ผู้ผ่านการทดสอบ:")
        for name in pass_names:
            print(name)
        print(f"จำนวน: {pass_count}")

        print("\nผู้ไม่ผ่านการทดสอบ:")
        for name in fail_names:
            print(name)
        print(f"จำนวน: {fail_count}")



driving_license_system = DrivingLicenseSystem()

driving_license_system.record_exam_result("John", "Doe", 85, 90, 88)


print("____A____")
for record in driving_license_system.exam_records:
    print("Name:", record['first_name'], record['last_name'])
    print("Physical Exam:", record['physical_exam'])
    print("Theory Exam:", record['theory_exam'])
    print("Practical Exam:", record['practical_exam'])
    print("Timestamp:", record['timestamp'])
    print()

driving_license_system.update_exam_result(0, physical_exam=90, theory_exam=95, practical_exam=92)

print("\n____B (After updating exam record)____")
for record in driving_license_system.exam_records:
    print("Name:", record['first_name'], record['last_name'])
    print("Physical Exam:", record['physical_exam'])
    print("Theory Exam:", record['theory_exam'])
    print("Practical Exam:", record['practical_exam'])
    print("Timestamp:", record['timestamp'])
    print()

driving_license_system.delete_exam_record(0)

print("\n____B (After deleting exam record)____")
for record in driving_license_system.exam_records:
    print("Name:", record['first_name'], record['last_name'])
    print("Physical Exam:", record['physical_exam'])
    print("Theory Exam:", record['theory_exam'])
    print("Practical Exam:", record['practical_exam'])
    print("Timestamp:", record['timestamp'])
    print()

print("\n____C____")
print("Exam Processes:", driving_license_system.get_exam_processes())

# Example usage for D
print("\n____D____")
results = {'step1': 'pass', 'step2': 'pass', 'step3': 'fail', 'step4': 'pass'}
evaluation = driving_license_system.evaluate_physical_exam(results)
print("Physical Exam Evaluation:", evaluation)

# Example usage for E
print("\n____E____")
results = {'question1': 85, 'question2': 90, 'question3': 88}
evaluation = driving_license_system.evaluate_theory_exam(results)
print("Theory Exam Evaluation:", evaluation)


# Example usage for F
print("\n____F____")
practical_result = 'pass'
record_result = driving_license_system.record_practical_exam_result(practical_result)
print("Practical Exam Result:", record_result)

# Example usage for G
print("\n____G____")
results = {'physical': 'pass', 'theory': 'pass', 'practical': 'fail'}
test_evaluation = driving_license_system.evaluate_driving_license_test(results)
print("Driving License Test Evaluation:", test_evaluation)


# สร้างระบบ
driving_license_system = DrivingLicenseSystem()

# บันทึกข้อมูลทดสอบอย่างน้อย 20 รายการ
driving_license_system.record_exam_result("John", "Doe", "pass", 85, "pass")
driving_license_system.record_exam_result("Jane", "Doe", "fail", 70, "pass")
driving_license_system.record_exam_result("Alice", "Smith", "pass", 90, "fail")
driving_license_system.record_exam_result("Bob", "Johnson", "fail", 75, "fail")
driving_license_system.record_exam_result("Emily", "Brown", "pass", 80, "pass")
driving_license_system.record_exam_result("David", "Lee", "pass", 85, "pass")
driving_license_system.record_exam_result("Emma", "Taylor", "fail", 65, "fail")
driving_license_system.record_exam_result("Michael", "Wilson", "pass", 95, "pass")
driving_license_system.record_exam_result("Olivia", "Martinez", "pass", 85, "fail")
driving_license_system.record_exam_result("William", "Davis", "fail", 75, "fail")
driving_license_system.record_exam_result("Sophia", "Rodriguez", "pass", 90, "pass")
driving_license_system.record_exam_result("James", "Garcia", "fail", 70, "fail")
driving_license_system.record_exam_result("Ava", "Lopez", "pass", 85, "pass")
driving_license_system.record_exam_result("Logan", "Hernandez", "pass", 80, "fail")
driving_license_system.record_exam_result("Isabella", "Gonzalez", "fail", 65, "fail")
driving_license_system.record_exam_result("Benjamin", "Perez", "pass", 95, "pass")
driving_license_system.record_exam_result("Mia", "Sanchez", "pass", 85, "fail")
driving_license_system.record_exam_result("Ethan", "Ramirez", "fail", 75, "fail")
driving_license_system.record_exam_result("Charlotte", "Torres", "pass", 60, "pass")
driving_license_system.record_exam_result("Alexander", "Flores", "fail", 70, "fail")

# Generate report
driving_license_system.generate_report()
