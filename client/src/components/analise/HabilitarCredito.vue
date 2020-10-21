<template>
  <div class="habilitar-credito">
      <AnaliseHeader />
        
        <div class="outro-juizo" v-if="msg_processos_piloto1">

            <div class="alerta-processo-piloto">
                {{ this.msg_processos_piloto1 }}
            </div>
            <div class="alerta-processo-piloto">
                {{ this.msg_processos_piloto2 }}
            </div>
            <b-row>
                <b-col md="12" align="center" class="mt-3">
                    <!--<button class="btn btn-warning mr-4" @click="gravaComPiloto()">Sim, creditar em outro juízo.</button>
                    <button class="btn btn-primary mr-3" @click="gravaSemPiloto()">Não, creditar na vara atual.</button>-->
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="modo"
                             id="inlineRadio1" value="comPiloto">
                        <label class="form-check-label" for="inlineRadio1">
                            Sim, habilitar crédito no processo piloto
                        </label>
                    </div>
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="modo"
                             id="inlineRadio2" value="semPiloto">
                        <label class="form-check-label" for="inlineRadio2">
                            Não, habilitar crédito na vara atual
                        </label>
                    </div>
                </b-col>
            </b-row>

        </div>
       
        <div class="form-confirma">

          <b-row>
              <b-col md="12" class="mt-5">
                Valor a ser creditado <input type="number" min="0.0" step="0.01" class="mx-2" :value="this.processo.valor_causa" />
                <button class="btn btn-primary" @click="grava()">Confirma</button>
              </b-col>
          </b-row>
        </div>


         
  </div>
</template>

<script>
import { mapState } from 'vuex';
import AnaliseHeader from './AnaliseHeader';
import { baseApiUrl } from '@/global';
import axios from 'axios'

export default {
    name: 'HabilitarCredito',
    components: { AnaliseHeader },
    computed:  mapState(['processo']),
    data: function() {
        return {
            confirma: false,
            msg_processos_piloto1: '',
            msg_processos_piloto2: '',
            processos_piloto: [],
            vara_piloto: '',
            processo_piloto: '',
            tribunal_piloto: '',
            modo: 'semPiloto'
        }
    },
    methods: {
        confirmaCredito() {
            let vara_piloto = '';
            let piloto = '';
            let varas = '';
            let tribunal_piloto = '';

            
            
            axios.post(`${baseApiUrl}/search`, {'cnpj_demandada': this.processo.cnpj}).then((processos) => {
                this.processos_piloto = processos.data.pilotos;

                if (this.processos_piloto.length > 0) {

                    this.modo = 'comPiloto';

                    for (let processo of this.processos_piloto) {
                      
                        if (processo.num_processo_piloto !== '') {
                            piloto = processo.num_processo_piloto;
                            vara_piloto = processo.vara_piloto;
                            tribunal_piloto = processo.sigla_tribunal_piloto;
                        }
                        varas += processo.vara + ', ';
                    }

                    if (vara_piloto === '') {   
                        vara_piloto = this.processos_piloto[0].vara;
                        piloto = this.processos_piloto[0].num_processo;
                        tribunal_piloto = this.processos_piloto[0].sigla_tribunal;

                    }
                   
                    this.msg_processos_piloto1 = 'Existe(m) ' + this.processos_piloto.length + ' processo(s) em execução para o CNPJ '
                        + this.processo.cnpj  + ' nas vara(s) ' + varas + '.';
                    this.msg_processos_piloto2 = 'Deseja habilitar crédito no processo piloto do juízo centralizador ' +
                        vara_piloto + '?';
                    this.processo_piloto = piloto;
                    this.vara_piloto = vara_piloto;
                    this.tribunal_piloto = tribunal_piloto;
                }
            })
        },

        gravaSemPiloto() {
            axios.post(`${baseApiUrl}/insert`, 
                {
                    'num_processo': this.processo.num_processo,
                    'sigla_tribunal': this.processo.trt,
                    'vara': this.processo.vara,
                    'num_processo_piloto': '',
                    'sigla_tribunal_piloto': '',
                    'vara_piloto': '',
                    'cnpj_demandada': this.processo.cnpj,
                    'valor_demanda': this.processo.valor_causa
                }
            ).then((processos) => {
                this.$toasted.global.defaultSuccess();
                this.$router.push({ path: '/analise' });
   

            });
        },

        gravaComPiloto() {
             axios.post(`${baseApiUrl}/insert`, 
                {
                    'num_processo': this.processo.num_processo,
                    'sigla_tribunal': this.processo.trt,
                    'vara': this.processo.vara,
                    'num_processo_piloto': this.processo_piloto,
                    'sigla_tribunal_piloto': this.tribunal_piloto,
                    'vara_piloto': this.vara_piloto,
                    'cnpj_demandada': this.processo.cnpj,
                    'valor_demanda': this.processo.valor_causa
                }
            ).then((processos) => {
                this.$toasted.global.defaultSuccess();
                this.$router.push({ path: '/analise' });

            });           
        },
        grava() {
            if (this.modo === 'semPiloto') {
                this.gravaSemPiloto();
            }
            else {
                this.gravaComPiloto();
            }
        }
    },
    mounted() {
        this.confirmaCredito();
        
    }
}
</script>

<style>

.outro-juizo {
    display: flex;
    flex-direction: column;
    align-items: center;
}


.dados-processo {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
}

.form-confirma {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.alerta-processo-piloto {
    margin-top: 30px;
    margin-left: 20px;
    color: red;
    font-size: 1.2rem;
}

</style>