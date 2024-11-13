from openai import OpenAI

client = OpenAI(
    api_key='your-api-key'
)

# Ścieżka do pliku z artykułem
input_file_path = 'tresc artykulu.txt'
output_file_path = 'artykul.html'

# Wczytanie treści artykułu z pliku
with open(input_file_path, 'r', encoding='utf-8') as file:
    article_text = file.read()

# Prompt dla OpenAI, który przekazuje nasze wytyczne dotyczące struktury HTML
prompt = f"""
Zastosuj odpowiednie tagi HTML do strukturyzacji treści poniższego artukułu.
Przy pomocy tagu <img> z atrybutem src="image_placeholder.jpg" wstaw sugestie miejsc na grafiki poglądowe, które będą generowane przez AI.
Dla każdego obrazu dodaj atrybut alt z bardzo szczegółowym promptem dla modelu służącego do generowania grafiki.
Umieść podpisy pod grafikami używając odpowiednich tagów HTML.
Nie dodawaj żadnego kodu CSS ani JavaScript. Nie dołączaj nagłówków HTML, znaczników <html>,
<head> ani <body>. Twoja odpowiedź ma zawierać tylko i wyłącznie zawartość do wstawienia do szablonu HTML pomiędzy <body> a </body> bez żadnych zbędnych znaków.

Artykuł:
{article_text}
"""

# Wysyłanie żądania do OpenAI API
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Jesteś pomocnym asystentem z zaawansowaną znajomością HTML."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.5
)


# Zapisz odpowiedź w pliku HTML
html_content = response.choices[0].message.content.strip()

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

print("Zapisano wygenerowany kod HTML w pliku artykul.html")
