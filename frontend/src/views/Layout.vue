<script>
import { Message } from '@arco-design/web-vue';
export default{
    methods: {
		onClickMenuItem(key) {
			Message.info({ content: `You select ${key}`, showIcon: true})
		}
	},
    mounted() {
		
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
				:default-selected-keys="['1']"
				:style="{ width: '100% '}"
				@menu-item-click="onClickMenuItem">
				<RouterLink to="/">
					<a-menu-item key="1">
						<IconHome></IconHome>
						Home
					</a-menu-item>
				</RouterLink>
				<RouterLink to="/user/GiggleDing">
					<a-menu-item key="2">
						<IconCalendar></IconCalendar>
						我的
					</a-menu-item>
				</RouterLink>
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
				<!-- TODO: 更改 breadcrumb -->
				<a-breadcrumb :style="{ margin: '16px 0' }">
					<a-breadcrumb-item>Home</a-breadcrumb-item>
					<a-breadcrumb-item>List</a-breadcrumb-item>
					<a-breadcrumb-item>App</a-breadcrumb-item>
				</a-breadcrumb>
				<a-layout-content>
					<RouterView />
				</a-layout-content>
				<a-layout-footer>Designed by Giggle Ding</a-layout-footer>
			</a-layout>
		</a-layout>
	</a-layout>
</template>

<style scoped>
.layout {
	height: 95vh;
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
	/* color: var(--color-white); */
	font-size: 16px;
	font-stretch: condensed;
	text-align: center;
}
</style>