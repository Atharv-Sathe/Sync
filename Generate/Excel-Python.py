import pandas as pd , csv ,random,os,qrcode

excel_file = 'Test.xlsx'

convert= pd.read_excel(excel_file)

#Generating Random Codes
codelist=[]
def ranum():
    # Generate a random 4-digit number between 1000 and 9999 (inclusive)
    code=random.randint(1000, 9999) 
    if code not in codelist:
        codelist.append(code)
        return code
convert['Code'] = [ranum() for _ in range(len(convert))]
csv_file = 'Output.csv'
#Converting Excel to csv
convert.to_csv(csv_file, index=False)
#Printing CSV File
with open(csv_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    '''
    with open ('new_test.csv','w',newline='') as new_file:
        #fieldnames = ['SerialNo.','Reg. No.','Name','Email']
        csv_writer=csv.writer(new_file,) #fieldnames=fieldnames
        for line in csv_reader:
            csv_writer.writerow(line)
            line.append(ranum)
            '''
    for row in csv_reader:
        print(row)
#Creating Qr Codes
df = pd.read_csv(csv_file)

# Create a folder to save the QR codes
if not os.path.exists('qrcodes'):
    os.makedirs('qrcodes')

# Function to generate and save QR codes
def generate_qr_code(row):
    reg_no = row['Reg No.']
    code = row['Code']
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(code)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    qr_code_path = os.path.join('qrcodes', f'{reg_no}.png')
    img.save(qr_code_path)

# Apply the function to each row of the DataFrame
df.apply(generate_qr_code, axis=1)


             
         