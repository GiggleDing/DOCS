<script>
export default {
	data() {
		return {
			content: "",
			docx: [
				{
					"paragraph": [
						{
							"text": "\u8fd9\u4e16\u754c",
							"properties": {
								"bold": true
							},
							"color": null
						},
						{
							"text": "\u603b\u8fd9\u6837\uff0c\u8001\u8fd9\u6837\u2014\u2014",
							"properties": {},
							"color": null
						}
					]
				},
				{
					"paragraph": [
						{
							"text": "\u89c2",
							"properties": {},
							"color": [
								255,
								0,
								0
							]
						},
						{
							"text": "\u97f3",
							"properties": {
								"bold": true
							},
							"color": [
								255,
								0,
								0
							]
						},
						{
							"text": "\u5728\u8fdc\u8fdc",
							"properties": {},
							"color": null
						},
						{
							"text": "\u7684\u5c71\u4e0a",
							"properties": {
								"italic": true
							},
							"color": null
						},
						{
							"text": "\uff0c\u7f42\u7c9f\u5728",
							"properties": {},
							"color": null
						},
						{
							"text": "\u7f42\u7c9f",
							"properties": {
								"underline": true
							},
							"color": null
						},
						{
							"text": "\u7684\u7530\u91cc\u3002",
							"properties": {},
							"color": null
						}
					]
				}
			]
		}
	},
	methods: {
		async onFileChange(event) {
			const file = event.target.files[0];
			const reader = new FileReader();

			reader.onload = () => {
				const parser = new DOMParser();
				const xml = parser.parseFromString(reader.result, "text/xml");
				this.content = this.xmlToString(xml);
			};

			reader.readAsText(file);
		},
		xmlToString(xml) {
			console.log(xml)
			const serializer = new XMLSerializer();
			console.log(serializer.serializeToString(xml))
			return serializer.serializeToString(xml);
		}
	}
}
</script>
<template>
	<div>
		<a-typographu>
			<a-typography-paragraph v-for="item in docx">
				<span v-for="i in item.paragraph">
					<span v-if="i.properties.bold">
						<a-typography-text bold>
							{{ i.text }}
						</a-typography-text>
					</span>
					<span v-else-if="i.properties.italic">
						<a-typography-text><i>
							{{ i.text }}
						</i>
						</a-typography-text>
					</span>
					<span v-else-if="i.properties.underline">
						<a-typography-text underline>
							{{ i.text }}
						</a-typography-text>
					</span>
					<span v-else>
						<a-typography-text >
							{{ i.text }}
						</a-typography-text>
					</span>
				</span>
			</a-typography-paragraph>
		</a-typographu>
	</div>
</template>