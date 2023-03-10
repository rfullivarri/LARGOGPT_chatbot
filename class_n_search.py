import sys
print(sys.version)
import pandas as pd
import numpy as np


df= pd.read_excel(r"/Users/ramirofernandezdeullivarri/Documents/GitHub/LARGOGPT_chatbot/Maestro de producto.xlsx",sheet_name="BD")
#df= df.head(20)
#print(df)

Product=[]
class Producto: 
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def Products_DB(self):
        for i in range(len(df)):
            a=Producto(codigo=str(df['Codigo'][i]), marca=df['marca'][i], calibre=str(df['Calibre'][i]), negocio=df['Negocio'][i], stock=str(10), estado=True)
            Product.append(a)
        return Product
    

    def search_product_info(self, inputs, Product):
        matching_products = []
        for product in Product:
            for i in range(len(inputs[1]['tag'])):
                if inputs[1]['tag'][i] not in product.attributes:
                    break
                elif inputs[1]['value'][i] != product.attributes[inputs[1]['tag'][i]]:
                    break
            else:
                matching_products.append(product)
        return matching_products

    # def search_product_info(self, inputs, Product):
    #     matching_products = []
    #     for product in Product:
    #         for input_ in inputs:
    #             if input_['tag'] not in product.attributes:
    #                 break
    #             elif input_['value'] != product.attributes[input_['tag']]:
    #                 break
    #         else:
    #             matching_products.append(product)
    #     return matching_products

    def get_product_output(self, matching_products):
           product_info = []
           for product in matching_products:
                product_info.append({
                    'codigo': product.attributes['codigo'],
                    'marca': product.attributes['marca'],
                    'calibre': product.attributes['calibre'],
                    'stock': product.attributes['stock'],
                    'negocio': product.attributes['negocio']
                })
               #product_info.append({output_tag: product.attributes[output_tag]})
           return product_info
Products=Producto()
product_list = Products.Products_DB()



# #ARMADO DE PROMPT PARA AI
# atributo1= []
# for product in product_list:  
#     [atributo1.append(p) for p in product.attributes.keys() if p != 'estado']   
# atributo1 = set(atributo1) 

# calibres= []
# for product in product_list:  
#     #print(product.attributes['calibre'])
#     calibres.append(product.attributes['calibre'])   
# calibres = list(set(calibres) )



# reglas1= ['las','los','de la','del','la','el']
# # pregunta1= ['Cual es', 'Sabes', 'Pasame', 'Necesito']
# # pregunta2= ['Cu??les son', 'Sabes', 'Pasame', 'Necesito']
# pregunta1= ['Cual es']
# pregunta2= ['Cu??les son']

# largogpt1= pd.DataFrame(columns=["", "", "", "", "", ""])
# largogpt1.columns = ["prompts","outputs_tags","tags","values","tags2","values2"]



