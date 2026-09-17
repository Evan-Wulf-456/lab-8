# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException


def compute_BMI(height: float, weight: float) -> float:
    """
    compute body-mass-index:  weight / (mass**2)
    :param height: height in meters
    :param weight: weight in kg
    :return: BMI in kg/m**2
    """
    return weight / (height ** 2)
    


def parse_row(row: str) -> list:
    """
    Accepts a single row (string) read from the data file.
    Splits it into a list of individual values, cast to numeric datatypes where appropriate.
    :param row: the string row read from the file
    :return: the parsed row, as a list
    """
    values = row.strip() .split(",") 
    try:
        if values[0]=="" or values[1]=="" or values[2]=="" or values[3]=="" or values[4]=="":
                    raise MissingValueException()
        Date=values[1]
        Exam_ID=int(values[0])
        height=float(values[4])

        if height > 3:
            raise MeasurementUnitException()

        weight=float(values[3])
        Patient_name=str(values[2])
        
        
    except (ValueError, IndexError):
        raise TextFormatException(f"Error parsing row: {row}")
        
    
    return [Exam_ID, Date, Patient_name, weight, height]
    


def main():
    input_file= open("data.csv", "r")
    output_file= open("bmioutput.csv", "w")
    output_file.write("Exam ID,BMI\n")
    input_file.readline()
    for row in input_file:
        try:
            parsed_row=parse_row(row)
            height=parsed_row[4]
            weight=parsed_row[3]
            BMI=compute_BMI(height,weight)
            output_file.write(f"{parsed_row[0]},{BMI}\n")
        except TextFormatException:
            exam_id = row.strip().split(",")[0]
            print(f"Error parsing row: {exam_id}")
        except MissingValueException:
            exam_id = row.strip().split(",")[0]
            print(f"Missing value in row: {exam_id}")
        except MeasurementUnitException:
            exam_id = row.strip().split(",")[0]
            print(f"Invalid measurement unit in row: {exam_id}")

    input_file.close()
    output_file.close()

main()