import Analise from '@/components/analise/Analise';
import HabilitarCredito from '@/components/analise/HabilitarCredito';
import ListaProcessos from '@/components/analise/ListaProcessos';
import Vue from 'vue';
import VueRouter from 'vue-router';


Vue.use(VueRouter);

const routes = [
{
    name: 'lista-processos',
    path: '/',
    component: ListaProcessos
},   

{
    name: 'analise',
    path: '/analise',
    component: Analise
},
{
    name: 'habilitar-credito',
    path: '/habilitar-credito',
    component: HabilitarCredito
},
{
    name: 'lista-processos',
    path: '/lista-processos',
    component: ListaProcessos
}
]

export default new VueRouter({
    mode: 'history',
    routes
});
