<template>
    <div id="app">
        <Nav/>
    </div>

    <main class="form-signin w-100 m-auto">
        <router-view/>
    </main>
</template>

<script>
    import Nav from "@/components/Nav";

    export default {
        components: {Nav}
    }
</script>

<style>
    .form-signin {
        max-width: 330px;
        padding: 15px;
    }

    .form-signin input[type="email"] {
        margin-bottom: -1px;
        border-bottom-right-radius: 0;
        border-bottom-left-radius: 0;
    }

    .form-signin input[type="password"] {
        margin-bottom: 10px;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
    }
</style>
