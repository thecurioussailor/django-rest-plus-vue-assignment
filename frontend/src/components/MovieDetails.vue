<script setup>
    import movieImage from '@/assets/image/movieimage.jpg'
    import moviePortrait from '@/assets/image/movieportrait.jpg'
    import chrispratt from '@/assets/image/chrispratt.jpg'
    import zoesaldana from '@/assets/image/zoesaldana.jpg'
    import davebautista from '@/assets/image/davebautista.jpg'
    import vin from '@/assets/image/vin.jpg'
    import karen from '@/assets/image/karen.jpg'
    import kurt from '@/assets/image/kurt.jpg'
    import bradly from '@/assets/image/bradly.jpg'
    import emo1 from '@/assets/image/emo1.svg'
    import emo2 from '@/assets/image/emo2.svg'
    import emo3 from '@/assets/image/emo3.svg'
    import { ref, onMounted } from 'vue'
    import axios from 'axios'

    const movieData = ref({});
    onMounted( async () => {
        try{
            const response = await axios.get("https://www.omdbapi.com/?i=tt3896198&apikey=d2132124");
            movieData.value = response.data;
        }catch(error){
            console.error("Error fetching movie details", error)
        }
    })
</script>
<template>
    <div class="bg-movie-image bg-cover bg-no-repeat flex flex-col md:flex-row justify-center flex-wrap">
        <div class="flex justify-center bg-custom-gradient flex-wrap w-full z-0">
            <div class="py-5 px-6 md:py-[30px] md:px-[40px] max-w-[1400px] w-full">
                <section class="text-white w-full flex flex-col items-center md:flex-row flex-wrap ">
                    <div class=" min-w-[300px] h-auto w-[300px] rounded-lg overflow-hidden">
                        <div class="rounded-b-0 min-w-[300px] h-[450px] relative overflow-hidden">
                            <div>
                                <img :src="movieData.Poster">
                            </div>
                            <div></div>
                        </div>
                        <div></div>
                    </div>
                    <div class="flex text-white lg:w-[1020px]">
                        <section class="md:pl-[40px] text-white flex justify-center flex-wrap md:flex-start items-center">
                            <div class="flex flex-wrap flex-col text-white mb-6 ">
                                <h2 class="text-[2.2rem] font-semibold">
                                    <a class="font-bold">{{ movieData.Title }}</a>
                                    <span class="opacity-80 font-normal pl-2">({{ movieData.Year }})</span>
                                </h2>
                                <div class="flex text-white">
                                    <span class="border-2 inline-flex items-center border-[#ffffff60] rounded-sm pt-[0.06em] pb-[0.15] leading-4 px-1 mr-[7px] ">
                                        12
                                    </span>
                                    <span class="">
                                        {{ movieData.Released }} (FR)
                                    </span>
                                    <span class="pl-[20px]">
                                        <a>{{ movieData.Genre }}</a>
                                    </span>
                                    <span class="pl-[20px]">
                                        {{ movieData.Runtime }}
                                    </span>
                                </div>
                            </div>
                            <div class="flex flex-col">
                                <div class="!mb-0 text-white">
                                    <div class="flex flex-col md:flex-row items-center">
                                        <div class="flex items-center justify-center space-2 mr-4">
                                            <div class="flex items-center justify-center !mr-0">
                                                <div class="w-[68px] h-[68px] inline-block transition-all ease-in-out hover:scale-110">
                                                    <div class="inline-block w-[68px] h-[68px] rounded-full bg-[#081c22] p-1">
                                                        <div class="text-white relative text-center w-full h-full">
                                                            <div class="w-full h-full flex items-center border-4 border-green-300 rounded-full justify-center">
                                                                <span class="leading-4 normal-case">76%</span>
                                                            </div>
                                                            <canvas height="75" width="75" ></canvas>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="text font-bold ml-1">User<br>Score</div>
                                                <ul class="flex items-center justify-between ml-4">
                                                    <li class="!mx-0 w-9 h-9 bg-tmdb-dark-blue" title="Grinning face"><img :src="emo1" class="w-7 h-7"></li>
                                                    <li class="!mx-0 w-9 h-9 bg-tmdb-dark-blue" title="Smiling face with heart eyes"><img :src="emo2" class="w-7 h-7"></li>
                                                    <li class="!mx-0 w-9 h-9 bg-tmdb-dark-blue" title="Face with tears of joy"><img :src="emo3" class="w-7 h-7"></li>
                                                </ul>
                                                </div>
                                        </div>
                                        <div class="flex bg-[#032541] items-center justify-center w-48  rounded-full py-2 pt-3 pb-3 cursor-pointer hover:scale-105 transition ease-in-out duration-150">
                                            <div class="flex items-center justify-center">
                                                <div class="flex items-center text-white text-sm font-bold cursor-pointer transform">
                                                    <div class="flex flex-nowrap items-center whitespace-nowrap">
                                                        What's your
                                                        <span class="flex pl-1 underline underline-offset-2 decoration-2 decoration-[#01b4e4]">Vibe</span>?
                                                        <span class="flex items-center ml-2"><i class="pi pi-info-circle"></i></span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <ul class="auto actions">
                                    <li class="tooltip use_tooltip list tooltip_hover" title="" data-role="tooltip">
                                        <a class="no_click" href="#"><span class="glyphicons_v2 thumbnails-list white"></span></a>
                                    </li>
                                    <li class="tooltip use_tooltip" title="" data-role="tooltip">
                                        <a id="favourite" class="no_click add_to_account_list favourite" href="#"><span class="glyphicons_v2 heart white false"></span></a>
                                    </li>
                                    <li class="tooltip use_tooltip" title="" data-role="tooltip">
                                        <a id="watchlist" class="no_click add_to_account_list watchlist" href="#"><span class="glyphicons_v2 bookmark white false"></span></a>
                                    </li>
                                    <div id="vibes_mobile_tooltip_item" class="flex items-center hide" data-role="tooltip">
                                        <li id="vibes_mobile_item" class="flex flex-col items-center justify-center tooltip use_tooltip tooltip_hover" title="Login to use TMDB's new rating system." data-role="tooltip">
                                        <a id="rate_it" class="no_click rating" href="#"><span class="flex glyphicons_v2 star white false"></span></a>
                                        </li>

                                        <div class="vibes_mobile_panel_tooltip hide">
                                        <p>Welcome to Vibes, TMDB's new rating system! For more information, visit the <span class="italic underline underline-offset-2"><a> contribution bible</a></span>.</p>
                                        </div>
                                    </div>

                                        <li class="video none flex items-center ml-1">
                                        <a class="no_click play_trailer" href="#" data-site="YouTube" data-id="wUn05hdkhjM" data-title="Play Trailer"><span class="glyphicons_v2 play"></span> Play Trailer</a>
                                        </li>
                                </ul>
                            </div>
                            <div class="w-full">
                                <h3 class="text-[1.1em] italic opacity-70">Obviously.</h3>
                                <h3 class="mt-[10px] mb-2 font-semibold text-[1.3em]">Overview</h3>
                                <div class="overview" dir="auto">
                                    <p>{{ movieData.Plot }}</p>
                                </div>

                                <ol class="mt-5 flex flex-wrap flex-start relative top-0 left-0">
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden"><a class="font-bold">{{ movieData.Director }}</a></p>
                                        <p class="text-[0.9em] overflow-hidden">Director, Writer</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden"><a class="font-bold">Larry Lieber</a></p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden">
                                            <a class="font-bold">Val Mayerik</a>
                                        </p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden pt-5">
                                            <a class="font-bold">Steve Gan</a>
                                        </p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden pt-5">
                                            <a class="font-bold">Jim Starlin</a>
                                        </p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden pt-5">
                                            <a class="font-bold">Steve Gerber</a>
                                        </p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden pt-5">
                                            <a class="font-bold">Stan Lee</a>
                                        </p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden pt-5">
                                            <a class="font-bold">Jack Kirby</a>
                                        </p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden pt-5">
                                            <a class="font-bold">Bill Mantlo</a>
                                        </p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden pt-5">
                                            <a class="font-bold">Keith Giffen</a>
                                        </p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                    <li class="bg-transparent h-auto mb-0 w-[33%] pr-5 min-w-[140px]">
                                        <p class="text-[1em] overflow-hidden pt-5">
                                            <a class="font-bold">Steve Englehart</a>
                                        </p>
                                        <p class="text-[0.9em] overflow-hidden">Characters</p>
                                    </li>
                                </ol>
                            </div>
                        </section>
                    </div>
                </section>
            </div>
        </div>
    </div>
    <div class="my-0 bg-white w-full flex justify-center flex-wrap items-center">
        <div class="flex items-center justify-center ">
            <div class="max-w-[1400px] w-full py-[30px] px-[40px] flex flex-col md:flex-row items">
                <div>
                    <div class="flex justify-center flex-wrap pr-[30px] w-[calc(100vw - 80px - 268px)]">
                        <section class="py-[30px] ">
                            <h3 class="font-semibold text-[1.4em] mb-[20px]">Top billed Cast</h3>
                            <div class="relative top-0 left-0">
                                <ol class="overflow-x-scroll overflow-y-hidden -ml-[10px] pb-[10px] flex flex-col md:flex-row relative top-0 left-0">
                                    <li class="mb-[10px] ml-[10px] mr-[4px] border pb-[10px] rounded-lg overflow-hidden min-w-[140px] w-[140px] bg-white shadow-inner shadow-[#00000010]">
                                        <a>
                                            <div>
                                                <img :src="chrispratt">
                                            </div>
                                        </a>
                                        <p class="px-[10px] pt-[10px] font-bold">Chris Pratt</p>
                                        <p class="px-[10px] text-[0.9em]">Peter Quill / Star-Lord</p>
                                    </li>
                                    <li class="mb-[10px] ml-[10px] mr-[4px] border pb-[10px] rounded-lg overflow-hidden min-w-[140px] w-[140px] bg-white shadow-inner shadow-[#00000010]">
                                        <a>
                                            <div>
                                                <img :src="zoesaldana">
                                            </div>
                                        </a>
                                        <p class="px-[10px] pt-[10px] font-bold">Zoe Saldaña</p>
                                        <p class="px-[10px] text-[0.9em]">Gamora</p>
                                    </li>
                                    <li class="mb-[10px] ml-[10px] mr-[4px] border pb-[10px] rounded-lg overflow-hidden min-w-[140px] w-[140px] bg-white shadow-inner shadow-[#00000010]">
                                        <a>
                                            <div>
                                                <img :src="davebautista">
                                            </div>
                                        </a>
                                        <p class="px-[10px] pt-[10px] font-bold">Dave Bautista</p>
                                        <p class="px-[10px] text-[0.9em]">Drax</p>
                                    </li>
                                    <li class="mb-[10px] ml-[10px] mr-[4px] border pb-[10px] rounded-lg overflow-hidden min-w-[140px] w-[140px] bg-white shadow-inner shadow-[#00000010]">
                                        <a>
                                            <div>
                                                <img :src="vin">
                                            </div>
                                        </a>
                                        <p class="px-[10px] pt-[10px] font-bold">Vin Diesel</p>
                                        <p class="px-[10px] text-[0.9em]">Baby Groot (voice)</p>
                                    </li>
                                    <li class="mb-[10px] ml-[10px] mr-[4px] border pb-[10px] rounded-lg overflow-hidden min-w-[140px] w-[140px] bg-white shadow-inner shadow-[#00000010]">
                                        <a>
                                            <div>
                                                <img :src="bradly">
                                            </div>
                                        </a>
                                        <p class="px-[10px] pt-[10px] font-bold">Bradley Cooper</p>
                                        <p class="px-[10px] text-[0.9em]">Rocket (voice)</p>
                                    </li>
                                    <li class="mb-[10px] ml-[10px] mr-[4px] border pb-[10px] rounded-lg overflow-hidden min-w-[140px] w-[140px] bg-white shadow-inner shadow-[#00000010]">
                                        <a>
                                            <div>
                                                <img :src="kurt">
                                            </div>
                                        </a>
                                        <p class="px-[10px] pt-[10px] font-bold">Kurt Russell</p>
                                        <p class="px-[10px] text-[0.9em]">Ego</p>
                                    </li>
                                    <li class="mb-[10px] ml-[10px] mr-[4px] border pb-[10px] rounded-lg overflow-hidden min-w-[140px] w-[140px] bg-white shadow-inner shadow-[#00000010]">
                                        <a>
                                            <div>
                                                <img :src="karen">
                                            </div>
                                        </a>
                                        <p class="px-[10px] pt-[10px] font-bold">Karen Gillan</p>
                                        <p class="px-[10px] text-[0.9em]">Nebula</p>
                                    </li>
                                </ol>
                            </div>
                        </section>
                    </div>
                </div>
                <div class="min-w-[260px] w-[260px] flex flex-wrap">
                    <div>
                        <section class="flex flex-wrap w-full max-w-[300px]">
                            <div class="w-full">
                                <div class="w-full">
                                    <section class="flex flex-col mb-[30px] w-full">
                                        <div class="w-full flex justify-center md:justify-start mb-[30px] min-h-[31px]">
                                            <button class="px-4 py-2 bg-[#57AFD5] rounded-lg text-white"><i class="pi pi-play"></i>Play Now</button>
                                        </div>
                                        <div class="flex justify-center md:justify-start">
                                            <div class="h-[30px] mb-[30px]">
                                                <a class="block text-[1.9em] text-black">
                                                    <span class="relative top-0 left-0 inline-flex min-w-[1em] w-[1em] min-h-[1em] h-[1em] bg-center bg-no-repeat box-border"><i class="pi pi-facebook"></i></span>
                                                </a>
                                            </div>
                                            <div class="h-[30px] mb-[30px] ml-[10px]">
                                                <a class="block text-[1.9em] text-black">
                                                    <span class="relative top-0 left-0 inline-flex min-w-[1em] w-[1em] min-h-[1em] h-[1em] bg-center bg-no-repeat box-border"><i class="pi pi-twitter"></i></span>
                                                </a>
                                            </div>
                                            <div class="h-[30px] mb-[30px] ml-[10px]">
                                                <a class="block text-[1.9em] text-black">
                                                    <span class="relative top-0 left-0 inline-flex min-w-[1em] w-[1em] min-h-[1em] h-[1em] bg-center bg-no-repeat box-border"><i class="pi pi-instagram"></i></span>
                                                </a>
                                            </div>
                                            <div class="h-[30px] mb-[30px] ml-[10px]">
                                                <a class="block text-[1.9em] text-black">
                                                    <span class="relative top-0 left-0 inline-flex min-w-[1em] w-[1em] min-h-[1em] h-[1em] bg-center bg-no-repeat box-border"><i class="pi pi-whatsapp"></i></span>
                                                </a>
                                            </div>
                                        </div>
                                        <p class="flex flex-col text-center md:text-left mb-5">
                                            <strong>Status</strong>
                                            {{ movieData.Released ? "Released": null }}
                                        </p>
                                        <p class="flex flex-col text-center md:text-left mb-5">
                                            <strong>Original Language</strong>
                                            {{ movieData.Language }}
                                        </p>
                                        <p class="flex flex-col text-center md:text-left mb-5">
                                            <strong>Box Office</strong>
                                            {{ movieData.BoxOffice }}
                                        </p>
                                        <p class="flex flex-col text-center md:text-left mb-5">
                                            <strong>Country</strong>
                                            {{ movieData.Country }}
                                        </p>
                                        <p class="flex flex-col text-center md:text-left mb-5">
                                            <strong>Awards</strong>
                                            {{ movieData.Awards }}
                                        </p>
                                        <p></p>
                                    </section>
                                </div>
                            </div>
                            <div></div>
                            <div></div>
                            <div></div>
                            <div></div>
                        </section>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>