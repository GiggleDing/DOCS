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
            return this.word.properties.bold
        },
        isUnderline() {
            return this.word.properties.underline
        },
        getColor() {
            const color = this.word.properties.color;
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
        <a-typography-text :bold="isBold" :underline="isUnderline" :color="getColor">
            {{ word.text }}
        </a-typography-text>
    </span>
</template>