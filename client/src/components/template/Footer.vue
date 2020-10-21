<template>
  <footer class="footer">
      <span>Copyright <strong>Ixtepô</strong> @ 2020</span>
  </footer>
</template>

<script>
export default {
    name: "Footer",
    data: function() {
        return { 
            contador: 0
        }
    }
}
</script>

<style>
    .footer {
        grid-area: footer;
        background-color: #DDD;
        color: #333;

        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 10px;
    }
</style>