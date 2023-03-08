import { defineStore } from "pinia"
import { setToken, clearToken } from "../../../utils/auth"
import {
    login as userLogin,
    logout as userLogout
} from '../../../api'

const useUserStore = defineStore('user', {
    state: () => {
        return {
            username: undefined
        }
    },
    getters: {

    },
    actions: {
        async login(loginForm) {
            try{
                const res = await userLogin(loginForm)
                setToken(res.data.session_id)
            } catch(err) {
                clearToken()
                throw err
            }
        },
        async logout() {
            try {
                await userLogout()
            } finally {
                clearToken()
            }
        }
    }
})

export default useUserStore