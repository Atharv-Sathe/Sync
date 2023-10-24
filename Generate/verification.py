import csv
# Initialize a set to store verified codes
verified_codes = set()
# Function to verify a student by code
def verify_student(student_code):
    if student_code in verified_codes:
        print("Code",student_code,"has already been used for verification.")
    else:
        with open('Output.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[4] == student_code:
                    if student_code in verified_codes:
                        print(row[1],"with Reg No.",row[2],"has already been verified.")
                        break
                    else:
                        verified_codes.add(student_code)
                        print(row[1],"with Reg No.",row[2],"is verified.")                   
'''
                else:
                     print(student_code,"Not found")
                     break
              ''' 
while True:        
  student_code = input("Enter a 4-digit code for verification or type exit to exit the program")
  if student_code=='exit':
      break
  else:
   verify_student(student_code)
