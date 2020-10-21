<template>
    <div>
        <AnaliseHeader />
        <div class="analise">
            <div class="tarefas">
                <div class="tarefa-item">
                    <button class="btn btn-primary">
                        <i class="fa fa-lg fa-cogs" />
                    </button>
                    <div class="titulo-tarefa">Aguardando audiência</div>
                </div>

                <div class="tarefa-item">
                    <button class="btn btn-warning" disabled>
                        <i class="fa fa-lg fa-clock-o"/>
                    </button>
                    <div class="titulo-tarefa">Aguardando prazo</div>
                </div>

                <div class="tarefa-item">
                    <button class="btn btn-warning" disabled>
                        <i class="fa fa-lg fa-archive"/>
                    </button>
                    <div class="titulo-tarefa">Arquivar o processo</div>
                </div>

                <div class="tarefa-item">
                    <button class="btn btn-warning" disabled>
                        <i class="fa fa-lg fa-envelope"/>
                    </button>
                    <div class="titulo-tarefa">Comunicações e experidentes</div>
                </div>

                <div class="tarefa-item">
                    <button class="btn btn-warning" disabled>
                        <i class="fa fa-lg fa-calendar-check-o"/>
                    </button>
                    <div class="titulo-tarefa">Conclusão ao magistrado</div>
                </div>
                <div class="tarefa-item">
                    <button class="btn btn-warning">
                        <i class="fa fa-lg fa-handshake-o"/>
                    </button>
                    <div class="titulo-tarefa">Controle de acordo</div>
                </div>
                <div class="tarefa-item">
                    <button class="btn btn-primary">
                        <i class="fa fa-lg fa-list-ol" />
                    </button>
                    <div class="titulo-tarefa">Cumprimento de providências</div>
                </div>

                
                <div class="tarefa-item">
                    <button class="btn btn-warning">
                        <i class="fa fa-lg fa-undo"/>
                    </button>
                    <div class="titulo-tarefa">Devolver processo para vara de origem</div>
                </div>

                <div class="tarefa-item">
                    <button class="btn btn-warning" disabled>
                        <i class="fa fa-lg fa-calculator"/>
                    </button>
                    <div class="titulo-tarefa">Iniciar liquidação</div>
                </div>

                <div class="tarefa-item">
                    <button class="btn btn-warning" disabled>
                        <i class="fa fa-lg fa-exchange"/>
                    </button>
                    <div class="titulo-tarefa">Redistribuir</div>
                </div>

                <div class="tarefa-item">
                    <button class="btn btn-danger" @click="habilitarCredito()">
                        <i class="fa fa-lg fa-bank"/>
                    </button>
                    <div class="titulo-tarefa">Reunião de execuções</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import AnaliseHeader from './AnaliseHeader';
import AnaliseTarefa from './AnaliseTarefa';

export default {
    name: 'Analise',
    components: { AnaliseHeader, AnaliseTarefa },
    methods: {
        habilitarCredito() {
            this.$router.push({ path: '/habilitar-credito' })
        }
    }
}
</script>

<style>

.analise {

    height: 100vh;
  
}

.tarefas {
    margin: 10%;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

.tarefa-item btn {
    height: 80px !important;
    width: 60px !important;
}

.tarefa-item {
    margin: 10px;
    width: 150px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
}

.titulo-tarefa {
    text-align: center;
}


</style>