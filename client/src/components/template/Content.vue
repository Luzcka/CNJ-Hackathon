<template>
    <div class="content">
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'Content'
}
</script>

<style scoped>
    .content {
        grid-area: content;
        background-color: #efefef;
        padding: 20;
    }
</style>