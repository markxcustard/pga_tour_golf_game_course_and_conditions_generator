<template>
  <div id="app">
    <h1>PGA Tour Golf Game</h1>
    <RandomGolfGameForm />
  </div>
</template>

<script>
import RandomGolfGameForm from "@/components/RandomGolfGameForm.vue";
import { generateCourseInfo } from '../../golf_game_generator.py';

export default {
  name: "App",
  components: {
    RandomGolfGameForm
  },
  // Provide a method to generate course information
  methods: {
    generateCourseInfo() {
      // Call the generateCourseInfo function to get the golf game information
      return generateCourseInfo();
    }
  }
};
</script>

<style>
/* Add your styles here */
</style>
