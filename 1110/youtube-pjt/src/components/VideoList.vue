<template>
  <div>
    <ul>
      <VideoListItem
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
        @select-video="onSelectVideo"
      >
      </VideoListItem>
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array
  },
}
</script>

<style>

</style>