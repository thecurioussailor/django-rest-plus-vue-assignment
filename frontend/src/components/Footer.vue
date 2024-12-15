<template>
    <footer class="max-w-full w-[100vw] bg-no-repeat bg-top bg-footer-gradient bg-cover text-white py-10">
      <nav class="flex flex-col items-center md:flex-row md:justify-between px-4 md:px-10">
        <div class="text-center mb-8 md:mb-0 md:-top-9">
          <img class="mx-auto" :src="footLogo" alt="The Movie Database (TMDB)" width="130" height="94">
          <a class="mt-6 inline-block text-[#01B4E4] bg-white text-[1em] font-bold py-2 px-6 rounded" href="/signup">Join the Community</a>
        </div>
        <div class="grid grid-cols-2 gap-8 md:flex md:space-x-10">
          <div>
            <h3 class="text-lg font-bold uppercase">The Basics</h3>
            <ul>
              <li class="mt-2"><a href="/about" class="text-sm">About TMDB</a></li>
              <li class="mt-2"><a href="/about/staying-in-touch" class="text-sm">Contact Us</a></li>
              <li class="mt-2"><a href="/talk" class="text-sm">Support Forums</a></li>
              <li class="mt-2"><a href="https://developer.themoviedb.org/docs" target="_blank" class="text-sm">API</a></li>
              <li class="mt-2"><a href="https://status.themoviedb.org/" target="_blank" rel="noopener" class="text-sm">System Status</a></li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-bold uppercase">Get Involved</h3>
            <ul>
              <li class="mt-2"><a href="/about" class="text-sm">Contribution Bible</a></li>
              <li class="mt-2"><a href="/about/staying-in-touch" class="text-sm">Add New Movie</a></li>
              <li class="mt-2"><a href="/talk" class="text-sm">Add New TV Show</a></li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-bold uppercase">Community</h3>
            <ul>
              <li class="mt-2"><a href="/about" class="text-sm">Guidelines</a></li>
              <li class="mt-2"><a href="/about/staying-in-touch" class="text-sm">Discussions</a></li>
              <li class="mt-2"><a href="/talk" class="text-sm">Leaderboard</a></li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-bold uppercase">Terms of Use</h3>
            <ul>
              <li class="mt-2"><a href="/about" class="text-sm">API Terms of Use</a></li>
              <li class="mt-2"><a href="/about/staying-in-touch" class="text-sm">Privacy Policy</a></li>
              <li class="mt-2"><a href="/talk" class="text-sm">DMCA Policy</a></li>
            </ul>
          </div>
        </div>
      </nav>
      <section class="text-center mt-10 text-[0.7em] opacity-70">Build 87d8563 (8296)</section>
    </footer>
  </template>
  
  <script setup>
  import footLogo from '@/assets/image/footerlogo.svg'
  </script>
  
  <style>
  /* Add specific styles if needed */
  </style>
  