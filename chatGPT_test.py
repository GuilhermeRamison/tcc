from openai import OpenAI

api_key = 'TOKEN'
client = OpenAI(api_key=api_key)

def generate_questions_answers(context):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=context,
        max_tokens=512,
        temperature=0.5
    )

    return response.choices[0].text.strip()

context = """Gere uma pergunta e uma resposta sobre o contexto: 
A Fisiologia Respiratória é o ramo da fisiologia que estuda o funciona-
mento do sistema respiratório humano. O sistema respiratório é res-
ponsável pela troca gasosa entre o corpo e o ambiente, fornecendo
oxigênio aos tecidos e removendo dióxido de carbono. Consiste em
órgãos como nariz, faringe, laringe, traqueia, brônquios e pulmões.
Durante a inspiração, os músculos respiratórios, incluindo o diafragma
e os músculos intercostais, se contraem, expandindo a caixa torácica
e diminuindo a pressão dentro dos pulmões. Isso permite que o ar
entre nos pulmões, onde ocorre a troca gasosa nos alvéolos pulmo-
nares.
Na expiração, os músculos respiratórios relaxam e a caixa torácica
retorna à sua posição de repouso, empurrando o ar rico em dióxido
de carbono para fora dos pulmões. O sistema respiratório também
desempenha um papel na regulação do pH sanguíneo, controlando
os níveis de ácido carbônico no sangue.
Distúrbios respiratórios, como asma, enfisema e bronquite crônica,
podem afetar a função pulmonar e prejudicar a troca gasosa. O estudo
da fisiologia respiratória é crucial para entender esses distúrbios e
desenvolver tratamentos eficazes para melhorar a saúde pulmonar.
"""

generated_question_answer = generate_questions_answers(context)
print(generated_question_answer)
