import os
import json

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

def main():
    with open('products.json', 'r', encoding='utf-8') as f:
        products_data = json.load(f)

    llm = ChatOpenAI(
        api_key=os.getenv('OPENAI_API_KEY'),
        model='gpt-5-mini',
    )

    system_prompt = '''
    Você é um assistente que gera relatórios de produtos para WhatsApp.
    Seja direto, use emojis e formate de forma clara para mensagem mobile.
    '''
    user_prompt = '''Com base nestes dados de produtos: {products_data}
    Gere um relatório resumido e atrativo para envio no WhatsApp, incluindo
    informações principais dos produtos de forma organizada.
    '''
    user_prompt = user_prompt.format(products_data=products_data)

    response = llm.invoke([
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt}
    ])
    report_text = response.content

    with open('ai_report.txt', 'w', encoding='utf-8') as f:
        f.write(report_text)


if __name__ == '__main__':
    main()
