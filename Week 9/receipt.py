import csv
from datetime import datetime
from modulefinder import STORE_NAME
import modulefinder
current_date_and_time = datetime.now()


#products Indexs
PRODUCT_NUM_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
#requests Indexs
REQUEST_PRODUCT_NUM = 0
REQUEST_PRODUCT_QUAN = 1

def main():
    try:
        requests = read_dict('request.csv', REQUEST_PRODUCT_NUM)
        products = read_dict('products.csv', PRODUCT_NUM_INDEX)
        get_list(requests,products)
        
    except (FileNotFoundError, PermissionError) as Error:
        print(Error,'\nPlease choose a different file.')   
    except ValueError as ValError:
        print('Error:', ValError)
    
def get_list(dict_1,dict_2):
    num_items = 0
    subtotal = 0
    for list_key, item in dict_1.items():
        key = item[REQUEST_PRODUCT_NUM]
        quan = item[REQUEST_PRODUCT_QUAN]
        if key in dict_2:
            product = dict_2[key]
            name = product[PRODUCT_NAME_INDEX]
            price = product[PRODUCT_PRICE_INDEX]
            print(f'{name}: {quan} @ {price}')
            num_items += int(quan)
            subtotal += float(price)*int(quan)
            subtotal = round(subtotal, 2)
    salestax = round(subtotal * .06, 2)
    total = salestax + subtotal
    print('Number of Items',num_items)
    print('Subtotal',subtotal)
    print('Sales Tax',salestax)
    print('Total', total)
    print('Thank you for shopping')
    print(current_date_and_time)



        


def read_dict(filename, Index_Key):
    try:
        dictionary = {}
        with open(filename,"rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row_list in reader:
                key = row_list[Index_Key]
                if key in dictionary:
                    product = dictionary[key]
                    num = int(product[1])
                    num += int(row_list[1])
                    num = str(num)
                    row_list = [key, num]
                dictionary[key] = row_list
    except(csv.Error, KeyError) as Error:
        print(f'Error: line {reader.line_num} of {csv_file.name} is formatted incorrectly.')
    except ZeroDivisionError as zero_div_error:
        print(f"Error: line {reader.line_num} of {csv_file.name} contains 0 n the 'Fatal Crashes' or 'Cell Phone Use' column.")
            
            
    return dictionary

if __name__ == "__main__":
    main()
