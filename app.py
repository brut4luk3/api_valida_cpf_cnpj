from flask import Flask, request, jsonify

app = Flask(__name__)

def validar_cpf(cpf):
    # Remove pontuação
    cpf = cpf.replace(".", "").replace("-", "")

    # Verifica se todos os caracteres são numéricos
    if not cpf.isdigit():
        return False

    # Verifica se possui 11 dígitos
    if len(cpf) != 11:
        return False

    return True

def validar_cnpj(cnpj):
    # Remove pontuação
    cnpj = cnpj.replace(".", "").replace("-", "").replace("/", "")

    # Verifica se todos os caracteres são numéricos
    if not cnpj.isdigit():
        return False

    # Verifica se possui 14 dígitos
    if len(cnpj) != 14:
        return False

    return True

@app.route('/api/valida_cpf_cnpj', methods=['POST'])
def validar_cpf_cnpj():
    dados = request.json
    documento = dados.get('documento', '')

    # Remove pontuação do documento
    documento = documento.replace('.', '').replace('-', '').replace('/', '')

    if len(documento) == 11:
        resultado = validar_cpf(documento)
    elif len(documento) == 14:
        resultado = validar_cnpj(documento)
    else:
        resultado = False

    # Formato do retorno
    response = {
        "result": resultado
    }

    # Decisor de exibição do response code
    if resultado == True:
        return jsonify(response), 200
    else:
        return jsonify(response), 400

if __name__ == '__main__':
    app.run()