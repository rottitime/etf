import { defineConfig } from 'vite'
import postcssNesting from 'postcss-nesting'
import postcssCustomMedia from 'postcss-custom-media'

export default defineConfig({
  css: {
    postcss: {
      plugins: [postcssNesting, postcssCustomMedia],
    },
  },
  build: {
    outDir: '../static/dist',
    rollupOptions: {
      output: {
        entryFileNames: `assets/[name].js`,
        chunkFileNames: `assets/[name].js`,
        assetFileNames: `assets/[name].[ext]`,
      },
    },
  },
})
