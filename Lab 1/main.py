# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException


def compute_BMI(height: float, weight: float) -> float: #calculates BMI and returns those values to be written in the computed_basal_metabolic_index file 
    

    body_mass_index = weight/(height**2)
    return body_mass_index #return the values to be used 


def parse_row(row: str) -> list: #error checks for missing strings, heights that are greater than 3 meters, 
    values = row.strip().split(",") #.strip removes the newline (\n) at the end and .split (parse) breaks the strings into a list with commas
    try: 
        exam_id = int(values[0]) #convert exam_id_number from a string into an integer; exam id starts at index 0 in the list examination_date
        Date = values[1] #convert examination date to a string in the list
        Patient_Name = values[2] #convert patient_name to a string in the list
        weight = float(values[3]) #convert weight to a floating point number in the list
        height = float(values[4]) #convert height to a floating point number in the list
    except ValueError:
        raise TextFormatException
    

    if height > 3: 
        raise MeasurementUnitException (f"Invalid height input for examination id number {values[0]}")
    return(exam_id, Date, Patient_Name, weight, height)

def main(): #main function reads files, opens files, strips new lines, splits each word into an individual list, 
    #raises value errors for weights and heights that are not floats (aka strings), prints the parsed and stripped values, raises a value exception error, writes the new BMI file, 
    #and Main calls the BMI function and receives the calculated value to write to the file
    input_file = open("data.csv", "r")         

    output_file = open("computed_basal_metabolic_index.csv", "w")  #open and read the file, #write the new calculated BMI file

    output_file.write("Examination ID, BMI\n")

    next(input_file) #move on from the exam_id_number because it apparently crashes the program

    for line in input_file: #make a for loop reading the data.csv file row-by-row

        try: #try to execute the program with the variables 

            exam_identification_number, examination_date, patient_name, weight, height = parse_row(line) #unpack the tuple into variables and then call the function  (you can't assign a function as a variable, so it has to be this way)

            print(exam_identification_number, examination_date, patient_name, weight, height) #print out the result into a list

            BMI = compute_BMI(height, weight) #call the compute_BMI function, calculate BMI and return it

            output_file.write(f"{exam_identification_number}, {BMI:.2f}\n") # write the new calculated BMI values for each examination number and output it in a newline 

        except (MissingValueException, TextFormatException, MeasurementUnitException) as entry: #tries to catch errors except the ones in the error exceptions

            print(f"Skipping the entry due an error in entry {entry}") #print the skipped entry since there was an error 

main()