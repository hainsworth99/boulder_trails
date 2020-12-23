// basic app creation and mount app on DOM element
const Counter = {
  data() {
    return {
      counter: 0
    }
  },
  mounted() {
    setInterval(() => {
      this.counter++
    }, 1000)
  }
}
Vue.createApp(Counter).mount('#counter')

// loading data
const AttributeBinding = {
  data() {
    return {
      message: 'You loaded this page on ' + new Date().toLocaleString()
    }
  }
}
Vue.createApp(AttributeBinding).mount('#bind-attribute')

// event handling
const EventHandling = {
  data() {
    return {
      message: 'Hello Vue.js!'
    }
  },
  methods: {
    reverseMessage() {
      this.message = this.message
        .split('')
        .reverse()
        .join('')
    }
  }
}
Vue.createApp(EventHandling).mount('#event-handling')

// two way binding
const TwoWayBinding = {
  data() {
    return {
      message: 'Hello Vue!'
    }
  }
}
Vue.createApp(TwoWayBinding).mount('#two-way-binding')

// conditional rendering
const ConditionalRendering = {
  data() {
    return {
      seen: true // if changed to false, won't render
    }
  }
}
Vue.createApp(ConditionalRendering).mount('#conditional-rendering')

// for each rendering
const ListRendering = {
  data() {
    return {
      todos: [
        { text: 'Learn JavaScript' },
        { text: 'Learn Vue' },
        { text: 'Build something awesome' }
      ]
    }
  }
}
Vue.createApp(ListRendering).mount('#list-rendering')

// components
const TodoList = {
  data() {
    return {
      listName: 'My Grocery List',
      groceryList: [
        { id: 0, text: 'Vegetables' },
        { id: 1, text: 'Cheese' },
        { id: 2, text: 'Whatever else humans are supposed to eat' }
      ]
    }
  }
}
const app = Vue.createApp(TodoList)
app.component('todo-item', {
  props: ['todo'],
  template: `<li>{{ todo.text }}</li>`
})
app.mount('#todo-list-app')