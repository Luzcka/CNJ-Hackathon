from flask import Flask, jsonify, request
from flask_restplus import reqparse, abort, Api, Resource, fields


app = Flask(__name__)
api = Api(app=app, version="0.1", title="Teste de API usando Flask RESTplus", description="Teste de API usando Flask RESTplus")
ns_conf = api.namespace('processos', description='Consulta processos')


busca_model = api.model("Teste de API usando Flask RESTplus",
		  {"num_processo": fields.String(required = True, 
           description="Numero unico do processo",
           help="Deve ser preenchido."),
           "sigla_tribunal": fields.String(required = True, 
           description="Sigla para identificar o tribunal onde o numero do processo é unico.",
           help="Deve ser preenchido."),
           "cnpj_demandada": fields.String(required = True, 
           description="CNPJ sem mascara da demandada.",
           help="Deve ser preenchido.")}
)
        

@ns_conf.route("/") 
class GetProcessInfo(Resource):
    @api.expect(busca_model)
    def post(self):
        """
        Faz consulta para verificação de processo piloto
        """
        #try:
        json_data = request.get_json()
        num_processo = json_data["num_processo"]
        sigla_tribunal = json_data["sigla_tribunal"]
        cnpj_demandada = json_data["cnpj_demandada"]

        result = jsonify({"mensagem":f"Pesquisando o processo {num_processo} do tribunal {sigla_tribunal} contra {cnpj_demandada}"})
        return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5610, debug=False)




