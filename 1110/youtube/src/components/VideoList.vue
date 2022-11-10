<template>
  <div>
    <h1>VideoList</h1>
    <VideoListItem/>
    <VideoListItem/>
    <VideoListItem/>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
}
</script>

<style>

</style>