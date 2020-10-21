<template>
    <div class="processo">
        <div class="processo-numero">{{ processo.num_processo }}</div>
        <div class="processo-vara">{{ processo.vara }}</div>
        <div class="processo-executado">{{ processo.cnpj}}</div>
    </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
    name: 'HeaderProcesso',
    computed: mapState(['processo'])
}
</script>

<style>

    .processo {
        padding: 10px;
        font-size: 0.7rem;
        color: #fff;
        font-weight: 100;
        align-items: center;
    }

</style>