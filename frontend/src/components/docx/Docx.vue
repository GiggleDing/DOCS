<script>
import Paragraph from './Paragraph.vue'
export default {
    components: {
        Paragraph
    },
    data() {
        return {
            "docx": [
                {
                    "paragraph": [
                        {
                            "text": "Lorem Ipsum",
                            "properties": {},
                            "color": [
                                0,
                                0,
                                0
                            ]
                        },
                        {
                            "text": "\u00a0is simply ",
                            "properties": {},
                            "color": [
                                0,
                                0,
                                0
                            ]
                        },
                        {
                            "text": "dummy",
                            "properties": {
                                "underline": true,
                                "bold": true
                            },
                            "color": [
                                255,
                                0,
                                0
                            ]
                        },
                        {
                            "text": " text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                            "properties": {},
                            "color": [
                                0,
                                0,
                                0
                            ]
                        }
                    ]
                },
                {
                    "paragraph": [
                        {
                            "text": "Lorem Ipsum",
                            "properties": {},
                            "color": [
                                0,
                                0,
                                0
                            ]
                        },
                        {
                            "text": "\u00a0is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                            "properties": {},
                            "color": [
                                0,
                                0,
                                0
                            ]
                        }
                    ]
                },
                {
                    "paragraph": [
                        {
                            "text": "Lorem Ipsum",
                            "properties": {},
                            "color": [
                                0,
                                0,
                                0
                            ]
                        },
                        {
                            "text": "\u00a0is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                            "properties": {},
                            "color": [
                                0,
                                0,
                                0
                            ]
                        }
                    ]
                },
                {
                    "paragraph": []
                }
            ]
        }
    },
    computed: {
        
    }
}
</script>
<template>
    <a-typography>
        <Paragraph v-for="item in docx" :pp="item"/>
    </a-typography>
</template>