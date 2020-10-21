<template>
	<div id="app">
		<Header title="Desafio 1 - Time 9 Inova Ixtepô" :hideToggle="false"
			:hideUserDropdown="false"/>
		<Content />
		<Footer />
	</div>
</template>

<script>

import Header from "@/components/template/Header";

import Content from "@/components/template/Content";
import Footer from "@/components/template/Footer";

export default {
	name: "App",
	components: { Header, Content, Footer }
}
</script>

<style>

	* {
		font-family: "Lato", sans-serif;
	}

	body {
		margin: 0;

	}

	#app {
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;

		height: 100vh;
		display: grid;
		grid-template-rows: 60px 1fr 40px;
		grid-template-columns: 1fr;
		grid-template-areas:
			"header"
			"content"
			"footer"
	}

</style>