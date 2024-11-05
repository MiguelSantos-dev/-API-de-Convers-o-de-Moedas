# currency_converter.rb
require 'httparty'
require 'json'

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def convert_currency(amount, from_currency, to_currency)
  # Fazer requisição para a API de câmbio
  response = HTTParty.get("#{API_URL}#{from_currency}")
  data = response.parsed_response

  # Verificar se a moeda de destino está nas taxas de câmbio
  if data["rates"].key?(to_currency)
    rate = data["rates"][to_currency]
    converted_amount = amount * rate
    {
      original_amount: amount,
      from_currency: from_currency,
      to_currency: to_currency,
      converted_amount: converted_amount.round(2)
    }
  else
    { error: "Moeda não encontrada." }
  end
end

# Exemplo de uso
puts "Digite o valor a ser convertido: "
amount = gets.chomp.to_f
puts "Digite a moeda de origem (ex: USD): "
from_currency = gets.chomp.upcase
puts "Digite a moeda de destino (ex: EUR): "
to_currency = gets.chomp.upcase

result = convert_currency(amount, from_currency, to_currency)
puts JSON.pretty_generate(result)
