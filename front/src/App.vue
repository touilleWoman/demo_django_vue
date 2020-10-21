<template>
  <div id="app">
    <p>Here is your plan for next week:</p>
    <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo"/>
  </div>
</template>

<script>
import Todos from './components/Todos'

export default {
  name: 'App',
  components: {
    Todos
  },
  data: function() {
    return {
      todos:[
        {
          id:1,
          title: "task 1",
          content: "mail alert system",
          completed: false
        },
        {
          id:2,
          title: "task 2",
          content: "make a new componant",
          completed: true         
        }
      ]
    }
  },
  methods: {
    deleteTodo(id) {
      this.todos = this.todos.filter(todo => todo.id !== id)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
