<template>
    <header>
        <div class="header_container">
            <div class="header_main_logo_block">
                <router-link to="/">
                    <div class="avatar_logo"></div>
                </router-link>
                <router-link to="/">
                    <div class="name_logo"></div>
                </router-link>
            </div>
            <div class="header_main_list_block">
                <ul class="list_categories_block">
                    <li class="list">
                        <router-link to="/">Home</router-link>
                    </li>
                    <li class="list">
                        <router-link to="/about-us">About us</router-link>
                    </li>
                    <li class="list">
                        <router-link to="/articles">Articles</router-link>
                    </li>
                    <li class="list">
                        <router-link to="/blog">Blog</router-link>
                    </li>
                    <li class="list">
                        <router-link to="/tests">Tests</router-link>
                    </li>
                    <li class="list" v-if="!auth">
                        <router-link to="/auth/sign-up">Log in/Sign up</router-link>
                    </li>
                    <li class="list" v-if="auth">
                        <router-link to="/profile">{{ fullname }}</router-link>
                    </li>
                    <li class="list">
                        <img src="@/images/english_version.png" alt="">
                    </li>
                </ul>
            </div>
        </div>
    </header>
</template>

<script lang="ts">
import {useStore} from "vuex";
import {computed, onMounted, ref} from "vue";

export default {
    name: "NavPage",
    setup() {

        const store = useStore();
        const fullname = ref('');
        const auth = computed(() => store.state.authenticated);

        onMounted(async () => {
            try {
                const response = await fetch('http://localhost:8000/api/auth/user', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    credentials: 'include'
                });

                const content = await response.json();
                fullname.value = content.fullname

                await store.dispatch('setAuth', true);
            } catch (e) {
                await store.dispatch('setAuth', false);
            }
        });

        const logout = async () => {
            await fetch('http://localhost:8000/api/auth/sign-out', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                credentials: 'include'
            });
        };

        return {
            fullname,
            auth,
            logout
        }
    }
}
</script>

<style>
    .header_container {
        background-color: #FFF;
        display: flex;
        align-items: center;
        padding: 10px 20px;
        justify-content: space-between;
        z-index: 2;
    }

    .header_main_logo_block, .list_categories_block {
        display: flex;
        align-items: center;
    }

    .header_main_logo_block {
        justify-content: flex-start;
    }

    .avatar_logo {
        width: 90px;
        height: 60px;
        background-image: url('@/images/avatar.png');
    }

    .name_logo {
        width: 260px;
        height: 60px;
        background-image: url('@/images/logo.png');
    }

    .avatar_logo, .name_logo {
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }

    .list_categories_block {
        justify-content: flex-end;
        list-style: none;
    }

    .list {
        margin-left: 30px;
    }

    .list a {
        font-family: "Inter", serif;
        font-style: normal;
        font-weight: 400;
        font-size: 20px;
        line-height: 29px;
        color: #000;
        text-decoration: none;
    }

    .list img {
        cursor: pointer;
        width: 30px;
        height: 20px;
    }

</style>