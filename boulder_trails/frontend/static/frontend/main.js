// author: Harold Ainsworth

// app initialization options
const BoulderTrailsApp = {
    data() {
        return {
            trails: null,
            segments: null,
        }
    },
    mounted() {
        axios({ method: "GET", "url": "http://localhost:8000/trails" }).then(result => {
            console.log(result)
        }, error => {
            console.error(error);
        })
    }
}


// create app
const app = Vue.createApp(BoulderTrailsApp).mount('#BoulderTrailsApp')