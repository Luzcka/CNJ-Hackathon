<template>
    <header class="header">
        <div class="logo-processo">
            <img src="@/assets/logo-pje.png" class="logo-pje"/>
            <HeaderProcesso />
        </div>
        <h1 class="title">          
            <router-link to="/"> {{ title }}</router-link>
        </h1>
        <UserDropdown v-if="!hideUserDropdown" />
    </header>
</template>

<script>

import UserDropdown from './UserDropdown';
import HeaderProcesso from './HeaderProcesso';

export default {
    name: 'Header',
    components: { UserDropdown, HeaderProcesso },
    props: {
        title: String,
        hideUserDropdown: Boolean
    },
    computed: {

    },
    methods: {

    }
}
</script>

<style>
    .header {
        grid-area: header;
        background-color: #007AB9;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .title {
        font-size: 1.2rem;
        color: #fff;
        font-weight: 100;
        flex-grow: 1;
        text-align: center;

    }

    .title a {
        color: #fff;
        text-decoration: none;
    }

    .title a:hover {
        color: #fff;
        text-decoration: none;
    }

    .logo-pje {
        margin: 10px;
    }

    .logo-processo {
        display: flex;
    }

</style>