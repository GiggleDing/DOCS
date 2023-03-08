import { defineStore } from "pinia"
import { clearToken } from "../../../utils/auth"
import {
    login as userLogin
} from '../../../api/user'

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
                setToken(res.data.token)
            } catch(err) {
                clearToken()
                throw err
            }
        }
    }
})

export default useUserStore