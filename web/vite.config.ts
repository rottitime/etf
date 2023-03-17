import { defineConfig } from 'vite'
import postcssNesting from 'postcss-nesting'

export default defineConfig({
  css: {
    postcss: {
      plugins: [postcssNesting],
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
