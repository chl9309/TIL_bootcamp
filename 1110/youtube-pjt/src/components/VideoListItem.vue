<template>
  <li @click="selectVideo">
    <img
      :src="video.snippet.thumbnails.default.url"
    >
    {{ video.snippet.title | stringUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object
  },
  methods: {
    selectVideo() {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    thumbnailImgUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    stringUnescape() {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>

</style>