<template>
  <div class="tarefa">
    <button class="btn" :class="this.color" :disabled="this.disabled">
        TEste
    </button>
    <span>{{ title }}</span>
  </div>
</template>

<script>
export default {
    name: 'AnaliseTarefa',
    props: ['title', 'icon', 'color', 'disabled'],
    computed: {
        style() {
            return "background-color: " + (this.color || "#C8D1D1");
        }
    }
}
</script>

<style scoped>
.tarefa {
    height: 80px;
    width: 60px; 
    display: flex;
    flex-direction: column;
    justify-content: center;
}

</style>