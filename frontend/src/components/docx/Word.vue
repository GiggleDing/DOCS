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
            return this.word.bold
        },
        getColor() {
            const color = this.word.color;
            if (color && Array.isArray(color)) {
                return `rgb(${color.join(",")})`;
            } else if (color && typeof color === "number") {
                return `rgb(${color},${color},${color})`;
            } else {
                return color;
            }
        }
    }
}
</script>
<template>
    <span>
        <a-typography-text :bold="isBold" :color="getColor">
            {{ word.text }}
        </a-typography-text>
    </span>
</template>