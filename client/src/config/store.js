import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        isMenuVisible: true,
        user: {
            name: 'Servidor Fulano',
            email: 'fulano@email.com'
        },
        processo: {}
    },
    mutations: {
        
    }
});