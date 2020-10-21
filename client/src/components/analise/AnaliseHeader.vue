<template>
   <header class="analise-header">
       <div>{{ user.name }}</div>
       <div class="titulo">Análise</div>
       <i class="fa fa-bars"></i>

   </header>
</template>

<script>
import { mapState } from 'vuex';

export default {
    name: 'AnaliseHeader',
    computed: mapState(['user'])
}
</script>

<style>

.analise-header {
    height: 40px;
    background-color: #85D4EB;
    display: flex;
    justify-content: space-between;
    padding: 5px 10px 0px 10px;
}

.titulo {
    font-weight: 600;
}

</style>