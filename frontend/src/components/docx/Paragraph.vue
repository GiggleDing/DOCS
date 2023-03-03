<script>
import Word from './Word.vue'
export default {
    components: {
        Word
    },
    props: {
        pp: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            "paragraph": this.pp.paragraph
        }
    },
    computed: {
        
    }
}
</script>
<template>
    <a-typography-paragraph>
        <Word v-for="item in paragraph" :ziiiii="item"/>
    </a-typography-paragraph>
</template>