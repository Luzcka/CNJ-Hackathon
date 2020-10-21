import os
import pathlib

import yaml
from tinydb import TinyDB, Query, where
from flask import Flask, jsonify, request
from flask_restplus import reqparse, abort, Api, Resource, fields
from flask_cors import CORS


CONFIG_FILE_NAME = "GroupAPI.yaml"
JSON_DB_NAME = "db.json"
JSON_DB_NAME_FONTE = "processos.json"
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

 # Load configuration
ConfigFile = os.path.join(CURRENT_DIR, CONFIG_FILE_NAME)
with open(ConfigFile, "r", encoding="utf-8") as ConfigFile:
    Configuration = yaml.load(ConfigFile, Loader=yaml.SafeLoader)
RootDataDir = pathlib.Path(Configuration["Input"]["RootDataDir"])
JsonDB = os.path.join(RootDataDir, JSON_DB_NAME)
JsonDBFonte = os.path.join(RootDataDir, JSON_DB_NAME_FONTE)

app = Flask(__name__)
CORS(app)
api = Api(app=app, version="0.1", 
          title="API RESTplus de agrupamento de execuções",
          description="API RESTplus de agrupamento de execuções")
ns_conf = api.namespace('processos', description='Processos')
db = TinyDB(JsonDB)
db_fonte = TinyDB(JsonDBFonte)

busca_processo_model = api.model("Busca dados do processo na origem",
                                {"num_processo": fields.String(required = True, 
                                description="Número único do processo.",
                                help="Deve ser preenchido.")})

busca_model = api.model("Busca de processos piloto",
                        {"cnpj_demandada": fields.String(required = True, 
                         description="CNPJ sem mascara da demandada.",
                         help="Deve ser preenchido.")})

agrupamento_model = api.model("Agrupamento de execuções",
                              {"num_processo": fields.String(required = True,
                              description="Numero unico do processo a ser agrupado",
                              help="Deve ser preenchido."),
                              "sigla_tribunal": fields.String(required = True, 
                              description="Sigla do tribunal onde o numero do processo é unico.",
                              help="Deve ser preenchido."),
                              "vara": fields.String(required = True, 
                              description="Vara do processo.",
                              help="Deve ser preenchido."),
                              "num_processo_piloto": fields.String(required = True,
                              description="Numero unico do processo piloto do agrupamento",
                              help="Deve ser preenchido."),
                              "sigla_tribunal_piloto": fields.String(required = True, 
                              description="Sigla para identificar o tribunal onde o numero do processo piloto é unico.",
                              help="Deve ser preenchido."),
                              "vara_piloto": fields.String(required = True, 
                              description="Vara do processo piloto.",
                              help="Deve ser preenchido."),
                              "cnpj_demandada": fields.String(required = True, 
                              description="CNPJ sem mascara da demandada.",
                              help="Deve ser preenchido."),
                              "valor_demanda": fields.Fixed(required = True, 
                              description="CNPJ sem mascara da demandada.",
                              help="Deve ser preenchido.",
                              decimals=2)})


@ns_conf.route("/source_search") 
class SearchSourceProcessInfo(Resource):
    @api.expect(busca_processo_model)
    def post(self):
        """
        Faz busca de processo na base origem.
        """
        try:
            json_data = request.get_json()
            num_processo = json_data["num_processo"]

            processo = Query()
            query_result = db_fonte.search(processo.num_processo == num_processo)
            result = jsonify({"processo":query_result})
        except Exception as erro:
            result = jsonify({"mensagem":str(erro)})
        finally:            
            return result


@ns_conf.route("/search") 
class SearchPilotProcessInfo(Resource):
    @api.expect(busca_model)
    def post(self):
        """
        Faz busca de processo piloto para um CNPJ.
        """
        try:
            json_data = request.get_json()
            cnpj_demandada = json_data["cnpj_demandada"]

            processo = Query()
            cnpj_demandada = cnpj_demandada[0:8]
            query_result = db.search((where('cnpj_demandada').matches(cnpj_demandada + ".*")) &
                                     #(processo.num_processo_piloto == "") &
                                     #(processo.sigla_tribunal_piloto == "") &
                                     (processo.situacao == "em_execucao"))
            result = jsonify({"pilotos":query_result})
        except Exception as erro:
            result = jsonify({"mensagem":str(erro)})
        finally:            
            return result


@ns_conf.route("/insert") 
class InsertProcessInfo(Resource):
    @api.expect(agrupamento_model)
    def post(self):
        """
        Faz inserçãp de processo no grupo do piloto.
        """
        try:
            json_data = request.get_json()
            num_processo = json_data["num_processo"]
            sigla_tribunal = json_data["sigla_tribunal"]
            num_processo_piloto = json_data["num_processo_piloto"]
            sigla_tribunal_piloto = json_data["sigla_tribunal_piloto"]
            valor_demanda = json_data["valor_demanda"]

            processo = Query()
            query_result = db.search((processo.num_processo == num_processo) &
                           (processo.sigla_tribunal == sigla_tribunal))
            if not query_result:
                dados_piloto = db.search((processo.num_processo == num_processo_piloto) &
                                         (processo.sigla_tribunal == sigla_tribunal_piloto) &
                                         (processo.situacao == "em_execucao"))
                if not dados_piloto:
                    valor_total = 0
                else:
                    valor_total =  dados_piloto[0]["valor_total"]
                valor_total += valor_demanda

                if (num_processo_piloto != "") & (sigla_tribunal_piloto != ""):
                    db.update({'valor_total': valor_total},
                            (processo.num_processo == num_processo_piloto) &
                            (processo.sigla_tribunal == sigla_tribunal_piloto))
                    db.update({'valor_total': valor_total},
                            (processo.num_processo_piloto == num_processo_piloto) &
                            (processo.sigla_tribunal_piloto == sigla_tribunal_piloto))

                json_data["valor_total"] = valor_total
                json_data["situacao"] = "em_execucao"
                db.insert(json_data)

                result = jsonify({"mensagem":f"Processo {num_processo} do tribunal {sigla_tribunal} inserido"})
            else:
                result = jsonify({"mensagem":f"Processo já existente: {num_processo} do tribunal {sigla_tribunal}"})
        except Exception as erro:
            result = jsonify({"mensagem":str(erro)})
        finally:            
            return result



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5610, debug=False)
