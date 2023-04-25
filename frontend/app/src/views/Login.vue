<template>
    <div class="authorization_block_container">
        <form @submit.prevent="submit">
            <h1 class="h3 mb-3 fw-normal">Sign in</h1>

            <input v-model="data.email" type="email" class="form-control" placeholder="Email" required>
            <input v-model="data.password" type="password" class="form-control" placeholder="Password" required>

            <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
        </form>
    </div>
</template>

<script lang="ts">
import {reactive} from "vue";
import {useRouter} from "vue-router";

export default {
    name: "Login-Page",
    setup() {
        const data = reactive({
            email: '',
            password: ''
        });

        const router = useRouter();

        const submit = async () => {
            await fetch('http://localhost:8000/api/auth/sign-in', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials: 'include',
                body: JSON.stringify(data)
            });

            await router.push('/');
        }

        return {
            data,
            submit
        }
    }
}
</script>

<style scoped>

</style>