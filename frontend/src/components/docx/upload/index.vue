<script>
import { useUserStore } from '../../../store'
export default {
    data() {
        return {
            userStore: useUserStore()
        }
    },
    methods: {
        logout() {
            this.userStore.logout()
        }
    }
}
</script>

<template>
    <div>
        <a-button type="primary" @click="logout">登出</a-button>
    </div>
</template>