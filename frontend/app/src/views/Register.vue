<template>
    <form>
        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

        <input type="text" class="form-control" placeholder="Full name" required>
        <input type="email" class="form-control" placeholder="Email" required>
        <input type="password" class="form-control" placeholder="Password" required>

        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
    </form>
</template>

<script lang="ts">
import {reactive} from 'vue';

export default {
    name: `Register`,
    setup() {
        const data = reactive({
            fullname: '',
            email: '',
            password: ''
        });

        return {
            data
        }
    }
}
</script>

<style scoped>

</style>