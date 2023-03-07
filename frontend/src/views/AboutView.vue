<script>
import axios from 'axios'
import { Message} from '@arco-design/web-vue';

export default {
	data() {
		return {
			fileData: null
		}
	},
	methods: {
		async upload(e) {
			try{
				const file = e.target.files[0]
				this.fileData = new FormData()
				this.fileData.append('file', file)
				console.log(this.fileData.get('file'))
				const response = await axios.post('http://127.0.0.1:5000/docx/upload', this.fileData)
				Message.info({ content: `${response}`, showIcon: true})
				console.log(response.data)
			} catch(error) {
				console.log(error)
			}
		}
	}
}
</script>
<template>
	<a-space direction="vertical" :style="{ width: '100%'}">
		<a-upload action="http://127.0.0.1:5000/docx/upload" @change="upload"/>
	</a-space>
</template>