<template>
    <div class="authorization_block_container">
        <form @submit.prevent="submit">
            <h1 class="h3 mb-3 fw-normal">Sign up</h1>

            <input v-model="data.fullname" type="text" class="form-control" placeholder="Full name" required>
            <input v-model="data.email" type="email" class="form-control" placeholder="Email" required>
            <input v-model="data.password" type="password" class="form-control" placeholder="Password" required>

            <button class="w-100 btn btn-lg btn-primary" type="submit">Sign up</button>
        </form>
    </div>
</template>

<script lang="ts">
import {reactive} from 'vue';
import {useRouter} from "vue-router";

export default {
    name: "Register-Page",
    setup() {
        const data = reactive({
            fullname: '',
            email: '',
            password: ''
        });

        const router = useRouter();

        const submit = async () => {
            await fetch('http://localhost:8000/api/auth/sign-up', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            await router.push('/auth/sign-in');
        }

        return {
            data,
            submit
        }
    }
}
</script>

<style>
    .authorization_block_container {
        padding: 100px 500px;
    }

    .authorization_block_container form input {
        margin-top: 20px;
    }

    .authorization_block_container form button {
        margin-top: 50px;
        font-size: 16px;
    }
</style>