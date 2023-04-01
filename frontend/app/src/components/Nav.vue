<template>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
        <div class="container-fluid">
            <router-link to="/" class="navbar-brand" href="#">Home</router-link>

            <div>
                <ul class="navbar-nav me-auto mb-2 mb-md-0">
                    <li class="nav-item">
                        <router-link to="/auth/sign-in" class="nav-link" aria-current="page" href="#">Login</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="auth/sign-up" class="nav-link" href="#">Register</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: `Nav`
}
</script>