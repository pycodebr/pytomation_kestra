import requests
import json


def main():
    response = requests.get(
        url='https://dummyjson.com/products',
    )
    products_data = response.json().get('products')
    
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products_data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
