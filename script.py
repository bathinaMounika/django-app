import csv

with open('results.csv', mode='w', newline='') as f:
    fwriter = csv.writer(f, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    fwriter.writerow(['student_id', 'student_name', 'exam_id', 'exam_name', 'marks', 'total_marks', 'percentage'])
f.close()
