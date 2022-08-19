def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname":"Gabriela", "lastname": "Vazquez"}

    super_list = [
         {"firstname": "Gabriela", "lastname": "Vazquez"},
        {"firstname": "Ruth", "lastname": "Parraguirre"},
        {"firstname": "Miguel", "lastname": "Serrano"},
        {"firstname": "Luis", "lastname": "Nava"},
        {"firstname": "Gerardo", "lastname": "Enriquez"},
    ] 
       
    

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums":[1.1, 4.5, 6.8]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == "_main_":
    run()