# for product in product_list:
#     random_index = random.randrange(len(calibres))    
#     for p1 in product.attributes:
#         if p1 not in atributo1:
#             continue
#         else: 
#             for p2 in product.attributes:
#                 input = [{'tag':str(p2) , 'value': str(product.attributes[str(p2)])}]
#                 Busqueda_productos = Products.search_product_info(input, Product)
#                 product_info = Products.get_product_output(Busqueda_productos)
#                 result = 0
#                 if len(Busqueda_productos) > 1:
#                     result = [info[str(p1)] for info in product_info]
#                 else:
#                     result = {info[str(p1)] for info in product_info}
#                 if p2 not in atributo1:
#                     continue
#                 elif (p1 == p2) or (p2== 'stock') :
#                     pass
#                 elif p1 == 'marca' or p1 == 'negocio':
#                     if p1 == 'marca':
#                         if p2 == 'codigo':
#                             for preg in pregunta1:
#                                 #prompt =f"prompt: ??{preg} {reglas1[4]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]}? ###, completion: {reglas1[4]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]} es: {result} ###" 
#                                 #promptsncompletatios.append(str(prompt))
#                                 add_row = {'prompts': f"??{preg} {reglas1[4]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]}?", 
#                                               'outputs_tags': p1,
#                                               'tags': p2,
#                                               'values': product.attributes[str(p2)]}
#                                 largogpt1 = largogpt1.append(add_row, ignore_index=True)       
#                         else:
#                             for preg in pregunta2:    
#                                  #prompt =f"prompt: ??{preg} {reglas1[0]} {p1}s {reglas1[3]} {p2} {product.attributes[str(p2)]}? ###, completion: {reglas1[0]} {p1}s {reglas1[3]} {p2} {product.attributes[str(p2)]} son: {set(result)} ###" 
#                                  #promptsncompletatios.append(str(prompt))
#                                 add_row = {'prompts': f"??{preg} {reglas1[0]} {p1}s {reglas1[3]} {p2} {product.attributes[str(p2)]}?", 
#                                               'outputs_tags': p1,
#                                               'tags': p2,
#                                               'values': product.attributes[str(p2)]}
#                                 largogpt1 = largogpt1.append(add_row, ignore_index=True)
#                     else:
#                        if p2 == 'marca':
#                             for preg in pregunta1:
#                                  #prompt =f"prompt: ??{preg} {reglas1[5]} {p1} {reglas1[2]} {p2} {product.attributes[str(p2)]}? ###, completion: {reglas1[5]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]} es: {result} ###"        
#                                  #promptsncompletatios.append(str(prompt))
#                                 add_row = {'prompts': f"??{preg} {reglas1[5]} {p1} {reglas1[2]} {p2} {product.attributes[str(p2)]}?", 
#                                               'outputs_tags': p1,
#                                               'tags': p2,
#                                               'values': product.attributes[str(p2)]}
#                                 largogpt1 = largogpt1.append(add_row, ignore_index=True)
#                        else:   
#                             for preg in pregunta2:    
#                                  #prompt =f"prompt: ??{preg} {reglas1[5]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]}? ###, completion: {reglas1[5]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]} es: {result} ###" 
#                                  #promptsncompletatios.append(str(prompt))
#                                 add_row = {'prompts': f"??{preg} {reglas1[5]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]}?", 
#                                               'outputs_tags': p1,
#                                               'tags': p2,
#                                               'values': product.attributes[str(p2)]}
#                                 largogpt1 = largogpt1.append(add_row, ignore_index=True)
#                 elif p2 == 'marca':
#                         for preg in pregunta2:    
#                              #prompt =f"prompt: ??{preg}  {reglas1[1]} {p1}s {reglas1[2]} {p2} {product.attributes[str(p2)]}? ###, completion: {reglas1[1]} {p1}s {reglas1[2]} {p2} {product.attributes[str(p2)]} son: {set(result)} ###"
#                              #promptsncompletatios.append(str(prompt))
#                             add_row = {'prompts': f"??{preg}  {reglas1[1]} {p1}s {reglas1[2]} {p2} {product.attributes[str(p2)]}?", 
#                                           'outputs_tags': p1,
#                                           'tags': p2,
#                                           'values': product.attributes[str(p2)]}
#                             largogpt1 = largogpt1.append(add_row, ignore_index=True)

#                             #SEARCH MARCA CALIBRE 
#                             if p1 != 'calibre':
#                                 add_row1 = {'prompts': f"??{preg}  {reglas1[1]} {p1}s {reglas1[2]} {product.attributes[str(p2)]} {calibres[random_index]}?", 
#                                               'outputs_tags': p1,
#                                               'tags': p2,
#                                               'values': product.attributes[str(p2)],
#                                               'tags2': 'calibre',
#                                               'values2':calibres[random_index]
#                                               }
#                                 largogpt1 = largogpt1.append(add_row1, ignore_index=True)
                            
