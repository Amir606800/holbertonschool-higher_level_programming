from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', "r") as it:
            data = json.load(it)
        items = data["items"] if data["items"] else []
    except:
        items = []
    
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    # First get the argument from the url link
    source = request.args.get('source')
    table_heads = []
    table_items = []
    error_message = None
    
    # Burda deyesen match case islemir. If else ile yazmaq lazimdir !!!!
    #check if it is json 
    match source:
        case "json":
            try:
                with open('./products.json', "r") as prod_json:
                    data = json.load(prod_json)
                table_heads = data[0].keys()
                table_items = data
            except FileNotFoundError:
                print("JSON file Not Found")

        #check if it is csv  
        case'csv':
            try:
                data = []
                with open('./products.csv', 'r') as p_csv:
                    data_csv = csv.DictReader(p_csv)
                    for i in data_csv:
                        data.append(i)
                table_heads = data[0].keys()
                table_items = data
            except FileNotFoundError:
                print("CSV file Not Found")
                
        # Handle invalid format
        case _:
            return "Wrong source"

    
    
    try:
        id = request.args.get('id')
        sel_item = None
        for i in table_items:
            if int(i.get('id')) == int(id):
                sel_item = i
                break
        if not (sel_item is None):
            table_items = [sel_item]
        else:
            error_message = 'Product not found'
    except Exception:
        pass
        
    
    return render_template(
        'product_display.html',
        table_heads=list(table_heads)[1:] or [],
        table_items=table_items or [{}],
        error_message=error_message or None
    )




if __name__ == '__main__':
    app.run(debug=True, port=5000)
