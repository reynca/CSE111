import csv

def main():
    #products Indexs
    PRODUCT_NUM_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    #requests Indexs
    REQUEST_PRODUCT_NUM = 0
    REQUEST_PRODUCT_QUAN = 1
    
    requests = read_dict('request.csv',REQUEST_PRODUCT_NUM)
    print(requests)
    products = read_dict('products.csv', PRODUCT_NUM_INDEX)




def read_dict(filename, Index_Key):
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
            
            
    return dictionary

if __name__ == "__main__":
    main()

print("hi")