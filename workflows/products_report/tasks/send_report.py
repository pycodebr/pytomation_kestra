import os

from dotenv import load_dotenv
from services.evolution import EvolutionApi


load_dotenv()

def main():
    with open('ai_report.txt', 'r', encoding='utf-8') as f:
        ai_report = f.read()

    evo_api = EvolutionApi()
    evo_api.send_message(
        number=os.getenv('RECIPIENT_REPORT_NUMBER'),
        text=ai_report,
    )


if __name__ == '__main__':
    main()
