<script setup>
import logo from '@/assets/image/logo.svg';
</script>

<template>
  <header class="fixed w-full flex justify-center bg-[#032541] z-50 top-0 left-0 items-center h-16 p-4">
    <div class="flex justify-center max-w-[1400px] w-full">
      <div class="flex justify-between relative w-full top-0 left-0 px-4 lg:px-[40px]">
        <!-- Logo and navigation -->
        <div class="flex justify-start items-center">
          <a class="mr-4 w-[154px] h-5 font-semibold">
            <img :src="logo" alt="The Movie Database" width="154" height="20">
          </a>
          <!-- Desktop navigation -->
          <ul class="hidden lg:flex py-2 flex-row">
            <li class="mr-[15px] font-normal">
              <a class="text-white flex gap-2">
                <span>Movies</span>
              </a>
            </li>
            <li class="mr-[15px] font-normal">
              <a class="text-white flex gap-2">
                <span>TV Shows</span>
              </a>
            </li>
            <li class="mr-[15px] font-normal">
              <a class="text-white flex gap-2">
                <span>People</span>
              </a>
            </li>
            <li class="mr-[15px] font-normal">
              <a class="text-white flex gap-2">
                <span>More</span>
              </a>
            </li>
          </ul>
        </div>
        <!-- Mobile menu toggle -->
        <button class="lg:hidden text-white" @click="toggleMenu = !toggleMenu">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
          </svg>
        </button>
        <!-- Mobile navigation -->
        <div v-if="toggleMenu" class="absolute top-16 left-0 w-full bg-[#032541] z-40 lg:hidden">
          <ul class="flex flex-col p-4">
            <li class="mb-2 font-normal">
              <a class="text-white flex gap-2">
                <span>Movies</span>
              </a>
            </li>
            <li class="mb-2 font-normal">
              <a class="text-white flex gap-2">
                <span>TV Shows</span>
              </a>
            </li>
            <li class="mb-2 font-normal">
              <a class="text-white flex gap-2">
                <span>People</span>
              </a>
            </li>
            <li class="mb-2 font-normal">
              <a class="text-white flex gap-2">
                <span>More</span>
              </a>
            </li>
          </ul>
        </div>
        <!-- Right-side actions -->
        <div class="hidden lg:flex">
          <ul class="flex items-center">
            <li class="ml-[30px] flex items-center">
              <a class="h-full">
                <span class="text-white">Add Movie</span>
              </a>
            </li>
            <li class="ml-[30px] text-white">
              <div class="h-[26px] w-[28px] border rounded-[3px] py-[3px] px-[4px] flex items-center uppercase text-sm">en</div>
            </li>
            <li class="ml-[30px] text-white">
              <a href="/login" aria-label="Login">Login</a>
            </li>
            <li class="ml-[30px] text-white">
              <a href="/signup" aria-label="Join TMDB">Join TMDB</a>
            </li>
            <li class="ml-[30px] glyph search_buttons">
              <a class="search" href="/search" aria-label="Search">
                <span class="glyphicons_v2 search blue"></span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import { ref } from 'vue';
const toggleMenu = ref(false);
</script>
