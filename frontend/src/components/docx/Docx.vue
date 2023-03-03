<script>
import axios from 'axios'
import Paragraph from './Paragraph.vue'
export default {
    components: {
        Paragraph
    },
    data() {
        return {
            docx: null
        }
    },
    methods: {

    },
    computed: {
        
    },
    mounted() {
        axios
            .get('http://127.0.0.1:5000')
            .then(response => (this.docx = response.data))
            .catch(function(error) {
                console.log(error)
            })
    }
}
</script>
<template>
    <a-typography>
        <Paragraph v-for="item in docx" :pp="item"/>
    </a-typography>
</template>