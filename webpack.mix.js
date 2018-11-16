const mix = require('laravel-mix');
const tailwindcss = require('tailwindcss');


mix.react('assets/js/app.js', 'static/js')
   .sass('assets/sass/app.scss', 'static/css')
   .options({
      processCssUrls: false,
      postCss: [ tailwindcss('./tailwind.js') ]
   })
   .copyDirectory('assets/img/favicon.png', 'static');
