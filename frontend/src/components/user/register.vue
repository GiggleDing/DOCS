<script>
import axios from 'axios'

export default{
    data() {
        return {
            form: {
                "username": "",
                "password": ""
            },
            usernameRules: {
                required: true,
                match: /^[a-zA-Z][a-zA-Z0-9]{5,7}$/
            },
            passwordRules: {
                required: true,
                match: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,10}$/
            }
        }
    },
    methods: {
        handleSubmit() {
            axios.post('http://127.0.0.1:5000/auth/register', {
                username: this.form.username,
                password: this.form.password
            })
                .then(response => {
                    this.$router.push('/')
                })
        }
    },
    mounted() {
        
    },
    computed: {
        
    }
}
</script>

<template>
    <h1>注册</h1>
    <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
        <a-form-item :rules="usernameRules" field="username" tooltip="请输入6～8位字母、数字组合，且不能以数字开头" label="Username">
            <a-input v-model="form.username" placeholder="Please enter your username..." allow-clear />
        </a-form-item>
        <a-form-item :rules="passwordRules" field="password" tooltip="请输入6～10位字母、数字组合" label="Password">
            <a-input-password v-model="form.password" placeholder="Please enter your password..." allow-clear />
        </a-form-item>
        <a-form-item>
            <a-button html-type="subbmit">Submmit</a-button>
        </a-form-item>
    </a-form>
</template>