<script>
import { defineComponent } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'

export default {
	methods: {
		onClickMenuItem(key) {
			Message.info({ content: `You select ${key}`, showIcon: true})
		}
	}
}
</script>

<template>
	<a-layout class="layout">
		<a-layout-sider collapsible breakpoint="xl">
			<div class="logo" />
			<nav>
			<a-menu
				:default-open-keys="['1']"
				:default-selected-keys="['0_3']"
				:style="{ width: '100% '}"
				@menu-item-click="onClickMenuItem">
				<RouterLink to="/">
					<a-menu-item key="0_1">
						<IconHome></IconHome>
						Home
					</a-menu-item>
				</RouterLink>
				<RouterLink to="/about">
					<a-menu-item key="0_2">
						<IconCalendar></IconCalendar>
						上传文件
					</a-menu-item>
				</RouterLink>
				<RouterLink to="/test">
					<a-menu-item key="0_3">
						<IconCalendar></IconCalendar>
						分析结果
					</a-menu-item>
				</RouterLink>
				<a-sub-menu key="1">
					<template #title>
						<IconCalendar></IconCalendar>
						Navigation 1
					</template>
					<a-menu-item key="1_1">Menu 1</a-menu-item>
					<a-menu-item key="1_2">Menu 2</a-menu-item>
					<a-sub-menu key="2" title="Navigation 2">
						<a-menu-item key="2_1">Menu 1</a-menu-item>
						<a-menu-item key="2_2">Menu 2</a-menu-item>
					</a-sub-menu>
					<a-sub-menu key="3" title="Navigation 3">
						<a-menu-item key="3_1">Menu 1</a-menu-item>
						<a-menu-item key="3_2">Menu 2</a-menu-item>
						<a-menu-item key="3_3">Menu 3</a-menu-item>
					</a-sub-menu>
				</a-sub-menu>
				<a-sub-menu key="4">
					<template #title>
						<IconCalendar></IconCalendar> Navigation 4
					</template>
					<a-menu-item key="4_1">Menu 1</a-menu-item>
					<a-menu-item key="4_2">Menu 2</a-menu-item>
					<a-menu-item key="4_3">Menu 3</a-menu-item>
					<a-menu-item key="4_4">Menu 4</a-menu-item>
				</a-sub-menu>
			</a-menu>
			</nav>
			<template #trigger="{ collapsed }">
				<IconCaretRight v-if="collapsed"></IconCaretRight>
				<IconCaretLeft v-else></IconCaretLeft>
			</template>
		</a-layout-sider>
		<a-layout>
			<a-layout-header style="padding-left: 20px">
				Header
			</a-layout-header>
			<a-layout style="padding: 0 24px">
				<a-breadcrumb :style="{ margin: '16px 0' }">
					<a-breadcrumb-item>Home</a-breadcrumb-item>
					<a-breadcrumb-item>List</a-breadcrumb-item>
					<a-breadcrumb-item>App</a-breadcrumb-item>
				</a-breadcrumb>
				<a-layout-content>
					<RouterView />
				</a-layout-content>
				<a-layout-footer>Footer</a-layout-footer>
			</a-layout>
		</a-layout>
	</a-layout>
</template>

<style scoped>
.layout {
	height: 500px;
	background: var(--color-fill-2);
	border: 1px solid var(--color-border);
}
.layout :deep(.arco-layout-sider) .logo {
	height: 32px;
	margin: 12px 8px;
	background: rgba(255, 255, 255, 0.2);
}
.layout :deep(.arco-layout-sider-light) .logo {
	background: var(--color-fill-2);
}
.layout :deep(.arco-layout-header) {
	height: 64px;
	line-height: 64px;
	background: var(--color-bg-3);
}
.layout :deep(.arco-layout-footer) {
	height: 48px;
	color: var(--color-text-2);
	font-weight: 400;
	font-size: 14px;
	line-height: 48px;
}
.layout :deep(.arco-layout-content) {
	color: var(--color-text-2);
	font-weight: 400;
	font-size: 14px;
	background: var(--color-bg-3);
}
.layout :deep(.arco-layout-footer),
.layout :deep(.arco-layout-content) {
	display: flex;
	flex-direction: column;
	justify-content: center;
	color: var(--color-white);
	font-size: 16px;
	font-stretch: condensed;
	text-align: center;
}
</style>
