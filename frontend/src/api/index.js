import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://127.0.0.1:5000'
})

export function register() {
    return instance.post('auth/register', data)
}

export function login(data) {
    return instance.post('auth/login', data)
}

export function logout() {
    return instance.get('auth/logout')
}