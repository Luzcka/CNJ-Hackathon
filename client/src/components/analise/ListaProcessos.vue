<template>
  <div class="lista-processos">
    <b-table hover striped :items="processos" :fields="fields">
        <template slot="actions" slot-scope="data">
            <b-button variant="warning" @click="loadProcesso(data.item)" class="mr-2">
                <i class="fa fa-pencil"></i>
            </b-button>
        </template>
    </b-table>
  </div>
</template>

<script>

export default {
    name: 'ListaProcessos',

    data: function() {
        return {
            fields: [
                { key: 'num_processo', label: 'No. processo', sortable: true },
                { key: 'trt', label: 'TRT', sortable: true },
                { key: 'vara', label: 'Vara', sortable: true },
                { key: 'valor_causa', label: 'Valor da causa'},
                { key: 'cnpj', label: 'CNPJ'},
                { key: 'actions', label: 'Ações' }
            ],
            processos: [
                {
                    "num_processo":"00002630820205090664",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE LONDRINA",
                    "millis":1599735676950,
                    "codigo_vara":20358,
                    "data_ajuizamento":"20200326152740",
                    "valor_causa":54144.08,
                    "status":1,
                    "cnpj":"14662758000108"
                },
                {   //00002378920205090088
                    "num_processo":"0000237892020509009",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE CURITIBA",
                    "millis":1599733533390,
                    "codigo_vara":20340,
                    "data_ajuizamento":"20200319140509",
                    "valor_causa":408925.77,
                    "status":1,
                    "cnpj":"14662758000108"
                },
                {
                    "num_processo":"00002648820205090018",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE LONDRINA",
                    "millis":1599735810617,
                    "codigo_vara":20354,
                    "data_ajuizamento":"20200327100359",
                    "valor_causa":1679.0,
                    "status":0,
                    "cnpj":"14662758000108"
                },
                {
                    "num_processo":"00002481620205090025",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE UMUARAMA",
                    "millis":1597111904399,
                    "codigo_vara":20392,
                    "data_ajuizamento":"20200324162953",
                    "valor_causa":10000.0,
                    "status":0,
                    "cnpj":"52265287001238"
                },
                {
                    "num_processo":"00001511820205090089",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE APUCARANA",
                    "millis":1599726328531,
                    "codigo_vara":20298,
                    "data_ajuizamento":"20200326141802",
                    "valor_causa":40960.15,
                    "status":1,
                    "cnpj":"14239542000800"
                },
                {
                    "num_processo":"00002682820205090018",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE LONDRINA",
                    "millis":1599847735529,
                    "codigo_vara":20354,
                    "data_ajuizamento":"20200327152209",
                    "valor_causa":7105.62,
                    "status":0,
                    "cnpj":"74837061001116"
                },
                {
                    "num_processo":"00001461820205090017",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE JACAREZINHO",
                    "millis":1599725903450,
                    "codigo_vara":20351,
                    "data_ajuizamento":"20200324103646",
                    "valor_causa":26000.0,
                    "status":0,
                    "cnpj":"34240621004070"
                },
                {
                    "num_processo":"00001164720205090125",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE PATO BRANCO",
                    "millis":1599843787588,
                    "codigo_vara":20375,
                    "data_ajuizamento":"20200320150917",
                    "valor_causa":4573.66,
                    "status":0,
                    "cnpj":"94060287000199"
                },
                {
                    "num_processo":"00002040620205090022",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE PARANAGU\u00c1",
                    "millis":1599892672986,
                    "codigo_vara":20370,
                    "data_ajuizamento":"20200322001726",
                    "valor_causa":34205.86,
                    "status":0,
                    "cnpj":"16076685000190"
                },
                {
                    "num_processo":"00002430920205090020",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE MARING\u00c1",
                    "millis":1596247688874,
                    "codigo_vara":20363,
                    "data_ajuizamento":"20200318150255",
                    "valor_causa":275537.92,
                    "status":0,
                    "cnpj":"71651021001197"
                },
                {
                    "num_processo":"00004473520205090026",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE UNIÃO DA VITÓRIA",
                    "millis":1599852387461,
                    "codigo_vara":20394,
                    "data_ajuizamento":"20200324143655",
                    "valor_causa":17735.53,
                    "status":0,
                    "cnpj":"40028226002169"
                },
                {
                    "num_processo":"00002494020205090012",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE CURITIBA",
                    "millis":1599847250575,
                    "codigo_vara":20329,
                    "data_ajuizamento":"20200326162324",
                    "valor_causa":8893.28,
                    "status":0,
                    "cnpj":"48338838000973"
                },
                {
                    "num_processo":"00002547420205090008",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE CURITIBA",
                    "millis":1599847408520,
                    "codigo_vara":20325,
                    "data_ajuizamento":"20200325171227",
                    "valor_causa":2000.0,
                    "status":0,
                    "cnpj":"34763855000781"
                },
                {
                    "num_processo":"00002378620205090671",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE TELÊMACO BORBA",
                    "millis":1597110273004,
                    "codigo_vara":20389,
                    "data_ajuizamento":"20200325195143",
                    "valor_causa":1000.0,
                    "status":1,
                    "cnpj":"31041605002440"
                },
                {
                    "num_processo":"00002564720205090007",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE CURITIBA",
                    "millis":1597112489466,
                    "codigo_vara":20324,
                    "data_ajuizamento":"20200326003206",
                    "valor_causa":34421.08,
                    "status":0,
                    "cnpj":"25707189000188"
                },
                {
                    "num_processo":"00002512820205090006",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE CURITIBA",
                    "millis":1599847306202,
                    "codigo_vara":20323,
                    "data_ajuizamento":"20200320163004",
                    "valor_causa":19350.0,
                    "status":0,
                    "cnpj":"86843193000915"
                },
                {
                    "num_processo":"00002187820205090122",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE SÃO JOSÉ DOS PINHAIS",
                    "millis":1599846462308,
                    "codigo_vara":20387,
                    "data_ajuizamento":"20200325185009",
                    "valor_causa":42985.57,
                    "status":0,
                    "cnpj":"83179000350"
                },
                {
                    "num_processo":"00002297220205090651",
                    "trt":"TRT9",
                    "vara":"VARA DO TRABALHO DE CURITIBA",
                    "millis":1596247323596,
                    "codigo_vara":20334,
                    "data_ajuizamento":"20200318134227",
                    "valor_causa":5215.15,
                    "status":0,
                    "cnpj":"24374534000308"
                }
            ]
        }
    },
    methods: {
        loadProcesso(processo) {
            this.$store.state.processo = processo;
            this.$router.push({path: '/analise'});
        }
    }

}
</script>

<style>

</style>