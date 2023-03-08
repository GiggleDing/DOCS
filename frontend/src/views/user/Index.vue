<script>
export default {

}
</script>
<template>
    <div>
        <h2>User Index</h2>
        <p>Welcome, {{ $route.params.username }}</p>
        <RouterView></RouterView>
    </div>
</template>