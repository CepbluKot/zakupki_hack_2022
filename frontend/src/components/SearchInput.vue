<template>
  <div>
    <v-text-field
        solo
        @input="handleInput"
        append-icon="mdi-magnify"
        :label="label"
        :placeholder="placeholder"
    />
  </div>
</template>

<script>
export default {
  name: 'SearchInput',
  prop: [
    'value'
  ],
  props: [
    'placeholder',
    'label'
  ],
  data() {
    return {
      content: this.value
    }
  },
  methods: {
    handleInput() {
      this.$emit('input', this.content)
    }
  }
}
</script>