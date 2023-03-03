<script>
export default {
    props: {
        ziiiii: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            word: this.ziiiii
        }
    },
    computed: {
        isBold() {
            if(this.word.bold === 1)
                return true
            else
                return false
        },
        getColor() {
            const color = this.word.color;
            if (color && typeof color === "string" && color.length === 6) {
                return `#${color}`;
            } else {
                return null;
            }
        }
    }
}
</script>
<template>
    <span>
            <a-typography-text :bold="isBold">
                {{ word.text }}
            </a-typography-text>
    </span>
</template>