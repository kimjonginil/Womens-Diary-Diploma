<template>
    <form>
        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

        <input type="email" class="form-control" id="floatingInput" placeholder="Email" required>
        <input type="password" class="form-control" id="floatingPassword" placeholder="Password" required>

        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
    </form>
</template>

<script>
export default {
    name: `Login`
}
</script>

<style scoped>

</style>