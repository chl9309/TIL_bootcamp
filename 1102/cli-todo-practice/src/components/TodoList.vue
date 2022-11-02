<template>
  <div>
    <ul v-for="(todo, index) in todos" :key="index">
      <TodoListItem :todo="todo" @delete-todo='deleteTodo'/>
    </ul>
    <h1>TodoList</h1>
    {{ todos }}
    <TodoListItem/>
  </div>
</template>

<script>
import TodoLIstItem from '@/components/TodoListItem'
export default {
  name: 'TodoList',
  compoonents: {
    TodoLIstItem,
  },
  props: {
    todos: Array,
  },
  methods: {
    deleteTodo: function (todo) {
        this.$emit('delete-todo', todo)
    }
  }
}
</script>

<style>

</style>