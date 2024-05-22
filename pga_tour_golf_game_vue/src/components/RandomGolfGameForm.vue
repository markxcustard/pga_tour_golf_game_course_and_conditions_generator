<template>
    <div id="app">
      <h1>PGA Tour Golf Game</h1>
      <button @click="generateRandomGame" class="random-button">Generate Random Game</button>
  
      <div v-if="generatedGame" class="game-info">
        <h2>Generated Golf Game Information:</h2>
        <ul>
          <li><strong>Course:</strong> {{ generatedGame.Course }}</li>
          <li><strong>Crowd:</strong> {{ generatedGame.Crowd }}</li>
          <li><strong>Time of Day:</strong> {{ generatedGame['Time of Day'] }}</li>
          <li><strong>Tee:</strong> {{ generatedGame.Tee }}</li>
          <li><strong>Pin:</strong> {{ generatedGame.Pin }}</li>
          <li><strong>Wind Speed:</strong> {{ generatedGame['Wind Speed'] }}</li>
          <li><strong>Wind Direction:</strong> {{ generatedGame['Wind Direction'] }}</li>
          <li><strong>Green Firmness:</strong> {{ generatedGame['Green Firmness'] }}</li>
          <li><strong>Green Speed:</strong> {{ generatedGame['Green Speed'] }}</li>
          <li><strong>Fringe Firmness:</strong> {{ generatedGame['Fringe Firmness'] }}</li>
          <li><strong>Fringe Speed:</strong> {{ generatedGame['Fringe Speed'] }}</li>
          <li><strong>Fairway Firmness:</strong> {{ generatedGame['Fairway Firmness'] }}</li>
          <li><strong>Fairway Speed:</strong> {{ generatedGame['Fairway Speed'] }}</li>
          <li><strong>First Cut Firmness:</strong> {{ generatedGame['First Cut Firmness'] }}</li>
          <li><strong>First Cut Length:</strong> {{ generatedGame['First Cut Length'] }}</li>
          <li><strong>Second Cut Firmness:</strong> {{ generatedGame['Second Cut Firmness'] }}</li>
          <li><strong>Second Cut Length:</strong> {{ generatedGame['Second Cut Length'] }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  // Import the generateCourseInfo function from golf_game_generator.py
  import { generateCourseInfo } from '../golf_game_generator.py';
  
  export default {
    name: "RandomGolfGameForm",
    data() {
      return {
        generatedGame: null
      };
    },
    methods: {
      generateRandomGame() {
        // Call the generateCourseInfo function to get the golf game information
        this.generatedGame = generateCourseInfo();
      }
    }
  };
  </script>
  
  <style>
  /* Add your styles here */
  .random-button {
    margin-bottom: 20px;
  }
  .game-info {
    border: 1px solid #ccc;
    padding: 10px;
    margin-top: 20px;
  }
  </style>
  