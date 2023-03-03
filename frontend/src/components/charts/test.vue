<script>
import * as echarts from 'echarts'

export default {
    data() {

    },
    methods: {
        
    },
    mounted() {
        var myCharts = echarts.init(document.getElementById('main'))
        myCharts.setOption({
            title: {
                text: 'Echarts 入门示例'
            },
            tooltip: {},
            xAxis: {
                data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
            },
            yAxis: {},
            series: [
                {
                    name: '销量',
                    type: 'bar',
                    data: [5, 20, 36, 10, 10, 20]
                }
            ]
        })
    }
}
</script>
<template>
    <div style="width: 600px; height: 400px;" id="main"></div>
</template>