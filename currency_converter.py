import requests
import json

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def convert_currency(amount, from_currency, to_currency):
    # Fazer requisição para a API de câmbio
    response = requests.get(API_URL + from_currency)
    data = response.json()

    # Verificar se a resposta contém a chave "rates"
    if "rates" not in data:
        print("Erro: A resposta da API não contém as taxas de câmbio.")
        print("Resposta da API:", data)
        return {"error": "Falha ao obter taxas de câmbio. Verifique a moeda de origem e tente novamente."}

    # Verificar se a moeda de destino está nas taxas de câmbio
    if to_currency in data["rates"]:
        rate = data["rates"][to_currency]
        converted_amount = amount * rate
        return {
            "original_amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "converted_amount": round(converted_amount, 2)
        }
    else:
        return {"error": f"Moeda de destino '{to_currency}' não suportada."}

# Exemplo de uso
if __name__ == "__main__":
    amount = float(input("Digite o valor a ser convertido: "))
    from_currency = input("Digite a moeda de origem (ex: USD): ").upper()
    to_currency = input("Digite a moeda de destino (ex: EUR): ").upper()
    
    result = convert_currency(amount, from_currency, to_currency)
    print(json.dumps(result, indent=4))