#                 else:
#                     if p2 == 'codigo':
#                         for preg in pregunta1:    
#                              #prompt =f"prompt: ??{preg}  {reglas1[5]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]}? ###, completion: {reglas1[4]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]} es: {result} ###"
#                              #promptsncompletatios.append(str(prompt))
#                             add_row = {'prompts': f"??{preg}  {reglas1[5]} {p1} {reglas1[3]} {p2} {product.attributes[str(p2)]}?", 
#                                           'outputs_tags': p1,
#                                           'tags': p2,
#                                           'values': product.attributes[str(p2)]}
#                             largogpt1 = largogpt1.append(add_row, ignore_index=True)
#                     else:   
#                              #prompt =f"prompt: ??{preg}  {reglas1[1]} {p1}s {reglas1[3]} {p2} {product.attributes[str(p2)]}? ###, completion: {reglas1[1]} {p1}s {reglas1[3]} {p2} {product.attributes[str(p2)]} son: {set(result)} ###"
#                              #promptsncompletatios.append(str(prompt))
#                             add_row = {'prompts': f"??{preg}  {reglas1[1]} {p1}s {reglas1[3]} {p2} {product.attributes[str(p2)]}?", 
#                                           'outputs_tags': p1,
#                                           'tags': p2,
#                                           'values': product.attributes[str(p2)]}
#                             largogpt1 = largogpt1.append(add_row, ignore_index=True)

# #print(largogpt1)
# largogpt1 = largogpt1.drop_duplicates()
# largogpt1 = largogpt1.iloc[1:].sample(frac=1).reset_index(drop=True)
# filename = ("PROMPTS_N_COMPLETATIONS_PRODUCT2.csv")
# largogpt1.to_csv(f"/Users/ramirofernandezdeullivarri/Documents/GitHub/LARGOGPT_chatbot/prompts/{filename}", sep=",")







#inputs=({'outputs_tags': 'stock'}, {'tag': ['marca', 'calibre'], 'value': ['budweiser', '410']}) 
# inputs= results
# output_tag= inputs[0]['outputs_tags']
# print(inputs)




# tag1= inputs[1]['tag'][0]
# value1= inputs[1]['value'][0]
# tag2= inputs[1]['tag'][1]
# value2= inputs[1]['value'][1]
# 
# print(tag1,value1,"\n")
# print(tag2,value2,"\n")
# print(output_tag,"\n")
# for input in inputs:
#     print(input,"\n")
#     for i in input:
#         print(i, "\n")



#BUSCADOR A PARTI DE: promptsncompletatios INPUTS/OUTPUTS
#inputs = [{'tag': 'marca', 'value': 'pepsi'}, {'tag': 'calibre', 'value': '500 cc pet'}] 
#inputs = [{'tag': 'codigo', 'value': str(26)}]
#output_tag = [{'outputs_tags': 'stock'}]


def search_P(inputs):
    try:
        #tag1= inputs[1]['tag'][0]
        value1= inputs[1]['value'][0]
        #tag2= inputs[1]['tag'][1]
        value2= inputs[1]['value'][1]
        output_tag= inputs[0]['outputs_tags']

        Busqueda_productos = Products.search_product_info(inputs, Product)

        if Busqueda_productos:
            if len(Busqueda_productos) > 1:
                PP= []
                #print(f'Se encontraron los siguientes productos de {inputs[0]["tag"]} "{inputs[0]["value"]}":')
                product_info = Products.get_product_output(Busqueda_productos)
                for info in product_info:
                    PP.append(f"- Codigo: {info['codigo']}, Marca: {info['marca']}, Calibre: {info['calibre']}, Stock: {info['stock']}")
                return(f'Se encontraron los siguientes productos de {value1} {value2}: \n {PP}')    
            else:
                product_info = Products.get_product_output(Busqueda_productos)
                #print(f"{output_tag} del producto de {inputs[0]['tag']} {inputs[0]['value']} es:\n - Codigo: {product_info[0]['codigo']}, Marca: {product_info[0]['marca']}, Calibre: {product_info[0]['calibre']}, Stock: {product_info[0]['stock']}")
                return(f"{output_tag} del producto de {value1} {value2} es:\n - Codigo: {product_info[0]['codigo']}, Marca: {product_info[0]['marca']}, Calibre: {product_info[0]['calibre']}, Stock: {product_info[0]['stock']}")
        else:
            #print(f'No se encontraron productos de {inputs[0]["tag"]} "{inputs[0]["value"]}"')
            return(f'No se encontraron productos de {value1} "{value2}"')
    except:
        pass

# #print(f"PRUEBA: {search_P(inputs,output_tag)}\n")